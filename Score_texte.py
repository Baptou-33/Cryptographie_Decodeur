# Import des bibliothèques ---------------------------------------------------------------------------------------------
import math
import random
import re
import unicodedata
from collections import Counter

from wordfreq import top_n_list, word_frequency



# Paramètres -----------------------------------------------------------------------------------------------------------
SEUIL_VRAISEMBLANCE = 0.5 # Seuil en dessous duquel on considère que ce n'est pas une phrase en francais

NB_MOTS_VOCABULAIRE = 20000 # Nombre de mots français courants (wordfreq) utilisés pour fabriquer le corpus
NB_MOTS_CORPUS = 200000     # Taille du corpus d'apprentissage (en mots tirés au hasard selon leur fréquence)
NB_MOTS_TEST = 30000        # Taille du corpus de calibration (différent de celui d'apprentissage)
LONGUEUR_ECHANTILLON = 40   # Longueur (en lettres) des extraits utilisés pour calibrer l'échelle
NB_ECHANTILLONS = 300       # Nombre d'extraits utilisés pour calibrer l'échelle
GRAINE = 42                 # Graine aléatoire fixe : le score d'un texte est toujours le même

# Poids du modèle : trigrammes, bigrammes, lettres seules, et un petit reste uniforme (lissage)
LAMBDA_3, LAMBDA_2, LAMBDA_1, LAMBDA_0 = 0.60, 0.30, 0.09, 0.01



# Normalisation ----------------------------------------------------------------------------------------------------------
CARACTERE_INCONNU = '#' # À utiliser dans les décodeurs pour une valeur qui n'a pas pu être convertie

def normaliser(texte):
    # On ne garde que les lettres a-z, en minuscules, sans accents, sans espaces ni ponctuation.
    # CARACTERE_INCONNU est volontairement conservé : comme il n'existe dans aucun mot français,
    # le modèle n'a aucune statistique pour lui, ce qui fait chuter le score dès qu'il apparaît
    texte = texte.lower().replace('œ', 'oe').replace('æ', 'ae')
    decompose = unicodedata.normalize('NFD', texte) # "é" devient "e" + accent séparé
    return ''.join(c for c in decompose if 'a' <= c <= 'z' or c == CARACTERE_INCONNU)

def extraire_mots(texte):
    return re.findall(r"[^\W\d_]+", texte.lower())



# Construction du modèle de langue (une seule fois au chargement du module) ----------------------------------------------
def _charger_vocabulaire():
    mots, poids = [], []
    for mot in top_n_list('fr', NB_MOTS_VOCABULAIRE):
        mot_normalise = normaliser(mot)
        if mot_normalise:
            mots.append(mot_normalise)
            poids.append(word_frequency(mot, 'fr'))
    return mots, poids

_MOTS, _POIDS = _charger_vocabulaire()

def _generer_texte(nb_mots, graine):
    # Simule du français écrit SANS espaces : on tire des mots au hasard selon leur fréquence
    # réelle d'usage, puis on les colle bout à bout
    generateur = random.Random(graine)
    return ''.join(generateur.choices(_MOTS, weights=_POIDS, k=nb_mots))

_TEXTE_APPRENTISSAGE = _generer_texte(NB_MOTS_CORPUS, GRAINE)
_N1 = Counter(_TEXTE_APPRENTISSAGE)
_N2 = Counter(_TEXTE_APPRENTISSAGE[i:i + 2] for i in range(len(_TEXTE_APPRENTISSAGE) - 1))
_N3 = Counter(_TEXTE_APPRENTISSAGE[i:i + 3] for i in range(len(_TEXTE_APPRENTISSAGE) - 2))
_TOTAL = len(_TEXTE_APPRENTISSAGE)



# Calcul de vraisemblance ------------------------------------------------------------------------------------------------
def _proba(a, b, c):
    # Probabilité que la lettre c suive les lettres a, b (mélange trigramme / bigramme / lettre seule)
    p3 = _N3[a + b + c] / _N2[a + b] if _N2[a + b] else 0
    p2 = _N2[b + c] / _N1[b] if _N1[b] else 0
    p1 = _N1[c] / _TOTAL
    return LAMBDA_3 * p3 + LAMBDA_2 * p2 + LAMBDA_1 * p1 + LAMBDA_0 / 26

def _log_proba_moyenne(lettres):
    # Moyenne (par lettre) du log de la probabilité : plus c'est haut, plus ça ressemble à du français
    if len(lettres) < 3:
        return None
    total = sum(math.log(_proba(lettres[i], lettres[i + 1], lettres[i + 2]))
                for i in range(len(lettres) - 2))
    return total / (len(lettres) - 2)

def _calibrer():
    # Deux points de repère, mesurés sur des extraits de même longueur :
    # - du vrai français sans espaces  -> ce qui vaudra 1
    # - les mêmes lettres mélangées    -> ce qui vaudra 0 (bonnes lettres, mauvais ordre)
    texte = _generer_texte(NB_MOTS_TEST, GRAINE + 1)
    generateur = random.Random(GRAINE + 2)
    francais, melange = [], []
    for _ in range(NB_ECHANTILLONS):
        debut = generateur.randrange(len(texte) - LONGUEUR_ECHANTILLON)
        extrait = texte[debut:debut + LONGUEUR_ECHANTILLON]
        lettres = list(extrait)
        generateur.shuffle(lettres)
        francais.append(_log_proba_moyenne(extrait))
        melange.append(_log_proba_moyenne(''.join(lettres)))
    return sum(melange) / len(melange), sum(francais) / len(francais)

_REF_MELANGE, _REF_FRANCAIS = _calibrer()



# Fonction principale de scoring -----------------------------------------------------------------------------------------
def score_francais(texte):
    lettres = normaliser(texte)
    log_proba = _log_proba_moyenne(lettres)
    if log_proba is None:
        return 0.0
    score = (log_proba - _REF_MELANGE) / (_REF_FRANCAIS - _REF_MELANGE)
    return max(0.0, min(1.0, score))
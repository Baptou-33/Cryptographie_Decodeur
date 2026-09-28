# Import des bibliothèques ---------------------------------------------------------------------------------------------
import re
from spellchecker import SpellChecker
from collections import defaultdict
from wordfreq import top_n_list, word_frequency



# Paramètres -----------------------------------------------------------------------------------------------------------
NB_MOTS_CORPUS = 5000 # Nombre de mots français les plus fréquents qu'on utilise pour construire less n-grammes



# Initialisation -------------------------------------------------------------------------------------------------------
SPELL_FR = SpellChecker(language='fr')



# Avec espaces ---------------------------------------------------------------------------------------------------------
def extraire_mots(texte):
    # On construit des chaines de caractère à avec toutes les lettres
    return re.findall(r"[^\W\d_]+", texte.lower())

def score_mots(texte):
    # Score basé sur la reconnaissance de mots entiers (efficace quand le texte a des espaces)
    mots = extraire_mots(texte)
    if not mots:
        return 0
    connus = SPELL_FR.known(mots)
    return len(connus) / len(mots)



# Sans espaces ---------------------------------------------------------------------------------------------------------
def construire_frequences_ngrammes(n, nb_mots=NB_MOTS_CORPUS):
    # On compte le nbr de ngrammes dans les mots français les plus courants
    frequences = defaultdict(float)
    total = 0
    for mot in top_n_list('fr', nb_mots):
        freq_mot = word_frequency(mot, 'fr')
        for i in range(len(mot) - n + 1):
            ngramme = mot[i:i + n]
            frequences[ngramme] += freq_mot
            total += freq_mot
    if total > 0:
        for ngramme in frequences:
            frequences[ngramme] /= total
    return frequences

FREQUENCES_BIGRAMMES = construire_frequences_ngrammes(2)
FREQUENCES_TRIGRAMMES = construire_frequences_ngrammes(3)

SCORE_MAX_BIGRAMME = max(FREQUENCES_BIGRAMMES.values())
SCORE_MAX_TRIGRAMME = max(FREQUENCES_TRIGRAMMES.values())

def extraire_lettres(texte):
    return re.findall(r"[^\W\d_]", texte.lower())

def extraire_ngrammes(texte, n):
    lettres = extraire_lettres(texte)
    return [''.join(lettres[i:i + n]) for i in range(len(lettres) - n + 1)]

def score_bigrammes(texte):
    bigrammes = extraire_ngrammes(texte, 2)
    if not bigrammes:
        return 0
    score = sum(FREQUENCES_BIGRAMMES.get(bg, 0) for bg in bigrammes) / len(bigrammes)
    return min(score / SCORE_MAX_BIGRAMME, 1.0)

def score_trigrammes(texte):
    trigrammes = extraire_ngrammes(texte, 3)
    if not trigrammes:
        return 0
    score = sum(FREQUENCES_TRIGRAMMES.get(tg, 0) for tg in trigrammes) / len(trigrammes)
    return min(score / SCORE_MAX_TRIGRAMME, 1.0)

def score_ngrammes(texte):
    # Trigrammes + significatifs que les bigrammes donc + de poids
    return (score_bigrammes(texte) + 2 * score_trigrammes(texte)) / 3

# Fonction utilisée dans les autres algorithmes de cryptographie -------------------------------------------------------
def score_francais(texte):
    return max(score_mots(texte), score_ngrammes(texte))
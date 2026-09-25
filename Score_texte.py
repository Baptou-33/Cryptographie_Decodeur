# Import des bibliothèques ---------------------------------------------------------------------------------------------
import re
from spellchecker import SpellChecker



# Paramètres -----------------------------------------------------------------------------------------------------------
SEUIL_VRAISEMBLANCE = 0.5 # Seuil en dessous duquel on considère que ce n'est pas une phrase en francais



# Initialisation -------------------------------------------------------------------------------------------------------
SPELL_FR = SpellChecker(language='fr')



# Fonctions ------------------------------------------------------------------------------------------------------------
def extraire_mots(texte):
    # On construit des chaines de caractère à avec tous les a-z + avec accents collés
    return re.findall(r"[a-zàâäéèêëîïôöùûü]+", texte.lower())

def score_francais(texte):
    mots = extraire_mots(texte)
    if not mots:
        return 0
    connus = SPELL_FR.known(mots)
    return len(connus)/len(mots)
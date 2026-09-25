# Import des bibliothèques ---------------------------------------------------------------------------------------------
import string
import re
from spellchecker import SpellChecker



# Paramètres -----------------------------------------------------------------------------------------------------------
SEUIL_VRAISEMBLANCE = 0.5 # Seuil en dessous duquel on considère que ce n'est pas une phrase en francais



# Initialisation -------------------------------------------------------------------------------------------------------
SPELL_FR = SpellChecker(language='fr')



# Fonctions ------------------------------------------------------------------------------------------------------------
def decaler_lettre(lettre, decalage):
    if lettre in string.ascii_lowercase:
        # On fait - décalage, car on décode et ord(lettre) = son code numérique : ord('a') = 97
        return chr((ord(lettre) - ord('a') - decalage) % 26 + ord('a'))
    if lettre in string.ascii_uppercase:
        return chr((ord(lettre) - ord('A') - decalage) % 26 + ord('A'))
    return lettre # Si c'est un autre symbole ou chiffre, on le laisse tel quel

def appliquer_cesar(texte, decalage):
    return ''.join(decaler_lettre(c, decalage) for c in texte)

def extraire_mots(texte):
    # On construit des chaines de caractère à avec tous les a-z+avec accents collés
    return re.findall(r"[a-zàâäéèêëîïôöùûü]+", texte.lower())

def score_francais(texte):
    mots = extraire_mots(texte)
    if not mots:
        return 0
    connus = SPELL_FR.known(mots)
    return len(connus)/len(mots)

def cesar_brute_force(texte):
    resultats = []
    for decalage in range(26):
        texte_decode = appliquer_cesar(texte, decalage)
        score = score_francais(texte_decode)
        resultats.append((decalage, score, texte_decode))
    resultats.sort(key=lambda x: x[1], reverse=True)
    return resultats

# Fonction utilisée dans la fonction principale
def decoder_cesar(texte):
    resultats = cesar_brute_force(texte)
    return resultats[0]



# Main pour test / usage unique ----------------------------------------------------------------------------------------
def main():
    text_test = input("Texte à déchiffrer: ")
    resultats = cesar_brute_force(text_test)
    for decalage, score, texte_decode in resultats:
        if score < SEUIL_VRAISEMBLANCE:
            break
        print(decalage, score, texte_decode)


if __name__ == '__main__':
    main()
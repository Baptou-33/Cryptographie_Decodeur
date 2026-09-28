# Import des bibliothèques ---------------------------------------------------------------------------------------------
from Fonction_globales import *
from morse3 import Morse



# Fonctions ------------------------------------------------------------------------------------------------------------
def appliquer_morse(texte):
    mots = texte.split('/')
    mots_decodes = [Morse(mot).morseToString().lower() for mot in mots]
    return ' '.join(mots_decodes)

# Fonction utilisée dans la fonction principale
def decoder_morse(texte):
    resultat = appliquer_morse(texte)
    score = score_francais(resultat)
    return [("Code Morse", score, resultat, None)]



# Main pour test / usage unique ----------------------------------------------------------------------------------------
def main():
    text_test = safe_input("le texte à decoder")
    resultats = decoder_morse(text_test)
    afficher_resultat(resultats[0])


if __name__ == '__main__':
    main()
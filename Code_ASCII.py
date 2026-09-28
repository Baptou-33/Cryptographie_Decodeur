# Import des bibliothèques ---------------------------------------------------------------------------------------------
from Fonction_globales import *



# Fonctions ------------------------------------------------------------------------------------------------------------
def nombre_lettre(nombre):
    if 32 <= nombre <= 126:
        return chr(nombre)
    return CARACTERE_INCONNU # En cas de symbole inconnu, on met le CARACTERE_INCONNU

def appliquer_ascii(texte):
    nombres = extraire_nombres(texte)
    return ''.join(nombre_lettre(n) for n in nombres)

# Fonction utilisée dans la fonction principale
def decoder_ascii(texte):
    resultat = appliquer_ascii(texte)
    score = score_francais(resultat)
    return [("Code ASCII", score, resultat, None)] # On envoie tous les premiers



# Main pour test / usage unique ----------------------------------------------------------------------------------------
def main():
    text_test = safe_input("le texte à decoder")
    resultats = decoder_ascii(text_test)
    afficher_resultat(resultats[0])


if __name__ == '__main__':
    main()
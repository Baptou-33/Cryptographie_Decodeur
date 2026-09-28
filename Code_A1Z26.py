# Import des bibliothèques ---------------------------------------------------------------------------------------------
from Fonction_globales import *



# Fonctions ------------------------------------------------------------------------------------------------------------
def nombre_lettre(nombre):
    # On considère que 0 est un espace
    if nombre == 0:
        return ' '
    if 1 <= nombre <= 26:
        return chr(nombre - 1 + ord('a'))
    return CARACTERE_INCONNU # En cas de symbole inconnu, on met le CARACTERE_INCONNU

def appliquer_a1z21(texte):
    nombres = extraire_nombres(texte)
    return ''.join(nombre_lettre(n) for n in nombres)

# Fonction utilisée dans la fonction principale
def decoder_a1z21(texte):
    resultat = appliquer_a1z21(texte)
    score = score_francais(resultat)
    resultats = [("Code A1Z21", score, resultat, None)]
    resultats.sort(key=lambda x: x[1], reverse=True)
    meilleur_score = resultats[0][1]
    return [r for r in resultats if r[1] == meilleur_score] # On envoie tous les premiers



# Main pour test / usage unique ----------------------------------------------------------------------------------------
def main():
    text_test = safe_input("le texte à decoder")
    resultats = decoder_a1z21(text_test)
    afficher_resultat(resultats[0])


if __name__ == '__main__':
    main()
# Import des bibliothèques ---------------------------------------------------------------------------------------------
import re
from Score_texte import score_francais, CARACTERE_INCONNU



# Fonctions ------------------------------------------------------------------------------------------------------------
def extraire_nombres(texte):
    return [int(n) for n in re.findall(r"\d+", texte)] # On ne récupère que les nombres, n'importe le séparateur

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
    text_test = input("Texte à déchiffrer: ")
    resultats = decoder_a1z21(text_test)
    nom, score, texte_decode, parametre = resultats[0]
    print(f"\n{nom} a décodé :\n"
          f"{texte_decode}\n"
          f"avec un score de {score}\n")


if __name__ == '__main__':
    main()
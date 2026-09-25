# Import des bibliothèques ---------------------------------------------------------------------------------------------
import re
from Score_texte import score_francais



# Fonctions ------------------------------------------------------------------------------------------------------------
def extraire_nombres(texte):
    return [int(n) for n in re.findall(r"\d+", texte)] # On ne récupère que les nombres, n'importe le séparateur

def nombre_lettre(nombre, offset):
    if 0 + offset <= nombre <= 25 + offset:
        return chr(nombre - offset + ord('a'))
    return '?' # En cas de symbole inconnu, on met ?

def appliquer_a1z21(texte, offset):
    nombres = extraire_nombres(texte)
    return ''.join(nombre_lettre(n, offset) for n in nombres)

# Fonction utilisée dans la fonction principale
def decoder_a1z21(texte):
    resultats = []
    # Même si a priori a = 1, on teste si ca ne commencerait pas avec a = 0
    for offset in range(2):
        resultat = appliquer_a1z21(texte, offset)
        score = score_francais(resultat)
        resultats.append(("Code A1Z21", score, resultat, offset))
    resultats.sort(key=lambda x: x[1], reverse=True)
    meilleur_score = resultats[0][1]
    return [r for r in resultats if r[1] == meilleur_score] # On envoie tous les premiers



# Main pour test / usage unique ----------------------------------------------------------------------------------------
def main():
    text_test = input("Texte à déchiffrer: ")
    resultats = decoder_a1z21(text_test)
    nom, score, texte_decode, offset = resultats[0]
    print(f"\n{nom} a décodé :\n"
          f"{texte_decode}\n"
          f"avec un score de {score}\n"
          f"et où le 'a' a pour indice {offset}")


if __name__ == '__main__':
    main()
# Import des bibliothèques ---------------------------------------------------------------------------------------------
import re
from Score_texte import score_francais



# Fonctions ------------------------------------------------------------------------------------------------------------
def extraire_nombres(texte):
    return [int(n) for n in re.findall(r"\d+", texte)] # On ne récupère que les nombres, n'importe le séparateur

def nombre_lettre(nombre):
    if 32 <= nombre <= 126:
        return chr(nombre)
    return '?' # En cas de symbole inconnu, on met ?

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
    text_test = input("Texte à déchiffrer: ")
    resultats = decoder_ascii(text_test)
    nom, score, texte_decode, parametres = resultats[0]
    print(f"\n{nom} a décodé :\n"
          f"{texte_decode}\n"
          f"avec un score de {score}")


if __name__ == '__main__':
    main()
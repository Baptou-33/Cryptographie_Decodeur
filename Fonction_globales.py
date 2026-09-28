# Import des bibliothèques ---------------------------------------------------------------------------------------------
from Score_texte import score_francais, CARACTERE_INCONNU, extraire_mots
import re


# Fonctions ------------------------------------------------------------------------------------------------------------
# Accepte les inputs sur plusieurs lignes
def safe_input(info):
    print(f"Entrez {info} puis appuyez sur Entrée deux fois :")
    lignes = []
    while True:
        ligne = input()
        if ligne == "":
            break
        lignes.append(ligne)
    return " ".join(lignes)



def extraire_nombres(texte):
    return [int(n) for n in re.findall(r"\d+", texte)] # On ne récupère que les nombres, n'importe le séparateur



def afficher_resultat(resultat):
    nom, score, texte_decode, parametre = resultat
    print(f"\n{nom} a décodé :\n"
          f"{texte_decode}\n"
          f"avec un score de {score}\n")
    if parametre:
          print(f"avec pour paramètre {parametre}\n")
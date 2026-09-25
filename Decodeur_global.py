# Import des bibliothèques ---------------------------------------------------------------------------------------------
from Code_Cesar import decoder_cesar



# Initialisation -------------------------------------------------------------------------------------------------------
resultats = []



# Main -----------------------------------------------------------------------------------------------------------------
def main():
    # On entre le code encrypté
    texte_chiffre = input("Texte à decoder: ")

    # On teste tous les algorithmes
    resultats.extend(decoder_cesar(texte_chiffre))

    # On affiche le meilleur résultat
    print(f"\n{resultats[0][0]} a décodé :\n"
          f"{resultats[0][2]}\n"
          f"avec un score de {resultats[0][1]}\n"
          f"et avec comme paramètres :\n"
          f"{resultats[0][3]}")


if __name__ == '__main__':
    main()
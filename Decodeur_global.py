# Import des bibliothèques ---------------------------------------------------------------------------------------------
from Code_Cesar import decoder_cesar
from Code_A1Z26 import decoder_a1z21
from Code_ASCII import decoder_ascii
from Code_transposition import decoder_transposition
from Code_Acrostiche import decoder_acrostiche
from Code_Periodique import decoder_periodique



# Initialisation -------------------------------------------------------------------------------------------------------
exemples = {"12;1;0;19;15; 12;21;20;9;15; 14;0;4;5;0; 12;0;5;14;9; 7;13;5;0;5; 19;20;0;15;18; 4;9;14;1;20; 5;21;18" : "la?solution?de?l?enigme?est?ordinateur",
            "76 69 32 77 79 84 32 68 69 32 80 65 83 83 69 32 68 69 32 67 69 84 84 69 32 69 78 73 71 77 69 32 69 83 84 32 65 83 67 73 73 32 76 69 32 77 79 89 69 78 32 69 77 80 76 79 89 69 32 80 79 85 82 32 67 79 68 69 82 32 67 69 32 67 79 68 69" : "LE MOT DE PASSE DE CETTE ENIGME EST ASCII LE MOYEN EMPLOYE POUR CODER CE CODE",
            "LLTGSREETMTAMDEEAMOEECNMTCNIAECEIEGS" : "LEMOTCLEDECETTEENIGMECIESTANAGRAMMES",
            "L’asticot sénégalais orientait l’Ukraine ton idiot ours nous est satisfaisant ta chère hyène indoue est née": "lasolutionestchien",
            "ivu wvby jlaal mvpz sh ylwvuzl lza sh zvbzayhjapvu kl xbpugl why kpe" : "bon pour cette fois la reponse est la soustraction de quinze par dix",
            "84 92 R 31 G 7 68 53 L 9 A 92 T E 7 T R 68 31 32" : "PoURGaGNErILFAUTENTRErGaGe"}



# Main -----------------------------------------------------------------------------------------------------------------
def chercher_solution(texte_chiffre, parametres, verification = False, attendu = ""):
    resultats = []

    resultats.extend(decoder_cesar(texte_chiffre, parametres))
    resultats.extend(decoder_a1z21(texte_chiffre))
    resultats.extend(decoder_ascii(texte_chiffre))
    resultats.extend(decoder_transposition(texte_chiffre, parametres))
    resultats.extend(decoder_acrostiche(texte_chiffre))
    resultats.extend(decoder_periodique(texte_chiffre))

    if not resultats:
        print(f"\nAucun décodeur n'a renvoyé de résultat pour ce texte :\n{texte_chiffre}")
        return

    # On affiche le meilleur résultat
    resultats.sort(key=lambda x: x[1], reverse=True)
    if (not verification) or verification and resultats[0][2] != attendu:
        print(f"\n{texte_chiffre}\n"
              f"{resultats[0][0]} a décodé :\n"
              f"{resultats[0][2]}\n"
              f"avec un score de {resultats[0][1]}\n"
              f"et avec comme paramètres :\n"
              f"{resultats[0][3]}")


def main():
    # On entre le code encrypté
    texte_chiffre = input("Texte à decoder: ")
    if texte_chiffre == "check":
        for texte_chiffre, resultat_attendu in exemples.items():
            chercher_solution(texte_chiffre, "", True, resultat_attendu)
        return

    parametres = input("Paramètres: ")

    chercher_solution(texte_chiffre, parametres)




if __name__ == '__main__':
    main()
# Import des bibliothèques ---------------------------------------------------------------------------------------------
from Fonction_globales import *
from Code_Cesar import decoder_cesar
from Code_A1Z26 import decoder_a1z21
from Code_ASCII import decoder_ascii
from Code_transposition import decoder_transposition
from Code_Acrostiche import decoder_acrostiche
from Code_Periodique import decoder_periodique
from Code_Clavier_9_touches import decoder_clavier_9_touches
from Code_Premiers_mots import decoder_premiers_mots
from Code_Morse import decoder_morse
from Code_0_non_1_A1Z26 import decoder_0_non_1_a1z21



# Initialisation -------------------------------------------------------------------------------------------------------
exemples = {"12;1;0;19;15; 12;21;20;9;15; 14;0;4;5;0; 12;0;5;14;9; 7;13;5;0;5; 19;20;0;15;18; 4;9;14;1;20; 5;21;18" : "la solution de l enigme est ordinateur",
            "76 69 32 77 79 84 32 68 69 32 80 65 83 83 69 32 68 69 32 67 69 84 84 69 32 69 78 73 71 77 69 32 69 83 84 32 65 83 67 73 73 32 76 69 32 77 79 89 69 78 32 69 77 80 76 79 89 69 32 80 79 85 82 32 67 79 68 69 82 32 67 69 32 67 79 68 69" : "LE MOT DE PASSE DE CETTE ENIGME EST ASCII LE MOYEN EMPLOYE POUR CODER CE CODE",
            "LLTGSREETMTAMDEEAMOEECNMTCNIAECEIEGS" : "LEMOTCLEDECETTEENIGMECIESTANAGRAMMES",
            "L’asticot sénégalais orientait l’Ukraine ton idiot ours nous est satisfaisant ta chère hyène indoue est née": "lasolutionestchien",
            "ivu wvby jlaal mvpz sh ylwvuzl lza sh zvbzayhjapvu kl xbpugl why kpe" : "bon pour cette fois la reponse est la soustraction de quinze par dix",
            "84 92 R 31 G 7 68 53 L 9 A 92 T E 7 T R 68 31 32" : "PoURGaGNErILFAUTENTRErGaGe",
            "21 53 32 93 21 62 31 32 73 41 73 21 42 21 61 22 32 53 53": "alexandergrahambell",
            "-... .-. .- ...- --- / .- / ...- --- ..- ... / .-.. .- / ... --- .-.. ..- - .. --- -. / . ... - / -- --- .-. ... .": "bravo a vous la solution est morse",
            "112 012 11 09 089 118 15 116 076 115 015 114 119 016 15 15 119 120 112 023 15 116 118 015 115 14 121 19 120 14 15 117 121 016 19 114 126 15 116 11 118 14 15 121 124 096 112 11 118 012 15 116 115 114 119 15 14 085 115 046 19 120 15 120 118 15 14 02 085 115 114 114 15 15 020 15 114 112 052 15 120 063 120 118 15 119": "lareponseestleproduitdequinzepardeuxlareponsedoitetredonneeenlettres"}



# Fonctions ------------------------------------------------------------------------------------------------------------
def chercher_solution(texte_chiffre, parametres, verification = False, attendu = ""):
    resultats = []

    resultats.extend(decoder_cesar(texte_chiffre, parametres))
    resultats.extend(decoder_a1z21(texte_chiffre))
    resultats.extend(decoder_ascii(texte_chiffre))
    resultats.extend(decoder_transposition(texte_chiffre, parametres))
    resultats.extend(decoder_acrostiche(texte_chiffre))
    resultats.extend(decoder_periodique(texte_chiffre))
    resultats.extend(decoder_clavier_9_touches(texte_chiffre))
    resultats.extend(decoder_premiers_mots(texte_chiffre))
    resultats.extend(decoder_morse(texte_chiffre))
    resultats.extend(decoder_morse(texte_chiffre))

    if not resultats:
        print(f"\nAucun décodeur n'a renvoyé de résultat pour ce texte :\n{texte_chiffre}")
        return

    # On affiche le meilleur résultat
    resultats.sort(key=lambda x: x[1], reverse=True)
    if (not verification) or verification and resultats[0][2] != attendu:
        afficher_resultat(resultats[0])



# Main -----------------------------------------------------------------------------------------------------------------
def main():
    # On entre le code encrypté
    texte_chiffre = safe_input("le texte à decoder")
    if texte_chiffre == "check":
        for texte_chiffre, resultat_attendu in exemples.items():
            chercher_solution(texte_chiffre, "", True, resultat_attendu)
        return

    parametres = safe_input("les paramètres")

    chercher_solution(texte_chiffre, parametres)




if __name__ == '__main__':
    main()
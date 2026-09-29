# Import des bibliothèques ---------------------------------------------------------------------------------------------
from Fonction_globales import *
from Code_A1Z26 import decoder_a1z21



# Fonctions ------------------------------------------------------------------------------------------------------------
def extraire_nombres_caractere(texte):
    return re.findall(r"\d+", texte)

# Fonction utilisée dans la fonction principale
def decoder_0_non_1_a1z21(texte):
    nombres = extraire_nombres_caractere(texte)
    print(nombres)
    nombres_utiles = [n for n in nombres if str(n)[0] == '1']
    print(nombres_utiles)
    nombres_extraits = [n[1:] for n in nombres_utiles]
    print(nombres_extraits)
    print(' '.join(nombres_extraits))
    return decoder_a1z21(' '.join(nombres_extraits))



# Main pour test / usage unique ----------------------------------------------------------------------------------------
def main():
    text_test = safe_input("le texte à decoder")
    resultats = decoder_0_non_1_a1z21(text_test)
    afficher_resultat(resultats[0])


if __name__ == '__main__':
    main()
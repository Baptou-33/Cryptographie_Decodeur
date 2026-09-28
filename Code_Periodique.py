# Import des bibliothèques ---------------------------------------------------------------------------------------------
from Score_texte import score_francais, CARACTERE_INCONNU



# Initialisation -------------------------------------------------------------------------------------------------------
# Table périodique : numéro atomique -> symbole chimique (données fixes, ne changent jamais)
SYMBOLES = [
    None, # le 0 ne correspond à aucun élément
    "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
    "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
    "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
    "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
    "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
    "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
    "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
    "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
    "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
    "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
    "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og",
]



# Fonctions ------------------------------------------------------------------------------------------------------------
def convertir_token(mot):
    if mot.isdigit():
        numero = int(mot)
        if 1 <= numero < len(SYMBOLES):
            return SYMBOLES[numero]
        return CARACTERE_INCONNU # Nombre ne correspondant à aucun élément
    return mot  # Si ce n'est pas un nombre, on le garde tel quel

def appliquer_periodique(texte):
    mots = texte.split()
    return ''.join(convertir_token(mot) for mot in mots)

# Fonction utilisée dans la fonction principale
def decoder_periodique(texte):
    resultat = appliquer_periodique(texte)
    score = score_francais(resultat)
    return [("Table périodique", score, resultat, None)]



# Main pour test / usage unique ----------------------------------------------------------------------------------------
def main():
    text_test = input("Texte à déchiffrer: ")
    resultats = decoder_periodique(text_test)
    nom, score, texte_decode, decalage = resultats[0]
    print(f"\n{nom} a décodé :\n"
          f"{texte_decode}\n"
          f"avec un score de {score}")


if __name__ == '__main__':
    main()
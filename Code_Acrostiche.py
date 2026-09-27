# Import des bibliothèques ---------------------------------------------------------------------------------------------
from Score_texte import score_francais, extraire_mots



# Fonctions ------------------------------------------------------------------------------------------------------------
def extraire_acrostiche(texte):
    mots = extraire_mots(texte)
    return ''.join(mot[0] for mot in mots)  # Première lettre de chaque mot trouvé


# Fonction utilisée dans la fonction principale
def decoder_acrostiche(texte):
    resultat = extraire_acrostiche(texte)
    score = score_francais(resultat)
    return [("Acrostiche (1ere lettre de chaque mot)", score, resultat, None)]



# Main pour test / usage unique ----------------------------------------------------------------------------------------
def main():
    text_test = input("Texte à déchiffrer: ")
    resultats = decoder_acrostiche(text_test)
    nom, score, texte_decode, decalage = resultats[0]
    print(f"\n{nom} a décodé :\n"
          f"{texte_decode}\n"
          f"avec un score de {score}\n")


if __name__ == '__main__':
    main()
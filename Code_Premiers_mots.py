# Import des bibliothèques ---------------------------------------------------------------------------------------------
from Score_texte import score_francais, extraire_mots



# Fonctions ------------------------------------------------------------------------------------------------------------
def extraire_premiers_mots(texte):
    phrases = texte.split(".")

    premiers_mots = []
    for phrase in phrases:
        phrase = phrase.strip()
        # On ignore les phrases vides
        if not phrase:
            continue

        mots = phrase.split()
        if mots:
            premiers_mots.append(mots[0])
    return " ".join(premiers_mots)


# Fonction utilisée dans la fonction principale
def decoder_premiers_mots(texte):
    resultat = extraire_premiers_mots(texte)
    score = score_francais(resultat)
    return [("Premiers mots de chaque phrase", score, resultat, None)]



# Main pour test / usage unique ----------------------------------------------------------------------------------------
def main():
    text_test = input("Texte à déchiffrer: ")
    resultats = decoder_premiers_mots(text_test)
    nom, score, texte_decode, parametre = resultats[0]
    print(f"\n{nom} a décodé :\n"
          f"{texte_decode}\n"
          f"avec un score de {score}\n")


if __name__ == '__main__':
    main()
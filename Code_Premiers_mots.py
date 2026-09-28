# Import des bibliothèques ---------------------------------------------------------------------------------------------
from Fonction_globales import *



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
    text_test = safe_input("le texte à decoder")
    resultats = decoder_premiers_mots(text_test)
    afficher_resultat(resultats[0])


if __name__ == '__main__':
    main()
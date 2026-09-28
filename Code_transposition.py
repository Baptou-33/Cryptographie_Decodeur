# Import des bibliothèques ---------------------------------------------------------------------------------------------
from Fonction_globales import *



# Fonctions ------------------------------------------------------------------------------------------------------------
def diviseurs(n):
    # On ne prend pas 1 et n, car ça ne changerait rien
    return [d for d in range(2, n) if n % d == 0]

def appliquer_transposition(texte, colonnes):
    lignes = len(texte) // colonnes
    grille = [texte[i * colonnes:(i + 1) * colonnes] for i in range(lignes)]
    # Lecture colonne par colonne
    return ''.join(grille[ligne][col] for col in range(colonnes) for ligne in range(lignes))

def est_colonnes_valide(parametres, texte):
    try:
        valeur = int(parametres)
    except (ValueError, TypeError):
        return False
    return valeur in diviseurs(len(texte))

# Fonction utilisée dans la fonction principale
def decoder_transposition(texte, parametres):
    if est_colonnes_valide(parametres, texte):
        valeur = int(parametres)
        colonnes_a_tester = {valeur, len(texte) // valeur}
    else:
        colonnes_a_tester = diviseurs(len(texte))

    resultats = []
    for colonnes in colonnes_a_tester:
        texte_decode = appliquer_transposition(texte, colonnes)
        score = score_francais(texte_decode)
        resultats.append(("Code transposition", score, texte_decode, colonnes))

    if not resultats:
        # Nombre premier donc aucun tableau possible
        return []

    resultats.sort(key=lambda x: x[1], reverse=True)
    meilleur_score = resultats[0][1]
    return [r for r in resultats if r[1] == meilleur_score]  # On envoie tous les premiers



# Main pour test / usage unique ----------------------------------------------------------------------------------------
def main():
    text_test = safe_input("le texte à decoder")
    parametre = safe_input("les paramètres")
    resultats = decoder_transposition(text_test, parametre)
    afficher_resultat(resultats[0])


if __name__ == '__main__':
    main()
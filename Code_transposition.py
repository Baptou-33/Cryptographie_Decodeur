# Import des bibliothèques ---------------------------------------------------------------------------------------------
from Score_texte import score_francais



# Fonctions ------------------------------------------------------------------------------------------------------------
def diviseurs(n):
    # On ne prend pas 1 et n, car ça ne changerait rien
    return [d for d in range(2, n) if n % d == 0]

def appliquer_transposition(texte, colonnes):
    lignes = len(texte) // colonnes
    grille = [texte[i * colonnes:(i + 1) * colonnes] for i in range(lignes)]
    # Lecture colonne par colonne
    return ''.join(grille[ligne][col] for col in range(colonnes) for ligne in range(lignes))

# Fonction utilisée dans la fonction principale
def decoder_transposition(texte):
    resultats = []
    for colonnes in diviseurs(len(texte)):
        texte_decode = appliquer_transposition(texte, colonnes)
        score = score_francais(texte_decode)
        resultats.append(("Code transposition", score, texte_decode, colonnes))
    resultats.sort(key=lambda x: x[1], reverse=True)
    meilleur_score = resultats[0][1]
    return [r for r in resultats if r[1] == meilleur_score]  # On envoie tous les premiers



# Main pour test / usage unique ----------------------------------------------------------------------------------------
def main():
    text_test = input("Texte à déchiffrer: ")
    resultats = decoder_transposition(text_test)
    nom, score, texte_decode, colonne = resultats[0]
    print(f"\n{nom} a décodé :\n"
          f"{texte_decode}\n"
          f"avec un score de {score}\n"
          f"et avec des colonnes de -{colonne}")


if __name__ == '__main__':
    main()
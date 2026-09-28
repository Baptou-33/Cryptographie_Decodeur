# Import des bibliothèques ---------------------------------------------------------------------------------------------
from Fonction_globales import *



# Fonctions ------------------------------------------------------------------------------------------------------------
def nombre_lettre(touche, clicks):
    if touche < 2 or touche > 9:
        return CARACTERE_INCONNU
    if touche == 9:
        if clicks >4:
            return CARACTERE_INCONNU
    else:
        if clicks > 3:
            return CARACTERE_INCONNU
    return chr((touche-2) * 3 + clicks - 1 + ord('a'))

def appliquer_clavier_9_touches(texte, sens = 0):
    nombres = extraire_nombres(texte)
    if sens == 0:
        return ''.join(nombre_lettre(n//10, n%10) for n in nombres)
    return ''.join(nombre_lettre(n % 10, n // 10) for n in nombres)

def decoder_clavier_9_touches(texte, sens = -1):
    resultats = []

    if sens in (0, 1):
        parametres = {sens}
    else:
        parametres = range(1)

    for i in parametres:
        resultat = appliquer_clavier_9_touches(texte, i)
        score = score_francais(resultat)
        resultats.append(("Code Clavier 9 touches", score, resultat, i))

    resultats.sort(key=lambda x: x[1], reverse=True)
    meilleur_score = resultats[0][1]
    return [r for r in resultats if r[1] == meilleur_score] # On envoie tous les premiers



# Main pour test / usage unique ----------------------------------------------------------------------------------------
def main():
    text_test = safe_input("le texte à decoder")
    resultats = decoder_clavier_9_touches(text_test)
    afficher_resultat(resultats[0])


if __name__ == '__main__':
    main()
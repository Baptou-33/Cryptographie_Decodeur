# Import des bibliothèques ---------------------------------------------------------------------------------------------
from Fonction_globales import *
import string



# Fonctions ------------------------------------------------------------------------------------------------------------
def decaler_lettre(lettre, decalage):
    if lettre in string.ascii_lowercase:
        # On fait - décalage, car on décode et ord(lettre) = son code numérique : ord('a') = 97
        return chr((ord(lettre) - ord('a') - decalage) % 26 + ord('a'))
    if lettre in string.ascii_uppercase:
        return chr((ord(lettre) - ord('A') - decalage) % 26 + ord('A'))
    return lettre # Si c'est un autre symbole ou chiffre, on le laisse tel quel

def appliquer_cesar(texte, decalage):
    return ''.join(decaler_lettre(c, decalage) for c in texte)

def est_decalage_valide(parametres):
    try:
        valeur = int(parametres)
    except (ValueError, TypeError):
        return False
    return 1 <= valeur <= 25

def cesar_brute_force(texte, decalages_a_tester=range(1, 26)):
    resultats = []
    for decalage in decalages_a_tester:
        texte_decode = appliquer_cesar(texte, decalage)
        score = score_francais(texte_decode)
        resultats.append(("Code César", score, texte_decode, decalage))
    return resultats

# Fonction utilisée dans la fonction principale
def decoder_cesar(texte, parametres=None):
    if est_decalage_valide(parametres):
        valeur = int(parametres)
        resultats = cesar_brute_force(texte, [valeur, -valeur])
    else:
        resultats = cesar_brute_force(texte)
    resultats.sort(key=lambda x: x[1], reverse=True)
    meilleur_score = resultats[0][1]
    return [r for r in resultats if r[1] == meilleur_score]  # On envoie tous les premiers



# Main pour test / usage unique ----------------------------------------------------------------------------------------
def main():
    text_test = safe_input("le texte à decoder")
    parametre = safe_input("les paramètres")
    resultats = decoder_cesar(text_test, parametre)
    for i in resultats:
        afficher_resultat(i)


if __name__ == '__main__':
    main()
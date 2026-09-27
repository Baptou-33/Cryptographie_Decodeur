# Import des bibliothèques ---------------------------------------------------------------------------------------------
import string
from Score_texte import score_francais



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

def cesar_brute_force(texte, decalages_a_tester=range(26)):
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
    text_test = input("Texte à déchiffrer: ")
    parametre = input("Paramètre: ")
    resultats = decoder_cesar(text_test, parametre)
    nom, score, texte_decode, decalage = resultats[0]
    print(f"\n{nom} a décodé :\n"
          f"{texte_decode}\n"
          f"avec un score de {score}\n"
          f"et avec un décalage de {decalage}")


if __name__ == '__main__':
    main()
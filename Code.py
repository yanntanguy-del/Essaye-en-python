import random

def jouer():
    print("=" * 40)
    print(" JEU DE DEVINETTE ")
    print("=" * 40)

    # L'ordi choisit un nombre entre 1 et 100
    nombre_secret = random.randint(1, 100)
    nombre_essais = 0
    max_essais = 10

    print(f"J'ai choisi un nombre entre 1 et 100.")
    print(f"Tu as {max_essais} essais pour le trouver. Bonne chance !\n")

    while nombre_essais < max_essais:  # On demande une réponse au joueur
        try:
            guess = int(input("Ta devinette : "))
        except ValueError:
            print("  Entre un nombre entier !\n")
            continue

        nombre_essais += 1
        essais_restants = max_essais - nombre_essais

        # On compare avec le nombre secret
        if guess < nombre_secret:
            print(f" Trop petit !")
        elif guess > nombre_secret:
            print(f" Trop grand !")
        else:
            print(f"\n Bravo ! Tu as trouvé {nombre_secret} en {nombre_essais} essai(s) !")
            return  # On quitte la fonction, le joueur a gagné

        # On affiche les essais restants
        if essais_restants > 0:
            print(f"   ({essais_restants} essai(s) restant(s))\n")

    # Si on arrive ici, le joueur a perdu
    print(f"\n Perdu ! Le nombre secret était {nombre_secret}.")


def main():
    jouer()

    # Proposer de rejouer
    while True:
        rejouer = input("\nVeux-tu rejouer ? (oui / non) : ").strip().lower()
        if rejouer in ("oui", "o"):
            print()
            jouer()
        elif rejouer in ("non", "n"):
            print("À bientôt ! ")
            break
        else:
            print("Réponds par 'oui' ou 'non'.")


# Point d'entrée du programme
if __name__ == "__main__":
    main()

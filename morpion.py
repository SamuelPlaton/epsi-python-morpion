import checks

def afficher_tableau(tab):
    for row in tab:
        for element in row:
            print(element, end=" ")
        print("")


def jouer_case(tab, signe):
    # Initial play, reset if position is not defined
    row = int(input("Entrez un numéro de ligne : "))
    while row > len(tab):
        row = int(input("Entrez un numéro de ligne VALIDE : "))
    column = int(input("Entrez un numéro de colonne : "))
    while column > len(tab):
        row = int(input("Entrez un numéro de colonne VALIDE : "))

    # If position is already picked
    while tab[row-1][column-1] != "-":
        print("INVALIDE : CET EMPLACEMENT EST DEJA PRIS")
        row = int(input("Entrez un numéro de ligne : "))
        while row > len(tab):
            row = int(input("Entrez un numéro de ligne VALIDE : "))
        column = int(input("Entrez un numéro de colonne : "))
        while column > len(tab):
            row = int(input("Entrez un numéro de colonne VALIDE : "))

    tab[row-1][column-1] = signe
    return tab

def lancer_partie():
    # Initialise variables
    tab = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]] # Initial tab
    win = 0 # if win settled
    actif = "X" # Active player

    # While there is no win
    while win != 1:
        print(actif+" Joue")
        afficher_tableau(tab) # Display tab
        tab = jouer_case(tab, actif) # The player play a case
        win = checks.check_victoire(tab, actif) # Check if there is a win
        if win == 1 : break # Don't switch player if there is a win
        actif = "Y" if actif == "X" else "X"

    afficher_tableau(tab)
    print("Bravo ! ")
    print(actif+" a gagné la partie !")

lancer_partie()
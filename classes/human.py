from classes.player import Player

class Human(Player):
    def __init__(self, signe):
        self.signe = signe


    def jouer_case(self, tab):
        # Initial play, reset if position is not defined
        row = int(input("Entrez un numéro de ligne : "))
        while row > len(tab):
            row = int(input("Entrez un numéro de ligne VALIDE : "))
        column = int(input("Entrez un numéro de colonne : "))
        while column > len(tab):
            row = int(input("Entrez un numéro de colonne VALIDE : "))

        # If position is already picked
        while tab[row - 1][column - 1] != "-":
            print("INVALIDE : CET EMPLACEMENT EST DEJA PRIS")
            row = int(input("Entrez un numéro de ligne : "))
            while row > len(tab):
                row = int(input("Entrez un numéro de ligne VALIDE : "))
            column = int(input("Entrez un numéro de colonne : "))
            while column > len(tab):
                row = int(input("Entrez un numéro de colonne VALIDE : "))

        tab[row - 1][column - 1] = self.signe
        return tab
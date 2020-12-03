# Class game
# Init players and a referee
class Game:
    def __init__(self, player1, player2, referee):
        self.player1 = player1
        self.player2 = player2
        self.referee = referee

    # Display our tab
    def afficher_tableau(self, tab):
        for row in tab:
            for element in row:
                print(element, end=" ")
            print("")

    # Launch our game
    def lancer_partie(self):
        # Initialise variables
        tab = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]  # Initial tab
        win = 0  # if win settled
        actif = self.player1  # Active player

        # While there is no win
        while win != 1:
            print(actif.signe + " Joue")
            self.afficher_tableau(tab)  # Display tab
            tab = actif.jouer_case(tab)  # The player play a case
            win = self.referee.check_victoire(tab, actif.signe)  # Check if there is a win
            if win == 1: break  # Don't switch player if there is a win
            actif = self.player2 if actif == self.player1 else self.player1

        self.afficher_tableau(tab)
        print("Bravo ! ")
        print(actif.signe + " a gagné la partie !")
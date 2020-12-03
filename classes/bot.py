import random
from classes.player import Player

class Bot(Player):
    def __init__(self, signe, difficulty):
        self.signe = signe
        self.difficulty = difficulty

    def jouer_case(self, tab):
        if self.difficulty == "easy":
            return self.jouer_case_easy(tab)
        elif self.difficulty == "hard":
            return self.jouer_case_hard(tab)

    def jouer_case_easy(self, tab):
        # Initial play, reset if position is not defined
        max_row = len(tab)
        row = random.randint(0, max_row-1)
        max_column = len(tab[row])
        column = random.randint(0, max_column-1)

        while(tab[row][column] != "-"):
            row = random.randint(0, max_row - 1)
            max_column = len(tab[row])
            column = random.randint(0, max_column - 1)

        tab[row][column] = self.signe
        return tab

    def jouer_case_hard(self, tab):
        for row in tab:
            for element in row:
                if element != "-" and element != self.signe: # If enemy sign
                    enemyRow = tab.index(row)
                    enemyColumn = row.index(element)
                    if enemyRow+1 < len(tab):
                        if tab[enemyRow+1][enemyColumn] == "-":
                            tab[enemyRow+1][enemyColumn] = self.signe
                        elif enemyColumn+1 < len(tab) and tab[enemyRow+1][enemyColumn+1] == "-":
                            tab[enemyRow+1][enemyColumn+1] = self.signe
                        elif enemyColumn-1 >= 0 and tab[enemyRow+1][enemyColumn-1] == "-" :
                            tab[enemyRow + 1][enemyColumn - 1] = self.signe
                        else:
                            tab = self.jouer_case_easy(tab)
                    elif enemyRow - 1 >=0:
                        if tab[enemyRow - 1][enemyColumn] == "-":
                            tab[enemyRow - 1][enemyColumn] = self.signe
                        elif enemyColumn + 1 < len(tab) and tab[enemyRow - 1][enemyColumn+1] == "-":
                            tab[enemyRow - 1][enemyColumn + 1] = self.signe
                        elif enemyColumn - 1 >= 0 and tab[enemyRow - 1][enemyColumn] == "-":
                            tab[enemyRow - 1][enemyColumn - 1] = self.signe
                        else:
                            tab = self.jouer_case_easy(tab)
                    else:
                        tab = self.jouer_case_easy(tab)
                    return tab
from classes.human import Human
from classes.referee import Referee
from classes.game import Game
from classes.bot import Bot

players = input("1 ou 2 joueurs ? ")
sign = input("Symbole joueur 1 : ")
player1 = Human(sign[0])

if(players == "2"):
    sign = input("Symbole joueur 2 : ")
    player2 = Human(sign[0])
else:
    difficulty = input("Difficulté easy (1) ou hard (2) : ")
    if difficulty == 1:
        player2 = Bot("Y", "easy")
    else:
        player2 = Bot("Y", "hard")

referee = Referee()
game = Game(player1, player2, referee)

game.lancer_partie()
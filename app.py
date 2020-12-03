from classes.human import Human
from classes.referee import Referee
from classes.game import Game
from classes.bot import Bot

player1 = Human("X")
player2 = Bot("Y", "hard")
referee = Referee()
game = Game(player1, player2, referee)

game.lancer_partie()
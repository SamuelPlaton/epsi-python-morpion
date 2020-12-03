from abc import ABC, abstractmethod

class Player(ABC):

    def __init__(self, signe):
        self.signe = signe

    @abstractmethod
    def jouer_case(self, tab):
        ...
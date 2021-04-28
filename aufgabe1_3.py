# Importiere Metaklasse
import abc

#Player
class Player():
    def __init__(self, player):
        self.player = player  

    def trinke(self):
        print("Trinke")

    def esse(self):
        print("Esse")

    def wandere(self):
        print("Wandere")

    def kaempfe(self):
        print("Kämpfe")

    def verteidige(self):
        print("Verteidige")

# Interface-Klasse-Command
class Command (metaclass=abc.ABCMeta):
    def __init__(self, player: Player):
        self.player = player
    
    def execute(self):
        raise NotImplementedError
        
class EsseKommando(Command):
    def execute(self):
        self.player.esse()

class TrinkeKommando(Command):
    def execute(self):
        self.player.trinke()

class VerteidigeKommando(Command):
    def execute(self):
        self.player.verteidige()

class WandereKommando(Command):
    def execute(self):
        self.player.wandere()

class KaempfeKommando(Command):
    def execute(self):
        self.player.kaempfe()

class TrinkeKommando(Command):
    def execute(self):
        self.player.trinke()

class Invoker:
    def __init__ (self):
        self.taste = {}
      
    def belegeTaste(self, taste, command: Command):
        self.taste[taste] = command

    def drueckeTaste(self, taste):
        self.taste[taste].execute()

mario = Player("Mario")
tastatur = Invoker()
tastatur.belegeTaste("x", KaempfeKommando(mario))
tastatur.belegeTaste("y", EsseKommando(mario))
tastatur.drueckeTaste("x")
tastatur.drueckeTaste("y")








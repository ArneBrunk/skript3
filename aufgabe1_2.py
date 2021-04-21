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
        pass

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
        self.taste1 = None
        self.taste2 = None
    
    def belegeTaste1(self, command: Command):
        self.taste1 = command
    
    def belegeTaste2(self, command: Command):
        self.taste2 = command
    
    def drueckeTaste1(self):
        self.taste1.execute()
    
    def drueckeTaste2(self):
        self.taste2.execute()

mario = Player("Mario")
tastatur = Invoker()

tastatur.belegeTaste1(WandereKommando(mario))
tastatur.belegeTaste2(TrinkeKommando(mario))

print("Jetzt drücke ich Taste 1")
tastatur.drueckeTaste1()

print("Jetzt drücke ich Taste 2")
tastatur.drueckeTaste2()





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
        self.aktion1 = None
        self.aktion2 = None
    
    def belegeAktion1(self, command: Command):
        self.aktion1 = command
    
    def belegeAktion2(self, command: Command):
        self.aktion2 = command
    
    def drueckeAktion1(self):
        self.aktion1.execute()
    
    def drueckeAktion2(self):
        self.aktion2.execute()

mario = Player("Mario")
tastatur = Invoker()

tastatur.belegeAktion1(WandereKommando(mario))
tastatur.belegeAktion2(TrinkeKommando(mario))

print("Jetzt mache Aktion 1")
tastatur.drueckeAktion1()

print("Jetzt mache Aktion 2")
tastatur.drueckeAktion2()





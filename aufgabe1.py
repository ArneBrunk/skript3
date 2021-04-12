# Importiere Metaklasse
import abc
# Interface-Klasse-Command
class Command (metaclass=abc.ABCMeta):
    def __init__(self, player: Player):
        self.player = player
    
    def execute():
        pass

#Command-Klasse
class CommandTrinke(Command):
    def execute():
        print("Trinke")

class CommandEsse(command):
    def execute():
        print("Esse")

#Player
class Player():
    def __init__(self, player):
        self.player = player  

#Invoker
class Invoker():
    def setBefehl(self, taste, aktion):
        pass


#main
tastatur = Invoker ():

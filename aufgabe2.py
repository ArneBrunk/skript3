# Importiere Metaklasse
import abc

#Player
class Player():
    def __init__(self, player):
        self.player = player  

# Interface-Klasse-Command
class Command (metaclass=abc.ABCMeta):
    def __init__(self, player: Player):
        self.player = player
    
    def execute(self):
        pass

#Command-Klasse
class CommandTrinke(Command):
    def execute(self):
        print("Trinke")

class CommandEsse(Command):
    def execute(self):
        print("Esse")

class CommandVerteidige(Command):
    def execute(self):
        print("Verteidige")

class CommandWandere(Command):
    def execute(self):
        print("Wandere")
class CommandKaempfe(Command):
    def execute(self):
        print("Kämpfe")

class CommandKombi(Command):
    def __init__(self, command_liste :list ):
        self.command_liste = command_liste
    def execute(self):
        for command in self.command_liste:
            command.execute()


        


#Invoker
class Invoker():
    def setBefehl(self, taste, aktion):
        self.aktion = aktion
        self.taste = taste
        globals ()[self.taste] = self.aktion

    def setKombi(self, taste, aktion:list):
        self.taste = taste 
        self.checkliste = aktion
        globals ()[self.taste] = CommandKombi(self.checkliste)
                  

       
#main
Mario = Player("Mario")
tastatur = Invoker ()
tastatur.setBefehl("command_x", CommandTrinke(Mario))
tastatur.setBefehl("command_y", CommandEsse(Mario))
tastatur.setKombi("command_6", [CommandEsse(Mario), CommandTrinke(Mario), CommandWandere(Mario)])
command_y.execute()
command_x.execute()
command_6.execute()


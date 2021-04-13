class Spiel():
    def __init__ (self, shipname, titel):
        shipCreator = EnemeyShipCreator()
        self.ship = shipCreator.createShip(shipname, titel)


#creator
class EnemeyShipCreator():
    def createShip(self, name, titel):
        if name == "UFO":
            ship = UFOEnemyShip(titel)
        elif name == "Rocket":
            ship = RocketEnemyShip(titel)
        ship.__init__(titel)
        return ship

        

#class Ship
class Ship():
    def __init__ (self, name):
        self.name = name
        self.damage = 50
    def followHeroShip(self):
        pass
    def displayEnemyShip(self):
        pass
    def enemeyShipsShoots(self):
        pass
    def setDamage(self, dmg):
        self.damage = dmg
    def getDamage(self):
        print(self.damage)

#Schifftypen
class RocketEnemyShip(Ship):
    def setName(self, name):
        self.name = name
    
    def getName(self):
        print("Dies ist das Raketenschiff:", self.name)

class UFOEnemyShip(Ship):
    def setName(self, name):
        self.name = name

    def getName(self):
        print("Dies ist das UFO:", self.name)

#main
newgame = Spiel("UFO", "Arne")
newgame.ship.getDamage()
newgame.ship.getName()
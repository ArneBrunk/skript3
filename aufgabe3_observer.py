import abc
#ObserverSubjekt
class ObserverSubjekt:
    def __init__(self):
        self._observers = []
    
    def register(self, observer):
        self._observers.append(observer)
    
    def unregister(self, observer):
        self._observers.remove(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self)

#Observer
class Observer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, subject:ObserverSubjekt):
        pass

class HealthDead(Observer):
    def __init__ (self):
        self._dead  = False
    
    def update(self, subjekt):
        if subjekt.healthpoints <= 0 and self._dead == False:
            self._dead = True
            subjekt.healthpoints = 0
            print("You are dead!")
            

class MaxHealth(Observer):
    def __init__ (self):
        self.maxHealth = False
    
    def update(self, subjekt):
        if subjekt.healthpoints > subjekt.maxhealthpoints:
            self.maxHealth = True
            subjekt.healthpoints = subjekt.maxhealthpoints
            print("You have Full-HP!")
        self.maxHealth = False

#Classes

class HealthGUI:
    def render(self, current, max):
        print("Health:", current, "/", max)

class Player(ObserverSubjekt):
    def __init__(self, healthGUI: HealthGUI, maxhealthpoints: int):
        ObserverSubjekt.__init__(self)
        self.healthGUI = healthGUI
        self.healthpoints = maxhealthpoints
        self.maxhealthpoints = maxhealthpoints
    
    def getHit(self, hitPoints):
        self.healthpoints -= hitPoints
        self.notify()
        self.healthGUI.render(self.healthpoints, self.maxhealthpoints)
    
    def getHealth(self, healthPoints):
        self.healthpoints += healthPoints
        self.notify()
        self.healthGUI.render(self.healthpoints, self.maxhealthpoints)

#main    
healthGUI = HealthGUI()

player = Player(healthGUI, 50)
player.register(HealthDead())
player.register(MaxHealth())

player.getHit(30)
player.getHit(15)
player.getHealth(10)
player.getHealth(100)
player.getHit(20)
player.getHit(100)

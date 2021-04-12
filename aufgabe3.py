class EventGUI:
    def dead(self):
        print("You are dead!")

class HealthGUI:
    def render(self, current, max):
        print("Health:", current, "/", max)

class Player:
    def __init__(self, healthGUI: HealthGUI, eventGUI:EventGUI, maxhealthpoints: int):
        self.healthGUI = healthGUI
        self.eventGUI = eventGUI
        self.healthpoints = maxhealthpoints
        self.maxhealthpoints = maxhealthpoints
    
    def getHit(self, hitPoints):
        self.healthpoints -= hitPoints
        if (self.healthpoints <= 0):
            self.healthpoints = 0
            self.eventGUI.dead()
        self.healthGUI.render(self.healthpoints, self.maxhealthpoints)
    
    def getHealth(self, healthPoints):
        self.healthpoints += healthPoints
        if (self.healthpoints > self.maxhealthpoints):
            self.healthpoints = self.maxhealthpoints
        self.healthGUI.render(self.healthpoints, self.maxhealthpoints)

#main    
healthGUI = HealthGUI()
eventGUI = EventGUI()
player = Player(healthGUI, eventGUI, 50)

player.getHit(30)
player.getHit(15)
player.getHealth(10)
player.getHit(20)

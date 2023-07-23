from Setting import *
from DiamondSquareMap import DiamondSquareMap


class App:
    def __init__(self):
        self.nextState = 0
        w = 65
        self.map = DiamondSquareMap(w, w, -150, 150, -2, 2)
        # self.map = Map(129, 129)

    def __eq__(self, other):
        if other.lower() == "menu":
            return True
        else:
            return False
    
    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.map.regenerate()

    def run(self):
        self.map.draw()

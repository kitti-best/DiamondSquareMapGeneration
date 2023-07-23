from Setting import *
from DiamondSquareMap import DiamondSquareMap


class App:
    def __init__(self, procedural_map: DiamondSquareMap):
        self.nextState = 0
        self.map = procedural_map
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

from Setting import *
from DiamondSquareMap import DiamondSquareMap


class App:
    def __init__(self):
        self.nextState = 0
        self.maps = []
        procedural_map1 = DiamondSquareMap((0, 0), MAPW, MAPH, -15, 15, -2, 2, (SCREENW, SCREENH))
        # procedural_map2 = DiamondSquareMap((SCREENH - 1, 0), MAPW, MAPH, -15, 15, -2, 2, (SCREENH, SCREENH))
        self.maps += [procedural_map1]

    def __eq__(self, other):
        if other.lower() == "menu":
            return True
        else:
            return False

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                for p_map in self.maps:
                    p_map.regenerate()

    def run(self):
        for p_map in self.maps:
            p_map.draw()

import pygame.display
import sys
import Color
from DiamondSquareMap import DiamondSquareMap
from Setting import *
from App import App


class Main:
    def __init__(self):
        self.state = []
        procedural_map = self.__make_map_instance()
        self.state.append(App(procedural_map))

    def __make_map_instance(self):
        # w, h, min_c, max_c, min_r, max_r = [int(e) for e in input("w, h, min_c, max_c, min_r, max_r : ").split()]
        pos = (0, 0)
        w, h, min_c, max_c, min_r, max_r = MAPW, MAPH, -50, 50, -5, 5
        return DiamondSquareMap(pos, w, h, min_c, max_c, min_r, max_r)

    def run(self):
        RUNNING = 1
        while RUNNING:
            pygame.display.set_caption(str(round(CLOCK.get_fps())))
            # clear screen
            SCREEN.fill(Color.PITCHBLACK)

            # wait
            delta = CLOCK.tick(FPS)/1000

            # handle quiting
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # handle game state
            current_state = self.state[-1]
            current_state.update(events)
            current_state.run()

            # update screen
            pygame.display.update()


main = Main()

if __name__ == '__main__':
    main.run()

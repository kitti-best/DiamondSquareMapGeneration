import pygame.display
import sys
import Color
from Setting import *
from App import App


class Main:
    def __init__(self):
        self.state = []
        self.state.append(App())

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

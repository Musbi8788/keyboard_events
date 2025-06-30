import sys
import pygame


class KeyboardEvents():
    """A classs to manage the keyboard events game
    """

    def __init__(self,):
        """Initailize the game's resources.
        """
        pygame.init()

        self.screen = pygame.display.set_mode((800, 300))
        pygame.display.set_caption("Hack the keyboard")
        self.bg_color = (255, 0, 0)

    def run_game(self):
        game_running = True
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key:
                        print(event.unicode)
                self._update_screen()

                
    def _update_screen(self):
        """update screen
        """
        self.screen.fill(self.bg_color)
        pygame.display.flip()

if __name__ == "__main__":
    hk = KeyboardEvents()
    hk.run_game()
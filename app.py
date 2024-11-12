'''app'''
import pygame
from pygame.locals import *

class App:
    '''App class'''
    def __init__(self) -> None:
        '''Constructor'''
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 640,400
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.rect1 = pygame.Rect(10,10,100,100)
        self._display_surf.fill((255,255,255))
        pygame.draw.rect(self._display_surf, (255,0,0), self.rect1)
        pygame.display.flip()

    def on_event(self, event):
        '''Check if quit happened'''
        pos = pygame.mouse.get_pos()
        click = self.rect1.collidepoint(pos)
        if event.type == pygame.QUIT:
            self._running = False

        if event.type == pygame.MOUSEBUTTONUP and click:
            print("Quited")
            self._running = False

        if event.type == pygame.MOUSEBUTTONUP and not click:
            pygame.draw.rect(self._display_surf, (225,0,0), self.rect1)
            pygame.display.flip()

        if event.type == pygame.MOUSEBUTTONDOWN and click:
            pygame.draw.rect(self._display_surf, (200,0,0), self.rect1)
            pygame.display.flip()
            print("Clicked")

    def on_cleanup(self):
        '''Cleanup'''
        pygame.quit()

    def on_execute(self) -> None:
        '''mainloop'''

        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
        self.on_cleanup()

if __name__ == "__main__":
    app = App()
    app.on_execute()
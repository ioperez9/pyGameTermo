import pygame, sys
from pygame.locals import *

class mainApp():
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415)) #tamaño pantalla
        pygame.display.set_caption("Termometro") #nombre pantalla
        self.__screen.fill((244, 236, 203)) #color de la pantalla
        
    def __on_close(self):
        pygame.quit()
        sys.exit()
        
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__on_close()
                    
            pygame.display.flip()
            
                   
                    
        
        
    
if __name__ == "__main__":
    pygame.init()
    app = mainApp()
    app.start()
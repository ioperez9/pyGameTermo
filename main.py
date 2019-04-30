import pygame, sys
from pygame.locals import *

class Termometro():
    def __init__(self):
        self.custome = pygame.image.load("images/term.png")
        

class NumbreImput():
    __value = 0
    __strValue = "0"
    __position = [0,0]
    __tamaño = [0,0]
    
    def __init__(self, value= 0):
        self.__font = pygame.font.SysFont("Arial", 24)
        testBlock = self.__font.render(self.__strValue, True (74, 74, 74))
        rect = textBlock.get_rect()
        rect.left = self.__position[0]
        rect.top = self.__position[1]
        rect.size = self.__size
        
        
        


class mainApp():
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415)) #tamaño pantalla
        pygame.display.set_caption("Termometro") #nombre pantalla
        self.__screen.fill((244, 236, 203)) #color de la pantalla
        
        self.termometro = Termometro()
        
        
        
    def __on_close(self):
        pygame.quit()
        sys.exit()
        
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__on_close()
                    
            self.__screen.blit(self.termometro.custome, (30, 150)) #dibuje el termometro   
            pygame.display.flip()
            
                       
    
if __name__ == "__main__":
    pygame.init()
    app = mainApp()
    app.start()
import pygame, sys
from pygame.locals import *

class Termometro():
    def __init__(self):
        self.custome = pygame.image.load("images/term.png")
        

class NumberImput():
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
        
    def value(self, val=None):
        if val=None:
            return self._value
        else:
            val = str(val) #convertir lo que metamos en una cadena
            try:
                self.__value = int(val) #lo volvemos a pasar a num entero
                self.__strValue = val #aquí tendremos lo que ha entrado en cadena
            except:
                pass
    
    def width(self, val=None):
        if val == None:
            return self.__size[0]
        else:
            try:
                self.__size[0]= int(val)
            except:
                pass
            
    def height(self, val=None):
        if val == None:
            return self.__size[1]
        else:
            try:
                self.__size[1]= int(val)
            except:
                pass
            
    def size(self, val=None):
        if val == None:
            return self.__size
        else:
            try:
                w = int(val[0])
                h = int(val[1])
                self.__size = [int(val[0]), int(val[1])]
            except:
                pass 
                      
    def posX(self, val=None):
        if val == None:
            return self.__position[0]
        else:
            try:
                self.__position[0]= int(val)
            except:
                pass
            
    def posY(self, val=None):
        if val == None:
            return self.__position[1]
        else:
            try:
                self.__position[1]= int(val)
            except:
                pass
                        
    def pos(self, val=None):
        if val == None:
            return self.__position
        else:
            try:
                self.__position = [int(val[0]), int(val[1])]
            except:
                pass     
    

class mainApp():
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415)) #tamaño pantalla
        pygame.display.set_caption("Termometro") #nombre pantalla
        self.__screen.fill((244, 236, 203)) #color de la pantalla
        
        self.termometro = Termometro()
        self.entrada = NumberInput()
        self.entrada.height(123)
        
        
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
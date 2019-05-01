import pygame, sys
from pygame.locals import *

class Termometro():
    def __init__(self):
        self.custome = pygame.image.load("images/term.png")
        
    def convertir(self, grados, toUnidad):
        resultado = 0
        if toUnidad == "F":
            resultado = grados * 9/5 + 32
        elif toUnidad == "C":
            resultado = (grados - 32) * 5/9
        else:
            resultado = grados
            
        return "{:10.2f}".format(resultado)
            
            
        
class Selector():
    __tipoUnidad = None
    
    def __init__(self, unidad = "C"):
        self.__customes = []
        self.__customes.append(pygame.image.load("images/posiF.png"))
        self.__customes.append(pygame.image.load("images/posiC.png"))
        
        self.__tipoUnidad = unidad
        
    def custome(self):
        if self.__tipoUnidad == "F":
            return self.__customes[0]
        else:
            return self.__customes[1]
        
    def change(self):
        if self.__tipoUnidad == "F":
            self.__tipoUnidad = "C"
        else:
            self.__tipoUnidad = "F"
    
    
    def unidad(self):
        return self.__tipoUnidad
        

class NumberInput():
    __value = 0
    __strValue = ""
    __position = [0, 0]
    __size = [0, 0]
    __pointsCount = 0
    
    def __init__(self, value=0):
        self.__font = pygame.font.SysFont("Arial", 24)
        #para que solo se puedan meter enteros hacemos lo siguiente:
        self.value(value)
        #podemos hacerlo llamandonos a nosotros mismos def value ya comprueba que sea un entero y no tenemos que repetirnos
        ''' sería lo mismo que esto:
        try:
            self.__value = float(value) #lo transformo 1 en un entero
            self.__strValue = str(value) #lo transformamos en cadena para poder pintarlo en la pantalla, pq solo funciona con cadenas
        except:
            pass
            '''
        
    def on_event(self, event):    
        if event.type == KEYDOWN:
            #comprobar que la tecla presionas es un numero
            if event.unicode.isdigit() and len(self.__strValue) < 10 or (event.unicode == "." and self.__pointsCount == 0): 
            #event.unicode in "0123456789" o if event.isdigit(): #otra manera de comprobar que lo que introduces es un número
                self.__strValue += event.unicode
                #se va añadiendo a strValue los num que introduciomos con el teclado
                self.value(self.__strValue)
                #setter, para que asigne el valor de value (int) y sea lo mismo que lo que está pintado en el cuadro de texto
                if event.unicode == ".":
                    self.__pointsCount += 1
            elif event.key == K_BACKSPACE:
                #si la tecla es retroceder
                if self.__strValue[-1] == ".":
                    self.__pointsCount -= 1
                self.__strValue = self.__strValue[:-1]
                self.value(self.__strValue)
                
    def render(self):
        textBlock = self.__font.render(self.__strValue, True, (74, 74, 74))
        rect = textBlock.get_rect()
        rect.left = self.__position[0]
        rect.top = self.__position[1]
        rect.size = self.__size
        '''
        return {
                "fondo" : rect,
                "texto" : textBlock
            }
            '''
        return (rect, textBlock)
    
    
    def value(self, val=None):
        
        if val == None:
            return self.__value
        else:
            val = str(val)
            #convertir lo que metamos en una cadena
            try:
                self.__value = float(val)
                #lo volvemos a pasar a num entero
                self.__strValue = val
                #aquí tendremos lo que ha entrado en cadena
                if "." in self.__strValue:
                    self.__pointsCount = 1
                else:
                    self.pointsCount = 0
            except:
                pass
    
    def width(self, val=None):
        if val == None:
            return self.__size[0]
        else:
            try:
                self.__size[0]= float(val)
            except:
                pass
            
    def height(self, val=None):
        if val == None:
            return self.__size[1]
        else:
            try:
                self.__size[1]= float(val)
            except:
                pass
            
    def size(self, val=None):
        if val == None:
            return self.__size
        else:
            try:
                w = float(val[0])
                h = float(val[1])
                self.__size = [float(val[0]), float(val[1])]
            except:
                pass 
                      
    def posX(self, val=None):
        if val == None:
            return self.__position[0]
        else:
            try:
                self.__position[0]= float(val)
            except:
                pass
            
    def posY(self, val=None):
        if val == None:
            return self.__position[1]
        else:
            try:
                self.__position[1]= float(val)
            except:
                pass
                        
    def pos(self, val=None):
        if val == None:
            return self.__position
        else:
            try:
                self.__position = [float(val[0]), float(val[1])]
            except:
                pass     
    

class MainApp():
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
         #tamaño pantalla
        self.__screen = pygame.display.set_mode((290, 415))
        pygame.display.set_caption("Termometro") #nombre pantalla
        #self.__screen.fill((244, 236, 203)) #color de la pantalla
        
        self.termometro = Termometro()
        self.entrada = NumberInput("")
        self.entrada.pos((106, 58))
        self.entrada.size((133,28))
        
        self.selector = Selector()
        
        
    def __on_close(self):
        pygame.quit()
        sys.exit()
        
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__on_close()
                
                self.entrada.on_event(event)
               
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.selector.change()
                    grados = self.entrada.value()
                    nuevaUnidad = self.selector.unidad()
               
                    temperatura = self.termometro.convertir(grados, nuevaUnidad)
                  
                    self.entrada.value(temperatura)
                
            #Pintamos el fondo de pantalla
            self.__screen.fill((244, 236, 203)) 

            #dibuje el termometro en su posicion        
            self.__screen.blit(self.termometro.custome, (5, 150))   
            
            #pintamos el cuadro de texto
            text = self.entrada.render()
            #obtenemos rectángulo blanco y foto de texto y lo asignamos a text
            pygame.draw.rect(self.__screen, (255, 255, 255), text[0])
            #pintar reclangulo blanco con sus datos(posicion y tamaño text[0])
            self.__screen.blit(text[1], self.entrada.pos())
            #esto es para pintar el num 0 (text[1])
            
            #pintamos el selector, con blit y le damos el disfraz y la posicion que siempre será la misma:
            self.__screen.blit(self.selector.custome(), (112,110))
            
            pygame.display.flip()
            
                       
    
if __name__ == "__main__":
    pygame.init()
    app = MainApp()
    app.start()
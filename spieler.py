import pygame
from spielfeld import Feld

pygame.init()









class Spieler():
    '''Die Spielerklasse'''

    def __init__(self,x, y):
        self.x=x
        self.y=y
        self.leben = 3
        self.punkte = 0
        self.schaden=1
        self.SpielerIMG_links = pygame.image.load(".\images\TestImage.png")
        self.SpielerIMG_links = pygame.transform.scale(self.SpielerIMG_links, (40, 40))
        self.SpielerIMG = pygame.image.load(".\images\TestImage.png")
        self.SpielerIMG = pygame.transform.scale(self.SpielerIMG, (40, 40))
        self.Aktuelles_bild=self.SpielerIMG
        self.Aktuelles_bild = pygame.transform.scale(self.Aktuelles_bild, (40, 40))
        
        self.spieler_images = ['self.SpielerIMG_links', 'self.SpielerIMG' , 'self.Aktuelles_bild']


    
    




    

        
    
    
    


    
    
    
    

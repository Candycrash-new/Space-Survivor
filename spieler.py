import pygame
from spielfeld import Feld

pygame.init()









class Spieler():
    '''Die Spielerklasse'''

    def __init__(self,x,y, feld_obj):
        self.x=x
        self.y=y
        self.last_position = [x,y]
        self.leben = 3
        self.punkte = 0
        self.schaden=1
        self.side=feld_obj.side
        self.SpielerIMG_links = pygame.image.load(".\images\TestImage.png")
        self.SpielerIMG_links = pygame.transform.scale(self.SpielerIMG_links, (int(0.05*feld_obj.Spielfeld_width), int(0.05*feld_obj.Spielfeld_width)))
        self.SpielerIMG_links = pygame.transform.scale(self.SpielerIMG_links, (int(0.05*feld_obj.Spielfeld_width), int(0.05*feld_obj.Spielfeld_width)))
        self.SpielerIMG_rechts = pygame.image.load(".\images\TestImage.png")
        self.SpielerIMG_rechts = pygame.transform.scale(self.SpielerIMG_rechts, (int(0.05*feld_obj.Spielfeld_width), int(0.05*feld_obj.Spielfeld_width)))
        self.SpielerIMG_oben = pygame.image.load(".\images\TestImage.png")
        self.SpielerIMG_oben = pygame.transform.scale(self.SpielerIMG_oben, (int(0.05*feld_obj.Spielfeld_width), int(0.05*feld_obj.Spielfeld_width)))
        
        
        self.SpielerIMG = pygame.image.load(".\images\TestImage.png")
        self.SpielerIMG = pygame.transform.scale(self.SpielerIMG, (int(0.05*feld_obj.Spielfeld_width), int(0.05*feld_obj.Spielfeld_width)))
        self.aktuelles_bild=self.SpielerIMG
        
        self.spieler_images = ['self.SpielerIMG_links', 'self.SpielerIMG' , 'self.Aktuelles_bild']


    
    




    

        
    
    
    


    
    
    
    

import pygame
from Spielfeld import Feld

pygame.init()
clock = pygame.time.Clock()








class Spieler():
    SpielerIMG = pygame.image.load(r"C:/Users/Mostafa Ganji/Desktop/Spiel_projekt//space.png")
    SpielerIMG = pygame.transform.scale(SpielerIMG, (40, 40))
    x = (Feld.Spielfeld_width * 0.45)
    y = (Feld.Spielfeld_height * 0.8)
    Leben = 3
    punkte = 0
    schaden=1





    

        
    
    
    
    
#Gehören zur Steuerung:
    #if(Leben <= 0):
        #Gui.lost_text()

    
    
    
    

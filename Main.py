
import pygame,sys
from pygame import *
import Personnage
import Background
import Menu
pygame.init() 

h=360
w=640
screen= pygame.display.set_mode((w,h))
clock=pygame.time.Clock()

menu=Menu.Menu(screen)
background=Background.Background(screen)

playerA= Personnage.Personnage(screen)
playerA.x=90
playerA.orientation=1


playerB= Personnage.Personnage(screen)
playerB.x=495
playerB.orientation=-1


while 1:

    for event in pygame.event.get():

        if pygame.mouse.get_pressed()[0]==True:
            clic=True
        elif pygame.mouse.get_pressed()[2]==True:
            clic2=True
        else:
            clic=False
            clic2=False

    menu.setmenu(clic,clic2,(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]))

    if menu.menu==4:

        screen.fill((0,0,0))
        clock.tick(60)
        background.update(8,menu.map)
        playerA.setinfo((0,0),(70,7))
        playerB.setinfo((584,0),(430,7))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        touchesPressees = pygame.key.get_pressed()

        if touchesPressees[pygame.K_DOWN] == True and playerA.compteurchelou<2 :
            playerA.drift=True
            if touchesPressees[pygame.K_RIGHT] == True :
                playerA.orientation=1
                playerA.drift=False
                playerA.dodge=True
            if touchesPressees[pygame.K_LEFT] == True:
                playerA.orientation=-1
                playerA.drift=False
                playerA.dodge=True
        elif touchesPressees[pygame.K_DOWN] == False:
            playerA.compteurchelou=0

        if touchesPressees[pygame.K_RIGHT] == True  and playerA.x<590 and playerA.collide!=1:
            playerA.vitesse=3
            playerA.orientation=1
        elif touchesPressees[pygame.K_LEFT] == True and playerA.x>0  and playerA.collide!=2:
            playerA.vitesse=3
            playerA.orientation=-1
        else:
            playerA.vitesse=0

        if touchesPressees[pygame.K_UP] == True and playerA.energie>=10:
            playerA.saut=True

        if touchesPressees[pygame.K_KP1] == True and playerA.energie>=20:
            if playerA.x>130 and playerA.orientation ==-1:
                playerA.teleport=True
            elif playerA.x<470 and playerA.orientation==1:
                playerA.teleport=True

        if touchesPressees[pygame.K_KP2] == True:
            playerA.attack=True




        if touchesPressees[pygame.K_s] == True and playerB.compteurchelou<2 :
            playerB.drift=True
            if touchesPressees[pygame.K_d] == True :
                playerB.orientation=1
                playerB.drift=False
                playerB.dodge=True
            if touchesPressees[pygame.K_q] == True:
                playerB.orientation=-1
                playerB.drift=False
                playerB.dodge=True

        elif touchesPressees[pygame.K_s] == False:
            playerB.compteurchelou=0
        if touchesPressees[pygame.K_d] == True and playerB.x<590 and playerB.collide!=1:
            playerB.vitesse=3
            playerB.orientation=1
        elif touchesPressees[pygame.K_q] == True and playerB.x>0 and playerB.collide!=2:
            playerB.vitesse=3
            playerB.orientation=-1
        else:
            playerB.vitesse=0
        if touchesPressees[pygame.K_z] == True and playerB.x>0:
            playerB.saut=True

        if touchesPressees[pygame.K_h] == True  and playerB.energie>=20:
            if playerB.x>130 and playerB.orientation==-1:
                playerB.teleport=True
            elif playerB.x<470 and playerB.orientation==1:
                playerB.teleport=True

        if touchesPressees[pygame.K_j] == True:
                playerB.attack=True





        playerA.detect(playerB)
        playerB.detect(playerA)
        playerA.set_perso(menu.persoA)
        playerB.set_perso(menu.persoB)

        if background.ndebut<60:
            playerA.animdebut()
            playerB.animdebut()
            background.ndebut+=1

        elif playerA.vie<=0:
            playerA.lose(playerB)
            playerB.win()
        elif playerB.vie<=0:
            playerB.lose(playerA)
            playerA.win()

        else:

            if playerA.teleport==True:
                playerA.teleportation()
            elif playerA.attack==True:
                playerA.attaquer()
            elif playerA.saut==True:
                playerA.sauter()
            elif playerA.drift==True:
                playerA.actionDrift()
            elif playerA.dodge==True:
                playerA.actionDodge()
            elif playerA.touched==True:
                playerA.stun(playerB)
            else:
                playerA.marche()




            if playerB.teleport==True :
                playerB.teleportation()
            elif playerB.attack==True:
                playerB.attaquer()
            elif playerB.saut==True:
                playerB.sauter()
            elif playerB.drift==True:
                playerB.actionDrift()
            elif playerB.dodge==True:
                playerB.actionDodge()
            elif playerB.touched==True:
                playerB.stun(playerA)
            else:
                playerB.marche()


            playerA.blit()
            playerB.blit()

    pygame.display.update()

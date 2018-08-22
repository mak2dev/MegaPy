import pygame,glob
from PIL import Image


class Personnage():
    def __init__(self,_screen):
        self.x=0
        self.y=260
        self.vie=100
        self.energie=100
        self.degat=0
        self.screen = _screen
        self.largeur=0
        self.hauteur=0
        self.dossier_perso="/perso1"
        self.dossier_fonct="/marche"
        self.dossier_orient="/gauche"
        self.orientation=0
        self.vitesse=0
        self.anim_speed=5
        self.animation= glob.glob("library/personnages"+self.dossier_perso+self.dossier_fonct+self.dossier_orient+"/image_*.png")
        self.animation.sort()
        self.numAnimation=0
        self.numAnimTeleport=0
        self.numAnimAttack=0
        self.numAnimSaut=0
        self.numAnimStun=0
        self.numAnimDodge=0
        self.img=pygame.image.load(self.animation[0])
        self.teleport=False
        self.attack=False
        self.saut=False
        self.collide=0
        self.touched=False
        self.drift=False
        self.dodge=False
        self.tir=False
        self.compteurchelou=0
        self.winnin=False




    def getRect(self):
        return pygame.Rect(self.x,self.y,self.largeur-10,self.hauteur)


    def set_perso(self,perso):

        self.dossier_perso=perso

        if self.orientation==1:
            self.dossier_orient="/droite"
        elif self.orientation==-1:
            self.dossier_orient="/gauche"

        if self.energie<100:
            self.energie+=0.02

        img=Image.open("library/personnages"+self.dossier_perso+self.dossier_fonct+self.dossier_orient+"/image_01.png")
        self.largeur,self.hauteur=img.size



    def setinfo(self,coordimage,coordbar):
        imageperso=pygame.image.load("library/personnages"+self.dossier_perso+"/image_01.png")
        self.screen.blit(imageperso,coordimage)
        if self.vie>=0:
            pygame.draw.rect(self.screen,(167,17,1),(coordbar[0],coordbar[1],1.5*self.vie,15))
        if self.energie<101 and self.energie>=0:
            pygame.draw.rect(self.screen,(30,127,203),(coordbar[0],coordbar[1]+22,1.5*self.energie,15))
        elif self.energie>100:
            pygame.draw.rect(self.screen,(30,127,203),(coordbar[0],coordbar[1]+22,150,15))
            pygame.draw.rect(self.screen,(239,216,7),(coordbar[0],coordbar[1]+22,1.5*self.energie-150,15))

        pixel=pygame.font.Font("library/menu/police.ttf",50)
        win = pixel.render("",True,(255,255,255))

        if self.dossier_perso=="/perso1" and self.winnin==True:
            win = pixel.render("Blue wins!!",True,(0,127,255))
        elif self.dossier_perso=="/perso2" and self.winnin==True:
            win = pixel.render("Red wins!!",True,(187,11,11))
        elif self.dossier_perso=="/perso3" and self.winnin==True:
            win = pixel.render("Purple wins!!",True,(128,0,128))
        elif self.dossier_perso=="/perso4" and self.winnin==True:
            win = pixel.render("Yellow wins!!",True,(240,195,0))
        self.screen.blit(win,(134,160))


    def blit(self):
        self.screen.blit(self.img,(self.x,self.y))

    def animdebut(self):
        self.dossier_fonct="/debut"
        self.animation= glob.glob("library/personnages"+self.dossier_perso+self.dossier_fonct+self.dossier_orient+"/image_*.png")
        self.animation.sort()
        self.anim_speed -= 1
        if self.anim_speed == 0:
            if self.numAnimation==0:
                self.numAnimation=1
            self.img=pygame.image.load(self.animation[self.numAnimation])
            self.anim_speed=7
            if self.numAnimation==len(self.animation)-1:
                pass
            else:
                self.numAnimation+=1
        self.screen.blit(self.img,(self.x,self.y-14))


    def marche(self):
        self.dossier_fonct="/marche"
        self.animation= glob.glob("library/personnages"+self.dossier_perso+self.dossier_fonct+self.dossier_orient+"/image_*.png")
        self.animation.sort()
        self.y=260

        if self.vitesse !=0:
            self.anim_speed -= 1
            self.x+=self.orientation*self.vitesse
            if self.anim_speed == 0:
                if self.numAnimation==0:
                    self.numAnimation=1
                self.img=pygame.image.load(self.animation[self.numAnimation])
                self.anim_speed=5
                if self.numAnimation==len(self.animation)-1:
                    self.numAnimation=0
                else:
                    self.numAnimation+=1
        if self.vitesse==0:
            self.img=pygame.image.load(self.animation[0])
            self.numAnimation=0

    def teleportation(self):

        self.dossier_fonct="/teleport"
        self.animation= glob.glob("library/personnages"+self.dossier_perso+self.dossier_fonct+self.dossier_orient+"/image_*.png")
        self.animation.sort()
        if self.y==260:
            self.y=246

        if self.teleport==True:
            self.anim_speed -= 1
            if self.anim_speed == 0:
                if self.numAnimTeleport==0:
                    self.numAnimTeleport=1
                self.img=pygame.image.load(self.animation[self.numAnimTeleport])
                self.anim_speed=4
                if self.numAnimTeleport==len(self.animation)/2:
                    if self.dossier_orient=="/droite":
                        self.x+=150
                    elif self.dossier_orient=="/gauche":
                        self.x-=150
                    self.numAnimTeleport+=1
                    self.y=246
                elif self.numAnimTeleport==len(self.animation)-1:
                    self.teleport=False
                    self.orientation=self.orientation*-1
                    self.numAnimTeleport=0
                    self.energie-=20
                else:
                    self.numAnimTeleport+=1


    def attaquer(self):
        self.animation= glob.glob("library/personnages"+self.dossier_perso+self.dossier_fonct+self.dossier_orient+"/image_*.png")
        self.animation.sort()
        self.dossier_fonct="/tak"

        if self.attack==True:
            self.anim_speed -= 1
            if self.anim_speed == 0:
                if self.numAnimAttack==0:
                    self.numAnimAttack=1
                self.img=pygame.image.load(self.animation[self.numAnimAttack])
                self.anim_speed=4
                if self.numAnimAttack==len(self.animation)-1:
                    self.attack=False
                    self.numAnimAttack=0
                else:
                    self.numAnimAttack+=1


    def sauter(self):

        self.dossier_fonct="/saut"
        self.animation= glob.glob("library/personnages"+self.dossier_perso+self.dossier_fonct+self.dossier_orient+"/image_*.png")
        self.animation.sort()

        if self.y==260 or self.y==246:
            self.y=236

        if self.saut==True:
            if self.numAnimSaut<len(self.animation)/2:
                self.y-=5
            else:
                self.y+=5
            self.x+=self.orientation*self.vitesse


            self.anim_speed -= 1
            if self.anim_speed == 0:
                if self.numAnimSaut==0:
                    self.numAnimSaut=1
                self.img=pygame.image.load(self.animation[self.numAnimSaut])
                self.anim_speed=5
                if self.numAnimSaut==len(self.animation)-2:
                    self.saut=False
                    self.numAnimSaut=0
                    self.energie-=10
                else:
                    self.numAnimSaut+=1


    def stun(self,other):

        self.dossier_fonct="/stun"
        self.animation= glob.glob("library/personnages"+self.dossier_perso+self.dossier_fonct+self.dossier_orient+"/image_*.png")
        self.animation.sort()
        self.y=261
        if self.x<590 and self.x>0:
            self.x+=(other.orientation-0.3)

        self.anim_speed -= 1
        if self.anim_speed == 0:
            if self.numAnimStun==0:
                self.numAnimStun=1
            self.img=pygame.image.load(self.animation[self.numAnimStun])
            self.anim_speed=4
            if self.numAnimStun==len(self.animation)-1:
                self.numAnimStun=0
            else:
                self.numAnimStun+=1


    def detect(self,other):
        if self.getRect().colliderect(other.getRect()):
            if self.x<=other.x and self.y==other.y:
                self.collide=1
            elif self.x>=other.x and self.y==other.y:
                self.collide=2

            if self.attack==True and self.orientation==1 and self.x<other.x:
                other.touched=True
                other.vie-=0.5
            elif self.attack==True and self.orientation==-1 and self.x>other.x :
                other.touched=True
                other.vie-=0.5
            elif self.dodge==True and self.orientation==other.orientation and self.x>other.x and self.y!=260:
                other.touched=True
                other.vie-=0.2
            elif self.dodge==True and self.orientation!=other.orientation and self.x<other.x and self.y!=260:
                other.touched=True
                other.vie-=0.2
            else :
                other.touched=False

        else:
            self.collide=0
            other.touched=False

    def actionDrift(self):
        self.dossier_fonct="/drift"
        self.animation= glob.glob("library/personnages"+self.dossier_perso+self.dossier_fonct+self.dossier_orient+"/image_*.png")
        self.animation.sort()
        if self.drift==True:
            self.img=pygame.image.load(self.animation[0])
            self.drift=False
            if self.energie<=200:
                self.energie+=0.1

    def actionDodge(self):
        self.dossier_fonct="/drift"
        self.animation= glob.glob("library/personnages"+self.dossier_perso+self.dossier_fonct+self.dossier_orient+"/image_*.png")
        self.animation.sort()
        if self.dodge==True:
            if self.x>=0 and self.x<=590:
                self.x+=self.orientation*5
            self.anim_speed -= 1
            if self.anim_speed == 0:
                    if self.numAnimDodge==0:
                        self.numAnimDodge=1
                    self.img=pygame.image.load(self.animation[self.numAnimDodge])
                    self.anim_speed=5
                    if self.numAnimDodge==len(self.animation)-1:
                        self.dodge=False
                        self.compteurchelou+=1
                        self.numAnimDodge=0
                    else:
                        self.numAnimDodge+=1


    def lose(self,other):
        self.dossier_fonct="/lose"
        self.animation= glob.glob("library/personnages"+self.dossier_perso+self.dossier_fonct+self.dossier_orient+"/image_*.png")
        self.animation.sort()
        self.anim_speed -= 1
        if self.anim_speed == 0:
            if self.numAnimation==0:
                self.numAnimation=1
            self.img=pygame.image.load(self.animation[self.numAnimation])
            self.anim_speed=8
            if self.numAnimation==len(self.animation)-1:
                self.img=pygame.image.load(self.animation[5])
                other.winnin=True
            else:
                self.numAnimation+=1
        self.screen.blit(self.img,(self.x,self.y-40))

    def win(self):
        self.dossier_fonct="/win"
        self.animation= glob.glob("library/personnages"+self.dossier_perso+self.dossier_fonct+self.dossier_orient+"/image_*.png")
        self.animation.sort()
        if self.winnin==True:
            self.anim_speed -= 1
            if self.anim_speed == 0:
                if self.numAnimation==0:
                    self.numAnimation=1
                self.img=pygame.image.load(self.animation[self.numAnimation])
                self.anim_speed=8
                if self.numAnimation==len(self.animation)-1:
                    self.img=pygame.image.load(self.animation[5])
                else:
                    self.numAnimation+=1
        self.screen.blit(self.img,(self.x,self.y-14))

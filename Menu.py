import pygame,glob

class Menu():
    def __init__(self,_screen):

        self.map="/cascade"
        self.persoA="/perso1"
        self.persoB="/perso2"
        self.clic=False
        self.clic2=False
        self.posouris=(0,0)
        self.menu=1
        self.fond=pygame.image.load("library/menu/menu1/image_01.png")
        self.screen=_screen
        self.animation= glob.glob("library/menu/menu2/perso1/image_*.png")
        self.animation.sort()
        self.img=pygame.image.load(self.animation[0])
        self.anim_speed = 5
        self.numAnimation=0
        self.pixel=pygame.font.Font("library/menu/police.ttf",20)
        self.xA=-120
        self.xB=-140
        self.nomap=""

        


    def setmenu(self,clic,clic2,pos):
        self.clic=clic
        self.clic2=clic2
        self.posouris=pos
        self.screen.blit(self.fond,(0,0))
        if self.menu==1:
            self.menubase()
        elif self.menu==2:
            self.menujoueur()
        elif self.menu==3:
            self.menumap()



    def menubase(self):
        self.fond=pygame.image.load("library/menu/menu1/image_01.png")
        pixel2=pygame.font.Font("library/menu/police.ttf",30)
        if self.posouris[0]>80 and self.posouris[0]<80+104 and self.posouris[1]>160 and self.posouris[1]<160+34:
            jouer = pixel2.render("Jouer!",True,(187,11,11))
            if self.clic==True:
                self.menu=2
        else:
            jouer = pixel2.render("Jouer!",True,(255,255,255))
        self.screen.blit(jouer,(80,160))



    def anim(self,perso):
        self.animation= glob.glob("library/menu/menu2"+perso+"/image_*.png")
        self.animation.sort()
        self.anim_speed -= 1
        img=pygame.image.load(self.animation[self.numAnimation])
        if self.anim_speed == 0:
            if self.numAnimation==0:
                self.numAnimation=1
            img=pygame.image.load(self.animation[self.numAnimation])
            self.anim_speed=5
            if self.numAnimation==len(self.animation)-1:
                self.numAnimation=0
            else:
                self.numAnimation+=1
        return img


    def getRect(self,x,y,l,h):
        return pygame.Rect(x,y,l,h)
        

    def menujoueur(self):
        self.fond=pygame.image.load("library/menu/menu2/image_01.png")
        j1 = self.pixel.render("Player 1",True,(255,255,255))
        j2 = self.pixel.render("Player 2",True,(0,0,0))

        if  self.getRect(65,95,80,167).collidepoint(self.posouris):
            img1=self.anim("/perso1")
            if self.clic==True and (self.getRect(65,95,80,167).collidepoint(self.xB,100))==False:
                self.xA=65
                self.persoA="/perso1"
            elif self.clic2==True and (self.getRect(65,95,80,167).collidepoint(self.xA,100))==False:
                self.xB=65
                self.persoB="/perso1"

        else:
            img1=pygame.image.load("library/menu/menu2/perso1/image_01.png")

        if  self.getRect(215,95,80,167).collidepoint(self.posouris):
            img2=self.anim("/perso2")
            if self.clic==True and (self.getRect(215,95,80,167).collidepoint(self.xB,100))==False:
                self.xA=215
                self.persoA="/perso2"
            elif self.clic2==True and (self.getRect(215,95,80,167).collidepoint(self.xA,100))==False:
                self.xB=215
                self.persoB="/perso2"

        else:
            img2=pygame.image.load("library/menu/menu2/perso2/image_01.png")

        if  self.getRect(365,95,80,167).collidepoint(self.posouris):
            img3=self.anim("/perso3")
            if self.clic==True and (self.getRect(365,95,80,167).collidepoint(self.xB,100))==False:
                self.xA=365
                self.persoA="/perso3"
            elif self.clic2==True and (self.getRect(365,95,80,167).collidepoint(self.xA,100))==False:
                self.xB=365
                self.persoB="/perso3"

        else:
            img3=pygame.image.load("library/menu/menu2/perso3/image_01.png")

        if  self.getRect(515,95,80,167).collidepoint(self.posouris):
            img4=self.anim("/perso4")
            if self.clic==True and (self.getRect(515,95,80,167).collidepoint(self.xB,100))==False:
                self.xA=515
                self.persoA="/perso4"
            elif self.clic2==True and (self.getRect(515,95,80,167).collidepoint(self.xA,100))==False:
                self.xB=515
                self.persoB="/perso4"
        else:
            img4=pygame.image.load("library/menu/menu2/perso4/image_01.png")

        if  self.getRect(10,305,30,49).collidepoint(self.posouris):
            precedent=pygame.image.load("library/menu/menu2/image_02bis.png")
            if self.clic==True:
                self.menu=1   
        else:
            precedent=pygame.image.load("library/menu/menu2/image_02.png")


        if  self.getRect(600,305,30,49).collidepoint(self.posouris):
            suivant=pygame.image.load("library/menu/menu2/image_03bis.png")
            if self.clic==True:
                self.menu=3
                self.xA=-120
                self.xB=-140

        else:
            suivant=pygame.image.load("library/menu/menu2/image_03.png")

        self.screen.blit(j1,(self.xA,273))
        self.screen.blit(j2,(self.xB,273))
        self.screen.blit(img1,(65,95))
        self.screen.blit(img2,(215,95))
        self.screen.blit(img3,(365,95))
        self.screen.blit(img4,(515,95))
        self.screen.blit(precedent,(10,305))
        self.screen.blit(suivant,(600,305))
        
    def menumap(self):

        self.fond=pygame.image.load("library/menu/menu3/image_01.png")
        map = self.pixel.render(self.nomap,True,(255,255,255))
        img1=pygame.image.load("library/menu/menu3/cascade/image_01.png")
        img2=pygame.image.load("library/menu/menu3/temple/image_01.png")
        img3=pygame.image.load("library/menu/menu3/bataille/image_01.png")
        img4=pygame.image.load("library/menu/menu3/jungle/image_01.png")



        if  self.getRect(25,116,128,72).collidepoint(self.posouris):
            if self.clic==True:
                self.xA=65
                self.nomap="Cascade"
                self.map="/cascade"


        if  self.getRect(215,116,128,72).collidepoint(self.posouris):
            if self.clic==True:
                self.xA=215
                self.nomap="Temple"
                self.map="/temple"
 

        if  self.getRect(365,116,128,72).collidepoint(self.posouris):
            if self.clic==True:
                self.xA=365
                self.nomap="Bataille"
                self.map="/bataille"

            

        if  self.getRect(515,116,128,72).collidepoint(self.posouris):
            if self.clic==True:
                self.xA=515
                self.nomap="Jungle"
                self.map="/jungle"


        if  self.getRect(10,305,30,49).collidepoint(self.posouris):
            precedent=pygame.image.load("library/menu/menu2/image_02bis.png")
            if self.clic==True:
                self.menu=2   
        else:
            precedent=pygame.image.load("library/menu/menu2/image_02.png")


        if  self.getRect(290,315,94,23).collidepoint(self.posouris):
            lancer = self.pixel.render("Lancer!",True,(187,11,11))
            if self.clic==True:
                self.menu=4
        else:
            lancer = self.pixel.render("Lancer!",True,(255,255,255))

        self.screen.blit(map,(self.xA-10,200))
        self.screen.blit(img1,(25,116))
        self.screen.blit(img2,(178,116))
        self.screen.blit(img3,(331,116))
        self.screen.blit(img4,(484,116))
        self.screen.blit(precedent,(10,305))
        self.screen.blit(lancer,(290,315))




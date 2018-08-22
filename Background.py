import pygame,glob


class Background():
    def __init__(self,_screen):

        self.back="/cascade"
        self.init_anim_speed=10
        self.anim_speed=self.init_anim_speed
        self.animation= glob.glob("library/backgrounds"+self.back+"/image_*.png")
        self.animation.sort()
        self.numAnimation=0
        self.animationMax=len(self.animation)-1
        self.img=pygame.image.load(self.animation[0])
        self.ndebut=0
        self.screen=_screen

    def update(self,vitesse,map):

        self.back=map
        self.animation= glob.glob("library/backgrounds"+self.back+"/image_*.png")
        self.animation.sort()
        self.anim_speed -= 1
        if self.anim_speed == 0:
            if self.numAnimation==0:
                self.numAnimation=1
            self.img=pygame.image.load(self.animation[self.numAnimation])
            self.anim_speed=vitesse
            if self.numAnimation==self.animationMax:
                self.numAnimation=0
            else:
                self.numAnimation+=1
        self.screen.blit(self.img,(0,0))
        




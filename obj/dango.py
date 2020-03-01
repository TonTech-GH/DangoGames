# -*- coding: utf-8 -*-

# -----------------------------------------------
# インポート
# -----------------------------------------------
import pygame

# -----------------------------------------------
# ダンゴムシ表示
# -----------------------------------------------
class Dango():
    def __init__(self, parent, x, y):
        self.parent = parent
        self.se =pygame.mixer.Sound('se/snare.wav')

        # 通常状態画像
        self.surN = pygame.image.load('img/dango01.PNG').convert_alpha()

        # 変形状態画像
        self.surC = pygame.image.load('img/dango02.PNG').convert_alpha()

        # 画像の反転
        self.surN = pygame.transform.flip(self.surN, True, False)
        self.surC = pygame.transform.flip(self.surC, True, False)

        # 画像の拡大縮小
        dst = (int(self.surN.get_width()/2), int(int(self.surN.get_height()/2)))
        self.surN = pygame.transform.scale(self.surN, dst)
        self.surC = pygame.transform.scale(self.surC, dst)

        # 初期位置
        self.rect = self.surN.get_rect()
        self.rect.center = (x, y)

        # 初期は通常状態
        self.bChanged = False

    def SetForm(self, bChanged):
        if (self.bChanged == False) and bChanged:
            self.se.play()

        self.bChanged = bChanged
    
    def Update(self):
        d = self.surN
        if self.bChanged: d = self.surC
        self.parent.blit(d, self.rect)

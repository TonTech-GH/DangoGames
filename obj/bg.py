# -*- coding: utf-8 -*-

# -----------------------------------------------
# インポート
# -----------------------------------------------
import pygame

# -----------------------------------------------
# 定義
# -----------------------------------------------
# スクロールスピード
speed = 4

# -----------------------------------------------
# 背景表示
# -----------------------------------------------
class BG():
    def __init__(self, parent):
        self.parent = parent
        bg1 = pygame.image.load('img/BG.jpg').convert_alpha()
        bg2 = pygame.image.load('img/BG.jpg').convert_alpha()
        bg2 = pygame.transform.flip(bg2, True, False)

        # 画像の拡大縮小
        rect = parent.get_rect()
        dst = rect.width, rect.height
        bg1 = pygame.transform.scale(bg1, dst)
        bg2 = pygame.transform.scale(bg2, dst)

        self.bg1 = bg1
        self.bg2 = bg2
        self.r1 = bg1.get_rect()
        self.r2 = bg2.get_rect()
        self.r2.x += self.r1.width

    def Update(self):
        self.r1.x -= speed
        self.r2.x -= speed
        if self.r1.right <= 0:
            self.r1.x = self.r2.width
        if self.r2.right <= 0:
            self.r2.x = self.r1.width
        self.parent.blit(self.bg1, self.r1)
        self.parent.blit(self.bg2, self.r2)

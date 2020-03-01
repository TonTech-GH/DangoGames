# -*- coding: utf-8 -*-

# -----------------------------------------------
# インポート
# -----------------------------------------------
import pygame

# -----------------------------------------------
# スコア表示
# -----------------------------------------------
class Score():
    def __init__(self, parent):
        self.parent = parent
        self.score = 0
        self.font = pygame.font.Font(None, 80)
    
    def Update(self):
        s = "{:0>7}".format(self.score)
        text = self.font.render(s, True, (255,255,255))
        r = text.get_rect()
        pr = self.parent.get_rect()
        self.parent.blit(text, (pr.width - r.width, pr.y))

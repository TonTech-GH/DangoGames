# -*- coding: utf-8 -*-

# -----------------------------------------------
# インポート
# -----------------------------------------------
import pygame
from pygame.locals import *
import sys
from obj.dango import Dango
from obj.star import Star
from obj.stars import Stars
from obj.score import Score
from obj.bg import BG

# -----------------------------------------------
# 定義
# -----------------------------------------------
# ダンゴムシスピード
ds_up = -5
ds_down = 10

# ダンゴムシ初期位置
(x, y) = (100, 200)

# -----------------------------------------------
# 星集めクラス
# -----------------------------------------------
class GetStar():
    def __init__(self, screen):
        # メイン画面
        self.screen = screen

        # 終了フラグ
        self.finished = False

        # 背景
        self.bg = BG(screen)

        # スコア表示
        self.score = Score(screen)

        # ダンゴ虫
        self.dango = Dango(screen, x, y)

        # 星
        self.stars = Stars(screen, self.dango, self.score)

        # BGM
        pygame.mixer.music.load('bgm/4 On The Floor 05.wav')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def Update(self):
        # Returnキー押している間ダンゴムシが丸まって下降
        pressed = pygame.key.get_pressed()
        if pressed[K_RETURN]:
            self.dango.SetForm(True)
            if self.dango.rect.bottom <= self.screen.get_height():
                self.dango.rect.move_ip(0, ds_down)
        else:
            self.dango.SetForm(False)
            if self.dango.rect.top >= 0 : 
                self.dango.rect.move_ip(0, ds_up)

        # スペースキーで戻る
        if pressed[K_SPACE]:
            self.finished = True

        # 終了判定
        if pressed[K_ESCAPE]:
            pygame.quit()
            sys.exit(0)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

    def Draw(self):
        # 表示更新
        pygame.display.update()
        pygame.time.wait(30)
        self.screen.fill((255, 255, 255))
        self.bg.Update()
        self.stars.Update()
        self.dango.Update()
        self.score.Update()

# -----------------------------------------------
# 単体テスト
# -----------------------------------------------
if __name__ == '__main__':
     # 初期化
    pygame.init()
    pygame.mixer.init()

    # 画面生成
    pygame.display.set_mode((800, 600), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption('Get Star')

    gs = GetStar(screen)

    while True:
        gs.Update()
        gs.Draw()
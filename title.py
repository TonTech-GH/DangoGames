# -*- coding: utf-8 -*-

# -----------------------------------------------
# インポート
# -----------------------------------------------
import pygame
from pygame.locals import *
import sys
from obj.dango import Dango
from obj.bg import BG

# -----------------------------------------------
# 定義
# -----------------------------------------------


# -----------------------------------------------
# 星集めクラス
# -----------------------------------------------
class Title():
    def __init__(self, screen):
        # メイン画面
        self.screen = screen
        r = screen.get_rect()
        dx, dy = r.center

        # 終了フラグ
        self.finished = False

        # 背景
        self.bg = BG(screen)

        # ダンゴ虫
        self.dango = Dango(screen, dx, dy )

        # タイトル文字
        font = pygame.font.Font(None, 120)
        self.text = font.render('Dango Games', True, (255,255,255))
        rt = self.text.get_rect()
        rt.center = r.center
        rt.y = dy / 2
        self.rt = rt

        # BGM
        #pygame.mixer.music.stop()
        pygame.mixer.music.load('bgm/trumpet2.wav')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(1)

    def Update(self):
        # Returnキー押している間ダンゴムシが丸まって下降
        pressed = pygame.key.get_pressed()
        if pressed[K_RETURN]:
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
        self.dango.Update()
        self.screen.blit(self.text, self.rt)

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
    pygame.display.set_caption('Title')

    title = Title(screen)

    while True:
        title.Update()
        title.Draw()
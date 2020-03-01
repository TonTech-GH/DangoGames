# -*- coding: utf-8 -*-

# -----------------------------------------------
# インポート
# -----------------------------------------------
import pygame
from pygame.locals import *
import sys
from title import Title
from get_star import GetStar

# -----------------------------------------------
# 定義
# -----------------------------------------------
(w, h) = (800, 500)

# シーン
SC_Title, SC_GetStar, SC_Result = (0, 1, 2)

# -----------------------------------------------
# メイン関数
# -----------------------------------------------
def main():
    # 初期化
    pygame.init()
    pygame.mixer.init()

    # 画面生成
    pygame.display.set_mode((w, h), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption('Dangomushi')
    
    title = None
    gs = None
    scene = SC_Title

    # ゲームループ
    while True:
        # タイトル
        if scene == SC_Title:
            if title == None:
                title = Title(screen)
            title.Update()
            title.Draw()
            if title.finished:
                scene = SC_GetStar
                title = None
        
        # 星集め
        elif scene == SC_GetStar:
            if gs == None:
                gs = GetStar(screen)
            gs.Update()
            gs.Draw()
            if gs.finished:
                scene = SC_Title
                gs = None
    
# -----------------------------------------------
# メイン処理
# -----------------------------------------------
if __name__ == '__main__':
    main()
 
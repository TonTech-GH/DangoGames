# -*- coding: utf-8 -*-

# -----------------------------------------------
# インポート
# -----------------------------------------------
import pygame
from obj.obj import ObjBase

# -----------------------------------------------
# 定義
# -----------------------------------------------
# 獲得スコア
score = 2000

# オブジェクトスピード
objSpeed = 30

# -----------------------------------------------
# 星表示
# -----------------------------------------------
class BigStar(ObjBase):
    def __init__(self, parent, x, y, player):
        super().__init__(parent, player, score, 'img/obj/big_star.png', 'se/decision24.wav')
        
        # 初期位置
        self.rect.center = (x, y)

        # 初期回転角度
        self.angl = 0

    # アプデ時に表示するサーフェスとその位置
    def DrawnSur(self):
        r = self.rect
        self.angl += 10
        
        # 一旦一時サーフェスに書き出し
        temp = pygame.Surface((r.width, r.height), pygame.SRCALPHA)
        temp.blit(self.sur, (0, 0))

        # 回転
        temp = pygame.transform.rotate(temp, self.angl)

        # 回転でレクトが変わるので補正
        ofstX = (r.width - temp.get_width()) / 2
        ofstY = (r.height - temp.get_height()) / 2
        r.x -= objSpeed

        # 書き出すサーフェスと位置を返す
        return temp, ((r.x + ofstX, r.y + ofstY))

        
 
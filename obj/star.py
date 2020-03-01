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
score = 100

# オブジェクトスピード
objSpeed = 10

# -----------------------------------------------
# 星表示
# -----------------------------------------------
class Star(ObjBase):
    def __init__(self, parent, x, y, player):
        super().__init__(parent, player, score, 'img/obj/star.png', 'se/switch1.wav')
        
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
    pygame.display.set_caption('Star')

    class Dummy():
        def __init__(self):
            self.rect = pygame.Rect(0,0,1,1)
            self.score = 0
    dum = Dummy()
    star = Star(screen, 400, 300, dum, dum.score)

    while True:
        star.Update()
        
 
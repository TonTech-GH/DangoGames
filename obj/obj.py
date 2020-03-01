# -*- coding: utf-8 -*-

# -----------------------------------------------
# インポート
# -----------------------------------------------
import pygame

# -----------------------------------------------
# オブジェクト表示(基底クラス)
# -----------------------------------------------
class ObjBase():
    # parent : オブジェクトを描画するサーフェス
    # player : 自機
    # score  : ゲット時のスコア値
    # img    : 画像ファイルパス
    # se     : ゲット時のSEファイルパス
    def __init__(self, parent, player, score, img, se):
        self.parent = parent
        self.player = player
        self.score = score

        # 画像ロード
        self.sur = pygame.image.load(img).convert_alpha()

        # SEロード
        self.se = pygame.mixer.Sound(se)

        # 位置
        self.rect = self.sur.get_rect()

        # ゲットされたか
        self.bGat = False

    def Update(self):
        # 自機との衝突判定
        bGat = self.Colli()

        # 獲得したスコアを返す
        if bGat: return self.score

        # ゲット済みなら描画しない
        if self.bGat: return 0

        # サーフェスと位置
        sur, pos = self.DrawnSur()
        self.parent.blit(sur, pos)
        
        return 0

    # アプデ時に表示するサーフェスとその位置
    def DrawnSur(self):
        sur = self.sur
        r = self.rect
        return sur, (r.x, r.y)

    # 自機との衝突判定
    def Colli(self):
        if (self.bGat): return False
        dr = self.player.rect
        cx, cy = self.rect.center
        # 自身の中心が自機のレクトに入ったらゲット扱いとする
        if dr.left <= cx and cx <= dr.right:
            if dr.top <= cy and cy <= dr.bottom:
                self.se.play()
                self.bGat = True
                return True
        return False

 
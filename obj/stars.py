# -*- coding: utf-8 -*-

# -----------------------------------------------
# インポート
# -----------------------------------------------
import pygame
import random
import time
from obj.star import Star
from obj.big_star import BigStar
from obj.obj_map import *

# -----------------------------------------------
# 星群
# -----------------------------------------------
class Stars():
    def __init__(self, parent, player, score):
        self.parent = parent
        self.player = player
        self.score = score
        self.count = 0
        self.time_start = int(time.time())
        self.time_now   = 0

        # 小星群
        self.star = []
        self.CreateStars()

        # 大星
        self.bigStar = []
    
    def FirstObjPos(self):
        w = self.parent.get_width()
        h = self.parent.get_height()
        y = int(random.uniform(50, h - 50))
        return w, y

    def CreateStars(self):
        x0, y = self.FirstObjPos()

        for i in range(5):
            xi = x0 + 100 * i
            star = Star(self.parent, xi, y, self.player)
            self.star.append(star)
        
        self.count += 1
    
    def CreateBigStar(self):
        x, y = self.FirstObjPos()
        # 確率で生成
        #if random.randrange(5) == 0:
        if self.count % 5 == 3:
            bigStar = BigStar(self.parent, x, y, self.player)
            self.bigStar.append(bigStar)

    def Update(self):
        # 小星群
        deleted = []
        for star in self.star:
            self.score.score += star.Update()
            if star.bGat or (star.rect.right < 0):
                deleted.append(star)

        # 画面外 or ゲット済みの星を削除
        for d in deleted:
            self.star.remove(d)

        if len(self.star) == 0:
            self.CreateStars()
            self.CreateBigStar()

        # 大星
        deleted = []
        for bs in self.bigStar:
            self.score.score += bs.Update()
            if bs.bGat or (bs.rect.right < 0):
                deleted.append(bs)
        
        for d in deleted:
            self.bigStar.remove(d)
        
        # 定期星以外のマップ用
        now = int(time.time()) - self.time_start
        if now > self.time_now:
            # 秒数が進んでいればオブジェクト生成判定
            kind = ObjMap.get(now)
            x, y = self.FirstObjPos()
            if kind == ObjStar:
                self.star.append(Star(self.parent, x, y, self.player))
            elif kind == ObjBigStar:
                self.bigStar.append(BigStar(self.parent, x, y, self.player))
        self.time_now = now

        # マップを全て出し切っていたらタイマーをリセット
        if now > max(ObjMap.keys()):
            self.time_start = int(time.time())
            self.time_now = 0



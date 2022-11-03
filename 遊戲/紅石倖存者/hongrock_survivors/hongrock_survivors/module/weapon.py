#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame

# 值班
class Duty(pygame.sprite.Sprite):
    def __init__(self, atk, radius, speed, slave):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('img/duty.png').convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.atk = atk
        self.slave = slave

        # 初始化錄入各角度座標，減輕運算
        self.vectList = []
        vect = pygame.math.Vector2(radius, 0)
        ang = 0       

        while ang < 360:
            self.vectList.append(vect.rotate(ang))
            ang += speed
        self.vectIndex = 0

    def update(self):
        self.rect.center = self.slave.rect.center + self.vectList[self.vectIndex]
        self.vectIndex += 1

        if self.vectIndex >= len(self.vectList):
            self.vectIndex = 0

# 網路波動拳
class NetFist(pygame.sprite.Sprite):
    def __init__(self, atk, cd, slave):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('img/fist.png').convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.atk = atk
        self.cd = cd
        self.slave = slave

        
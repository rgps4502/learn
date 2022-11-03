#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import math
import pygame

# 業務
class Business(pygame.sprite.Sprite):
    def __init__(self, img, speed, atk, defense, slave, screen):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(f'img/{img}').convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.atk = atk
        self.defense = defense
        self.slave = slave

        width = screen[0]
        height = screen[1]
        rand = random.randrange(width * 2 + height * 2)

        # 業務從畫面外出生
        if rand < height:
            self.rect.x = 0 - self.rect.width
            self.rect.y = rand
        elif rand < height + width:
            self.rect.x = rand - height
            self.rect.y = height
        elif rand < height * 2 + width:
            self.rect.x = width
            self.rect.y = rand - height - width
        else:
            self.rect.x = rand - height * 2 - width
            self.rect.y = 0 - self.rect.height

    def update(self):
        xs = self.slave.rect.x
        ys = self.slave.rect.y
        x = self.rect.x
        y = self.rect.y

        # 與社畜座標重疊不移動
        if xs == x and ys == y:
            return

        # 向社畜移動，維持等速
        dx = (xs - x) / math.sqrt((xs - x) ** 2 + (ys - y) ** 2)
        dy = (ys - y) / math.sqrt((xs - x) ** 2 + (ys - y) ** 2)
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
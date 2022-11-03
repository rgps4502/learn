#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame

# 社畜
class Slave(pygame.sprite.Sprite):
    def __init__(self, img, hp, speed, defense, recover, screen):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(f'img/{img}').convert()
        self.image.set_colorkey((255, 255, 255))
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.rect = self.image.get_rect()
        self.limitX = screen[0] - self.width
        self.limitY = screen[1] - self.height

        self.hpLimit = hp  # 血量上限
        self.hp = self.hpLimit
        self.speed = speed
        self.speedObl = self.speed * 0.7  # 斜向速度
        self.defense = defense
        self.recover = 0
        self.lv = 1
        self.exp = 0
        self.expUp = 100  # 升級所需經驗

        self.upgrade = False
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def update(self):
        goUp = self.up and not self.down
        goDown = self.down and not self.up
        goLeft = self.left and not self.right
        goRight = self.right and not self.left

        # 斜向移動
        if (goUp or goDown) and (goLeft or goRight):
            speed = self.speedObl
        else:
            speed = self.speed

        if goUp:
            self.rect.y -= speed
        elif goDown:
            self.rect.y += speed
        if goLeft:
            self.rect.x -= speed
        elif goRight:
            self.rect.x += speed

        # 移動修正
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > self.limitX:
            self.rect.x = self.limitX
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > self.limitY:
           self.rect.y = self.limitY

        # 血量
        self.hp += self.recover

        if self.hp > self.hpLimit:
            self.hp = self.hpLimit
        elif self.hp < 0:
            self.hp = 0

        # 經驗值
        if self.exp >= self.expUp:
            self.lv += 1
            self.exp -= self.expUp
            self.expUp = int(self.expUp * 1.4)
            self.upgrade = True
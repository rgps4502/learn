#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import pygame

# 下午茶
class Dessert(pygame.sprite.Sprite):
    def __init__(self, img, heal, screen):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(f'img/{img}').convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, screen[0] - self.image.get_width())
        self.rect.y = random.randrange(0, screen[1] - self.image.get_height())
        self.heal = heal
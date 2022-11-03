#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import random
import math
import datetime
import pygame
from random import randint
from module.slave import *
from module.business import *
from module.dessert import *
from module.weapon import *

FPS = 30
WIDTH, HEIGHT = 1280, 720

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption('hongrock survivors')
    screen = (WIDTH, HEIGHT)
    win = pygame.display.set_mode(screen)
    font = 'microsoftyaheimicrosoftyaheiui'
    fontBold = 'microsoftyaheimicrosoftyaheiuibold'

    # 載入音樂
    soundBgm = pygame.mixer.Sound('sound/bgm.ogg')
    soundBgm.set_volume(0.4)
    soundHit = pygame.mixer.Sound('sound/hit.ogg')
    soundHit.set_volume(0.2)
    soundLevelUp = pygame.mixer.Sound('sound/level_up.ogg')
    soundLevelUp.set_volume(0.2)
    soundGameOver = pygame.mixer.Sound('sound/game_over.ogg')
    soundGameOver.set_volume(0.2)
    soundIntro = pygame.mixer.Sound('sound/intro.ogg')
    soundIntro.set_volume(0.2)

    # 主選單
    imgMenu = pygame.image.load('img/menu.png').convert()
    imgStart = pygame.image.load('img/start.png').convert()
    rectStart = imgStart.get_rect()
    rectStart.center = (WIDTH / 2, HEIGHT / 2 + 50)

    # 腳色選擇
    imgCharacters = pygame.image.load('img/characters.png').convert()
    rectCharacters = imgCharacters.get_rect()
    rectCharacters.center = (WIDTH / 2, HEIGHT / 2)
    imgAndrew = pygame.image.load('img/andrew.png').convert()
    rectAndrew = imgAndrew.get_rect()
    rectAndrew.center = (WIDTH / 2 - 146, HEIGHT / 2 - 110)

    # 升級介面
    imgUpgrade = pygame.image.load('img/upgrade.png').convert()
    rectUpgrade = imgUpgrade.get_rect()
    rectUpgrade.center = (WIDTH / 2, HEIGHT / 2)

    imgMeditate = pygame.image.load('img/meditate.png').convert()  # 打坐
    rectMeditate = imgMeditate.get_rect()

    imgDutyUp = pygame.image.load('img/duty_up.png').convert()  # 值班升級
    rectDutyUp = imgDutyUp.get_rect()
    dutyLv = 1

    imgBahamut = pygame.image.load('img/bahamut.png').convert()  # 巴哈姆特
    rectBahamut = imgBahamut.get_rect()

    spriteGrp = pygame.sprite.Group()
    ywGrp = pygame.sprite.Group()
    srGrp = pygame.sprite.Group()
    kfcGrp = pygame.sprite.Group()
    drinksGrp = pygame.sprite.Group()

    clock = pygame.time.Clock()
    mode = 'menu'
    soundIntro.play()
    click = ''

    while True:
        while mode == 'menu':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if rectStart.collidepoint(event.pos):
                        mode = 'characters'
            win.blit(imgMenu, [0, 0])
            win.blit(imgStart, rectStart)

            pygame.display.update()
            clock.tick(FPS)
        while mode == 'characters':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if rectAndrew.collidepoint(event.pos):
                        soundIntro.stop()
                        mode = 'working'

                        # 社畜入職
                        slave = Slave('slave.png', 100, 9, 0, 0, screen)
                        slave.rect.center = (WIDTH / 2, HEIGHT / 2)
                        spriteGrp.add(slave)

                        # 添加值班
                        duty = Duty(20, 70, 6, slave)
                        spriteGrp.add(duty)

                        # 開始工作
                        startTime = datetime.datetime.now()
                        soundBgm.play(-1)
                        mode = 'working'
            win.blit(imgCharacters, rectCharacters)
            win.blit(imgAndrew, rectAndrew)

            pygame.display.update()
            clock.tick(FPS)
        while mode == 'working':
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        slave.up = not slave.up
                    elif event.key == pygame.K_DOWN:
                        slave.down = not slave.down
                    elif event.key == pygame.K_LEFT:
                        slave.left = not slave.left
                    elif event.key == pygame.K_RIGHT:
                        slave.right = not slave.right
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # 畫面刷白
            win.fill('white')

            # 全物件更新
            spriteGrp.update()
            spriteGrp.draw(win)

            # 血條
            pygame.draw.rect(
                win,
                (255, 0, 0),
                (slave.rect.x, slave.rect.y + slave.height + 5, slave.width * (slave.hp / slave.hpLimit), 5))

            # 等級
            pygame.draw.rect(win, (0, 0, 0), (0, 0, WIDTH, 15))
            pygame.draw.rect(win, (0, 0, 255), (0, 0, WIDTH * slave.exp / slave.expUp, 15))
            surfaceLv = pygame.font.SysFont(font, 12).render(
                f'Lv:{slave.lv} ', True, (255, 255, 255), (0, 0, 0))
            surfaceLv.set_colorkey((0, 0, 0))
            rectLv = surfaceLv.get_rect()
            win.blit(surfaceLv, [WIDTH - rectLv.width, 0])

            # 升級
            if slave.upgrade:
                soundLevelUp.play()
                mode = 'upgrade'

            # 工作時長
            day = int((datetime.datetime.now() - startTime).seconds / 3)
            surfaceDay = pygame.font.SysFont(fontBold, 20).render(
                f'工作第 {day} 天', True, (0, 0, 0), (255, 255, 255))
            surfaceDay.set_colorkey((255, 255, 255))
            rectDay = surfaceDay.get_rect()
            rectDay.center = (WIDTH / 2, 25)
            win.blit(surfaceDay, rectDay)

            # 業務難度變化
            if day < 10:
                ywFreq = 5
                srFreq = 2
            elif day < 20:
                ywFreq = 6
            elif day < 30:
                srFreq = 3
            elif day < 40:
                ywFreq = 7
            elif day < 50:
                srFreq = 4
            elif day < 60:
                ywFreq = 8
            elif day < 70:
                ywFreq = 9
            elif day < 80:
                srFreq = 5
            elif day < 90:
                ywFreq = 10

            # 添加業務
            if randint(0, 100) < ywFreq:
                yw = Business('yw.png', 4, 10, 0, slave, screen)  # YW單
                spriteGrp.add(yw)
                ywGrp.add(yw)
            if randint(0, 100) < srFreq:
                sr = Business('sr.png', 6, 20, 0, slave, screen)  # SR單
                spriteGrp.add(sr)
                srGrp.add(sr)

            # 添加下午茶
            if randint(0, 500) < 1:
                kfc = Dessert('kfc.png', 30, screen)  # 肯德基
                spriteGrp.add(kfc)
                kfcGrp.add(kfc)
            if randint(0, 500) < 1:
                drinks = Dessert('drinks.png', 15, screen)  # 飲料
                spriteGrp.add(drinks)
                drinksGrp.add(drinks)

            # 碰撞
            if pygame.sprite.spritecollide(slave, ywGrp, True):
                slave.hp -= yw.atk
                slave.exp += 10
                soundHit.play()
            if pygame.sprite.spritecollide(slave, srGrp, True):
                slave.hp -= sr.atk
                slave.exp += 20
                soundHit.play()
            if pygame.sprite.spritecollide(slave, kfcGrp, True):
                slave.hp += kfc.heal
            if pygame.sprite.spritecollide(slave, drinksGrp, True):
                slave.hp += drinks.heal
            if pygame.sprite.spritecollide(duty, ywGrp, True):
                slave.exp += 10
            if pygame.sprite.spritecollide(duty, srGrp, True):
                slave.exp += 20
            if dutyLv > 2:
                if pygame.sprite.spritecollide(duty2, ywGrp, True):
                    slave.exp += 10
                if pygame.sprite.spritecollide(duty2, srGrp, True):
                    slave.exp += 20

            # 是否離職
            if slave.hp <= 0:
                surfaceOver = pygame.font.SysFont(fontBold, 40).render(
                    f' 不畜ㄌ ', True, (0, 255, 0), (0, 0, 128))
                rectOver = surfaceOver.get_rect()
                rectOver.center = (WIDTH / 2, HEIGHT / 2)
                soundBgm.stop()
                soundGameOver.play()
                mode = 'hr09'

            pygame.display.flip()
            clock.tick(FPS)
        while mode == 'upgrade':
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        slave.up = not slave.up
                    elif event.key == pygame.K_DOWN:
                        slave.down = not slave.down
                    elif event.key == pygame.K_LEFT:
                        slave.left = not slave.left
                    elif event.key == pygame.K_RIGHT:
                        slave.right = not slave.right
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if rectMeditate.collidepoint(event.pos):
                        slave.hpLimit += 20
                        slave.upgrade = False
                        mode = 'working'
                    elif rectDutyUp.collidepoint(event.pos):
                        if dutyLv == 1:
                            duty.kill()
                            duty = Duty(20, 70, 9, slave)
                            spriteGrp.add(duty)
                            dutyLv += 1
                        elif dutyLv == 2:
                            duty.kill()
                            duty = Duty(20, 70, 6, slave)
                            duty2 = Duty(20, 70, 6, slave)
                            duty2.vectIndex = 29
                            spriteGrp.add(duty)
                            spriteGrp.add(duty2)
                            dutyLv += 1
                        elif dutyLv == 3:
                            duty.kill()
                            duty2.kill()
                            duty = Duty(20, 70, 9, slave)
                            duty2 = Duty(20, 70, 9, slave)
                            duty2.vectIndex = 19
                            spriteGrp.add(duty)
                            spriteGrp.add(duty2)
                            dutyLv += 1
                        slave.upgrade = False
                        mode = 'working'
                    elif rectBahamut.collidepoint(event.pos):
                        slave.recover += 0.02
                        slave.upgrade = False
                        slave.upgrade = False
                        mode = 'working'
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            win.blit(imgUpgrade, rectUpgrade)

            # 打坐
            rectMeditate.center = (WIDTH / 2, HEIGHT / 2 - 75)
            win.blit(imgMeditate, rectMeditate)

            # 值班升級
            rectDutyUp.center = (WIDTH / 2, HEIGHT / 2 + 40)
            win.blit(imgDutyUp, rectDutyUp)

            # 巴哈姆特
            rectBahamut.center = (WIDTH / 2, HEIGHT / 2 + 155)
            win.blit(imgBahamut, rectBahamut)

            pygame.display.update()
            clock.tick(FPS)
        while mode == 'hr09':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            win.blit(surfaceOver, rectOver)
            pygame.display.update()
            clock.tick(FPS)

if __name__ == '__main__':
    main()
# -*- coding: utf-8 -*-

from os import path
import pygame

pygame.font.init()

FONT_PRIMARY_SMALL = pygame.font.Font(path.join('assets', 'SourceHanSansCN-Regular.ttf'), 14) 
FONT_PRIMARY_MEDIUM = pygame.font.Font(path.join('assets', 'SourceHanSansCN-Regular.ttf'), 20)
FONT_PRIMARY_LARGE = pygame.font.Font(path.join('assets', 'SourceHanSansCN-Regular.ttf'), 24)
FONT_PRIMARY_XLARGE = pygame.font.Font(path.join('assets', 'SourceHanSansCN-Regular.ttf'), 30)
FONT_PRIMARY_XXLARGE = pygame.font.Font(path.join('assets', 'SourceHanSansCN-Regular.ttf'), 40)

FONT_SECONDARY_XXXSMALL = pygame.font.Font(path.join('assets', 'SourceHanSansCN-Regular.ttf'), 8)
FONT_SECONDARY_XXSMALL = pygame.font.Font(path.join('assets', 'SourceHanSansCN-Regular.ttf'), 9)
FONT_SECONDARY_XSMALL = pygame.font.Font(path.join('assets', 'SourceHanSansCN-Regular.ttf'), 12)
FONT_SECONDARY_SMALL = pygame.font.Font(path.join('assets', 'SourceHanSansCN-Regular.ttf'), 14)
FONT_SECONDARY_MEDIUM = pygame.font.Font(path.join('assets', 'SourceHanSansCN-Regular.ttf'), 20)

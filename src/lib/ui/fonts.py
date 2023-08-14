from os import path
import pygame

pygame.font.init()

FONT_PRIMARY_SMALL = pygame.font.SysFont(path.join('assets', 'SourceCodePro-Regular.ttf'), 14) 
FONT_PRIMARY_MEDIUM = pygame.font.SysFont(path.join('assets', 'SourceCodePro-Regular.ttf'), 20)
FONT_PRIMARY_LARGE = pygame.font.SysFont(path.join('assets', 'SourceCodePro-Regular.ttf'), 24)
FONT_PRIMARY_XLARGE = pygame.font.SysFont(path.join('assets', 'SourceCodePro-Regular.ttf'), 30)
FONT_PRIMARY_XXLARGE = pygame.font.SysFont(path.join('assets', 'SourceCodePro-Regular.ttf'), 40)

FONT_SECONDARY_XXXSMALL = pygame.font.SysFont(path.join('assets', 'SourceCodePro-Regular.ttf'), 8)
FONT_SECONDARY_XXSMALL = pygame.font.SysFont(path.join('assets', 'SourceCodePro-Regular.ttf'), 9)
FONT_SECONDARY_XSMALL = pygame.font.SysFont(path.join('assets', 'SourceCodePro-Regular.ttf'), 12)
FONT_SECONDARY_SMALL = pygame.font.SysFont(path.join('assets', 'SourceCodePro-Regular.ttf'), 14)
FONT_SECONDARY_MEDIUM = pygame.font.SysFont(path.join('assets', 'SourceCodePro-Regular.ttf'), 20)

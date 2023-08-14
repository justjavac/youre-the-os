# -*- coding: utf-8 -*-

from lib.drawable import Drawable
from lib.ui.color import Color
from lib.ui.fonts import FONT_PRIMARY_MEDIUM

class ScoreManagerView(Drawable):
    def __init__(self, score_manager):
        self._score_manager = score_manager
        super().__init__()

    @property
    def width(self):
        return FONT_PRIMARY_MEDIUM.size(u'分数 : ' + format(self._score_manager.score, '09'))[0]

    @property
    def height(self):
        return FONT_PRIMARY_MEDIUM.size(u'分数 : ' + format(self._score_manager.score, '09'))[1]

    def draw(self, surface):
        surface.blit(FONT_PRIMARY_MEDIUM.render(u'分数 : ' + format(self._score_manager.score, '09'), True, Color.WHITE), (840, 10))

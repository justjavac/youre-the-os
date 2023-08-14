from lib.drawable import Drawable
from lib.ui.color import Color
from lib.ui.fonts import FONT_PRIMARY_LARGE
from window_size import WINDOW_HEIGHT

class PageManagerView(Drawable):
    def __init__(self, page_manager):
        self._page_manager = page_manager
        super().__init__()
        
        self._pages_in_ram_text_surface = FONT_PRIMARY_LARGE.render('RAM 内存页:', False, Color.WHITE)
        self._pages_in_swap_space_text_surface = FONT_PRIMARY_LARGE.render('磁盘内存页:', False, Color.WHITE)        

    @property
    def width(self):
        return 691

    @property
    def height(self):
        return WINDOW_HEIGHT

    def draw(self, surface):
        surface.blit(self._pages_in_ram_text_surface, self._page_manager.pages_in_ram_label_xy)
        if self._page_manager.pages_in_swap_label_xy is not None:
            surface.blit(self._pages_in_swap_space_text_surface, self._page_manager.pages_in_swap_label_xy)

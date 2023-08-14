# -*- coding: utf-8 -*-

from os import path
import pygame
from random import randint

from lib.ui.color import Color
from game_objects.button import Button
from game_objects.how_to_play_part import HowToPlayPart
from lib.scene import Scene

_parts = [
    HowToPlayPart(
        [
            u'在这个游戏中，你是一台计算机的操作系统。',
            u'您必须管理进程、内存和输入/输出（I/O）事件。'
        ], 
        [
            pygame.image.load(path.join('assets', 'how_to_play_0_0.png'))
        ]
    ),
    HowToPlayPart(
        [
            u'在屏幕顶部，你可以看到所有 CPU。'
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_1_0.png'))
        ]
    ),
    HowToPlayPart(
        [
            u'在 CPU 下面，是你的空闲进程的列表。'
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_2_0.png'))
        ]
    ),
    HowToPlayPart(
        [
            u'您可以单击空闲进程，将其分配给可用的 CPU。',
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_3_0.png')),
            pygame.image.load(path.join('assets', 'how_to_play_3_1.png'))
        ]
    ),
    HowToPlayPart(
        [
            u'同样，你也可以单击正在运行的进程，将其从 CPU 里移除。',
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_4_0.png')),
            pygame.image.load(path.join('assets', 'how_to_play_4_1.png'))
        ]
    ),
    HowToPlayPart(
        [
            u'随着时间的推移，空闲进程将经历 6 个饥饿(starvation)级别。'
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_5_0.png')),
            pygame.image.load(path.join('assets', 'how_to_play_5_1.png')),
            pygame.image.load(path.join('assets', 'how_to_play_5_2.png')),
            pygame.image.load(path.join('assets', 'how_to_play_5_3.png')),
            pygame.image.load(path.join('assets', 'how_to_play_5_4.png')),
            pygame.image.load(path.join('assets', 'how_to_play_5_5.png'))
        ]
    ),
    HowToPlayPart(
        [
            u'根据进程的饥饿级别，你可以了解哪些进程空闲时间最长。',
            u'当进程空闲时间过长时，用户会变得不耐烦并将其杀死。'
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_6_0.png')),
            pygame.image.load(path.join('assets', 'how_to_play_6_1.png'))
        ]
    ),
    HowToPlayPart(
        [
            u'进程也可以正常终止。在这种情况下，你只需单击它即可将其删除。'
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_7_0.png'))
        ]
    ),
    HowToPlayPart(
        [
            u'有时，运行中的进程会因为等待 I/O 事件而被阻塞。',
            u'阻塞的进程会浪费 CPU 时间。这时你应该将它们从 CPU 中删除。',
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_8_0.png'))
        ]
    ),
    HowToPlayPart(
        [
            u'当有阻塞进程出现时，请查看 I/O 事件栏。',
            u'当 I/O 栏有事件时，一定要点击它，否则你的进程将阻塞并饿死。'
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_9_0.png')),
            pygame.image.load(path.join('assets', 'how_to_play_9_1.png'))
        ]
    ),
    HowToPlayPart(
        [
            u'你还必须管理内存！进程在运行时会创建内存页。',
            u'当前正在使用的内存页显示为白色，当前未使用的内存页显示为灰色。'
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_10_0.png'))
        ]
    ),
    HowToPlayPart(
        [
            u'当 RAM 用完时，新的内存页会写入到磁盘。',
            u'您可以通过单击在 RAM 和磁盘之间移动内存页。'
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_11_0.png')),
            pygame.image.load(path.join('assets', 'how_to_play_11_1.png'))
        ]
    ),
    HowToPlayPart(
        [
            u'进程只能使用 RAM 中的内存页。如果尝试使用磁盘上的内存页，进程将闪烁。',
            u'此时你应该交换内存页！进程尝试访问的内存页也将闪烁。'
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_12_0.png')),
            pygame.image.load(path.join('assets', 'how_to_play_12_1.png'))
        ],
        animation_interval=200
    ),
    HowToPlayPart(
        [
            u"如果在进程需要交换内存页的时候你没有进行操作，那么这个进程最终会饿死。",
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_13_0.png'))
        ],
        animation_interval=200
    ),    
    HowToPlayPart(
        [
            u'一旦死亡的进程数达到 10 个，用户就会生气并重新启动你。然后游戏结束。',
            u'你的目标是在不重启的情况下尽可能长时间地生存!'
        ],
        [
            pygame.image.load(path.join('assets', 'how_to_play_14_0.png'))
        ]
    )
]

class HowToPlay(Scene):
    def __init__(self, screen, scenes):
        super().__init__(screen, scenes, background_color=Color.LIGHT_GREY)
        
        self._parts = []
        self._current_part_id = 0
        self._previous_button = None
        self._next_button = None
        
    def setup(self):       
        self._scene_objects = []
        
        self._parts = _parts
        
        self._current_part_id = 0
        self._scene_objects.append(self._parts[self._current_part_id])
        
        self._previous_button = Button('<', self._go_to_previous_part)
        self._previous_button.view.set_xy(
            52,
            self._screen.get_height() - 78
        )
        self._scene_objects.append(self._previous_button)
        
        self._next_button = Button('>', self._go_to_next_part)
        self._next_button.view.set_xy(
            self._screen.get_width() - self._next_button.view.width - 52,
            self._screen.get_height() - 78
        )
        self._scene_objects.append(self._next_button)
        
    def _go_to_previous_part(self):
        if self._current_part_id == 0:
            self._return_to_main_menu()
        else:
            self._scene_objects.remove(self._previous_button)
            self._scene_objects.remove(self._next_button)
            self._scene_objects.remove(self._parts[self._current_part_id])
            
            self._current_part_id -= 1
            self._parts[self._current_part_id].initial_time = self.current_time
            
            self._scene_objects.append(self._parts[self._current_part_id])
            self._scene_objects.append(self._previous_button)
            self._scene_objects.append(self._next_button)
        
    def _go_to_next_part(self):
        if self._current_part_id == len(self._parts) - 1:
            self._return_to_main_menu()
        else:
            self._scene_objects.remove(self._previous_button)
            self._scene_objects.remove(self._next_button)
            self._scene_objects.remove(self._parts[self._current_part_id])
            
            self._current_part_id += 1
            self._parts[self._current_part_id].initial_time = self.current_time
            
            self._scene_objects.append(self._parts[self._current_part_id])
            self._scene_objects.append(self._previous_button)
            self._scene_objects.append(self._next_button)
    
    def _return_to_main_menu(self):
        self._scenes['main_menu'].start()
    
    def update(self, current_time, events):
        for game_object in self._scene_objects:
            game_object.update(current_time, events)

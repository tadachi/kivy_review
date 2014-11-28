from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.utils import *

from kivy.properties import ListProperty, NumericProperty

spacing = 15

colors = (
    'eee4da', 'ede0c8', 'f2b179', 'f59563',
    'f67c5f', 'f65e3b', 'edcf72', 'edcc61',
    'edc850', 'edc53f', 'edc22e')

class Board(Widget):
    b = None
    on_pos = resize
    on_size = resize

    def __init__(self, **kwargs):
        super(Board, self).__init__(**kwargs)
        self.resize()

    def cell_pos(self, board_x, board_y):
        return (self.x + board_x *
                (self.cell_size[0] + spacing) + spacing,
                self.y + board_y *
                (self.cell_size[1] + spacing) + spacing)

    def resize(self, *args):
        self.cell_size = (0.25 * (self.width - 5 * spacing), ) * 2
        self.canvas.before.clear()
        with self.canvas.before:
            BorderImage(pos=self.pos, size=self.size,
                        source='board.png')
            Color(*get_color_from_hex('ccc0b4'))
            for board_x, board_y in all_cells():
                BorderImage(pos=self.cell_pos(board_x, board_y),
                            size=self.cell_size,
                            source='cell.png')

        def reset(self):
        self.b = [[None for i in range(4)]
                  for j in range(4)]

class GameApp(App):
    def on_start(self):
        board = self.root.ids.board
        board.reset()

class Tile(Widget):
    font_size = NumericProperty(24)
    number = NumericProperty(2)
    color = ListProperty(get_color_from_hex(tile_colors[2]))
    number_color = ListProperty(get_color_from_hex('776e65'))

    def __init__(self, number=2, **kwargs):
    super(Tile, self).__init__(**kwargs)
    self.font_size = 0.5 * self.width
    self.number = number
    self.update_colors()

    def resize(self, pos, size):
    self.pos = pos
    self.size = size
    self.font_size = 0.5 * self.width

if __name__ == '__main__':

    Board().run()

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivy.base import EventLoop
from kivy.graphics import Color, Line

from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.togglebutton import ToggleButton

class CanvasWidget(Widget):
    line_width = 2

    def on_touch_move(self, touch):
        if 'current_line' in touch.ud:
            touch.ud['current_line'].points += (touch.x, touch.y)

    def on_touch_down(self, touch):
        print(touch.x, touch.y)

        if Widget.on_touch_down(self, touch):
            return
        with self.canvas:
            touch.ud['current_line'] = Line(
                points=(touch.x, touch.y),
                width=self.line_width)

    def set_line_width(self, line_width='Normal'):
        self.line_width = {
            'Thin': 1, 'Normal': 2, 'Thick': 4
        }[line_width]

    def clear_canvas(self):
        # self.canvas.clear()
        # self.canvas.children = [widget.canvas
        #                         for widget in self.children]
        saved = self.children[:]  # See below
        self.clear_widgets()
        self.canvas.clear()
        for widget in saved:
            self.add_widget(widget)
    pass

    def set_color(self, new_color):
        self.canvas.add(Color(*new_color))

class RadioButton(ToggleButton):
    def _do_press(self):
        if self.state == 'normal':
            ToggleButtonBehavior._do_press(self)

class PaintApp(App):
    def build(self):
        EventLoop.ensure_window()
        if EventLoop.window.__class__.__name__.endswith('Pygame'):
            try:
                from pygame import mouse
                # pygame_compile_cursor is a fixed version of
                # pygame.cursors.compile
                a, b = pygame_compile_cursor()
                mouse.set_cursor((24, 24), (9, 9), a, b)
            except:
                pass

        self.canvas_widget = CanvasWidget()
        self.canvas_widget.set_color(
            get_color_from_hex('#2980b9'))
        return self.canvas_widget

if __name__ == '__main__':
    from kivy.config import Config
    Config.set('graphics', 'width', '1280')
    Config.set('graphics', 'height', '800')  # 16:9
    Config.set('graphics', 'resizable', '0') # Disables Resize

    from kivy.core.window import Window # Must be imported after Config
    Window.clearcolor = get_color_from_hex('#FFFFFF')
    # Config.set('input', 'mouse', 'mouse,disable_multitouch')


    PaintApp().run()

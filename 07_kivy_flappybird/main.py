from kivy.core.image import Image
from kivy.uix.widget import Widget

from kivy.properties import ObjectProperty

from kivy.app import App
from kivy.clock import Clock

class BaseWidget(Widget):
    def load_tileable(self, name):
        t = Image('%s.png' % name).texture
        t.wrap = 'repeat'
        setattr(self, 'tx_%s' % name, t)


class Background(BaseWidget):
    tx_floor = ObjectProperty(None)
    tx_grass = ObjectProperty(None)
    tx_cloud = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Background, self).__init__(**kwargs)

        for name in 'floor grass cloud'.split():
            self.load_tileable(name)

    def set_background_size(self, t):
        t.uvsize = (self.width / t.width, -1)

    def on_size(self, *args):
        for t in (self.tx_floor, self.tx_grass, self.tx_cloud):
            self.set_background_size(t)

class KivyBirdApp(App):
    def on_start(self):
        self.background = self.root.ids.background
        Clock.schedule_interval(self.update, 0.016)

    def update(self, nap):
        self.background.update(nap)

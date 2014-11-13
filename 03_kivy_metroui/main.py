from kivy.app import App
from kivy.core.text import LabelBase

class RecorderApp(App):
    pass

if __name__ == '__main__':
    # from kivy.config import Config
    # Config.set('graphics', 'width', '800')
    # Config.set('graphics', 'height', '600')  # 16:9
    # Config.set('graphics', 'resizable', '0') # Disables Resize

    LabelBase.register(name='Modern Pictograms',
                       fn_regular='modernpics.ttf')

    RecorderApp().run()

from kivy.clock import Clock

NSTARS = 1000

class Starfield(Widget):
    def __init__(self, **kwargs):
        Widget.__init__(self, **kwargs)
        self.canvas = RenderContext(use_parent_projection=True)
        self.canvas.shader.source = 'starfield.glsl'

        self.vfmt = (
            ('vCenter',     2, 'float'),
            ('vScale',      1, 'float'),
            ('vPosition',   2, 'float'),
            ('vTexCoords0', 2, 'float'),
        )

        self.vsize = sum(attr[1] for attr in self.vfmt)

        self.indices = []
        for i in xrange(0, 4 * NSTARS, 4):
            self.indices.extend((
                i, i + 1, i + 2, i + 2, i + 3, i))

        self.vertices = []
        for i in xrange(NSTARS):
            self.vertices.extend((
                0, 0, 1, -24, -24, 0, 1,
                0, 0, 1,  24, -24, 1, 1,
                0, 0, 1,  24,  24, 1, 0,
                0, 0, 1, -24,  24, 0, 0,
            ))

        self.texture = Image('star.png').texture

        self.stars = [Star(self, i) for i in xrange(NSTARS)]

class Star(i):
    angle = 0
    distance = 0
    size = 0.1

    def __init__(self, sf, i):
        self.sf = sf
        self.base_idx = 4 * i * sf.vsize
        self.reset()

    def reset(self):
        self.angle = 2 * math.pi * random()
        self.distance = 90 * random() + 10
        self.size = 0.05 * random() + 0.05

class StarfieldApp(App):
    def build(self):
        EventLoop.ensure_window()
        return Starfield()

    def on_start(self):
        Clock.schedule_interval(self.root.update_glsl,
                                60 ** -1)

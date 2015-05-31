from kivy.config import Config
Config.read('config.ini')

from kivy.app        import App
from kivy.properties import ObjectProperty
from kivy.clock      import Clock
from kivy.uix.widget import Widget

from myutil     import *
from settings   import Settings
from controller import Controller
from world      import World
from renderer   import Renderer
#from walker   import Walker
#from mover    import Mover
#from zombie   import Zombie


class MainApp(App):
    settings = ObjectProperty(Settings())

    def build(self):
        self.controller = Controller()
        self.controller.build(self.settings)

        self.world = World()
        self.world.build(self.settings)

        self.renderer = Renderer()
        sync_property(self.renderer, 'size', self.settings, 'world_size')
        self.root.add_widget(self.renderer)

        return self.root

    def on_start(self):
        Clock.schedule_interval(self.gameloop, 1.0/60.0)

    def gameloop(self, dt):
        self.world.update(dt)
        self.renderer.update(self.world, dt)

    def on_test(self):
        self.settings.use_avoidance = not self.settings.use_avoidance

if __name__ == '__main__':
    MainApp().run()

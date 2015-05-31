from kivy.config import Config
Config.read('config.ini')

from kivy.app         import App
from kivy.properties  import ObjectProperty
from kivy.clock       import Clock
from kivy.core.window import Window
from kivy.uix.widget  import Widget

from myutil     import *
from settings   import Settings
from controller import Controller
from world      import World
from renderer   import Renderer


class MainApp(App):
    settings = ObjectProperty(Settings())

    def build(self):
        self._register_keyboard()
        self.running = False

        self.world = World()
        self.world.build(self.settings)

        self.renderer = Renderer(size_hint_x=2)
        sync_property(self.renderer, 'size', self.settings, 'world_size')
        self.root.add_widget(self.renderer)

        return self.root

    def gameloop(self, dt):
        self.world.update(dt)
        self.renderer.update(self.world, dt)

    def _register_keyboard(self):
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if (keycode[1] == 'spacebar'):
            if self.running:
                Clock.unschedule(self.gameloop)
                self.running = False
            else:
                Clock.schedule_interval(self.gameloop, 1.0/60.0)
                self.running = True
        return True

if __name__ == '__main__':
    MainApp().run()

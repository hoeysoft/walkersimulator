from kivy.config import Config
Config.read('config.ini')

from kivy.app         import App
from kivy.properties  import ObjectProperty
from kivy.clock       import Clock
from kivy.core.window import Window

from myutil     import *
from settings   import Settings
from controller import Controller
from world      import World
from screen     import Screen


class MainApp(App):
    settings = ObjectProperty(Settings())

    def build(self):
        self.running = False
        self._register_keyboard()

        self.world = World()
        self.world.build(self.settings)

        self.screen = Screen(size_hint_x=2)
        self.screen.build(self.settings, self.world)
        sync_property(self.screen, 'size', self.settings, 'world_size')
        self.root.add_widget(self.screen)
        return self.root

    def gameloop(self, dt):
        if self.running:
            self.world.update(dt)
        self.screen.update(dt)

    def on_start(self):
        # start after 0.5sec
        Clock.schedule_once(self._toggle_running, 0.5)
        Clock.schedule_interval(self.gameloop, 1/60.)

    def _toggle_running(self, *args):
        self.running = not self.running

    def _register_keyboard(self):
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self.root, 'text')
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if (keycode[1] == 'spacebar'):
            self._toggle_running()
        return True

if __name__ == '__main__':
    MainApp().run()

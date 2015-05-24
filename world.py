from kivy.core.window import Window
from kivy.uix.widget  import Widget
from kivy.vector      import Vector

from myutil import *
from zombie import Zombie


class World(Widget):
    def build(self):
        self._register_keyboard()

        self.zombie = Zombie()
        self.zombie.build()

        self.add_widget(self.zombie)

    def update(self, dt):
        self.zombie.update()


    def _register_keyboard(self):
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_up=self._on_keyboard_up)
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if is_arrowkey(keycode[1]):
            self.zombie.acc(keycode[1])
        return True

    def _on_keyboard_up(self, keyboard, keycode):
        if is_arrowkey(keycode[1]):
            self.zombie.deacc(keycode[1])
        return True

from kivy.core.window import Window
from kivy.uix.widget  import Widget
from kivy.vector      import Vector

from random import uniform

from myutil  import *
from options import *
from zombie  import Zombie
from man     import Man


class World(Widget):
    def build(self):
        self._register_keyboard()

        self.zombie = Zombie()
        self.zombie.build()
        self.add_widget(self.zombie)

        self.men = []
        for i in xrange(MAN_COUNT):
            man = Man()
            man.build()
            self.add_widget(man)
            self.men.append(man)

    def start(self):
        self.zombie.pos = self.center
        for man in self.men:
            man.pos = self._randpos()
            man.set_target(self.zombie)

    def update(self, dt):
        self.zombie.update()
        for man in self.men:
            man.update()

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

    def _randpos(self):
        x = uniform(MAN_SIZE*2, self.width-MAN_SIZE*2)
        y = uniform(MAN_SIZE*2, self.height-MAN_SIZE*2)
        return (x, y)

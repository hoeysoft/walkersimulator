from kivy.config import Config
Config.read('config.ini')

from kivy.app        import App
from kivy.clock      import Clock
from kivy.uix.widget import Widget

from world  import World
from zombie import Zombie


class ZombieWalkApp(App):
    def build(self):
        self.world = World()
        self.world.build()
        return self.world

    def on_start(self):
        self.world.start()
        Clock.schedule_interval(self.world.update, 1.0/60.0)

if __name__ == '__main__':
    ZombieWalkApp().run()

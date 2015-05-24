from kivy.app        import App
from kivy.clock      import Clock
from kivy.uix.widget import Widget

from world  import World
from zombie import Zombie


class ZombieWalkApp(App):
    def build(self):
        world = World()
        world.build()

        Clock.schedule_interval(world.update, 1.0/60.0)
        return world

if __name__ == '__main__':
    ZombieWalkApp().run()

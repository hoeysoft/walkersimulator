from kivy.config import Config
Config.read('config.ini')

from kivy.app        import App
from kivy.clock      import Clock
from kivy.uix.widget import Widget

from settings import Settings
from world    import World
#from walker   import Walker
#from mover    import Mover
#from zombie   import Zombie


class MainApp(App):
    def build(self):
        self.settings = Settings()

        self.world = World()
        self.world.build(self.settings)
        self.settings.set_default()
        #w = Walker()
#        mover = Mover()
#        mover.update(10, self.settings)
#        self.settings.use_avoidance = False
#        self.settings.use_avoidance = True
#        mover.update(10, self.settings)
# 
#        self.world = World()
#        self.world.build(self.settings)
#
#        self.root.add_widget(self.world)
#        return self.root

    def on_start(self):
        #self.world.start()
        Clock.schedule_interval(self.world.update, 1.0/60.0)

    def gameloop(self, dt):
        self.world.update(dt)

    def on_test(self):
        self.settings.use_avoidance = not self.settings.use_avoidance

if __name__ == '__main__':
    MainApp().run()

from kivy.app            import App
from kivy.properties     import ObjectProperty, StringProperty
from kivy.uix.boxlayout  import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label      import Label
from kivy.uix.slider     import Slider

from myutil import *


class Controller(GridLayout):
    pass

class OptSlider(BoxLayout):
    optname = StringProperty('')

    def __init__(self, *args, **kwargs):
        super(OptSlider, self).__init__(*args, **kwargs)
        self.orientation = 'horizontal'
        self.bind(optname=self._connect)

    def _connect(self, ins, optname):
        settings = App.get_running_app().settings

        minval = settings.property(optname).get_min(settings)
        maxval = settings.property(optname).get_max(settings)
        value  = getattr(settings, optname) 

        slider = Slider(value=value, min=minval, max=maxval)
        label = Label(text=self._tostr(value), halign='left', size_hint_x=0.3)
        def on_value(ins, value):
            label.text = self._tostr(value)
            setattr(settings, optname, self._totype(value))
        slider.bind(value=on_value)

        self.add_widget(slider)
        self.add_widget(label)

    def _tostr(self, value):
        return '{:.0f}'.format(value)

    def _totype(self, value):
        return value


class OptSliderInt(OptSlider):
    def _totype(self, value):
        return int(value+.5)

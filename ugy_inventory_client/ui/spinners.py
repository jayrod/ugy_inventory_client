import imp
import os
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.factory import Factory
Builder.load_string("""
<IconButton>
    StackLayout:
        pos             : self.parent.pos
        size            : self.parent.size
        orientation     : 'lr-tb'
        spacing         : 5
        padding         : 5      
        canvas.before:
            Color:
                rgba:(1,1,1,1)
            Rectangle:
                pos:self.pos
                size:self.size
        Label:
            id          : label
            size_hint_x : 0.80
            text_size   : self.size
            text        : "Quantity"
            color:(0,0,0,1)
            
        Image:
            id          : icon
            source      : 'assets/dropicon.png'
            size_hint_x : 0.20
""")
class IconButton(BoxLayout, Button, ButtonBehavior):
    """ Button with icon image and text aligned side by side"""
    def _init_(self, **kwargs):
        super()._init_(**kwargs)

    def _set_font(self, value):
        self.ids.label.font_size = value
    font_size = property(lambda a:None, _set_font)

    def _set_icon_src(self, value):
        self.ids.icon.source    = value 
    icon_source = property(lambda a:None, _set_icon_src)
    
    def _set_text(self, value):
        self.ids.label.text = value
    text = property(lambda a:None, _set_text)
    
    def _set_bold(self, value):
        self.ids.label.bold = value
    bold = property(lambda a:None, _set_bold)

    # def _set_color(self, value):
    #     self.ids.label.color = value
    # color = property(lambda a:None, _set_color)

    def _set_halign(self, value):
        self.ids.label.halign = value
    halign = property(lambda a:None, _set_halign)

    def _set_valign(self, value):
        self.ids.label.valign = value
    valign = property(lambda a:None, _set_valign)



Factory.register("IconButton",      IconButton)


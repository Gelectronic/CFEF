from kivymd.app import MDApp
import json
from datetime import datetime
from kivy.lang import Builder
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.button import  MDFlatButton ,MDRectangleFlatButton, MDRaisedButton, MDFillRoundFlatButton, MDFillRoundFlatIconButton, MDRoundFlatIconButton ,MDFlatButton, MDIconButton, MDRectangleFlatIconButton
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem
from kivy.core.window import Window
from kivymd.uix.menu import MDDropdownMenu, MDMenuItem 


classs.packageweight_button
        sizebutton = self.ids.packagesize_button
        typebutton= self.ids.packagetype_button
        weightdropdown_item=[{"viewclass": "MDMenuItem", "text": "0-5 kgs"},
        {"viewclass": "MDMenuItem", "text": "5-10 kgs"},
        {"viewclass": "MDMenuItem", "text": "10-15 kgs"},
        {"viewclass": "MDMenuItem", "text": "15-20 kgs"}]
        self.weightdropdown = MDDropdownMenu(caller=weightbutton,position="bottom",ver_growth= "up",hor_growth= "right", width_mult=4, max_height=250, items=weightdropdown_item, callback= self.dropdown_callback)
        sizedropdown_item=[{"viewclass": "MDMenuItem", "text": "Small"},
        {"viewclass": "MDMenuItem", "text": "Medium"},
        {"viewclass": "MDMenuItem", "text": "Large"}]
        self.sizedropdown = MDDropdownMenu(caller=sizebutton,position="bottom",ver_growth= "up",hor_growth= "right", width_mult=4, max_height=250, items=sizedropdown_item, callback= self.menu_callback)
        
        typedropdown_item=[{"viewclass": "MDMenuItem", "text": "Electronic"},
        {"viewclass": "MDMenuItem", "text": "Stationary"},
        {"viewclass": "MDMenuItem", "text": "Food items"},
        self.typedropdown = MDDropdownMenu(caller=typebutton,position="bottom",ver_growth= "up",hor_growth= "right", width_mult=4, max_height=350,  items=typedropdown_item,callback= self.ddmenu_callback)
    
    def weightdrop(self):
        self.weightdropdown.open()

    def sizedrop(self):
        self.sizedropdown.open()

    def typedrop(self):
        self.typedropdown.open()

    def dropdown_callback(self, instance):
        self.weightdropdown.dismiss()

    def menu_callback(self, instance):
        self.sizedropdown.dismiss()
    
    def ddmenu_callback(self, instance):
        self.typedropdown.dismiss()


class MainApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette= "Green"
        return RootWidget()
    
if __name__ == "__main__":
    MainApp().run() 

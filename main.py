from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
#from kivy.properties import ObjectProperty
from kivy.properties import ObjectProperty
#from openpyxl import Workbook

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    
    




class MainApp(MDApp):
    def build(self):
        kvbyla = Builder.load_file("manokv.kv")
        self.theme_cls.primary_palette = "Blue"
        return kvbyla

MainApp().run()
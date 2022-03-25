from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.clock import Clock


class Room_Rent_Khata(MDApp):
    global screen_manager
    screen_manager = ScreenManager()

    def build(self):
        kv = Builder.load_file("welcome.kv")
        kv1 = Builder.load_file("main.kv")
        self.theme_cls.primary_palette = "Green"
        screen_manager.add_widget(kv)
        screen_manager.add_widget(kv1)
        return screen_manager
    def on_start(self):
        Clock.schedule_once(self.change_screen, 10)
    def change_screen(self, dt):
        screen_manager.current="MainScreen"
    
Room_Rent_Khata().run()

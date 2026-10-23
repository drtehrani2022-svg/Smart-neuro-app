# -*- coding: utf-8 -*-
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.core.text import LabelBase

FONT_PATH = "Vazirmatn-Regular.ttf"
if os.path.exists(FONT_PATH):
    LabelBase.register(name="Vazir", fn_regular=FONT_PATH)

class TestApp(App):
    def build(self):
        Window.softinput_mode = 'below_target'
        Window.clearcolor = (0.03, 0.07, 0.12, 1)

        root = BoxLayout(orientation='vertical', padding=10)

        self.txt = TextInput(
            text="",
            hint_text="اینجا تایپ کنید... (فارسی یا انگلیسی)",
            multiline=True,
            font_name="Vazir",
            font_size=18,
            background_color=(0.1, 0.2, 0.3, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(0, 0.85, 0.95, 1),
            padding=(15, 15)
        )
        
        root.add_widget(self.txt)
        return root

if __name__ == '__main__':
    TestApp().run()

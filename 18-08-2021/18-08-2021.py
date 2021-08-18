import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


kv = Builder.load_file("18-08-2021.kv")
class Widgets(Widget):
    def btn(self):
        show_popup()

class P(FloatLayout):

    def showtext(self):
        with open("abcd.txt", "r") as f:
            return (f.read())

    def btn(self):
        # print("Name:", self.name.text, "email:", self.email.text())
        print("Name:", self.name.text)
        self.name.text = ""
        self.name.email = ""

class MyApp(App):
    def build(self):
        return Widgets()

def show_popup():
    show = P()
    popupWindow =Popup(title="popup Window", content=show, size_hint=(None,None),size =(600,600) )
    popupWindow.open()



if __name__ == '__main__':
    MyApp().run()
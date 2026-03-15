from kivy.app import App
from kivy.uix.label import Label

class RiderAI(App):
    def build(self):
        return Label(text="Hello Rider AI")

RiderAI().run()

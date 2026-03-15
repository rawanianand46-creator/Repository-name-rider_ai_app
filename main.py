from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class RiderAIApp(App):

    def build(self):
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        self.output = Label(text="Hello! I am Rider AI 🤖", size_hint=(1,0.4))
        self.layout.add_widget(self.output)

        self.input = TextInput(hint_text="Ask something...", size_hint=(1,0.2))
        self.layout.add_widget(self.input)

        ask_btn = Button(text="Ask Rider AI", size_hint=(1,0.2))
        ask_btn.bind(on_press=self.ask_ai)
        self.layout.add_widget(ask_btn)

        return self.layout

    def ask_ai(self, instance):
        question = self.input.text.lower()

        if "hello" in question:
            answer = "Hello! How can I help you?"
        elif "name" in question:
            answer = "I am Rider AI."
        elif "who made you" in question:
            answer = "I was created by Ayush."
        else:
            answer = "Sorry, I don't understand yet."

        self.output.text = answer

RiderAIApp().run()

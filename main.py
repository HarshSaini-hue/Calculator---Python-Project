from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# Set window background color (dark mode)
Window.clearcolor = (0.1, 0.1, 0.1, 1)


class Calculator(GridLayout):
    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)
        self.cols = 1

        # Display area
        self.display = TextInput(
            multiline=False,
            readonly=True,
            halign="right",
            font_size=40,
            background_color=(0.2, 0.2, 0.2, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(1, 1, 1, 1),
            size_hint_y=0.3,
            padding_y=(20, 20)
        )
        self.add_widget(self.display)

        # Buttons layout
        buttons = GridLayout(cols=4, spacing=5, size_hint_y=0.7)

        button_texts = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]

        for text in button_texts:
            button = Button(
                text=text,
                font_size=28,
                background_normal="",
                background_color=self.get_button_color(text),
                color=(1, 1, 1, 1),
                size_hint=(1, 1)
            )
            button.bind(on_press=self.on_button_press)
            buttons.add_widget(button)

        self.add_widget(buttons)

    def get_button_color(self, text):
        """Set different colors for operators, numbers, and actions"""
        if text in ["+", "-", "*", "/"]:
            return (0.9, 0.4, 0.2, 1)  # orange for operators
        elif text == "=":
            return (0.2, 0.7, 0.2, 1)  # green for equals
        elif text == "C":
            return (0.8, 0.1, 0.1, 1)  # red for clear
        else:
            return (0.2, 0.2, 0.2, 1)  # dark gray for numbers

    def on_button_press(self, instance):
        if instance.text == "C":
            self.display.text = ""
        elif instance.text == "=":
            try:
                self.display.text = str(eval(self.display.text))
            except Exception:
                self.display.text = "Error"
        else:
            self.display.text += instance.text


class CalculatorApp(App):
    def build(self):
        return Calculator()


if __name__ == "__main__":
    CalculatorApp().run()

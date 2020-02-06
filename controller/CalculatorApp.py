from kivy.app import App
from layout.CalculatorGridLayout import CalculatorGridLayout


class CalculatorApp(App):

    def build(self):
        return CalculatorGridLayout()

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
Window.size = (400, 500)

class MyGrid(GridLayout):

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

# Creating App class
class CalculatorApp(App):

    def build(self):
        return MyGrid()

if __name__ == "__main__":
    CalculatorApp().run()
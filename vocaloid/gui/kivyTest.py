import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
# from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.uix.filechooser import FileChooserIconView

class FileChooserPopup(GridLayout):

    def __init__(self, **kwargs):
        super(FileChooserPopup, self).__init__(**kwargs)
        self.cols = 2

        self.file_chooser = FileChooserIconView()
        self.add_widget(self.file_chooser)

        self.lyric_button = Button(text='Choose lyric file')
        self.add_widget(self.lyric_button)


class MyApp(App):

    def build(self):
        return FileChooserPopup()


if __name__ == '__main__':
    MyApp().run()

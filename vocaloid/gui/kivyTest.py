import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

from kivy.uix.filechooser import FileChooserIconView

class FileChooserPopup(GridLayout):

    def __init__(self, **kwargs):
        super(FileChooserPopup, self).__init__(**kwargs)
        self.cols = 2

        self.file_chooser = FileChooserIconView()
        self.add_widget(self.file_chooser)

        self.lyric_button = Button(text='Confirm lyric file')
        self.add_widget(self.lyric_button)

class BaseScreen(GridLayout):

    def __init__(self, **kwargs):
        super(BaseScreen, self).__init__(**kwargs)
        self.cols = 1

        self.lyric_popup = Popup(title='Select file')
        self.lyric_popup.add_widget(FileChooserPopup())

        self.lyric_chooser = Button(text='Choose lyric file', on_press=self.lyric_popup.open)
        
        self.add_widget(self.lyric_chooser)


class MyApp(App):

    def build(self):
        return BaseScreen()


if __name__ == '__main__':
    MyApp().run()

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

        # self.lyric_button = Button(text='Confirm lyric file')
        # self.add_widget(self.lyric_button)

class BaseScreen(GridLayout):

    def __init__(self, **kwargs):
        super(BaseScreen, self).__init__(**kwargs)
        self.cols = 2
        # self.size_hint = (1.0, 0.5)

        self.lyric_popup = Popup(title='Select file')
        file_chooser = FileChooserPopup()
        self.lyric_popup.add_widget(file_chooser)

        file_chooser.add_widget(Button(text='Confirm lyric file',
                                       on_press=lambda x: self.lyric_popup.dismiss()))

        self.lyric_chooser = Button(text='Choose lyric file', on_press=self.lyric_popup.open)
        self.add_widget(self.lyric_chooser)

        self.music_generator = Button(text='Generate music file', on_press=self.generate_callback)
        self.add_widget(self.music_generator)


    def generate_callback(self, instance):
        self.music_generator.text = 'Generated!'


class MyApp(App):

    def build(self):
        return BaseScreen()


if __name__ == '__main__':
    MyApp().run()

import sys, os
# sys.path.insert(0,'../')
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPalette, QBrush, QKeyEvent
from PyQt5.QtCore import QSize, QCoreApplication, QThreadPool, QRunnable, Qt
from PyQt5.QtMultimedia import QSound
from mido.sockets import PortServer, connect
import mido
from urllib.parse import *
from urllib.request import *
import time

from .gui.mainUI import MainUI
from vocaloid.utils import *
from vocaloid.syllablesParser import *
from vocaloid.song import *
from vocaloid.midiMonitor import *

import qdarkstyle

MAX_NUM_SYLLABLES = 36

class MainWindow(QMainWindow, MainUI, QRunnable):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.tutorialButton.clicked.connect(self.onTutorialButtonClick)
        self.startButton.clicked.connect(self.onStartButtonClick)
        self.lyricsFilePath = ""
        self.lyrics = ""
        self.syllables = []
        self.song = Song("")
        self.curr_len = 2 # It's a quarter note.
        self.threadpool = QThreadPool()
        self.num = 0 # This is for positioning note display.
        if not os.path.exists("./tmp"):
            os.makedirs("./tmp")


    def onStartButtonClick(self):
        self.setupUi2(self)
        self.chooseButton.clicked.connect(self.openFile)
        self.nextButton.clicked.connect(self.loadFile)
        self.backButton.clicked.connect(self.onBackButtonClick)


    def onTutorialButtonClick(self):
        print("Try tutorial!")


    def onBackButtonClick(self):
        self.setupUi(self)
        self.tutorialButton.clicked.connect(self.onTutorialButtonClick)
        self.startButton.clicked.connect(self.onStartButtonClick)


    def onBack2ButtonClick(self):
        self.setupUi2(self)
        self.lyrics = ""
        self.syllables = []
        self.lyricsFilePath = ""
        self.song = Song("")
        self.curr_len = 2
        self.num = 0
        self.chooseButton.clicked.connect(self.openFile)
        self.nextButton.clicked.connect(self.loadFile)
        self.backButton.clicked.connect(self.onBackButtonClick)


    def openFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*)", options=options)
        if fileName:
            self.lyricsFilePath = fileName
            self.fileLabel.setText(fileName.split("/")[-1])
            self.lyrics = get_lyrics_from_filepath(self.lyricsFilePath)
            self.textEdit.setText(self.lyrics)


    def loadFile(self):
        if self.lyricsFilePath:
            self.lyrics = get_lyrics_from_filepath(self.lyricsFilePath)
        else:
            self.lyrics = self.textEdit.toPlainText()
        self.song.addLyrics(self.lyrics)
        self.syllables = parse_syllables(self.lyrics)
        self.setupUi3(self)
        self.back2Button.clicked.connect(self.onBack2ButtonClick)
        self.next2Button.clicked.connect(self.onNext2ButtonClick)
        self.renderSyllables(self.syllables)


    def renderSyllables(self, syllables):
        for i, syl in enumerate(syllables):
            # Sorry, the UI now can only handle 35 syllables...
            if i >= MAX_NUM_SYLLABLES:
                print("too many syllables in the lyrics")
                break
            label = getattr(self, "label_%i" % i)
            label.setText(syl)
        midiListener = MidiListener(self)
        self.threadpool.start(midiListener)
        midiMonitor = MidiMonitor()
        self.threadpool.start(midiMonitor)


    def onNext2ButtonClick(self):
        self.setupUi4(self)
        self.generateButton.clicked.connect(self.generateSong)
        self.playButton.clicked.connect(self.playSong)
        self.playButton.setDisabled(True)
        self.restartButton.clicked.connect(self.restartProgram)
        self.exitButton.clicked.connect(self.exitProgram)


    def restartProgram(self):
        self.setupUi(self)
        self.tutorialButton.clicked.connect(self.onTutorialButtonClick)
        self.startButton.clicked.connect(self.onStartButtonClick)
        self.lyricsFilePath = ""
        self.lyrics = ""
        self.syllables = []
        self.song = Song("")
        self.curr_len = 2 # It's a quarter note.
        self.num = 0


    def exitProgram(self):
        sys.exit()


    def generateSong(self):
        xml = self.song.convertToMaryXML()
        file = open("./tmp/song.xml", "w")
        file.write(xml);
        file.close();
        host_name = "http://localhost"
        port_num = ":59125"
        operation = "/process?"
        input_text = xml
        input_type = "RAWMARYXML"
        output_type = "AUDIO"
        locale = "en_US"
        audio = "WAVE_FILE"
        get_string = host_name + port_num + operation + "INPUT_TEXT=" \
                     + quote_plus(xml) + "&INPUT_TYPE=" + input_type \
                     + "&OUTPUT_TYPE=" + output_type + "&LOCALE=" + locale\
                     + "&AUDIO=" + audio
        urlopen(get_string)
        self.soundfilename = './tmp/speech.wav'
        urlretrieve(get_string, self.soundfilename)
        self.playButton.setDisabled(False)


    def playSong(self):
        QSound.play(self.soundfilename)


    def keyPressEvent(self, event):
        if type(event) == QKeyEvent:
            if event.key() == Qt.Key_D and self.curr_len < 4:
                self.curr_len += 1
            elif event.key() == Qt.Key_H and self.curr_len > 1:
                self.curr_len -= 1
            elif event.key() == Qt.Key_R:
                prev_label = getattr(self, "label_" + str(self.num))
                prev_text = prev_label.text()
                prev_label.setText("Rest")
                for i in range(self.num + 1, MAX_NUM_SYLLABLES):
                    label = getattr(self, "label_" + str(i))
                    next_text = label.text()
                    label.setText(prev_text)
                    prev_text = next_text
                self.num += 1
            event.accept()
        else:
            event.ignore()


class MidiListener(QRunnable):
    def __init__(self, window_in):
        super().__init__()
        self.window = window_in


    @pyqtSlot()
    def run(self):
        try:
            server = PortServer('localhost', 8080)
        except:
            print("midi listener already up!")
            return
        for message in server:
            if message.type == 'note_on':
                if self.window.num >= MAX_NUM_SYLLABLES:
                    continue
                label = getattr(self.window, "label_" + str(self.window.num))
                C0 = 24
                octave = (message.note - C0) // 12
                pitch = (message.note - C0) % 12
                length = self.window.curr_len
                self.window.song.addNote(octave, pitch, length)
                notation = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
                len_notation = ["eighth", "quarter", "half", "whole"]
                syllable = label.text()
                note_info = syllable + "\n" + notation[pitch] + " " + str(octave) + "\n" + len_notation[length - 1]
                label.setText(note_info)
                self.window.num += 1


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
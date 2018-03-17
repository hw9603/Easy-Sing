import sys, os, io
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
import pyaudio
import wave
from threading import Thread
import subprocess

MAX_NUM_SYLLABLES = 36
# for audio recording
CHUNK = 1024
FORMAT = pyaudio.paInt16 #paInt8
CHANNELS = 1
RATE = 16000 #sample rate
WAVE_OUTPUT_FILENAME = "./tmp/recorded.wav"

class MainWindow(QMainWindow, MainUI, QRunnable):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.tutorialButton.clicked.connect(self.onTutorialButtonClick)
        self.startButton.clicked.connect(self.onStartButtonClick)
        self.lyricsFilePath = ""
        self.lyrics = ""
        self.syllables = []
        self.song = Song("", self)
        self.curr_len = 2 # It's a quarter note.
        self.threadpool = QThreadPool()
        self.num = 0 # This is for positioning note display.
        # for recording:
        self.onRecording = False
        self.recordThread = 0
        if not os.path.exists("./tmp"):
            os.makedirs("./tmp")


    def onStartButtonClick(self):
        self.setupUi2(self)
        self.chooseButton.clicked.connect(self.openFile)
        self.nextButton.clicked.connect(self.loadFile)
        self.recordButton.clicked.connect(self.recordSound)
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
        self.song = Song("", self)
        self.curr_len = 2
        self.num = 0
        self.chooseButton.clicked.connect(self.openFile)
        self.nextButton.clicked.connect(self.loadFile)
        self.recordButton.clicked.connect(self.recordSound)
        self.backButton.clicked.connect(self.onBackButtonClick)

    def recordSound(self):
        # TODO to be added
        if self.onRecording:
            self.onRecording = False
            self.recordThread.join()
            if not os.path.isfile(WAVE_OUTPUT_FILENAME):
                self.textEdit.setText("Error! Check whether the recorded audio exist.")
                return
            self.lyrics = self.ask_google_for_text(WAVE_OUTPUT_FILENAME)
            self.textEdit.setText(self.lyrics)
        else:
            self.onRecording = True
            self.recordThread = Thread(target = self.record_and_save_to_file, args = ( ))
            self.recordThread.start()

    def record_and_save_to_file(self):
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK) #buffer

        print("* recording")
        self.recordButton.setStyleSheet("background-color: #881111;font: 36pt 'Arial';")
        self.recordButton.setText("Recording...")
        frames = []
        while self.onRecording:
            data = stream.read(CHUNK)
            frames.append(data) # 2 bytes(16 bits) per channel
        print("* done recording")
        self.recordButton.setStyleSheet("background-color: #31363b;font: 36pt 'Arial';")
        self.recordButton.setText("Record Lyrics")
        stream.stop_stream()
        stream.close()
        p.terminate()
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    def ask_google_for_text(self, speech_file):
        """Transcribe the given audio file."""
        from google.cloud import speech
        from google.cloud.speech import enums
        from google.cloud.speech import types
        client = speech.SpeechClient()

        with io.open(speech_file, 'rb') as audio_file:
            content = audio_file.read()

        audio = types.RecognitionAudio(content=content)
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code='en-US')
        response = client.recognize(config, audio)
        # Each result is for a consecutive portion of the audio. Iterate through
        # them to get the transcripts for the entire audio file.
        for result in response.results:
            # The first alternative is the most likely one for this portion.
            print('Transcript: {}'.format(result.alternatives[0].transcript))
            return result.alternatives[0].transcript

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
        # if self.lyricsFilePath:
        #     self.lyrics = get_lyrics_from_filepath(self.lyricsFilePath)
        # else:
        self.lyrics = self.textEdit.toPlainText()
        self.song.addLyrics(self.lyrics)
        self.syllables = parse_syllables(self.lyrics)
        # self.setupUi3(self)
        # self.back2Button.clicked.connect(self.onBack2ButtonClick)
        # self.next2Button.clicked.connect(self.onNext2ButtonClick)
        # self.renderSyllables(self.syllables)
        self.setupUi5(self)
        self.back5Button.clicked.connect(self.onBack2ButtonClick)
        self.next5Button.clicked.connect(self.onNext2ButtonClick)
        midiListener = MidiListener(self)
        self.threadpool.start(midiListener)
        midiMonitor = MidiMonitor()
        self.threadpool.start(midiMonitor)


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
        self.song = Song("", self)
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
            elif event.key() == Qt.Key_W and self.curr_len > 1:
                self.curr_len -= 1
            elif event.key() == Qt.Key_G:
                self.song.addRest(self.curr_len)
                # prev_label = getattr(self, "label_" + str(self.num))
                # prev_text = prev_label.text()
                # prev_label.setText("Rest")
                # for i in range(self.num + 1, MAX_NUM_SYLLABLES):
                    # label = getattr(self, "label_" + str(i))
                    # next_text = label.text()
                    # label.setText(prev_text)
                    # prev_text = next_text
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
                # label = getattr(self.window, "label_" + str(self.window.num))
                C0 = 24
                octave = (message.note - C0) // 12
                pitch = (message.note - C0) % 12
                length = self.window.curr_len
                self.window.song.addNote(octave, pitch, length)
                notation = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
                len_notation = ["eighth", "quarter", "half", "whole"]
                # syllable = label.text()
                # note_info = syllable + "\n" + notation[pitch] + " " + str(octave) + "\n" + len_notation[length - 1]
                # label.setText(note_info)
                self.window.num += 1


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
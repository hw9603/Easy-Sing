import mido
import sys
from mido.sockets import PortServer, connect
from PyQt5.QtCore import QRunnable, pyqtSlot

class MidiMonitor(QRunnable):
    @pyqtSlot()
    def run(self):
        try:
            rtmidi = mido.Backend('mido.backends.rtmidi')
            input = rtmidi.open_input()
            output = connect('localhost', 8080)
            for message in input:
                output.send(message)
        except:
            print("No input device detected!")

        
import mido
import sys
from mido.sockets import PortServer, connect
from PyQt5.QtCore import QRunnable, pyqtSlot

class MidiMonitor(QRunnable):
    @pyqtSlot()
    def run(self):
        rtmidi = mido.Backend('mido.backends.rtmidi')
        try:
           input = rtmidi.open_input()
        except:
            print("No input device detected!")
            sys.exit(1)

        output = connect('localhost', 8080)

        for message in input:
            output.send(message)
import Tkinter as tk
import threading
import pyaudio, wave

class App():
    def __init__(self, master):
        self.isrecording = False
        self.button = tk.Button(top, text = 'rec')
        self.button.bind("<Button-1>", self.OnMouseDown)
        self.button.bind("<ButtonRelease-1>", self.OnMouseUp)

        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.WAVE_OUTPUT_FILENAME = "output.wav"

        self.p = pyaudio.PyAudio()

        try: self.stream = self.p.open(format=self.FORMAT,
                    channels=self.CHANNELS,
                    rate=self.RATE,
                    input=True,
                    frames_per_buffer=self.CHUNK)
        except:
            raise Exception("There is no connected microphone. Check that you connect to the left hole if you have a PC.")
            return None

        self.frames = []

        self.button.pack()

    def recordFrame(self):
        try:
            data = self.stream.read(self.CHUNK)
            print "after try"
        except IOError as ex:
            print "inside except"
            if ex[1] != pyaudio.paInputOverflowed:
                print "before raise"
                raise
                print "after raise"

            data = '\x00' * self.CHUNK  # or however you choose to handle it, e.g. return None

        self.frames.append(data)

    def finishRecording(self):

        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

        wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()

    def OnMouseDown(self, event):
        self.mouse_pressed = True
        self.poll()

    def OnMouseUp(self, event):
        self.root.after_cancel(self.after_id)
        print "Finished recording!"
        self.finishRecording()

    def poll(self):
        if self.mouse_pressed:
            self.recordFrame()
            self.after_id = self.root.after(1, self.poll)

    def startrecording(self, event):
        self.isrecording = True
        t = threading.Thread(target=self._record)
        t.start()

    def stoprecording(self, event):
        self.isrecording = False

    def _record(self):
        while self.isrecording:
            print "Recording..."

def resize(ev=None):
    label.config(font='Helvetica -%d bold' % scale.get())

top=tk.Tk()
top.geometry('600x400')
label=tk.Label(top,text='Hello world!',font='Helvetica -12 bold')
label.pack(fill=tk.Y,expand=1)
scale=tk.Scale(top,from_=10,to=40,orient=tk.HORIZONTAL,command=resize)
scale.set(12)
scale.pack(fill=tk.X,expand=1)
quit = tk.Button(top,text='QUIT', command=top.quit, activeforeground='white', activebackground='red')
quit.pack()
app = App(top)
top.mainloop()
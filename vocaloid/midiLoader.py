from utils import *
import pygame
import pygame.midi
import pygame.mixer
from pygame.locals import *
from song import *

# # pygame.mixer.music.load(get("data_path")+"teddybear.mid")
# # pygame.mixer.music.play()
# s = Song("")
def midiLoader(s):
    pygame.init()
    pygame.fastevent.init()
    event_get = pygame.fastevent.get
    event_post = pygame.fastevent.post
    pygame.midi.init()
    input_id = pygame.midi.get_default_input_id()
    if input_id == -1:
        input_id = 1
    print(pygame.midi.get_device_info(0))
    print(pygame.midi.get_device_info(1))
    i = pygame.midi.Input(input_id)

    going = True
    length = -1
    while going:
        events = event_get()
        for e in events:
            if e.type in [KEYDOWN]:
                if int(e.unicode) in [1, 2, 3, 4]:
                    length = e.unicode
                if int(e.unicode) in [0]:
                    going = False
            if e.type in [QUIT]:
                going = False

        if i.poll():
            midi_events = i.read(10)
            if int(midi_events[0][0][0]) in [224,225,226]:#Pitch Bender
                    print("pitch blender: ", str(midi_events[0][0][2]))#right(0)  center(64)  left(124)

            # print("full midi_events " + str(midi_events))
            note = midi_events[0][0][1]
            velocity = midi_events[0][0][2]
            C0 = 24
            octave = (note - C0) // 12
            pitch = (note - C0) % 12
            note_off = (velocity == 0)
            if not note_off:
                if length != -1:
                    print("octave: ", octave, " pitch: ", pitch, " length: ", length)
                    s.addNote(octave, pitch, length)
                else:
                    print("Please first add the length for the note!")
            length = -1
            #convert them into pygame events.
            midi_evs = pygame.midi.midis2events(midi_events, i.device_id)

            for m_e in midi_evs:
                event_post( m_e )
    print("exit button clicked.")
    i.close()
    pygame.midi.quit()
    pygame.quit()

# midiLoader(s)
# print(s)


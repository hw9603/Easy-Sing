"""Object representation of a song."""
from vocaloid.note import *
from vocaloid.phonemesParser import parse_phonemes_by_syllables as parse_phonemes
from vocaloid.phonemesParser import get_phonemes_ssml as get_ssml
from vocaloid.phonemesParser import get_phonemes
from vocaloid.syllablesParser import *
from vocaloid.utils import write_to_filepath

from pdf2image import convert_from_path, convert_from_bytes
import tempfile
from PIL import Image
import os

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget

from vocaloid.__main__ import *

def convertToMilliseconds(length):
    """Convert note length to ms. Currently assumes bpm of 120."""
    if length.value == 1:
        return 125
    if length.value == 2:
        return 250
    if length.value == 3:
        return 500
    if length.value == 4:
        return 1000

def convertPitchToABS(pitch):
    # pitches ordered according to experimental correspondence data
    # lowest is C4, highest is B4
    # pitches = [1275, 1285, 1300, 1315,
    #            1330, 1350, 1380, 1400,
    #            1420, 1440, 1470, 1495]

    # pitches ordered according to experimental correspondence data
    # lowest is C3, highest is B3
    pitches = [1130, 1140, 1150, 1160,
               1170, 1180, 1192, 1204,
               1216, 1228, 1240, 1260]
    return pitches[pitch.value]

class Song:
    def __init__(self, lyrics, window_in):
        super().__init__()
        self.window = window_in
        self.num_notes = 0
        self.notes = []
        self.lyrics = ""
        self.lily_notes = []
        self.num_rest = 0
        self.syllables = parse_syllables(lyrics)
        self.phonemes = parse_phonemes(get_phonemes(get_ssml(lyrics)))

    def __str__(self):
        string = ""
        for x, note in enumerate(self.notes):
            string = string + str(note) + " "
            string = string + self.syllables[x] + "\n"
        return string

    def addNote(self, octave, pitch, length):
        if self.num_notes >= len(self.syllables):
            print("Can't add any more notes!")
            return
        syllable = self.syllables[len(self.notes) - self.num_rest]
        phonemes = self.phonemes[len(self.notes) - self.num_rest]
        if octave < 2:
            octave = 2
        elif octave > 4:
            octave = 4
        n = Note(octave, pitch, length, syllable, phonemes)
        self.notes.append(n)
        self.num_notes = self.num_notes + 1
        notation_map = ["c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "b"]
        octave_map = ['', '\'', '\'\''] # octave 2, 3, 4
        lily_note = notation_map[pitch] + octave_map[octave - 2] + str(length)
        print(lily_note)
        self.lily_notes.append(lily_note)
        self.convertToLilyPond()

    def addRest(self, length):
        if self.num_notes >= len(self.syllables):
            print("Can't add any more notes!")
            return
        syllable = ""
        phonemes = []
        self.num_rest += 1
        n = Note(0, 0, length, syllable, phonemes, True)
        lily_note = 'r' + str(length)
        self.notes.append(n)
        self.lily_notes.append(lily_note)
        self.convertToLilyPond()

    def addLyrics(self, line):
        self.lyrics = line
        for syllable in parse_syllables(line):
            self.syllables.append(syllable)
        for phonemes in parse_phonemes(get_phonemes(get_ssml(line))):
            self.phonemes.append(phonemes)

    def convertToMaryXML(self):
        # the first line is really long...
        res = '<?xml version="1.0" encoding="UTF-8"?>'
        res = res + '<maryxml xmlns="http://mary.dfki.de/2002/MaryXML"'
        res = res + ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
        res = res + ' version="0.5" xml:lang="en-US">\n'

        # write overhead at the beginning
        res = res + '<p>\n'
        res = res + '<s>\n'

        # for each note, write pitch, length, phonemes
        # (currently assumes octave is 4 due to lack of data)
        for note in self.notes:
            if note.is_rest:
                line = '<boundary duration="' + str(convertToMilliseconds(note.length)) + '"/>'
                res = res + line
            else:
                line = '<prosody rate="' + str(convertToMilliseconds(note.length)) + 'ms"'
                line = line + ' pitch="' + str(convertPitchToABS(note.pitch)) + 'abs">'
                res = res + line + "\n"
                line_ph = '<t ph="'
                for phoneme in note.phonemes:
                    line_ph = line_ph + phoneme
                line_ph.strip()
                line_ph = line_ph + '" >'
                res = res + line_ph + "\n"
                res = res + note.syllable + "\n"   # this line might not be necessary...
                res = res + "</t>\n"
                res = res + "</prosody>\n"

        # write overhead at the end
        res = res + "</s>\n"
        res = res + "</p>\n"
        res = res + "</maryxml>\n"

        return res

    def convertToLilyPond(self):
        musicOne = "musicOne = {\n\t"
        verseOne = "\n}\nverseOne = \lyricmode {\n\t"
        score = "\n}\n\score {\n\t<<\n\t\t"
        score += "\\new Voice = \"one\" {\n\t\t\t\\time 2/4\n\t\t\t\musicOne\n\t\t}\n\t\t"
        score += "\\new Lyrics \lyricsto \"one\" {\n\t\t\t\\verseOne\n\t\t}"
        score += "\n\t>>\n}"
        # sharp - is; flat - es
        # c - octave 2; c' - octave 3; c'' - octave 4
        # "cis4 bes'8. a'16 g'4. f'8 e'4 d'4 c'2 c''2"
        melody = ' '.join(self.lily_notes)
        lyrics = ' '.join(self.syllables)
        lily_string = musicOne + melody + verseOne + lyrics + score
        write_to_filepath("tmp/song.ly", lily_string)
        os.system("lilypond --output='tmp/' tmp/song.ly")
        self.displayMusic()

    def displayMusic(self):
        with tempfile.TemporaryDirectory() as path:
            images_from_path = convert_from_path('tmp/song.pdf', output_folder=path)
        # images_from_path[0].show()
        images_from_path[0].save("tmp/song.jpg", "JPEG") # Assume there is only one page in the pdf file.
        pixmap = QPixmap("tmp/song.jpg")
        # pixmap = pixmap.scaledToWidth(self.window.picLabel.width())
        self.window.picLabel.setPixmap(pixmap)
        self.window.picLabel.adjustSize()
        self.window.picLabel.show()

# convertToLilyPond()





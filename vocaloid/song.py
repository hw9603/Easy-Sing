"""Object representation of a song."""
from vocaloid.note import *
from vocaloid.phonemesParser import parse_phonemes_by_syllables as parse_phonemes
from vocaloid.phonemesParser import get_phonemes_ssml as get_ssml
from vocaloid.phonemesParser import get_phonemes
from vocaloid.syllablesParser import *

def convertToMilliseconds(length):
    """Convert note length to ms. Currently assumes bpm of 120."""
    if length.value == 1:
        return 250
    if length.value == 2:
        return 500
    if length.value == 3:
        return 1000
    if length.value == 4:
        return 2000

def convertPitchToABS(pitch):
    # pitches ordered according to experimental correspondence data
    # lowest is C4, highest is B4
    pitches = [1275, 1285, 1300, 1315,
               1330, 1350, 1380, 1400,
               1420, 1440, 1470, 1495]
    return pitches[pitch.value]

class Song:
    def __init__(self, lyrics):
        self.num_notes = 0
        self.notes = []
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
        syllable = self.syllables[len(self.notes)]
        phonemes = self.phonemes[len(self.notes)]
        n = Note(octave, pitch, length, syllable, phonemes)
        self.notes.append(n)
        self.num_notes = self.num_notes + 1

    def addRest(self, length):
        if self.num_notes >= len(self.syllables):
            print("Can't add any more notes!")
            return
        syllable = ""
        phonemes = []
        n = Note(0, 0, length, syllable, phonemes, True)
        self.notes.append(n)

    def addLyrics(self, line):
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

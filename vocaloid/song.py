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
        if len(self.notes) >= len(self.syllables):
            print("Can't add any more notes!")
            return
        syllable = self.syllables[len(self.notes)]
        phonemes = self.phonemes[len(self.notes)]
        n = Note(octave, pitch, length, syllable, phonemes)
        self.notes.append(n)
    def addLyrics(self, line):
        for syllable in parse_syllables(line):
            self.syllables.append(syllable)
        for phonemes in parse_phonemes(get_phonemes(get_ssml(line))):
            self.phonemes.append(phonemes)
    def convertToMaryXML(self):
        file = open("song.xml", "w")

        # the first line is really long...
        line = '<?xml version="1.0" encoding="UTF-8"?>'
        line = line + '<maryxml xmlns="http://mary.dfki.de/2002/MaryXML"'
        line = line + ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
        line = line + ' version="0.5" xml:lang="en-US">'

        # write overhead at the beginning
        file.write(line + "\n")
        file.write("<p>\n")
        file.write("<s>\n")

        # for each note, write pitch, length, phonemes
        # (currently assumes octave is 4 due to lack of data)
        for note in self.notes:
            line = '<prosody rate="' + str(convertToMilliseconds(note.length)) + 'ms"'
            line = line + ' pitch="' + str(convertPitchToABS(note.pitch)) + '">'
            file.write(line + "\n")
            line_ph = '<t ph="'
            for phoneme in note.phonemes:
                line_ph = line_ph + phoneme
            line_ph.strip()
            line_ph = line_ph + '" >'
            file.write(line_ph + "\n")
            file.write(note.syllable + "\n")   # this line might not be necessary...
            file.write("</t>\n")
            file.write("</prosody>\n")
        
        # write overhead at the end
        file.write("</s>\n")
        file.write("</p>\n")
        file.write("</maryxml>\n")

        file.close()

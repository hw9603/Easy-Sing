"""Object representation of a song."""

from note import *
from phonemesParser import parse_phonemes_by_syllables as parse_phonemes
from phonemesParser import get_phonemes_ssml as get_ssml
from phonemesParser import get_phonemes
from syllablesParser import *

class Song:
	def __init__(self, lyrics):
		self.notes = []
		self.syllables = parse_syllables(lyrics)
		self.phonemes = parse_phonemes(get_phonemes(get_ssml(lyrics)))
	def __str__(self):
		string = ""
		for x in range(self.notes):
			string = string + str(self.notes[x]) + " "
			string = string + self.syllables[x] + "\n"
		return string
	def AddNote(self, octave, pitch, length):
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
"""Object representation of a Note."""

from pitch import *
from length import *

class Note:
	def __init__(self, octave_in, pitch_in, length_in):
		self.octave = octave_in
		self.pitch = Pitch(pitch_in)
		self.length = Length(length_in)
		self.syllable = ""
		self.phonemes = ""

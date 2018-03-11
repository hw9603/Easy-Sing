"""Object representation of a Note."""
from enum import Enum

class Pitch(Enum):
	C = 0
	C_Sharp = 1
	D_Flat = 1
	D = 2
	D_Sharp = 3
	E_Flat = 3
	E = 4
	F = 5
	F_Sharp = 6
	G_Flat = 6
	G = 7
	G_Sharp = 8
	A_Flat = 8
	A = 9
	A_Sharp = 10
	B_Flat = 10
	B = 11

class Length(Enum):
	Eighth = 1
	Quarter = 2
	Half = 3
	Whole = 4

class Note:
	def __init__(self, octave_in, pitch_in, length_in
				 syllable_in, phonemes_in, is_rest_in=False):
		self.octave = octave_in
		self.pitch = Pitch(pitch_in)
		self.length = Length(length_in)
		self.syllable = syllable_in
		self.phonemes = phonemes_in
		self.is_rest = is_rest_in

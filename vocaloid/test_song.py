"""Test the generation of a song."""

from song import *

def test():
	lines = [
		"A lot of words are in this sentence",
		"I wonder how many words there are",
		"And how difficult it is to parse",
		"Based solely on this type of input"
	]

	# melody from Blue Danube by Strauss, transposed to C
	melody = [
		[
			[1, 0, 1],
			[1, 0, 1],
			[1, 4, 1],
			[1, 7, 1],
			[1, 7, 2],
			[1, 7, 1],
			[1, 7, 2],
			[1, 4, 1],
			[1, 4, 2]
		],
		[
			[1, 0, 1],
			[1, 0, 1],
			[1, 4, 1],
			[1, 7, 1],
			[1, 7, 2],
			[1, 7, 1],
			[1, 7, 2],
			[1, 5, 1],
			[1, 5, 2]
		],
		[
			[0, 11, 1],
			[0, 11, 1],
			[1, 2, 1],
			[1, 9, 1],
			[1, 9, 2],
			[1, 9, 1],
			[1, 9, 2],
			[1, 5, 1],
			[1, 5, 2]
		],
		[
			[0, 11, 1],
			[0, 11, 1],
			[1, 2, 1],
			[1, 9, 1],
			[1, 9, 2],
			[1, 9, 1],
			[1, 9, 2],
			[1, 7, 1],
			[1, 7, 2]
		],
	]

	s = Song("")

	for line in lines:
		s.addLyrics(line)
	for phrase in melody:
		for note in phrase:
			s.addNote(note[0], note[1], note[2])

	print(s)

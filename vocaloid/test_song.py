"""Test the generation of a song."""

from vocaloid.song import *

def test():
	lines = [
		"I made up this song to prove a point.",
		"I wonder how well I make it sound.",
		"And how difficult it is to rhyme.",
		"Based solely on this type of input."
	]

	# melody from Blue Danube by Strauss, in the key of D Major
	melody = [
		[
			[4, 2, 1],
			[4, 2, 1],
			[4, 6, 1],
			[4, 9, 1],
			[4, 9, 2],
			[4, 9, 1],
			[4, 9, 2],
			[4, 6, 1],
			[4, 6, 2]
		],
		[
			[4, 2, 1],
			[4, 2, 1],
			[4, 6, 1],
			[4, 9, 1],
			[4, 9, 2],
			[4, 9, 1],
			[4, 9, 2],
			[4, 7, 1],
			[4, 7, 2]
		],
		[
			[4, 1, 1],
			[4, 1, 1],
			[4, 4, 1],
			[4, 7, 1],
			[4, 11, 2],
			[4, 11, 1],
			[4, 11, 2],
			[4, 7, 1],
			[4, 7, 2]
		],
		[
			[4, 1, 1],
			[4, 1, 1],
			[4, 4, 1],
			[4, 7, 1],
			[4, 11, 2],
			[4, 11, 1],
			[4, 11, 2],
			[4, 9, 1],
			[4, 9, 2]
		],
	]

	s = Song("")

	for line in lines:
		s.addLyrics(line)
	for phrase in melody:
		for note in phrase:
			s.addNote(note[0], note[1], note[2])

	print("----------THIS IS THE SONG------------")
	print(s)

	s.convertToMaryXML()

test()

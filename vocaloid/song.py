"""Object representation of a song."""

from note import *

class Song:
	def __init__(self, words_in):
		self.notes = []
		self.words = words_in
	def addNote(self, n):
		self.notes.append(n)
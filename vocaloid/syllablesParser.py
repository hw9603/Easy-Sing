"""
Parse syllables from lyrics.

Example usage:

1.
    from utils import *
    lyrics = get_lyrics_from_file("lyrics.txt")
    syllables = parse_syllables(lyrics)
2.
    lyrics = "These are some lyrics stored in a string"
    syllables = parse_syllables(lyrics)
"""

import pyphen

def parse_syllables(lyrics):
    """
    Return a list of syllables. Input words are split into syllables using
    function in pyphen.
    """
    dic = pyphen.Pyphen(lang='en_US')
    words = lyrics.split()
    syllables_list = []
    for word in words:
        hyphened_word = dic.inserted(word)
        syllables = hyphened_word.split('-')
        for s in syllables:
            syllables_list.append(s)
    return syllables_list
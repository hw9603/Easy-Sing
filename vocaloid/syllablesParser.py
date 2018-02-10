import pyphen
from utils import *

def parse_syllables(filename):
    """
    Return a list of syllables. Input words are split into syllables using
    function in pyphen.
    """
    dic = pyphen.Pyphen(lang='en_US')
    data_path = get("data_path")
    lyrics_file = open(data_path + filename, "r")
    lyrics = lyrics_file.read()
    words = lyrics.split()
    syllables_list = []
    for word in words:
        hyphened_word = dic.inserted(word)
        syllables = hyphened_word.split('-')
        for s in syllables:
            syllables_list.append(s)
    return syllables_list


"""Sample Usage"""
# s = parse_syllables("lyrics.txt")
# print(len(s))
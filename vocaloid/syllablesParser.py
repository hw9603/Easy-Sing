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
from urllib.request import Request, urlopen
import json
import requests
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
        url = "https://wordsapiv1.p.mashape.com/words/" + word
        headers = {"X-Mashape-Key": "9Bp7D9Gq43mshVEnul9CQfqD05g7p1ZMv72jsnBTH0HWLrHM1B","Accept": "application/json"}
        response = requests.get(url, headers=headers)

        response = response.json()
        print(response)
        try:
            syllables = response["syllables"]["list"]
        except:
            hyphened_word = dic.inserted(word)
            syllables = hyphened_word.split('-')

        for s in syllables:
            syllables_list.append(s)
    return syllables_list
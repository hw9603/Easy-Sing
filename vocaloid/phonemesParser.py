"""
Parse phonemes from lyrics.

Obtain lyrics one of these two ways:

1.
    from utils import *
    lyrics = get_lyrics_from_file("lyrics.txt")
2.
    lyrics = "These are some lyrics stored in a string"

Then, call the functions listed below like this:

phonemes_ssml = get_phonemes_ssml(lyrics)
phonemes = get_phonemes(phonemes_ssml)
ph_syllables = parse_phonemes_by_syllables(phonemes)
"""

from urllib.parse import *
from urllib.request import *
import xml.etree.ElementTree as ET
import string

def get_phonemes_ssml(lyrics):
    """
    Return the SSML format string from marytts server.
    Input: lyrics

    Note: this requires the marytts server to be running already.
    (perhaps we should refactor to explicitly start running it here...)
    """
    # Remove all punctuations in order to have all sentences processed.
    if not lyrics:
        return
    for c in string.punctuation:
        lyrics = lyrics.replace(c, "")

    host_name = "http://localhost"
    port_num = ":59125"
    operation = "/process?"
    input_text = lyrics
    input_type = "TEXT"
    output_type = "PHONEMES"
    locale = "en_US"
    get_string = host_name + port_num + operation + "INPUT_TEXT=" \
                 + quote_plus(input_text) + "&INPUT_TYPE=" + input_type \
                 + "&OUTPUT_TYPE=" + output_type + "&LOCALE=" + locale
    phonemes_ssml = urlopen(get_string).read()
    return phonemes_ssml


def get_phonemes(phonemes_ssml):
    """
    Return a list of phonemes. Each element of the list corresponds to the
    phonemes of a word.
    """
    if not phonemes_ssml:
        return
    root = ET.fromstring(phonemes_ssml)
    prefix = "{http://mary.dfki.de/2002/MaryXML}"

    word_nodes = root.getchildren()[0].getchildren()[0].getchildren()
    phonemes_list = []
    for t in word_nodes:
        phonemes_list.append(t.get('ph'))
    return phonemes_list


def parse_phonemes_by_syllables(phonemes_list):
    """
    Return a list of phonemes parsed by syllables. Each element of the list
    corresponds to the phonemes of a single syllables. Parsing of syllables
    is based on the dash symbol in the phonemes string.
    """
    if not phonemes_list:
        return []
    phonemes_syllables_list = []
    for ph in phonemes_list:
        try:
            ph_syll = ph.split('-')
        except:
            return
        # Notice: the trailing/leading whitespace is not removed
        for ps in ph_syll:
            phonemes_syllables_list.append(ps)
    return phonemes_syllables_list


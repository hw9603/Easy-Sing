from urllib.parse import *
from urllib.request import *
import xml.etree.ElementTree as ET
import string
from utils import *

def get_phonemes_ssml(filename):
    """
    Return the SSML format string from marytts server.
    Input: name of lyrics file
    """
    data_path = get("data_path")
    lyrics_file = open(data_path + filename, "r")
    lyrics = lyrics_file.read()
    # Remove all punctuations in order to have all sentences processed.
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
    phonemes_syllables_list = []
    for ph in phonemes_list:
        ph_syll = ph.split('-')
        # Notice: the trailing/leading whitespace is not removed
        for ps in ph_syll:
            phonemes_syllables_list.append(ps)
    return phonemes_syllables_list


"""Sample Usage"""
# phonemes_ssml = get_phonemes_ssml("lyrics.txt")
# ph = get_phonemes(phonemes_ssml)
# ph_syll = parse_phonemes_by_syllables(ph)



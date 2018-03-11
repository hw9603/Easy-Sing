"""Test the generation of a song."""

from vocaloid.song import *
from urllib.parse import *
from urllib.request import *

def test():

    s = Song("")

    s.addLyrics("The rest goes in the middle")

    melody_one = [
        [4, 0, 1],
        [4, 0, 1],
        [4, 0, 1],
    ]

    for note in melody_one:
        s.addNote(note[0], note[1], note[2])

    s.addRest(4)

    melody_two = [
        [4, 0, 1],
        [4, 0, 1],
        [4, 0, 1],
    ]

    for note in melody_two:
        s.addNote(note[0], note[1], note[2])

    xml = s.convertToMaryXML()
    file = open("./tmp/song.xml", "w")
    file.write(xml);
    file.close();
    host_name = "http://localhost"
    port_num = ":59125"
    operation = "/process?"
    input_text = xml
    input_type = "RAWMARYXML"
    output_type = "AUDIO"
    locale = "en_US"
    audio = "WAVE_FILE"
    get_string = host_name + port_num + operation + "INPUT_TEXT=" \
                 + quote_plus(xml) + "&INPUT_TYPE=" + input_type \
                 + "&OUTPUT_TYPE=" + output_type + "&LOCALE=" + locale\
                 + "&AUDIO=" + audio
    urlopen(get_string)
    urlretrieve(get_string, './test_speech.wav')

if __name__ == "__main__":
    test()

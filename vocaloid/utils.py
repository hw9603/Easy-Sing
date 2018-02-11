def get(attr):
    if not hasattr(get, 'config'):
        with open('config.json') as f:
            get.config = eval(f.read())
    node = get.config
    for part in attr.split('.'):
        node = node[part]
    return node

def get_lyrics_from_file(filename):
	"""Return lyrics stored in filename as a string."""
	data_path = get("data_path")
    lyrics_file = open(data_path + filename, "r")
    lyrics = lyrics_file.read()
    return lyrics
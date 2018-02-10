def get(attr):
    if not hasattr(get, 'config'):
        with open('config.json') as f:
            get.config = eval(f.read())
    node = get.config
    for part in attr.split('.'):
        node = node[part]
    return node
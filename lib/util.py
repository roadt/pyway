
import inspect
import json

def write(o, f):
    with open(f, 'w') as fp:
        fp.write(o)

def func_name():
    parent_frame = inspect.getouterframes(inspect.currentframe())[1]
    return parent_frame.function

def json_format(o):
    return json.dumps(o, indent=4)


def setup_proxy():
    import os
    os.environ.update({
        'http_proxy': 'http://localhost:7890',
        'https_proxy': 'http://localhost:7890'
    })




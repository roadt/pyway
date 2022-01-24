import os
import time
import threading
import json
from feedparser import *
from pprint import *
import requests
from os.path import dirname, join
import pytest

skip=pytest.mark.skip

def read(f):
    with open(join(dirname(__file__), f)) as fp:
        return fp.read()

def write(o, f):
    with open(join(dirname(__file__), f), 'w') as fp:
        return fp.write(o)

@skip
def test_read():
    s = read('parse_ret.json')
    print(type(json.loads(s)))
    assert False


def test_parse_rss2():
    feed = parse(read('sample-rss-2.xml'))
    write(json.dumps(feed, indent=True), 'rss2.json')
    pprint(feed)
    assert False

def test_parse_rss092():
    feed = parse(read('sample-rss-092.xml'))
    write(json.dumps(feed, indent=True), 'rss092.json')
    pprint(feed)
    assert False

def test_parse_rss091():
    feed = parse(read('sample-rss-091.xml'))
    write(json.dumps(feed, indent=True), 'rss091.json')
    pprint(feed)
    assert False

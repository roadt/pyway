from  util import *


def test_read2():
    s = read2(__file__)
    assert len(s)  > 0


def test_json_format():
    ret = json_format({'a': 1})
    assert len(ret.split("\n")) > 0



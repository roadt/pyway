from  util import *

def test_json_format():
    ret = json_format({'a': 1})
    assert len(ret.split("\n")) > 0



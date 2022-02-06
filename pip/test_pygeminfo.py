import pytest

from pygeminfo.gems import *

puma = Stats('puma')
@pytest.fixture
def gem():
    return  puma

class Test():

    @classmethod
    def setup_class(self):
        print('setup')
        pass

    def test_name(self, gem):
        assert gem.name() == 'puma'

    def test_sourceurl(self, gem):
        assert gem.sourceURL() == 'https://github.com/puma/puma'
        

def test_simple():
    s = Stats("puma")
    assert s.name() == 'puma'
    assert s.sourceURL() == 'https://github.com/puma/puma'


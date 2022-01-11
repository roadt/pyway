


import pytest
import  scrapetube
from util import *

import os
os.environ.update({
    'http_proxy': 'http://localhost:7890',
    'https_proxy': 'http://localhost:7890'
})

@pytest.mark.skip()
def test_get_channel_videos():
    videos = list(scrapetube.get_channel("UCCezIgC97PvUuR4_gbFUs5g"))
    write(json_format(videos), func_name()+".json")
    assert len(videos) >0
    assert False

def test_get_playlist_videos():
    videos = list(scrapetube.get_playlist('PLmpHbCVUPqHO4gy_RtoiWzQs_Uff_Bud7'))
    write(json_format(videos), func_name()+".json")
    assert len(videos) >0




import pytest


import UnityPy as up

import os

class TestEnvironment():
    
    def test_load_file(self):
        e = up.Environment()
        with open(os.envrion.get("TEST_UNITY3D_FILE"), 'rb') as f:
            print(e.load_file(f))
        assert False


class TestFiles:

    def test_BundleFile(self):
        file1=os.envrion.get("TEST_UNITY3D_FILE")
        file_type, reader = up.helpers.ImportHelper.check_file_type(file1)
        assert  file_type != None
        assert reader != None
        a = up.files.BundleFile(reader, None)
        assert a == None








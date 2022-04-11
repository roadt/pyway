
import sys
import os



default_message = "Away, wait a seconds"



def test(*args):
    if len(args) > 0:
        default_message = args[0]
    print default_message


if __name__ == '__main__':
    test()
    test('aaaaaaaaaaaaaa')
    test()


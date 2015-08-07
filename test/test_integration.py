__author__ = 'philip_j'

import sys
from python_integration import show

def test_myoutput(capsys): # or use "capfd" for fd-level
    show()

    out, err = capsys.readouterr()
    assert out == "I'm a Speaking class.\nI'm a Satellite class.\nI'm a Station class.\n"

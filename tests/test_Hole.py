import pytest

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, '/Users/HomeFolder/projects/Forest_Game_v2/Forest_Game_v2')
from Hole import Hole_
# from Aban import Abandoned
from charac_fg import Character_

@pytest.fixture
def setupmodule():
    return Hole_()
    return Character_()

def test_init(setupmodule):

    assert Hole_.examine == """ Whoa Whoa! What's this!? There's a hole three times
    your size in diameter in the dirt!
    """

def test_caveprompt(setupmodule):
    Character_.inven.append('Torch!')
    assert Character_.inven == ['Torch!']

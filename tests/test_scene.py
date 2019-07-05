import pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, '/Users/HomeFolder/projects/Forest_Game_v2/Forest_Game_v2')

from Scene import Scene_
from charac_fg import Character_


scene = Scene_()
character = Character_()

# is this even set up right? idk keep watching the video and researching...
#https://www.youtube.com/watch?v=IVrGz8w0H8c&list=PLeo1K3hjS3utzQYDNRNluzqJqpMXx6hHu&index=3
# https://docs.pytest.org/en/latest/xunit_setup.html
# solution
# https://docs.pytest.org/en/latest/fixture.html
@pytest.fixture
def setupmodule():
    global scene
    global character

def test_scene(setupmodule):
    # scene = Scene_()


    assert scene.name == "-"
    assert scene.input == "-"
    assert scene.solved == False
    assert scene.up == "-"
    assert scene.input == "-"
    assert scene.examine == "-"

def test_enter(setupmodule):
    # enter = Scene_()
    # NOT SURE IF I NEED TO DO ANYTHING WITH THESE...
    character.location = scene.name
    scene.right = '-'
    scene.left = '-'

    assert character.location == scene.name
    assert scene.right == "-"
    assert scene.left == "-"

def test_enter_again(setupmodule):

    character.location = "Pile of Dung"

    if character.location == "Pile of Dung":
        r = "Blah"
        assert r == "Blah"

    character.location = "Edge of Forest"

    scene.enter_var = 'b'

    if character.location == "Edge of Forest" and scene.enter_var == 'b':
        s = "Bleh"
        assert s == "Bleh"

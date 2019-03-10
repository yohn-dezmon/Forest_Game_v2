from nose.tools import *
import unittest
from unittest import mock
# from the module folder (Forest_Game) import the file Aban.py
# and then Abandoned is the class I'm testing!
import sys
sys.path.insert(0, '/Users/HomeFolder/projects/Forest_Game/Forest_Game')
from Scene import Scene_
from charac_fg import Character_

class TestScene(unittest.TestCase):

    def setup(self):
        scene = Scene_()
        character = Character_()

    def teardown(self):
        del scene


    def test_scene(self):
        # scene = Scene_()


        assert_equal(scene.name, "-")
        assert_equal(scene.input, "-")
        assert_equal(scene.solved, False)
        assert_equal(scene.up, "-")
        assert_equal(scene.input, "-")
        assert_equal(scene.examine, "-")

    def test_enter(self):
        # enter = Scene_()
        # NOT SURE IF I NEED TO DO ANYTHING WITH THESE...
        character.location = scene.name
        scene.right = '-'
        scene.left = '-'

        assert_equal(character.location, scene.name)
        assert_equal(scene.right, "-")
        assert_equal(scene.left, "-")

        character.location = "Pile of Dung"

        if character.location == "Pile of Dung":
            r = "Blah"
            assert_equal(r, "Blah")

        character.location = "Edge of Forest"

        scene.enter_var = 'b'

        if character.location == "Edge of Forest" and enter.enter_var == 'b':
            s = "Bleh"
            assert_equal(s, "Bleh")
            
if __name__ == '__main__':
    unittest.main()


        # I'm not sure if I need to test the enter.prompt() thing...

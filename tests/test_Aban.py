import pytest

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, '/Users/HomeFolder/projects/Forest_Game_v2/Forest_Game_v2')

from Aban import Abandoned
from charac_fg import Character_

Abandoned = Abandoned()
character = Character_()

# from Aban import Abandoned

# from charac_fg import Character_

# I'm not sure if this setup thing will work since I need to continually add
# to the character.inven...
# so we'll see, I might need to restructure my tests so that they are
# class tests...
# @pytest.fixture
# def setupmodule():
#
#     from Aban import Abandoned
#     from charac_fg import Character_
#     return Abandoned()

def test_init():

    assert Abandoned.name == "Abandoned Fire Pit"
    assert Abandoned.down == "-"

def test_pickupsticks():

    character.inven.append('sticks')
    

    assert character.inven == ['sticks']
# #
# def test_inspectbag(setupmodule):
#     character.inven.append('steel')
#     character.get_inven()
#
#     # I'm not sure if this will work, b/c I'm not sure if sticks will also be there!
#     assert_equal(character.inven, ['sticks','steel'])
# #
# def test_pickuprocks_maketorch(setupmodule):
#     character.inven.append('flint')
#     character.get_inven()
#
#     assert_equal(character.inven, ['Torch!'])
#
#
# # ok based upon this link: https://forum.learncodethehardway.com/t/testing-input-and-print/1757/10
# # I think I need to create separate test functions for each possible
# # input and I need to use a module called mock from unittest to create fake inputs...
#
# def test_move_right(setupmodule):
#     right = Abandoned()
#
#     org_input = mock.builtins.input
#     mock.builtins.input = lambda _: "right"
#     # if anything causes an error it will most likely be this line...
#     assert_equal(right.move(), 'river')
#     mock.builtins.input = org_input

import pytest
from Forest_Game.Aban import Abandoned
# from Aban import Abandoned
from Forest_Game.charac_fg import Character_
# from charac_fg import Character_

# I'm not sure if this setup thing will work since I need to continually add
# to the character.inven...
# so we'll see, I might need to restructure my tests so that they are
# class tests... 
@pytest.fixture
def setupmodule():
    aban = Abandoned()
    character = Character_()

def test_init(setupmodule):


    assert aban.examine = """
    ... it appears someone has been here recently. You see
    an abandoned fire pit, some sticks lying next to the fire pit,
    and you see a small green bag off next to some rocks.
    """

    assert aban.name == "Abandoned Fire Pit"
    assert aban.down == "-"





def test_pickupsticks(setupmodule):
    # stick = Abandoned()
    character.inven.append('sticks')
    character.get_inven()

    assert_equal(character.inven, ['sticks'])
#
def test_inspectbag(setupmodule):
    character.inven.append('steel')
    character.get_inven()

    # I'm not sure if this will work, b/c I'm not sure if sticks will also be there!
    assert_equal(character.inven, ['sticks','steel'])
#
def test_pickuprocks_maketorch(setupmodule):
    character.inven.append('flint')
    character.get_inven()

    assert_equal(character.inven, ['Torch!'])


# ok based upon this link: https://forum.learncodethehardway.com/t/testing-input-and-print/1757/10
# I think I need to create separate test functions for each possible
# input and I need to use a module called mock from unittest to create fake inputs...

def test_move_right(setupmodule):
    right = Abandoned()

    org_input = mock.builtins.input
    mock.builtins.input = lambda _: "right"
    # if anything causes an error it will most likely be this line...
    assert_equal(right.move(), 'river')
    mock.builtins.input = org_input

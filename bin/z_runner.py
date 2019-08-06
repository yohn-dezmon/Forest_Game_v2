# import pdb
import sys
sys.path.insert(0, '/Users/HomeFolder/projects/Forest_Game_v2/Forest_Game_v2')

from Scene import Scene_
from Edge import Edge_
from Thorn import Thorn_
from Aban import Abandoned
from Gigan import GiganticTree
from Hole import Hole_
from Pile import PileDung
from River import River_
from charac_fg import Character_


class Runner(object):
    """
    This is the class that runs the game, and allows the user to enter into
    different scenes. The program is written such that once a player enters
    a scene, they can complete all of the activities within the methods available
    in the class and with the methods inherited from the parent Scene_ class.
    """
    # This is a dictionary which consists of string key values that refer to
    # the scene modules in the form of class instantiations.
    scenes = {
            'edge' : Edge_(),
            'thorn' : Thorn_(),
            'pile' : PileDung(),
            'aban_fire' : Abandoned(),
            'hole' : Hole_(),
            'river' : River_(),
            'gigan_tree' : GiganticTree(),
            'nothing' : "hmmm nothing really here"
    }

    def __init__(self):
        pass

    def start_edge(self):
        # The runner class is instantiated and then calls this method to start_edge
        # the game.

        # Here the edge key is used to instantiate the Edge_ class/scene.
        edge = Runner.scenes.get('edge')
        # Here the enter method is called for the Edge_ scene.
        Character_.location = "Edge of Forest"
        edge.enter()
        while Character_.location in ["Edge of Forest", 'location']:
            # This while loop takes the value of the scenes directional attributes
            # and calls functions that allow entry into other scenes.
            if edge.right == 'thorn':
                self.into_thorn()
            elif edge.left == 'pile':
                self.into_pile()
            elif edge.down == 'aban_fire':
                self.into_fire()

# All of the into_x methods only need if statements if they are actually going into another scene
# if the result of the movement is not a new scene, it is already accounted for in the
# Scene move method!
    def into_edge(self):
        edge = Runner.scenes.get('edge')
        edge.enter_again()
        while Character_.location == "Edge of Forest":
            if edge.right == 'thorn':
                self.into_thorn()
            elif edge.left == 'pile':
                self.into_pile()
            elif edge.down == 'aban_fire':
                self.into_fire()



    def into_thorn(self):
        thorn = Runner.scenes.get('thorn')
        thorn.enter()
        while Character_.location == "Thorny Patch!":
            if thorn.name == "Thorny Patch!" and thorn.left == 'edge':
                self.into_edge()

    def into_pile(self):
        pile = Runner.scenes.get('pile')
        pile.enter()
        while Character_.location == "Pile of Dung":
            if pile.name == "Pile of Dung" and pile.right == 'edge':
                self.into_edge()

    def into_fire(self):
        fire = Runner.scenes.get('aban_fire')
        fire.enter()
        while Character_.location == "Abandoned Fire Pit":
            if fire.name == "Abandoned Fire Pit" and fire.right == 'river':
                self.into_river()
            elif fire.name == "Abandoned Fire Pit" and fire.down == 'hole':
                self.into_hole()
            elif fire.name == "Abandoned Fire Pit" and fire.up == 'edge':
                self.into_edge()

    def into_river(self):
        river = Runner.scenes.get('river')
        river.enter()
        while Character_.location == "River":
            if river.name == "River" and river.right == 'gigan_tree':
                self.into_gigan()
            # I want to put a specific death scene for going down on the river...

    def into_gigan(self):
        gigan = Runner.scenes.get('gigan_tree')
        gigan.enter()
        while Character_.location == "Gigantic Tree":
            # I should really update this so that left puts you on the LEFT side of the river.
            if gigan.name == "Gigantic Tree" and gigan.left == 'river':
                self.into_river()
            elif gigan.name == "Gigantic Tree" and gigan.down == 'hole':
                self.into_hole()
            elif gigan.name == "Gigantic Tree" and gigan.up == 'edge':
                self.into_edge()

    def into_hole(self):
        hole = Runner.scenes.get('hole')
        hole.enter()
        while Character_.location == 'Hole':
            if hole.name == 'Hole' and hole.up == 'aban_fire':
                self.into_fire()

# debugging to fix 'move left' call in initial Edge of Forest map
# pdb.set_trace()
c = Character_()
b = Runner()

b.start_edge()

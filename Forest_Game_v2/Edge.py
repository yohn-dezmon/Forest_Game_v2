import sys
import Scene
from charac_fg import Character_

class Edge_(Scene.Scene_):
    """ This is the first scene on the map.
    From here you can either go to the thorns or the pile of dung scenes.
    """

    def __init__(self):
        super(Edge_, self).__init__()
        self.charac = Character_()
        # I needed to includ the enter_var attribute to distinguish between
        # the first entry into this scene and all other entries.
        self.enter_var = 'a'
        self.examine = """
        You look around, but there isn't much to see.
        Hmmm but something about those shrubs... looks quite pleasant!
        """
        self.name = "Edge of Forest"

    def enter(self):
        # This is the first entry into Edge_, distinguished by the value 'b' for enter_var
        # You can see the different text that is displayed in the enter method
        # of the Scene_ class.
        self.enter_var = 'b'
        self.name = "Edge of Forest"
        super(Edge_, self).enter()


    def enter_again(self):
        # This method is for all other entries into this scene, this is called
        # in the z_runner.py module.
        self.enter_var = 'a'
        super(Edge_, self).enter()

    def examine_(self):
        super(Edge_, self).examine_()

    def nothing_(self):
        super(Edge_, self).nothing_()

    def prompt(self):
        super(Edge_, self).prompt()

    def use_func(self):
        super(Edge_, self).use_func()

    def instructions(self):
        super(Edge_, self).instructions()

    # def moveleft(self):
    #     self.left = 'pile'
    #     return self.left
        # This method on all scenes allows the user's input to be translated
        # to a string that is then used as a key to call a value from a dictionary
        # in the z_runner.py module.
        # self.input = input("Which direction would you like to go? \n")
        # super(Edge_, self).move()
        # if self.input.lower() in ['right', 'east']:
        #     self.right = 'thorn'
        #     return self.right
        # elif self.input.lower() in ['left','west']:
        #     self.left = 'pile'
        #     return self.left
        # elif self.input.lower() in ['down','south']:
        #     self.down = 'aban_fire'
        #     return self.down
        # elif self.input.lower() in ['up','north']:
        #     self.nothing_()



# b = Edge_()
z = Character_()

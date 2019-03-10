import Scene
from charac_fg import Character_
# from Edge import Edge_

class PileDung(Scene.Scene_):

    def __init__(self):
        super(PileDung, self).__init__()
        self.charac = Character_()
        self.name = "Pile of Dung"
        self.examine = """
        The tree to the right of the pile of dung seems to be shaking ever so
        slightly...
        """


    def examine_(self):
        super(PileDung, self).examine_()

    def prompt(self):
        super(PileDung, self).prompt()

    def use_func(self):
        super(PileDung, self).use_func()

    def squirrel_tree(self):
        print("""
        aha! It was a squirrel that was shaking the tree.
        But this is not any squirrel, it's an enchanted squirrel.

        What will you do next?
        a. leave the squirrel alone
        b. tease the squirrel
        c. dance for the squirrel
        """)
        squirrel_inp = input("> ")
        if squirrel_inp in ['a','a.','A','A.']:
            PileDung.prompt(self)
        elif squirrel_inp in ['b','b.','B','B.']:
            print("The squirrel jumps down and bites you on the nose!")
            Character_.decrease_hp()
            PileDung.prompt(self)
        elif squirrel_inp in ['c','C','C.','c.']:
            print("The squirrel is impressed, he places a fedora on your head!")
            Character_.inven.append('fedora')
            Character_.get_inven()
            PileDung.prompt(self)


    def enter(self):
        super(PileDung, self).enter()


    def witch(self):
        print("""
        'Oh no, not so fast!'
        A Cursed Witch appears and casts a terrible spell on you.
        From now on, your lips are permanently chapped!
        and when you go to speak...
        """)
        Character_.curse = True
        Character_.decrease_hp()
        print("ouchie!")

    def move(self):
        self.input = input("Which direction would you like to go? \n")
        super(PileDung, self).move()
        if self.input.lower() in ['right', 'east']:
    # work on this still
            self.witch()
            self.right = 'edge'
            return self.right
        elif self.input.lower() in ['left','west']:
            self.nothing_()
        elif self.input.lower() in ['down','south']:
            self.nothing_()
        elif self.input.lower() in ['up','north']:
            self.nothing_()

z = Character_()

from Scene import Scene_
from charac_fg import Character_

class GiganticTree(Scene_):

    def __init__(self):
        super(GiganticTree, self).__init__()
        self.charac = Character_()
        self.examine = """
        Explain something bout the Gigantic Tree boi!
        """
        self.name = "Gigantic Tree"

    def enter(self):
        super(GiganticTree, self).enter()
        

    def examine_(self):
        super(GiganticTree, self).examine_()

    def nothing_(self):
        super(GiganticTree, self).nothing_()

    def prompt(self):
        super(GiganticTree, self).prompt()

    def use_func(self):
        super(GiganticTree, self).use_func()

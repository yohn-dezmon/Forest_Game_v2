from Scene import Scene_
from charac_fg import Character_
import time

class River_(Scene_):

    def __init__(self):
        super(River_, self).__init__()
        self.charac = Character_()
        self.examine = """
        There's not much around, just the river infront of you, some brush on the
        bank. And what ever that prickly thing was that poked your bum.
        """
        self.name = "River"

    def enter(self):
        super(River_, self).enter()

    def examine_(self):
        super(River_, self).examine_()

    def nothing_(self):
        super(River_, self).nothing_()

    def prompt(self):
        super(River_, self).prompt()

    def use_func(self):
        super(River_, self).use_func()

    def spirit(self):
        print("""
You find a piece of bark with the letters 'HISF' written on it


*@*@*!@*@*!*!*@*@!
 A spirit arises from the whitewater of the river
 *!@*#*@#*!@*#*@#**

 Spirit: Young boi boi! wooof! what a snout ya got on ya! :D
 Now riddle me this, YA FOOL!

 What is the hungry man's F?
        """)
        self.spirit_inp()

    def spirit_inp(self):

        usr_input = input(">>>>")


        while usr_input != 'fish':
            print("No no no! Think boi boi think!")
            self.spirit_inp()

        if usr_input == 'fish':
            print("""
    Yes yes! The Hungry Man's F...
IS FISH! jajajajajajajaj
Now I'll introduce you a good friend of mine...
OoooOoo Wise Man .... !
            """)
            time.sleep(2.0)
            print(".")
            time.sleep(2.0)
            print("\t.")
            time.sleep(2.0)
            print("\t\t.")
            time.sleep(2.0)
            print("""
        A long haired man on a raft approaches from your left hand side.
        He pulls the raft over to the bank and you hop on the raft with him


        Wise Man: ahhh you look hungry, here have some fish!
            """)
            time.sleep(10.0)
            Character_.increase_hp()
            time.sleep(4.0)
            print("""
The wise man goes to say something else, but before he can... you
reach the other side of the river and hop off!
            """)
            time.sleep(8.0)
            self.move_right()


        # def move_right():
        #
        #
        #     self.right == 'gigan_tree'
        #     return self.right

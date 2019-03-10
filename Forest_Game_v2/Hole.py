import Scene
from charac_fg import Character_

class Hole_(Scene.Scene_):

    def __init__(self):
        super(Hole_, self).__init__()
        self.examine = """ Whoa Whoa! What's this!? There's a hole three times
        your size in diameter in the dirt!
        """
        self.name = "Hole"

    def enter(self):
        super(Hole_, self).enter()

    def examine_(self):
        super(Hole_, self).examine_()

    def nothing_(self):
        super(Hole_, self).nothing_()

    def prompt(self):
        super(Hole_, self).prompt()

    def use_func(self):
        super(Hole_, self).use_func()




    def hole_dungeon(self):
        print(""""
        You take several steps before you begin uncontrollably sliding into
        the dirt hole! You've now reached a flat plain at the bottom of the hole.
        It's rather dark, but you hear chattering in the distance...
        """)
        self.cave_prompt()

    def cave_prompt(self):
        cave_inp = input("""
            What will you do next?

            a. Scream and cry for help!
            b. Use torch
            c. Start sprinting into the depths of the hole
        """)

        accept_inp = ['a','a.','A','A.','b','b.','B','B.','c','C','C.','c.']
        torch = ['torch']

        while cave_inp not in accept_inp:
            print("""
            please type either a, b, or c!""")
            cave_inp = input("> ")

        while (cave_inp in ['b','b.','B','B.']) and ('Torch!' not in Character_.inven):
            print("You do not have any torches silly boi!")
            cave_inp = input("""
                What will you do next?

                a. Scream and cry for help!
                c. Start sprinting into the depths of the hole
            """)

        if cave_inp in ['a','a.','A','A.']:
            print("Human sized rodents stampede towards you and trample you...")
            Character_.die()

        elif cave_inp in ['b','b.','B','B.'] and 'Torch!' in Character_.inven:
            print("You set fire to your torch, and voila, you have light!")
            print(""" boomp.... boomp....
                from further inside the hole you hear large footsteps
                    boomp .... boomp
                    It's an ogre!!! """)
            print("""OGRE: Hello little boi! Now tell me boi, what is the name
            of those holes in your nose?""")
            cave_inp_ = input("> ")
            while cave_inp_ not in ['nostrils','nostril']:
                print("The ogre flicks your rather large shnoz!")
                Character_.decrease_hp()
                cave_inp_ = input("> ")
            if cave_inp_.lower() in ['nostrils','nostril']:
                print("""OGRE: That's right! Now, what rhymes with nostrils?""")
                rhyme_inp = input("> ")
                possible_resp = ['soft gills','boss bills','soft thrills','boss tills',
                'ross bills', 'sauce hills','toss pills','fossils','cost bills',
                'soft fill','soft fills', 'austral', 'claustral', 'rostral', 'colossals',
                'colossal','boss bill','soft tills','soft till','soft bill','soft bills'
                'ross bill']
                while rhyme_inp not in possible_resp:
                    print("OGRE: I'll give you a hint, two words + slant rhyme!")
                    rhyme_inp = input("> ")
                if rhyme_inp.lower() in possible_resp:
                    print("""
                    OGRE: Aha! You are quite clever young boi boi!
The ogre reaches into his undewear, and pulls out a tiny wooden chest!
    """)
                if ('golden key' in Character_.inven):
                    print("you use the key to open the chest")
                    print("*"*10)
                    print("It's magical chapstick!")
                    Character_.inven.append('chap stick')
                    if Character_.curse == True:
                        print("The curse is lifted from thine lips!")
                        Character_.curse = False
                    elif Character_.curse == False:
                        print("""
OGRE: Ok clever boi, enough of your quips, out you go!""")
                    self.name = "Abandoned Fire Pit"
                    self.move_up()
                else:
                    print("""
OGRE: Ahh but you do not have the key to open my chest!
Please return once you do ;)
Out you go!!!!!""")
                    self.name = "Abandoned Fire Pit"
                    print("""


                    """
                    self.enter()



        elif cave_inp in ['c','C','C.','c.']:
            print("""Queue the music!!
                Here come the rodents
                    You're Running along side them!
                        Your pumping your arms up in a dance!
                    AHHH! You trip and fall!
                """)
            Character_.decrease_hp()
            self.cave_prompt()

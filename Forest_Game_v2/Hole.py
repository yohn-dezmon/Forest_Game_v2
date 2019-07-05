import Scene
from charac_fg import Character_
import time

class Hole_(Scene.Scene_):

    def __init__(self):
        super(Hole_, self).__init__()
        time.sleep(1.0)
        self.examine = """ Whoa Whoa! What's this!? There's a hole three times
        your size in diameter in the dirt!
        """
        self.name = "Hole"

    def enter(self):
        time.sleep(1.0)
        super(Hole_, self).enter()

    def examine_(self):
        time.sleep(1.0)
        super(Hole_, self).examine_()

    def nothing_(self):
        time.sleep(1.0)
        super(Hole_, self).nothing_()

    def prompt(self):
        super(Hole_, self).prompt()

    def use_func(self):
        super(Hole_, self).use_func()




    def hole_dungeon(self):
        time.sleep(1.0)
        print("""
You take several steps before you begin uncontrollably sliding into
the dirt hole! You've now reached a flat plain at the bottom of the hole.
It's rather dark, but you hear chattering in the distance...
        """)
        time.sleep(2.0)
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
            time.sleep(1.0)
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
            time.sleep(1.0)
            print("You set fire to your torch, and voila, you have light!")
            time.sleep(1.0)
            print("""
boomp.... boomp....""")
            time.sleep(1.0)
            print("""from further inside the hole you hear large footsteps
        boomp .... boomp""")
            time.sleep(1.0)
            print("It's an ogre!!!")
            time.sleep(1.0)
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
                split_inp = rhyme_inp.split(" ")
                possible_resp = ['soft gills','boss bills','soft thrills','boss tills',
                'ross bills', 'sauce hills','sauce kills', 'toss pills','fossils','cost bills',
                'soft fill','soft fills', 'austral', 'claustral', 'rostral', 'colossals', 'toss hills'
                'colossal','boss bill','soft tills','soft till','soft bill','soft bills', 'brothels'
                'ross bill', 'soft krill', 'boss krill']
                first_words = ['boss','loss','toss','cost','ross','soft','sauce','broth']
                second_words = ['krill','krills','pills','pill','till','tills','hill','hills','kill','kills',
                'bill','bills','mill','mills','gill','gills']
                while split_inp[0] not in first_words and split_inp[1] not in second_words:
                    print("OGRE: I'll give you a hint: the rhyme can be two words or just one")
                    rhyme_inp = input("> ")
                    split_inp = rhyme_inp.split(" ")
                while split_inp[0] in first_words and split_inp[1] not in second_words:
                    time.sleep(1.0)
                    print("the first word is correct, the second is not!")
                    rhyme_inp = input("> ")
                    split_inp = rhyme_inp.split(" ")
                while split_inp[0] not in first_words and split_inp[1] in second_words:
                    time.sleep(1.0)
                    print("the first word is incorrect, the second word is right!")
                    rhyme_inp = input("> ")
                    split_inp = rhyme_inp.split(" ")
                if (rhyme_inp.lower() in possible_resp) or (split_inp[0] in first_words and split_inp[1] in second_words):
                    print("""
OGRE: Aha! You are quite clever young boi boi!
The ogre reaches into his pocket, and pulls out a tiny wooden chest!
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
                    time.sleep(1.0)
                    print("""


                    """)
                    time.sleep(1.0)
                    self.enter()


        elif cave_inp in ['c','C','C.','c.']:
            time.sleep(1.0)
            print("Queue the music!!")
            time.sleep(1.0)
            print("""
            Here come the rodents""")
            time.sleep(1.0)
            print("""
                    You're Running along side them!""")
            time.sleep(1.0)
            print("""
                        Your pumping your arms up in a dance!""")
            time.sleep(2.0)
            print("""
                    AHHH! You trip and fall!
                """)
            Character_.decrease_hp()
            self.cave_prompt()

        def splitting_input(self):
            usr_inp = input("> ")
            split_input = usr_input.split(" ")
            return usr_inp, split_input;

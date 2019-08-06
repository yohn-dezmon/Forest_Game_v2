import sys
from charac_fg import Character_
from lexicon import Lexicon
from parser import *
import time

class Scene_(object):
    """ This is the parent class for all scene subclasses which are located
    in separate modules. Here I attempted to create methods that would apply
    to all of the subclasses and would include the basis for later modification.
    """

    def __init__(self):
        # This special method gives the general attributes for all of the
        # subclasses (scenes).  I set up the directional attributes as such
        # so that when they are assigned values in the move method of each
        # subclass, they will return a value that allows for movement
        # from one scene to the next in the z_runner module.
        self.name = '-'
        self.input = '-'
        self.solved = False
        self.up = '-'
        self.down = '-'
        self.left = '-'
        self.right= '-'
        # self.input = '-'
        self.examine = '-'
        self.usr_inp = '-'
        self.word_list = [('noun','player'), ('verb', 'kill'), ('noun', 'cabinet')]
        self.parse_var = Parser(self.word_list)
        self.action = self.parse_var.parse_sentence()
        self.filler_inp = "Filler"
        self.lexicon = Lexicon(self.filler_inp)
        # self.parser = Parser(self.word_list)



    def enter(self):
        # Here I set the character's location to the subclass' name.
        # This was done to allow for scene specific entrance text
        # that were printed with if statements.
        #
        # The self.right and self.left are set to their default dashes here
        # to ensure that upon entering a scene the values from the previous
        # scene do not carry over, or that the values from when this scene
        # was exited previously remain intact.
        Character_.location = self.name
        self.right = '-'
        self.left = '-'
        # This is the greeting displayed upon entering any scene
        greeting = (f"""
                You've entered: {self.name}!
        """)
        print("-"*50)
        print(f"""

        {greeting}

        """)
        print("-"*50)
        time.sleep(2.0)

        if Character_.location == "Pile of Dung":
            # This is an example of a specific greeting, in this case when the
            # character enters the Pile of Dung scene.
            print("""
            OoOoOO what is that smell?! Ahhhh, it's a large pile of dung!
            """)
        elif Character_.location == "Gigantic Tree":

            print("""

As you
            """)

        elif Character_.location == "Edge of Forest" and self.enter_var == 'b':
            # I had to use the self.enter_var == 'b' here to ensure that
            # Edge of forest had a different greeting upon being entered initially
            # versus later in the game, given that it is the first scene and
            # provides a text-introduction to the game.
            print("""
            ~*~**`*~*`
    You are an inexperienced lad, lacking in resources,
    and you have a rather large nose. You happen upon a forest where you
    think there may be food, shelter, and perhaps a magical potion to
    shrink your nose.
    ***~~**~*~

    You now find yourself at the edge of the forest, surrounded by shrubs.

    [please type help for instructions!]
            """)
            # time.sleep(6.0)
            # print("\t.")
            # time.sleep(1.0)
            # print("\t\t.")
            # time.sleep(1.0)
            # print("\t\t\t.")
            # time.sleep(1.0)
            # print("\t\t.")
            # time.sleep(1.0)
            # print("\t.")
            # time.sleep(2.0)
            self.instructions()

        elif Character_.location == "River":
            print("""
*~*~*~*~*
You step out of the bush and the moist air brushes against your rosy
cheeks.
Your shoe dips into the sticky dirt, and you notice that you are
approaching a rapidly flowing river!
*~*~*~*~*
You take a seat to catch some rest on the bank of the river, and as you
go to sit, you prick your buttox on something!
            """)


        # This is necessary to allow the player to continue playing.
        self.prompt()



    def nothing_(self):
        # This method is called upon when a character desires to walk in a
        # directional in which there is no scene to enter.
        print("""

                    Hmmmm.... not much to see here, ye young laddy!

        """)
        self.up = 'nothing'
        self.prompt()

    def examine_(self):
        # This method allows for the scene specific text to be displayed
        # giving the character a better idea of what can be accessed within
        # each scene.
        print(self.examine)
        print("\n")
        self.prompt()

    def scan_n_parse(self, usr_input):
        lexicon = Lexicon(usr_input)
        word_list = lexicon.scan()
        # print(word_list)
        self.parse_var = Parser(word_list)
        self.action = self.parse_var.parse_sentence()
        # IDK if this syntax is correct
        # hmm why wasn't self.action.object there? was that on purpose??
        return self.action.subject, self.action.verb, self.action.object, self.action.number

    def prompt(self):
        # This is the most used method of the game. From this method
        # the user can elect to move, examine, view the contents of their
        # inventory, and utilize the contents of their inventory.
        usr_input = input("What dare the young lad try next? \n")
        self.scan_n_parse(usr_input)

        # I'd like to create more lists like this to make my if statments
        # smaller!!
        bum_words = ['butt','bum','buttox','ass','bottom']
        move_words = ['go','walk','move']


        if (self.action.verb in ['examine','inspect','look','check out','eat',
        'cut'] and self.action.object in ['shrubs','shrub'] and
         self.name == 'Edge of Forest'):
        # This is the first time a scene specific if statement appears.
        # this is a conditional statement that requires that both a specific
        # command be given, and that it be within a certain scene.
        # if this statement evaluates to false, the else clause will be
        # executed, allowing the prompt method to restart.
            print("\nMmmm you eat some of the shrub fruit")
            # I chose to make the increase_hp method of Character_
            # be instantiation-independent so that the value of the
            # character's health will remain constant upon changing from
            # scene to scene.
            Character_.increase_hp()
            self.prompt()

        elif (self.action.subject in ['shrub','shrubs'] and
         self.name == 'Edge of Forest'):
            print("\nMmmm you eat some of the shrub fruit")

            Character_.increase_hp()
            self.prompt()


        elif (self.action.verb in ['examine','inspect','look','check',
        'pricked','prick'] and self.action.object in bum_words):
            self.spirit()

        elif (self.action.object in bum_words or self.action.subject in bum_words
        and self.name == 'River'):
            self.spirit()

        elif (self.action.verb in ['examine','inspect','look','check','eat',
        'cut'] and self.action.object in ['tree'] and self.name == 'Pile of Dung'):
            self.squirrel_tree()

        elif (self.action.verb in ['leave']):
            usr_input = input("Where to young b? \n")
            self.scan_n_parse(usr_input)

            if (self.action.subject in ['right','east']):
                self.move_right()
            elif (self.action.subject in ['left', 'west']):
                self.move_left()
            elif (self.action.subject in ['up', 'north']):
                self.move_up()
            elif (self.action.subject in ['down', 'south']):
                self.move_down()
            else:
                self.prompt()

        elif (self.action.verb in move_words and self.action.object
        in ['right', 'east']):
            self.move_right()

        elif (self.action.verb in move_words and self.action.object
        in ['left', 'west']):
            self.move_left()

        elif (self.action.verb in move_words and self.action.object
        in ['up', 'north']):
            self.move_up()

        elif (self.action.verb in move_words and self.action.object
        in ['down', 'south']):
            self.move_down()

        elif (self.action.verb in move_words and self.action.object
        in ['forest','woods']):
            self.move_down()

        elif (self.action.verb in ['examine','inspect','look','check']
        and self.action.object in ['forest','scene','area'] and
        self.name == 'Edge of Forest'):
            self.examine_()

            # I think this should work b/c what ever object comes after up will not be interpreted
            # as an object... It will get interpreted if anything as a number.
        elif (self.action.verb == 'pick' and self.action.object == 'up'):
            self.use_func()

        elif (self.action.verb in ['use','touch','examine','check','pick',
        'wear','don', 'inspect','look','put', 'get'] and self.action.object in ['mirror',
        'key','fedora','sticks', 'stick','torch','flint','steel','bag',
        'rock','rocks']):
            self.use_func()

        elif (self.action.verb == 'get' and self.action.object in
        ['hp','heatlh']):
            Character_.get_hp()
            self.prompt()

        elif self.action.object in ['inventory','item','items']:
            Character_.get_inven()
            self.prompt()

        elif self.action.subject in ['inventory','item','items']:
            Character_.get_inven()
            self.prompt()

        elif (self.action.verb in ['examine','inspect','look','check']):
            self.examine_()

        elif (self.action.verb in ['enter','go','explore','get']
        and self.action.object == 'hole' and self.name == "Hole"):
        # It's cool that with inheritance I can call a method from a child class
        # just by referencing self. before the method name!
            self.hole_dungeon()

        elif self.action.verb in ['crawl','go'] and self.name == "Thorny Patch!":
            self.crawl()

        elif self.action.verb == 'quit':
            quit(0)

        elif (self.action.verb in ['help','give','get'] and (self.action.object or
        self.action.subject in ['instructions','help'])):
            self.instructions()

        else:
            # This is the clause that is executed if a player choses a scene
            # specific action while not in the correct scene.
            self.error_specific()

    def move_right(self):
        # This function provides a list for all of the possible movement commands
        # I wonder if there is a way to condense all of the if statements for a
        # particular direction...
        if self.name == 'Edge of Forest':
            self.right = 'thorn'
            return self.right

        elif self.name == 'Abandoned Fire Pit':
            self.right = 'river'
            return self.right

        elif self.name == 'Hole' or self.name == 'Thorny Patch!':
            self.nothing_()

        elif self.name == 'Pile of Dung':
            self.witch()
            self.right = 'edge'
            return self.right

        elif self.name == 'River':
            self.right = 'gigan_tree'
            return self.right

        # we still need to set up directions for River and Gigantic tree.

    def move_left(self):

        if self.name == 'Edge of Forest':
            self.enter_var = 'a'
            self.left = 'pile'
            return self.left

        elif self.name in ['Abandoned Fire Pit','Hole','Pile of Dung']:
            self.nothing_()

        elif self.name == 'Thorny Patch!':
            self.left = 'edge'
            return self.left

    def move_up(self):

        if self.name in ['Edge of Forest','Thorny Patch!','Pile of Dung']:
            self.nothing_()

        elif self.name == 'Hole':
            self.up = 'aban_fire'
            return self.up

        elif self.name == 'Abandoned Fire Pit':
            self.up = 'edge'
            return self.up

    def move_down(self):

        if self.name == 'Edge of Forest':
            self.down = 'aban_fire'
            return self.down

        elif self.name in ['Thorny Patch!','Hole','Pile of Dung']:
            self.nothing_()

        elif self.name == 'Abandoned Fire Pit':
            self.down = 'hole'
            return self.up

        elif self.name == 'Gigantic Tree':
            Character_.die()


    def use_func(self):

        if (self.action.object == 'key'
        and self.name == "Hole final"):
            print("You unlock the chest, horah!")
            self.prompt()

        elif (self.action.object == 'key'
        and self.name != "Hole final"):
            print("ah I'm sorry, this cannot be used here")
            self.prompt()

        elif (self.action.object == 'mirror'
        and 'golden key' in Character_.inven):
            print("""
            oh man, is that really what I look like?
            """)
            self.prompt()

        elif (self.action.object == 'mirror'):
            print("""
            You stare into your mirror and observe your gaping nares.
            But wait, as you stare into the depths of your nostrils
            you notice something shiny... a wet booger perhaps?
            You take a closer look and you see that the tiny object is a
            golden key!
            You pick your nose and extract the key, congrats!
            """)
            Character_.add_inven('golden key')
            Character_.get_inven()
            self.prompt()

        # TO SAVE SPACE HERE, it would be cool to have dictionary where each object that is scene
        # specific was set up as a key:value thing wehre the object was the key and the value
        # was the name of the room... such that ....

        elif (self.action.object == 'fedora' and Character_.fedora == 'off'):
            print("""           !
            You place the fedora atop your little head
            lookin' fresh, lad!
            """)
            Character_.fedora = "on"
            self.prompt()

        elif (self.action.object == 'fedora' and Character_.fedora == 'on'):
            print("""
            You remove the fedora, revealing a mop of a hairdo.
            """)
            Character_.fedora == 'off'
            self.prompt()

        # set up a NESTED IF for Abandoned Fire Pit?   LET'S TRY!

        elif self.name == "Abandoned Fire Pit":
            if (self.action.object == 'bag' or self.action.number == 'bag'):
                self.inspect_bag()
            elif (self.action.object in ['rock','rocks']
             or self.action.number in ['rock','rocks']):
                self.pick_up_rocks()
            elif (self.action.object in ['stick', 'sticks']
            or self.action.number in ['stick', 'sticks']):
                self.pick_up_sticks()
            else:
                self.prompt()


        elif (self.action.object == 'torch' and Character_.torch == "out"):
            print("You set fire to your torch, and voila, you have light!")
            self.prompt()

        elif (self.action.object == 'torch' and Character_.torch == "lit"):
            print("You douse your flame, no more light for now!")
            Character_.torch = "out"
            self.prompt()

        elif self.action.object in ['flint', 'sticks', 'steel']:
            print("This item isn't very useful by itself...")
            self.prompt()

        elif (self.action.object not in Character_.inven):
            print("""
            You do not have that item.
            You must type the item as it appears in your inventory, ye young laddy!
            Here is a list of the items you have: """)
            for x in Character_.inven:
                print("\n")
                print(x)
            self.prompt()

        else:
            self.error_specific()


    def error_specific(self):
        print("\n\tOoOOoOps! You cannot use that command here!")
        self.prompt()

    def instructions(self):
        print("""
        LIST OF COMMANDS (please read carefully!):""")
        time.sleep(3.0)
        print("""
        MOVEMENT COMMANDS
        Type 'move', then any of the following:

        up, north - move to the scene north of your character
        down, south - move to the scene south of your character
        left, west - move to the scene west of your character
        right, east - move to the scene east of your character""")
        time.sleep(5.0)
        print("""

        GENERAL SCENE COMMANDS:

        examine (object/area) - allows you to examine the scene [or a particular
        object]
        help - will print this list of commands
        inventory - displays a list of the items your have in your inventory
        use (object within inventory)- combined with an item in your inventory,
        will allow you to use it
        health - view your current health""")
        time.sleep(7.0)

        print("""

        SCENE SPECIFIC COMMANDS:

        crawl - allows you to crawl
        tree - allows you to see what's going on with the tree
        shrubs - allows you to inspect the shrubs
        bag - lets you inspect the bag
        sticks - lets you pick up sticks
        rocks - allows you to inspect the rocks

        """)
        time.sleep(5.0)
        # hmm.. should this be Scene.prompt() instead of self.prompt() which leads to
        # Edge.py?
        # Edge_.enter_again()


    def break_loop(self):
        self.prompt()



    def exit(self):
        quit(0)

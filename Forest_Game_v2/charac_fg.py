# from Death import Death_

class Character_(object):

    health = 10
    inven = []
    location = "location"
    fedora = "off"
    torch = "out"
    curse = False

    def __init__(self):
        pass
        # I think this stuff is specific to a particular instantiation of Character_()
        # self.inven = []
        # self.health = 10
        # self.fedora = "off"
        # self.death = Death_()

    def get_hp():

        print(f"""
        CURRENT HP:
        {Character_.health}
        """)

    def get_inven():
        while all(x in Character_.inven for x in ['sticks','flint','steel']) == True:
                print("You've collected the items to create a Torch!")
                Character_.inven.append('Torch!')
                Character_.inven.remove('sticks')
                Character_.inven.remove('steel')
                Character_.inven.remove('flint')
                Character_.get_inven()

        print("\nYour current inventory:")
        print("\n".join(Character_.inven))


    def decrease_hp():
        Character_.health -= 1
        print(f"Your health has decreased to: {Character_.health}")

    def curse_decrease():
        global curse
        if Character_.curse == True:
            decrease_hp()


    def increase_hp():
        if Character_.health <= 9:
            Character_.health += 1
            print(f"You've increased your hp to: {Character_.health}")
        elif Character_.health == 10:
            print("\nYou're at full health!")
            pass

    def health_to_death():
        if Character_.health == 0:
            self.die()
        elif Character_.health != 0:
            pass

    def die():
        if Character_.location == 'River':
            print("""The river's current sweeps you by your feet and carries you
            to your untimely death!
            """)
            quit(0)
        else:
            print("GAME OVER")
            quit(0)

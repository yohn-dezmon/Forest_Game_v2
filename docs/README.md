# Forest Game

This is a text-based adventure, in which you control a character as he moves through  
different areas within a forested landscape.

### Set-up of files:

The runner class is within the **bin folder** and is entitled **z_runner.py.** If you download
this repository, you can run the game from the command line using:
$ python3 z_runner.py  

The first two lines of z_runner.py are what allow me to import the files from the other folder, namely:
import sys
sys.path.insert(0, '/Users/HomeFolder/projects/Forest_Game_v2/Forest_Game_v2')

If you are using this set of modules/classes on your computer, please update the pathway names accordingly. Thank you!

### Functionalities that I was able to successfully execute:

(1) Move between rooms infinitely without having the program crash  
(2) Have a 'runner' class in a separate file that runs all of the scenes  
(3) Having a parent Scene class and individual scene subclasses that inherited traits from  
the parent class using the super function both to access the attributes (.__init__()) and the parent class functions.  
(4) Having a general prompt class that includes prompts for certain classes by using if statements.  
(5) Having the subclasses within separate files.  
(6) Having a character class that includes an inventory that can be accessed at any point  
in the game.  
(7) Giving the character a health variable that can be lowered or increased due to  
circumstances in the game.  

### Shortcomings:

(1) The program as is is not written up to PEP8 standards.  
(2) The game itself is not entirely finished, some of the scenes later on in the game lack detail.
(3) Certain parsing errors will currently cause the application to close.   

### Game play:

The player is prompted at each scene for what they would like to do. If the player types  
help, they can access a function that provides instructions.  
Many of the actions can be accomplished by typing a single word.  


The player is introduced in the first scene as an inexperienced lad with a large nose,  
who is entering a forest where he thinks he may find a potion to shrink his nose.  
Along the way he encounters various challenges that he must surpass.
By doing so he collects the correct items to successfully traverse the forested  
landscape, and obtains the potion in the final scene.  

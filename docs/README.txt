Readme for my first game (ex 45)

This is the first game that I have designed from scratch and it is currently far from 
finished, but I wanted to upload what I have before I start editing it in the rest of
ex 45 from the_hard_way just as a reference for what I was able to do myself thus far.

If you are just trying to use this code yourself to play around with, please see the section "Set-up of files".

Functionalities that I was able to successfully execute:

(1) Move between rooms infinitely without having the program crash
(2) Have a 'runner' class in a separate file that runs all of the scenes
(3) Having a parent Scene class and individual scene subclasses that inherited traits from
the parent class using the super function both to access the attributes (.__init__()) and the parent class functions. 
(4) Having a general prompt class that includes prompts for certain classes by using if statements.
(5) Having the subclasses being in separate files.
(6) Having a character class that includes an inventory that can be accessed at any point
in the game.
(7) Giving the character a health variable that can be lowered or increased due to 
circumstances in the game.
(8) Giving the character an inventory that can be added to and recognized by the classes.
(9) I was able to import files from one folder into the folder where my runner class was
and where the directory for my terminal was as well. 


Shortcomings:

(1) The program as is is NOT written up to PEP8 standards. This is something I will work on soon.
(2) The game itself is far from finished, most of the scenes have yet to be detailed
with the proper structure to move to and from them. As of now you can only move between
Edge, Thorn, and Pile of Dung scenes as desired. 
(3) I would like to include more functionality, such as having enemies and puzzles. 
(4) As we will see with my revisions, I'm sure that the way I chose to execute some of my
functionalities could have been done much better/simpler... but what's important is that
I figured out these methods on my own. 
(5) To move currently the player must be prompted twice, once to select the move function
then again to tell the program which direction he/she would like to go. I would like
to make this functionality accessible through a single user input. 


Game play:

The player is prompted at each scene for what they would like to do. If the player types
help, they can access a function that provides instructions.
Many of the actions can be accomplished by typing a single word.
If the player types move, the player will be prompted for the direction in which they would like to move. This allows the player to move to different scenes within the game. 

The player is introduced in the first scene as an inexperienced lad with a large nose,
who is entering a forest where he thinks he may find a potion to shrink his nose.
Along the way he encounters various challenges that he must surpass. By doing so he collects the correct items to successfully traverse the forested landscape, and obtains the potion in the final scene. 


Set-up of files:

I had the runner class 'z_runner.py' in the folder where I set the directory to for my terminal application, which on my computer is /Users/Homefolder/Python1/the_hard_way. 
I had all of the files (Scene parent class, scenes, and character) in a separate folder that was within the 'Python1' folder called 'Forest_Gameee'. 
The first two lines of z_runner.py are what allow me to import the files from the other folder, namely:
import sys
sys.path.insert(0, '/Users/Homefolder/Python1/Forest_Gameee') 

If you are using this set of modules/classes on your computer, please update the pathway names accordingly. Thank you! 


---- notes after I went public ----

I included the underscore on class names when I was worried a particular method of
that class was going to be the exact name (despite case) to avoid confusion. 


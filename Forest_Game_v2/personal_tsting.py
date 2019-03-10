from lexicon import Lexicon
from parser import *

input_ = "pick up sticks"

l = Lexicon(input_)
word_list = l.scan()
print(word_list)

parse_inp = Parser(word_list)
parsed_out = parse_inp.parse_sentence()


#
# lexicon = Lexicon(usr_input)
# word_list = lexicon.scan()
# # print(word_list)
# self.parse_var = Parser(word_list)
# self.action = self.parse_var.parse_sentence()
# # IDK if this syntax is correct
# # hmm why wasn't self.action.object there? was that on purpose??
# return self.action.subject, self.action.verb, self.action.object

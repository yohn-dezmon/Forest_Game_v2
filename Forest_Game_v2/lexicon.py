class Lexicon(object):

    def __init__(self, usr_input):
        self.input = usr_input
        self.directions = ['north', 'south', 'east', 'west', 'down', 'up',
        'left', 'right', 'back','backwards','forwards']
        self.verbs = ['go','touch','wear','put','don','quit','cut','light','turn','eat',
        'inspect', 'explore','pick','enter','check','examine','use',
        'look','quit','move','get', 'stop', 'kill', 'eat','help','crawl',
        'pricked','prick', 'leave']
        self.stop_words = ['the','green','out','into', 'in','off' 'of', 'from',
         'at','it','to','my']
        self.nouns = ['hp','scene','tunnel','shrub','door','hole','tree','bag',
        'around','thorns','rocks','rock','stick','sticks','bag','shrub',
        'inventory','instructions','help','steel','flint','thorns', 'player',
         'bear', 'princess', 'fedora', 'mirror', 'cabinet', 'key','forest','woods'
         ,'buttox','butt','bum','ass','bottom','fish']
        self.all_words = [self.directions + self.verbs + self.stop_words
        + self.nouns]
        self.tuple_sent = []

    def scan(self):
        # stuff = input('> ')
        # the test is looking for a tuple ( which .split produces) within a list...
        self.words = self.input.split()
        for w in self.words:
            if w.lower() in self.directions:
                word = ('direction', w.lower())
                self.tuple_sent.append(word)
            elif w.lower() in self.verbs:
                word = ('verb', w.lower())
                self.tuple_sent.append(word)
            elif w.lower() in self.stop_words:
                word = ('stop', w.lower())
                self.tuple_sent.append(word)
            elif w.lower() in self.nouns:
                word = ('noun', w.lower())
                self.tuple_sent.append(word)
            elif w.isdigit():
                number = ('number', int(w))
                self.tuple_sent.append(number)
            else:
                err = ('error', w)
                self.tuple_sent.append(err)
        # If you don't have RETURN here, the nosetests will return
        # AssertionError: None != [('direction', 'north')]
        return self.tuple_sent

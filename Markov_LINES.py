### SOURCE : http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/ 

import random

class Markov_LINES(object):

    ### Initialize all class variables.
    def __init__(self, open_file):
        self.cache = {}
        self.open_file = open_file
        self.lines = self.file_to_lines()
        self.line_size = len(self.lines)
        self.database()
    
    ### Break syntax file into lines.
    def file_to_lines(self):
        with open(self.open_file) as f:
            content = f.readlines() # read line-by-line into set
            content = [x.strip() for x in content] # remove whitespace at end of each line
        
        return content
    
    ### REVISE TO N-TUPLES LATER
    ### Generates tuples from the given data.
    def tuples(self):
        if len(self.lines) < 3:
            return
        
        ## Generate tuples.
        for i in range(len(self.lines) - 2):
            yield (self.lines[i], self.lines[i+1], self.lines[i+2])
    
    ### Generates database of possible tuple options.
    def database(self):
        for L1, L2, L3 in self.tuples():
            key = (L1, L2)
            ## Chosen element retrieved from cache.
            if key in self.cache:
                self.cache[key].append(L3)
            else:
                self.cache[key] = [L3]
    
    ### Generates a body of size n sentences.
    def generate_body_template(self, size=10):
        ## Randomize beginning.
        seed = random.randint(0, self.line_size-3)
        seed_line, next_line = self.lines[seed], self.lines[seed+1]
        L1, L2 = seed_line, next_line

        gen_lines = []
        ## Further generate lines from tuples.
        for i in range(size):
            gen_lines.append(L1)
            L1, L2 = L2, random.choice(self.cache[(L1, L2)])
            gen_lines.append(L2)
            return ' '.join(gen_lines)

import os
import random


### SYNTAX KEY_
###     N : NOUN
###     PN : PRONOUN
###     VB : VERB
###     DET : DETERMINER
###     ADJ : ADJECTIVE
###     ADV : ADVERB
###     PREP : PREPOSITION
###     CONJ : CONJUNCTION
###     INTJ : INTERJECTION

### NOTES_
###     "tag"s always have brackets around them, as such: [START-PHRASE], [CONJ] [N] [VB-PHRASE]
###     "line"s are just sentences

### RESOURCES_
###     Syntax abbreviations : https://en.wikipedia.org/wiki/List_of_glossing_abbreviations 
###     Phrase categories : https://en.wikipedia.org/wiki/Category:Syntactic_categories 

class SyntaxMaster(object):

    ### d : domain of operation
    def __init__(self, d):
        self.domain = d
        self.syntaxDIR = "syntax/"
        self.phrase_tag_list = self.retrieve_all_phrase_tags_from_directory(self.syntaxDIR)
        self.word_tag_list = self.retrieve_all_word_tags_from_directory(self.syntaxDIR)

    ### TESTING METHOD
    def TEST(self):
        ## Test dictionary / domain.
        d = {"[SUBJ]" : "ANDREW SUTARDJI"}

        print ("GENERATOR")
        line = self.generate_random_line()
        print (line)
        line = self.replace_tags_in_line_by_dictionary(line, d)
        print (line)


##### ##### ##### ##### #####
##### ##### ##### ##### ##### SYNTAX RETRIEVAL
##### ##### ##### ##### #####
    
    ### Returns all phrase tags from a given syntax dictionary.
    def retrieve_all_phrase_tags_from_directory(self, DIR):
        tags = []

        ## Iterate through the dictionary.
        for subdir, dirs, files in os.walk(DIR):
            for file in files:
                if "-PHRASE.txt" in file and file != ".DS_Store":
                    label = file.replace(".txt", "")
                    tag_ID = "[" + label + "]"
                    tags.append(tag_ID)
        
        return (tags)

    ### Returns all word tags from a given syntax directory.
    def retrieve_all_word_tags_from_directory(self, DIR):
        tags = []

        ## Iterate through the dictionary.
        for subdir, dirs, files in os.walk(DIR):
            for file in files:
                if "-PHRASE" not in file and ".txt" in file and file != ".DS_Store":
                    label = file.replace(".txt", "")
                    tag_ID = "[" + label + "]"
                    tags.append(tag_ID)
        
        return (tags)

    ### Returns list of phrase tags.
    def get_phrase_tag_list(self):
        return (self.phrase_tag_list)

    ### Returns list of word tags.
    def get_word_tag_list(self):
        return (self.word_tag_list)

##### ##### ##### ##### #####
##### ##### ##### ##### ##### CONTENT ASSEMBLY
##### ##### ##### ##### #####

    ### Replaces all domain/user-specific tags given a dictionary.
    def replace_tags_in_line_by_dictionary(self, line, dictionary):
        s = line

        cleared = 0 # sets to 1 if no tags exist
        while cleared == 0:
            cleared = 1 # assume innocent until proven guilty

            ## Iterate over all keys.
            for item in dictionary:
                if item in s:
                    cleared = 0

                    ## If key is present, replace.
                    s = s.replace(item, dictionary[item])
        
        return (s)

##### ##### ##### ##### #####
##### ##### ##### ##### ##### PROTOTYPES : FULL / RANDOM TESTING
##### ##### ##### ##### #####

    ### Returns a randomly constructed sentence.
    def generate_random_line(self):
        s = "[START-PHRASE]"

        line = self.assign_random_phrase_tags_to_line(s)
        line = self.assign_random_word_tags_to_line(line)

        return (line)

    ### Returns a shell sentence with part-of-speech tags randomly assigned to a given line.
    def assign_random_phrase_tags_to_line(self, line):
        l = line

        cleared = 0 # sets to 1 if no tags exist
        while cleared == 0:
            cleared = 1 # assume innocent until proven guilty

            ## Iterate over all tags.
            for item in self.phrase_tag_list:
                if item in l:
                    cleared = 0

                    print (l) # TESTING

                    ## If the tag is present, replace the first instance.
                    pick = self.pick_random_phrase_by_tag(item)
                    l = l.replace(item, pick, 1)
        
        return (l)
    
    ### Returns a gramatically correct sentence with words randomly assigned to a given line.
    def assign_random_word_tags_to_line(self, line):
        l = line

        cleared = 0 # sets to 1 if no tags exist
        while cleared == 0:
            cleared = 1 # assume innocent until proven guilty

            ## Iterate over all tags.
            for item in self.word_tag_list:
                if item in l:
                    cleared = 0

                    print (l) # TESTING

                    ## If the tag is present, replace the first instance.
                    pick = self.pick_random_word_by_tag(item)
                    l = l.replace(item, pick, 1)
        
        return (l)

    ### Returns a random phrase from a given phrase tag.
    def pick_random_phrase_by_tag(self, tag):
        t = tag[1:-1]
        fp = self.syntaxDIR + t + ".txt"

        ## Split file into lines.
        lines = open(fp).read().splitlines()

        ## Randomly choose a line from the file.
        line = random.choice(lines).rstrip()

        return (line)

    ### Returns a random word from a given part-of-speech tag.
    ### PROTOTYPE FOR pick_synonym_by_word(self, word)
    def pick_random_word_by_tag(self, tag):
        t = tag[1:-1]
        fp = self.syntaxDIR + t + ".txt"

        ## Split file into lines.
        lines = open(fp).read().splitlines()

        ## Randomly choose a line from the file.
        line = random.choice(lines).rstrip()

        ## Split line into words.
        words = line.split(',')

        ## Randomly choose a word from a line.
        word = random.choice(words)

        return (word)


##### ##### ##### ##### #####
##### ##### ##### ##### ##### FEATURES
##### ##### ##### ##### #####

    ### Returns a random synonym from a given word.
    def pick_synonym_by_word(self, word):
        w = word

        # Iterate through 

        return (w)
import SyntaxMaster

## Set domain. IN PROGRESS
SM = SyntaxMaster.SyntaxMaster("weather")

## Construct a random sentence.
s = SM.TEST()

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

### Class handles syntax construction.
class SyntaxMaster(object):

    def __init__(self, syntaxDIR):
        self.syntaxDIR = syntaxDIR # syntax directory

        ## 2 LIST CATEGORIES
        ##  "phrase type"
        ##  "part-of-speech"

        ## Create all lists.
        self.phrase_type_list = {}
        self.part_of_speech_list = {}

        ## Threshold values of -1 are counted as not set.
        self.phrase_type_threshold_list = {}
        self.part_of_speech_threshold_list = {}

        ## Occupy lists with given syntax data.
        self.load_all_phrase_types_from_directory(self.syntaxDIR)
        self.load_all_parts_of_speech_from_directory(self.syntaxDIR)

##### ##### ##### ##### #####
##### ##### ##### ##### ##### TESTING METHODS
##### ##### ##### ##### #####

    ### TESTING METHOD
    def TEST(self):
        self.display_current_counters() # before
        print (self.generate_random_syntax_given_start("START-PHRASE"))
        print ()
        self.display_current_counters() # after

    
    ### Prints report of current counters and thresholds for all lists to the screen.
    def display_current_counters(self):
        print ("!!! CURRENT DICTIONARY COUNTERS AND THRESHOLDS_")
        print ()
        print ("Phrase type counters: ")
        print (self.get_counter_list_by_category("phrase type"))
        print ()
        print ("Phrase type thresholds: ")
        print (self.get_threshold_list_by_category("phrase type"))
        print ()
        print ("Part-of-speech counters: ")
        print (self.get_counter_list_by_category("part-of-speech"))
        print ()
        print ("Part-of-speech thresholds: ")
        print (self.get_threshold_list_by_category("part-of-speech"))
        print ()
    
##### ##### ##### ##### #####
##### ##### ##### ##### ##### SYNTAX ASSEMBLY + FORMATTING
##### ##### ##### ##### #####

    ### Returns a modified line with tags substituted according to a given dictionary.
    ### PRIMARILY FOR EXTERNAL USE
    def replace_tags_given_DICT(self, LINE, DICT):
        l = LINE

        ## Iterate over all dictionary terms for one round.
        for term in DICT:
            ## Format phrase type into tag.
            tag = "[" + term + "]"

            ## If the tag exists within the line...
            if tag in l:
                print (l) # <<< TESTING >>>
                ## Replace first instance.
                l = l.replace(tag, DICT[term], 1)
        
        return (l)

    ### Replace first instance of tags given a dictionary.

    ### Returns a modified line where the first phrast type tag located is replaced with a suggested phrase.
    def assign_any_phrase_given_line(self, LINE):
        category = "phrase type"
        l = LINE

        ## Locate first instance of a phrase type tag.
        first_type = self.find_first_phrase_type(l)

        print (l) # TESTING : TRACK LINE DEVELOPMENT

        ## If the tag is empty.
        if first_type == "":
            return (l)
        
        ## Format phrase type into tag.
        first_tag = "[" + first_type + "]"

        ## Suggest new phrase to substitute for given phrase type.
        suggestion = self.suggest_phrase_given_type(first_type)

        ## Increment phrase type counter.
        self.increment_term_counter_by_category(first_type, category) ## PHRASE TYPE COUNTER
        print ("FIRST TYPE : " + first_type)

        ## Return line with substitution.
        return (l.replace(first_tag, suggestion, 1))

    ### Returns the first identified phrase type tag in a given line.
    def find_first_phrase_type(self, LINE):
        category = "phrase type"
        l = LINE

        ## Iterate over all phrase type terms.
        for term in self.get_counter_list_by_category(category):
            ## Format phrase type to tag.
            tag = "[" + term + "]"

            ## If the phrase type is present, return the type.
            if tag in l:
                return (term)
        
        ## If no phrase type tags are present, return an empty string.
        return ("")
    
    ### Returns a suggested phrase given a line and phrase type.
    def suggest_phrase_given_type(self, TYPE):
        category = "phrase type"

        ## Replicate dictionary of phrase types and set all counters to zero.
        temp_count = self.get_counter_list_by_category(category)
        temp_count = self.set_all_DICT_values(temp_count, 0)

        ## Randomly choose a phrase from type.
        pick = self.pick_random_phrase_by_type(TYPE)
        split_pick = pick.split()

        ## Iterate through all possible phrase types.
        for term in temp_count:
            ## Format phrase type to tag.
            tag = "[" + term + "]"

            ## Count the number of times a phrase type tag appears in the line.
            for item in split_pick:
                if tag == item:
                    ## Increment local counter is the term appears.
                    temp_count[term] = temp_count[term] + 1

            ## If selected output phrase content exceeds phrase type threshold,
            ##  try assigning new phrase.
            #if temp_count[term] + self.get_term_counter_by_category(term, category) >= self.get_term_threshold_by_category(term, category):
            #    print (str(temp_count[term] + self.get_term_counter_by_category(term, category)) + " >= " + str(self.get_term_threshold_by_category(term, category)))
            if self.has_term_counter_met_threshold_by_category(TYPE, category):
                return (self.suggest_phrase_given_type(TYPE))
            
        return (pick)

##### ##### ##### ##### #####
##### ##### ##### ##### ##### GENERAL DICTIONARY HANDLING
##### ##### ##### ##### #####

    ### Returns a dictionary where all terms are set to a given value.
    ### PURPOSED FOR COUNTERS AND THRESHOLD DICTIONARIES.
    def set_all_DICT_values(self, DICT, val):
        dictionary = DICT

        ## Iterate over all dictionary terms.
        for term in dictionary:
            dictionary[term] = val
        
        return (dictionary)

    ### Adds a given term to lists corresponding to a given category if it does not already exist.
    ### FOR INTERNAL USE.
    def add_term_to_list_by_category(self, TERM, category):
        does_exist = 0 # flag

        if category == "phrase type":
            does_exist = self.does_term_exist_in_DICT(TERM, self.phrase_type_list)
        elif category == "part-of-speech":
            does_exist = self.does_term_exist_in_DICT(TERM, self.part_of_speech_list)
        else:
            print ("INVALID : " + category + " category does not exist.")
            does_exist = -1

        if does_exist == 0:
            self.set_term_counter_by_category(TERM, 0, category)
            self.set_term_threshold_by_category(TERM, -1, category)
        else:
            print ("INVALID : " + TERM + " already exists in " + category + " lists.")
            does_exist = 1
    
    ### Returns 1 if a given term exists in a given dictionary, and 0 if not.
    def does_term_exist_in_DICT(self, TERM, DICT):
        ## Iterate over the dictionary.
        for item in DICT:
            if TERM == item: # term found
                return (1)
            
        return (0) # term does not exist

    ### Returns the counter value list from a given category.
    def get_counter_list_by_category(self, category):
        if category == "phrase type":
            return (self.phrase_type_list)
        elif category == "part-of-speech":
            return (self.part_of_speech_list)
        else:
            print ("INVALID : could not retrieve counter list for " + category + ". Empty string returned.")
            return ("")

    ### Returns the counter value for a given term from a given category.
    def get_term_counter_by_category(self, TERM, category):
        if category == "phrase type":
            return (int(self.phrase_type_list[TERM]))
        elif category == "part-of-speech":
            return (int(self.part_of_speech_list[TERM]))
        else:
            print ("INVALID : could not retrieve term counter for " + TERM + " from " + category + " list. Empty string returned.")
            return ("")

    ### Sets a given term counter to a given value given a category.
    def set_term_counter_by_category(self, TERM, val, category):
        if category == "phrase type":
            self.phrase_type_list[TERM] = val
        elif category == "part-of-speech":
            self.part_of_speech_list[TERM] = val
        else:
            print ("INVALID : could not set term counter for " + TERM + " in " + category + " list.")

    ### Increments a given term counter within a given category.
    def increment_term_counter_by_category(self, TERM, category):
        count = self.get_term_counter_by_category(TERM, category)
        ## If term exists within given category...
        if not count == "":
            count = count + 1 # increment
            self.set_term_counter_by_category(TERM, count, category)

    ### Returns the threshold value list from a given category.
    def get_threshold_list_by_category(self, category):
        if category == "phrase type":
            return (self.phrase_type_threshold_list)
        elif category == "part-of-speech":
            return (self.part_of_speech_threshold_list)
        else:
            print ("INVALID : could not retrieve threshold list for " + category + ". Empty string returned.")
            return ("")
        
    ### Returns the theshold value for a given term from a given category.
    def get_term_threshold_by_category(self, TERM, category):
        if category == "phrase type":
            return (self.phrase_type_threshold_list[TERM])
        elif category == "part-of-speech":
            return (self.part_of_speech_threshold_list[TERM])
        else:
            print ("INVALID : could not retrieve term threshold for " + TERM + " from " + category + " list. Empty string returned.")
            return ("")

    ### Sets a given term threshold to a given value within given a category.
    def set_term_threshold_by_category(self, TERM, val, category):
        if category == "phrase type":
            self.phrase_type_threshold_list[TERM] = val
        elif category == "part-of-speech":
            self.part_of_speech_threshold_list[TERM] = val
        else:
            print ("INVALID : could not set term threshold for " + TERM + " in " + category + " list.")
    
    ### Returns 1 if a term's counter value has reached its threshold, and 0 if not.
    def has_term_counter_met_threshold_by_category(self, TERM, category):
        if self.get_term_threshold_by_category(TERM, category) == -1:
            ## If the term has no threshold in a given category...
            return (0)
        elif self.get_term_counter_by_category(TERM, category) < self.get_term_threshold_by_category(TERM, category):
            ## If the counter is still below its threshold...
            return (0)
        
        return (0)

##### ##### ##### ##### #####
##### ##### ##### ##### ##### CATEGORICAL LOADING / HANDLING
##### ##### ##### ##### #####

    ### Extracts all phrase types into corresponding dictionaries given a directory.
    ### Occupies : phrase_type_list, phrase_type_threshold_list
    def load_all_phrase_types_from_directory(self, DIR):
        ## Iterate through the directory.
        for subdir, dirs, files in os.walk(DIR):
            for file in files:
                ## Include only phrase files ending in ".txt".
                if "-PHRASE.txt" in file and file != ".DS_Store":
                    ## Reformats name and turns it into a dictionary key.
                    term = file.replace(".txt", "")

                    ### Add phrase type to dictionaries.
                    #self.add_phrase_type_to_list(term)
                    self.add_term_to_list_by_category(term, "phrase type")
        
    ### Extracts all part-of-speech into corresponding dictionaries given a directory.
    ### Occupies : part_of_speech_list, part_of_speech_threshold_list
    def load_all_parts_of_speech_from_directory(self, DIR):
        ## Iterate through the directory.
        for subdir, dirs, files in os.walk(DIR):
            for file in files:
                ## Include only files ending in ".txt" with no phrase files.
                if "-PHRASE" not in file and ".txt" in file and file != ".DS_Store":
                    ## Reformats name and turns it into a dictionary key.
                    term = file.replace(".txt", "")

                    ### Add part of speech to dictionaries.
                    self.add_term_to_list_by_category(term, "part-of-speech")

##### ##### ##### ##### #####
##### ##### ##### ##### ##### RANDOM + PROTOTYPE METHODS
##### ##### ##### ##### #####

    ### NLG TESTING : Returns full randomly expanded syntax order given start phrase.
    def generate_random_syntax_given_start(self, S):
        category = "phrase type"
        syntax = "[" + S + "]"

        cleared = 0 # sets to 1 if no more available terms exist
        while cleared == 0:
            cleared = 1 # assume innocent until proven guilty

             ## Iterate over all terms.
            for term in self.get_counter_list_by_category(category):
                ## Format term type to tag.
                tag = "[" + term + "]"

                if tag in syntax:
                    cleared = 0

                    print (syntax) # <<< TESTING >>>

                    ## If phrase type tag is present, replace the first instance.
                    pick = self.pick_random_phrase_by_type(term)
                    syntax = syntax.replace(tag, pick, 1)

                    ## Increment based on term.
                    self.increment_term_counter_by_category(term, category)
            
        return (syntax)
        
    ### Returns a random phrase syntax given a phrase type.
    def pick_random_phrase_by_type(self, TYPE):
        fp = self.syntaxDIR + TYPE + ".txt"

        ## Split file into lines.
        lines = open(fp).read().splitlines()

        ## Choose random line from file.
        return (random.choice(lines).rstrip())
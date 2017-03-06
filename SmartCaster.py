import os
import Markov_LINES
import nltk
from nltk.tag import pos_tag, map_tag
import shutil

### Globals
#token = [] # tokenized words
#pos = [] # part-of-speech tags

### Existing
F_INPUT = "FILES_IN" # directory of example texts as inputs

### Created
F_SYNTAX = "syntax.txt" # acceptable grammatical syntax list

##### ##### ##### ##### ##### ######################## ##### ##### ##### ##### #####
##### ##### ##### ##### ##### MAIN / RUNNING FUNCTIONS ##### ##### ##### ##### #####
##### ##### ##### ##### ##### ######################## ##### ##### ##### ##### #####

def RUN():
    CLEAR() # switch
    SETUP()
    FILES_IN(F_INPUT) # compile syntax from example texts

    ### TESTING
    GENERATE_BODY_TEMPLATE(F_SYNTAX)

### Resets program files.
def CLEAR():
    os.remove(F_SYNTAX)

### Initializes all necessary variables.
def SETUP():
    ## Open syntax file; create if non-existent.
    try:
        file_content = open(F_SYNTAX, 'r')
    except FileNotFoundError:
        file_content = open(F_SYNTAX, 'w')

##### ##### ##### ##### ##### ############### ##### ##### ##### ##### #####
##### ##### ##### ##### ##### TEXT GENERATION ##### ##### ##### ##### #####
##### ##### ##### ##### ##### ############### ##### ##### ##### ##### #####

### Generates the syntax template for the content body.
def GENERATE_BODY_TEMPLATE(_FILE):
    M = Markov_LINES.Markov_LINES(_FILE)
    S = M.generate_body_template()

    REMOVE_LINES_BEGINNING_WITH(_FILE, ".")

    ## Check functionality.
    print(S)

##### ##### ##### ##### ##### ################ ##### ##### ##### ##### #####
##### ##### ##### ##### ##### INPUT PROCESSING ##### ##### ##### ##### #####
##### ##### ##### ##### ##### ################ ##### ##### ##### ##### #####

### Takes a txt file as input and extracts its syntax.
def FILE_IN(_FILE):
    file_content = open(_FILE).read() # open file

    ## Tokensize content and assign POS tags.
    tokens = nltk.word_tokenize(file_content)
    pos = nltk.pos_tag(tokens)
    ## Universal tags (simple).
    pos_SIMPLE = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in pos]

    ## Check functionality. 
    #print (tokens)
    #print (pos)

    #PARSE_SYNTAX(pos)
    PARSE_SYNTAX(pos_SIMPLE)
    #CLEAN_SYNTAX()

### Takes a directory of texts files as input and extracts their syntax.
def FILES_IN(_DIR):
    ## Find all txt files within directory.
    for file in os.listdir(_DIR):
        if file.endswith(".txt"): 
            FILE_IN(os.path.join(_DIR, file))
    
    #CLEAN_SYNTAX(F_SYNTAX)

### Takes a list of POS-tagged words as input and adds to an accepted syntax list.
def PARSE_SYNTAX(POS):
    SYNTAX = "" # new syntax to add

    ## Turn POS tags into string.
    for i in POS:
        SYNTAX += i[1] + " "
        ## Begin new line after period.
        if i[1] == ".":
            SYNTAX += "\n"
    
    ## Insert syntax into file.
    with open(F_SYNTAX, "a") as f:
        f.write("\n")
        f.write(SYNTAX)
    
    ## Check functionality.
    #print(SYNTAX)

### Removes duplicated and unwanted lines from the syntax file.
### OPTION AT THE BOTTOM OF FILES_IN()
def CLEAN_SYNTAX(_FILE):
    ## Store and write back only unique lines.
    UL = set(open(_FILE).readlines())
    open(_FILE, "w").writelines(set(UL))
    
    ## Remove empty lines.
    REMOVE_LINES_BEGINNING_WITH(_FILE, "\n")
    REMOVE_LINES_BEGINNING_WITH(_FILE, " ")
    REMOVE_LINES_BEGINNING_WITH(_FILE, ".")

### Removes lines in file beginning with a specified string.
### Useful for when a line begins with "\n" or ".".
def REMOVE_LINES_BEGINNING_WITH(_FILE, _PRE):
    ## Duplicate file to temporary file.
    TEMP = "temp.txt"
    shutil.copy2(_FILE, TEMP)

    input = open(TEMP, "r")
    output = open(_FILE, "w")

    ## Exclude copying lines with prefix.
    for i, line in enumerate(input):
        if i == 0 or not line.lstrip().startswith(_PRE):
            output.write(line)

    ## Delete temporary file.
    os.remove(TEMP)
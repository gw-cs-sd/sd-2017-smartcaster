import FileHandler
import os
import Markov_LINES
import Markov_WORDS
import OpenWeather

### Globals
owm = '' # OnlineWeatherMap object
report = "" # temporary 

### Existing
F_INPUT = "FILES_IN" # directory of example texts as inputs

### Created
F_SYNTAX = "syntax.txt" # acceptable grammatical syntax list
F_EX = "ex.txt" # compiled example texts

##### ##### ##### ##### ##### ######################## ##### ##### ##### ##### #####
##### ##### ##### ##### ##### MAIN / RUNNING FUNCTIONS ##### ##### ##### ##### #####
##### ##### ##### ##### ##### ######################## ##### ##### ##### ##### #####

### Runs program.
### IF _SWITCH = 0, clear data before new run.
### ELSE, build atop current data.
### _KEY & _LOC : OWM API credentials.
###     _KEY : OpenWeatherMap API key
###     _LOC : specified location
def RUN(_SWITCH, _KEY, _LOC):
    if _SWITCH == 0:
        CLEAR() # clears current data

    SETUP(_KEY, _LOC)
    FileHandler.FILES_IN(F_INPUT, F_EX, F_SYNTAX) # compile syntax from example texts

    ## Check functionality.
    owm.RUN_FULL_TEST()

    ### MARKOV TESTING
    #GENERATE_BODY_TEMPLATE(F_SYNTAX)
    #GENERATE_MARKOV_TEXT(F_EX)

### Resets program files.
def CLEAR():
    if os.path.isfile(F_SYNTAX):
        os.remove(F_SYNTAX)
    if os.path.isfile(F_EX):
        os.remove(F_EX)

### Initializes all necessary files and variables.
def SETUP(_KEY, _LOC):
    global owm

    ## Login to OWM API with key and location.
    owm = OpenWeather.OpenWeather(_KEY, _LOC)

    ## Open syntax file; create if non-existent.
    try:
        file_content = open(F_SYNTAX, 'r')
    except FileNotFoundError:
        file_content = open(F_SYNTAX, 'w')

    ## Open example text; create in non-existent.
    try:
        file_content = open(F_SYNTAX, 'r')
    except FileNotFoundError:
        file_content = open(F_SYNTAX, 'w')

##### ##### ##### ##### ##### ############### ##### ##### ##### ##### #####
##### ##### ##### ##### ##### MARKOV CHAINING ##### ##### ##### ##### #####
##### ##### ##### ##### ##### ############### ##### ##### ##### ##### #####

### Generates the syntax template for the content body.
### BODY SIZE OPTION WITHIN OG METHOD
def GENERATE_BODY_TEMPLATE(_FILE):
    M = Markov_LINES.Markov_LINES(_FILE)
    S = M.generate_body_template()

    FileHandler.REMOVE_LINES_BEGINNING_WITH(_FILE, ".")

    ## Check functionality.
    print(S)

### Generates a Markov text using the full example text.
### TEXT SIZE OPTION WITHIN OG METHOD
def GENERATE_MARKOV_TEXT(_FILE):
    with open (_FILE, 'r') as f:
        M = Markov_WORDS.Markov_WORDS(f)
        S = M.generate_markov_text()

    ## Check functionality.
    print(S)


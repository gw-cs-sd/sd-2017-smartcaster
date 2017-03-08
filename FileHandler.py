import os
import nltk
from nltk.tag import pos_tag, map_tag
import shutil

### INPUTS_
### _DIR : directory of txt files
### _FILE : txt file

### OUTPUTS_
### _EX : file of compiled example texts
### _SYN : file of acceptable syntax templates

##### ##### ##### ##### ##### ################ ##### ##### ##### ##### #####
##### ##### ##### ##### ##### INPUT PROCESSING ##### ##### ##### ##### #####
##### ##### ##### ##### ##### ################ ##### ##### ##### ##### #####

### Takes a txt file and appends it to an example text.
### Input : text file.
### Output : example text, syntax list.
def FILE_IN(_FILE, _EX, _SYN):
    file_content = open(_FILE).read() # open file

    ## Append example text with new file.
    with open(_EX, 'a') as outfile:
        with open(_FILE) as infile:
            outfile.write(infile.read())

    ## Tokensize content and assign POS tags.
    tokens = nltk.word_tokenize(file_content)
    pos = nltk.pos_tag(tokens)
    ## Universal tags (simple).
    pos_SIMPLE = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in pos]

    ## Check functionality. 
    #print (tokens)
    #print (pos)

    PARSE_SYNTAX(pos_SIMPLE, _SYN)
    #CLEAN_SYNTAX(_SYN)

### Takes a directory of texts files as input and extracts their syntax.
### Input : directory.
### Output : example text, syntax list.
def FILES_IN(_DIR, _EX, _SYN):
    ## Find all txt files within directory.
    for file in os.listdir(_DIR):
        if file.endswith(".txt"): 
            FILE_IN(os.path.join(_DIR, file), _EX, _SYN)
    
    #CLEAN_SYNTAX(_SYN)

### Takes a list of POS-tagged words as input and adds to an accepted syntax list.
def PARSE_SYNTAX(POS, _SYN):
    SYNTAX = "" # new syntax to add

    ## Turn POS tags into string.
    for i in POS:
        SYNTAX += i[1] + " "
        ## Begin new line after period.
        if i[1] == ".":
            SYNTAX += "\n"
    
    ## Insert syntax into file.
    with open(_SYN, "a") as f:
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
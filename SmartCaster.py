import NFL
from fHandler import fHandler
from random import randint

### Core text.
txt = ''

### Data files.
f_game = 'exT-game.json'
f_profile = 'exP-profile.json'
f_roster = 'exT-roster.json'
f_schedule = 'exT-schedule.json'
f_stats = 'exP-stats.json'

### JSON strings.
exP = ''

## MAIN / RUNNING FUNCTION
def SC_RUN(_LAST, _FIRST, _POS, _TEAM, _YEAR, _WEEK):
    _TYPE = SC_findType(_POS)
    SC_IN(_LAST, _FIRST, _POS, _TYPE, _TEAM, _YEAR, _WEEK) # aggregate data
    SC_construct(_LAST, _FIRST, _POS, _TYPE, _TEAM, _YEAR, _WEEK) # construct content
    SC_PUBLISH() # publish content

##### ##### ##### DATA PROCESSING ##### ##### #####

## Aggregate data through all inputs.
def SC_IN(_LAST, _FIRST, _POS, _TYPE, _TEAM, _YEAR, _WEEK):
    global exP
    
    ## Write all files.
    exP = fHandler(f_stats, _LAST, _FIRST) ## FUNCTIONAL
    NFL.retrieve_game(f_game, _TEAM, _YEAR, _WEEK) ## FUNCTIONAL
    NFL.retrieve_profile(f_profile, exP.last, exP.first) ## FUNCTIONAL
    #NFL.retrieve_team_roster(f_roster, _TEAM) ## FUNCTIONAL
    #NFL.retrieve_team_schedule(f_schedule, _TEAM) ## FUNCTIONAL
    NFL.retrieve_stats(exP.fn, _TYPE, exP.last, exP.first, _YEAR, _WEEK) ## FUNCTIONAL

## Determines relevant stats based on position.
def SC_findType(_POS):
    if(_POS == 'QB'):
        return 'passing'
    if(_POS == 'RB'):
        return 'rushing'
    if(_POS == 'WR'):
        return 'receiving'

## Prints out final text.
## --> WILL PUBLISH TO DOCUMENT.
def SC_PUBLISH():
    print (txt)

##### ##### ##### CONTENT CONSTRUCTION ##### ##### #####

def SC_construct(_LAST, _FIRST, _POS, _TYPE, _TEAM, _YEAR, _WEEK):
    global txt # access global text

    ## Headline
    txt += SC_headline(_LAST, _FIRST, _POS, _TYPE, _TEAM, _YEAR, _WEEK)
    txt += '\n\n'

    ## Summary
    txt += SC_summary(_LAST, _FIRST, _POS, _TYPE, _TEAM, _YEAR, _WEEK)

## Constructs article headline.
def SC_headline(_LAST, _FIRST, _POS, _TYPE, _TEAM, _YEAR, _WEEK):
    txt_head = '__ [NAME]\'s Week [WEEK] Performance __'

    ## Puts together subject name.
    _NAME = _FIRST + ' ' + _LAST

    ## Substitute header info.
    txt_head = txt_head.replace('[NAME]', _NAME)
    txt_head = txt_head.replace('[WEEK]', _WEEK)

    return txt_head

## Determines what type of summary to construct.
def SC_summary(_LAST, _FIRST, _POS, _TYPE, _TEAM, _YEAR, _WEEK):
    if(_POS == 'QB'):
        return SC_QB_summary(_LAST, _FIRST, _POS, _TYPE, _TEAM, _YEAR, _WEEK)

##### ##### ##### SPECIFIED CONTENT CONSTRUCTION ##### ##### #####
##### ##### CURRENTLY ONLY WORKING ON QBS ##### ##### #####

## Constructs brief summary.
def SC_QB_summary(_LAST, _FIRST, _POS, _TYPE, _TEAM, _YEAR, _WEEK):
    ### PRIMARY CONTENT ###
    txt_main = '[NAME] threw for [ADJ_1][YARDS] yards and [TD] touchdowns'

    ## Substitute primary info.
    txt_main = txt_main.replace('[NAME]', (_FIRST + ' ' + _LAST))
    txt_main = txt_main.replace('[YARDS]', str(exP.get('passingYds')))
    txt_main = txt_main.replace('[TD]', str(exP.get('passingTds')))

    ## Correct grammar based on stats.
    if(exP.get('passingYds') == 1):
        txt_main = txt_main.replace('yards', 'yard')
    if(exP.get('passingTds') == 1):
        txt_main = txt_main.replace('touchdowns', 'touchdown')
    
    ## Statistically + probabalistically assign adjectives.
    if(exP.get('passingYds') > 300):
        if(randint(0,9) > 6): ## <--- WORK ON BETTER WAY TO ASSIGN ADJ
            txt_main = txt_main.replace('[ADJ_1]', 'an astounding ')
        else:
            txt_main = txt_main.replace('[ADJ_1]', '')
    txt_main = txt_main.replace('[ADJ_1]', '') # remove tag if still present

    ### PRIMARY CONTENT CLAUSES ###
    if(exP.get('passingInt') > 0):
        txt_main += ' and ' + str(exP.get('passingInt')) + ' interception'
        if(exP.get('passingInt') > 1):
            txt_main += 's'

    txt_main += '.'
    return txt_main
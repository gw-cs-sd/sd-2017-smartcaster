import csv
import nflgame
import shutil

## ### #### ##### NFL Game Center Contact ##### #### ### ##

## Stores week's plays up until now (.csv).
def retrieve_week(_YEAR, _WEEK, _FILE): ## RAW DATA
    #print "Populating %s" %_FILE
    games = nflgame.games(_YEAR, week=_WEEK)
    nflgame.combine(nflgame.combine_plays(games)).csv(_FILE)

## For demo. Source file is a .csv available for editing.
def retrieve_week_demo(_YEAR, _WEEK, _FILE):
    _DEMO = 'weekPlays_origin_demo.csv'
    open(_FILE, 'w').close() # clears the main file
    shutil.copy2(_DEMO, _FILE) # copies contents of new file into old

## Parses through raw data and prints relevant stats. 
def retrieve_stats(_FILE):
    #print "%s threw for %d yards." %(data["name"], data["passing_yds"])

    ## Convert .csv to 2D array.
    with open(_FILE, 'rb') as f:
        reader = csv.reader(f)
        val = map(tuple, reader) # val[content][header]

    ## Print only occupied stats. 
    for i in range(len(val)): ## iterate down rows
        #print val[i][0] # print list of names
        for j in range(len(val[0])): ## iterate across columns
            if (val[0][j] == val[i][j]): break
            if (val[i][j]):
                print "%s : %s \t" %(val[0][j], val[i][j]),
        print ""
    ## FIND WAY TO TAKE OUT NEW LINE


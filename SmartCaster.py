#import nflgame
import NFLGCC
import os
#import nltk
import shutil

## Roster (variable)
P01 = 'J.Winston' #TB #QB
P02 = 'D.Freeman' #ATL #RB
P03 = 'J.Ajayi' #MIA #RB
P04 = 'F.Gore' #IND #RB
P05 = 'D.Johnson' #CLE #RB
P06 = 'J.Rodgers' #TB #RB
P07 = 'T.Austin' #LA #RB
P08 = 'D.Adams' #GB #WR
P09 = 'R.Matthews' #TEN #WR
P10 = 'A.Cooper' #OAK #WR
P11 = 'J.Crowder' #WAS #WR
P12 = 'B.LaFell' #CIN #WR
P13 = 'J.Graham' #SEA #TE
P14 = 'C.Sturgis' #PHI #K
P15 = 'PHI' #DEF

## Starting Lineup (variable)
QB = P01
RB1 = P02
RB2 = P03
WR1 = P07
WR2 = P08
TE = P13
FLX = P09
K = P14
DEF = P15

## Files.
_FILE = 'weekPlays.csv'
_NEW = 'weekPlays_new.csv'
_TEMP = 'weekPlays_temp.csv'

## Settings (variable)
team = [QB, RB1, RB2, WR1, WR2, TE, FLX, K, DEF]

## Setup csv.
NFLGCC.retrieve_plays(2016, 9, _FILE)

## ### #### ##### RUNNING ##### #### ### ##
while True:
    ## Create new temp file with header.
    os.system('head -n 1 weekPlays.csv > weekPlays_temp.csv')

    NFLGCC.retrieve_plays(2016, 9, _NEW)

    os.system('grep -vf weekPlays_new.csv weekPlays.csv >> weekPlays_temp.csv') # appends temp file with difference
    os.system('grep -vf weekPlays_new.csv weekPlays.csv') # print to console
    
    # do things
    #for p in players: 

    ## Update original weekPlays.csv once data is used.
    #print "Closing %s" %_NEW
    open(_FILE, 'w').close() # clears the main file
    #print "Closed."
    shutil.copy2(_NEW, _FILE) # copies contents of new file into old

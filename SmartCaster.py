import nflgame
import os
#import nltk

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

## Settings (variable)
team = [QB, RB1, RB2, WR1, WR2, TE, FLX, K, DEF]
games = nflgame.games(2016, week=9)
players = nflgame.combine_game_stats(games)

## Setup csv.
nflgame.combine(nflgame.combine_plays(games)).csv('weekPlays.csv') ## store week's plays up until now

## QB
#for p in players: 
#    if p.name == QB:
#        msg = '%s : %d passing yards, %d completed out of %d attempts, %d passing TDs'
#        print msg % (p, p.passing_yds, p.passing_cmp, p.passing_att, p.passing_tds)

## ### #### ##### RUNNING ##### #### ### ##
while True:
    games = nflgame.games(2016, week=9)
    players = nflgame.combine_game_stats(games)

    ## Create new temp file.
    os.system('head -n 1 weekPlays.csv > weekPlays_temp.csv')

    nflgame.combine(nflgame.combine_plays(games)).csv('weekPlays_new.csv')
    os.system('grep -vf weekPlays_new.csv weekPlays.csv >> weekPlays_temp.csv') # appends temp file with difference
    #os.system('grep -vf weekPlays_new.csv weekPlays.csv') # print to console
    # do things
    #for p in players: 

    ## Update original weekPlays.csv once data is used.
    #write new to original

## PROBLEM WITH UPDATING NEW file
## PLAN: CALL METHOD AGAIN TO REFRESH
import nflgame
import os

games = nflgame.games(2016, week=9)
players = nflgame.combine_game_stats(games)
for p in players.rushing().sort('rushing_yds').limit(5):
    msg = '%s %d carries for %d yards and %d TDs'
    print msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds)

## Compile all stats from 2016 season into a csv file.
#nflgame.combine(nflgame.games(2016)).csv('season2016.csv')

## Compile all playes from the 2016 season into a csv file.
#nflgame.combine(nflgame.combine_plays(games)).csv('season2016plays.csv')

## Subtact 2 from 1.
nflgame.combine(nflgame.combine_plays(games)).csv('season2016plays-2.csv')
os.system('grep -vf season2016plays-2.csv season2016plays.csv')
os.system('grep -vf season2016plays-2.csv season2016plays.csv > season2016-diff.csv')
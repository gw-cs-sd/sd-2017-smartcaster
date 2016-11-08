import nflgame

## ### #### ##### NFL Game Center Contact ##### #### ### ##

## Stores week's plays up until now (.csv).
def retrieve_plays(_YEAR, _WEEK, _FILE):
    #print "Populating %s" %_FILE
    games = nflgame.games(_YEAR, week=_WEEK)
    nflgame.combine(nflgame.combine_plays(games)).csv(_FILE)

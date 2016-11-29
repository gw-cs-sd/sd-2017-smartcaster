import requests

## SuredBits API https://www.suredbits.com/api/

##### ##### ##### RETRIEVE DATA THROUGH SuredBits NFL API ##### ##### #####
## _FN : user-assigned filename
## _URL : url to JSON data
## 
## Methods construct a URL with given inputs.

## Retrieves JSON data from given URL.
def retrieve_data_from_URL(_FN, _URL):
    _URL.lower() # converts all characters to lower case if not already done
    
    ## Make a get request.
    response = requests.get(_URL)

    ## Store into JSON file.
    f = open(_FN, 'wb') # write into file as bytes (wb)
    f.write(response.content) # write content
    f.close()

## https://www.suredbits.com/api/nfl/games/
def retrieve_game(_FN, _TEAM, _YEAR, _WEEK):
    _URL = 'http://api.suredbits.com/nfl/v0/games'

    ## Includes team ID IF NOT EMPTY.
    if(_TEAM != ''):
        _URL += '/'
        _URL += _TEAM
    
    ## Includes year IF NOT EMPTY.
    if(_YEAR != ''):
        _URL += '/'
        _URL += _YEAR

        ## Includes week IF NOT EMPTY.
        if(_WEEK != ''):
            _URL += '/'
            _URL += _WEEK

    retrieve_data_from_URL(_FN, _URL)

## https://www.suredbits.com/api/nfl/players/
def retrieve_profile(_FN, _LAST, _FIRST):
    _URL = 'http://api.suredbits.com/nfl/v0/players/'

    ## Searches players by last name.
    _URL += _LAST

    ## Also searches by first name IF NOT EMPTY.
    if(_FIRST != ''):
        _URL += '/'
        _URL += _FIRST
    
    retrieve_data_from_URL(_FN, _URL)

## https://www.suredbits.com/api/nfl/team/
def retrieve_team_roster(_FN, _TEAM):
    _URL = 'http://api.suredbits.com/nfl/v0/team/'

    _URL += _TEAM
    _URL += '/roster'

    retrieve_data_from_URL(_FN, _URL)

## https://www.suredbits.com/api/nfl/team/
def retrieve_team_schedule(_FN, _TEAM):
    _URL = 'http://api.suredbits.com/nfl/v0/team/'

    _URL += _TEAM
    _URL += '/schedule'

    retrieve_data_from_URL(_FN, _URL)

## https://www.suredbits.com/api/nfl/stats/
def retrieve_stats(_FN, _TYPE, _LAST, _FIRST, _YEAR, _WEEK):
    _URL = 'http://api.suredbits.com/nfl/v0/stats/' # type/lastName/firstName/year/week

    ## If specified type IS NOT EMPTY.
    if(_TYPE != ''): 
        _URL += _TYPE
        _URL += '/'
    
    ## Add on name.
    _URL += _LAST
    _URL += '/'
    _URL += _FIRST
    _URL += '/'

    ## Add on year.
    _URL += _YEAR

    ## Add on week IF NOT EMPTY.
    if(_WEEK != ''):
        _URL += '/'
        _URL += _WEEK

    retrieve_data_from_URL(_FN, _URL)
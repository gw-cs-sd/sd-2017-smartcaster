import os
import pyowm

### SOURCES_
### OpenWeatherMap API : http://openweathermap.org/price#weather 
### PyOWM Wrapper : https://github.com/csparpa/pyowm 
### PyOWM Examples : https://github.com/csparpa/pyowm/blob/master/pyowm/docs/usage-examples.md

### Wrapper for the PyOWM API.
class OpenWeather(object):

    ### Initializes all class variables.
    ### _KEY : OpenWeatherMap API key 
    ### _LOC : specified location
    def __init__(self, _KEY, _LOC):
        self.key = _KEY
        self.loc = _LOC
        self.owm = pyowm.OWM(self.key)

        ## Retrieve weather observation at location.
        self.observation = self.owm.weather_at_place(self.loc)
        self.weather = self.observation.get_weather()
        self.location = self.observation.get_location()
        ## Retrieve weather forecast at location.
        #self.daily_forecast = self.owm.daily_forecast(self.loc)
        #self.three_hours_forecast = self.owm.three_hours_forecast(self.loc)
    
    ### Refreshes data.
    def refresh(self):
        self.observation = self.owm.weather_at_place(self.loc)
        self.weather = self.observation.get_weather()

        #self.daily_forecast = self.owm.daily_forecast(self.loc)
        #self.three_hours_forecast = self.owm.three_hours_forecast(self.loc)
    
    ### Produces a full printout report of all functions.
    def RUN_FULL_TEST(self):
        print ("CHECKING CLASS FOR COMPETENCE")
        self.test_weather()
        self.test_location()
        #self.test_daily_forecast()
        #self.test_three_hours_forecast()
        print ()

    ##### ##### ##### ##### ##### ################### ##### ##### ##### ##### #####
    ##### ##### ##### ##### ##### OBSERVATION METHODS ##### ##### ##### ##### #####
    ##### ##### ##### ##### ##### ################### ##### ##### ##### ##### #####

    ## Retrieval methods : https://github.com/csparpa/pyowm/blob/master/pyowm/docs/usage-examples.md

    ### Retrieves specified weather data from specified location.
    ### X : the type of weather data.
    def get_weather(self, x):
        if x == "time":
            return (self.weather.get_reference_time(timeformat='iso'))
        elif x == "clouds":
            return (self.weather.get_clouds())
        elif x == "rain":
            return (self.weather.get_rain())
        elif x == "snow":
            return (self.weather.get_snow())
        elif x == "wind (full)":
            return (self.weather.get_wind())
        elif x == "wind speed":
            return (self.weather.get_wind()['speed'])
        elif x == "wind direction":
            return (self.weather.get_wind()['deg'])
        elif x == "humidity":
            return (self.weather.get_humidity())
        elif x == "pressure (full)":
            return (self.weather.get_pressure())
        elif x == "sea level":
            return (self.weather.get_pressure()['sea_level'])
        elif x == "pressure":
            return (self.weather.get_pressure()['press'])
        elif x == "temperature (full)":
            return (self.weather.get_temperature('fahrenheit'))
        elif x == "temperature":
            return (self.weather.get_temperature('fahrenheit')['temp'])
        elif x == "temperature (min)":
            return (self.weather.get_temperature('fahrenheit')['temp_min'])
        elif x == "temperature (max)":
            return (self.weather.get_temperature('fahrenheit')['temp_max'])


        elif x == "status":
            return (self.weather.get_status())
        elif x == "detailed status":
            return (self.weather.get_detailed_status())
        elif x == "code":
            return (self.weather.get_weather_code())
        elif x == "sunrise":
            return (self.weather.get_sunrise_time('iso'))
        else:
            return (self.weather)
    
    ### Retrieves specified location data.
    ### X : the type of location data.
    def get_location(self, x):
        if x == "ID":
            return (self.location.get_ID())
        elif x == "lon":
            return (self.location.get_lon())
        elif x == "lat":
            return (self.location.get_lat())
        else:
            return (self.location.get_name())

    ### Test cases for get_weather(x).
    def test_weather(self):
        print ()
        print ("-W-E-A-T-H-E-R- -D-A-T-A-")

        print ("time : ", end='')
        print (self.get_weather("time"))
        print ("clouds : ", end='')
        print (self.get_weather("clouds"))
        print ("rain : ", end='')
        print (self.get_weather("rain"))
        print ("snow : ", end='')
        print (self.get_weather("snow"))
        print ("wind : ", end='')

        ## WIND
        print (self.get_weather("wind (full)"))
        print ("wind speed : ", end='')
        print (self.get_weather("wind speed"))
        print ("wind direction : ", end='')
        print (self.get_weather("wind direction"))

        print ("humidity : ", end='')
        print (self.get_weather("humidity"))

        ## PRESSURE
        print ("pressure (full): ", end='')
        print (self.get_weather("pressure (full)"))
        print ("sea level : ", end='')
        print (self.get_weather("sea level"))
        print ("pressure : ", end='')
        print (self.get_weather("pressure"))

        ## TEMPERATURE
        print ("temperature (full) : ", end='')
        print (self.get_weather("temperature (full)"))
        print ("temperature : ", end='')
        print (self.get_weather("temperature"))
        print ("temperature (min) : ", end='')
        print (self.get_weather("temperature (min)"))
        print ("temperature (max) : ", end='')
        print (self.get_weather("temperature (max)"))

        print ("status : ", end='')
        print (self.get_weather("status"))
        print ("detailed status : ", end='')
        print (self.get_weather("detailed status"))
        print ("code : ", end='')
        print (self.get_weather("code"))
        print ("sunrise : ", end='')
        print (self.get_weather("sunrise"))
        print ("observation : ", end='')
        print (self.get_weather(""))

        print ()
    
    ### Test cases for get_location(x).
    def test_location(self):
        print ()
        print ("-L-O-C-A-T-I-O-N- -D-A-T-A-")

        print ("ID : ", end='')
        print (self.get_location("ID"))
        print ("longitude : ", end='')
        print (self.get_location("lon"))
        print ("latitude : ", end='')
        print (self.get_location("lat"))
        print ("name : ", end='')
        print (self.get_location("name"))

        print ()

    ##### ##### ##### ##### ##### ################ ##### ##### ##### ##### #####
    ##### ##### ##### ##### ##### FORECAST METHODS ##### ##### ##### ##### #####
    ##### ##### ##### ##### ##### ################ ##### ##### ##### ##### #####

    ### Retrieves weather forecast from specified location.
    def get_forecast(self):
        tomorrow = pyowm.timeutils.tomorrow()
        s = self.forecast.will_be_sunny_at(tomorrow)

        print ("will be sunny : ")
        print (s)
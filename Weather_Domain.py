from DomainMaster import DomainMaster
import pyowm
import json

### SOURCES_
### OpenWeatherMap API : http://openweathermap.org/price#weather 
### PyOWM Wrapper : https://github.com/csparpa/pyowm 
### PyOWM Examples : https://github.com/csparpa/pyowm/blob/master/pyowm/docs/usage-examples.md

class Weather_Domain(DomainMaster):

    def __init__(self, domainDIR, d, PN):
        DomainMaster.__init__(self, domainDIR)
        self.set_pronoun_and_domain(PN, d)

        ## Enter API key.
        self.owm = pyowm.OWM('b29d29ef62921e78d4eae126872beec0')

        ## Retrieve weather observation data at location.
        self.refresh_data()
    
##### ##### ##### ##### #####
##### ##### ##### ##### ##### OBSERVATION RETRIEVAL
##### ##### ##### ##### #####

    ### Updates most recently available data.
    def refresh_data(self):
        self.observation = self.owm.weather_at_place(self.get_pronoun())
        self.weather = self.observation.get_weather()

        ## Update value dictionary.
        self.set_value_dict(self.get_domain())

    ### Retrieves specified weather data given a type term.
    def get_data_value(self, term):
        ## Check against available terms.
        if term == "temperature":
            val = self.weather.get_temperature('fahrenheit')['temp']
        elif term == "humidity":
            val = self.weather.get_humidity()
        elif term == "wind speed":
            val = self.weather.get_wind()['speed']
        else:
            return ("")
        
        return (val)
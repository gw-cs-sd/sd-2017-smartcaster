import OpenWeather
import SmartCaster

## OpenWeatherMap API variables.
owm_API_key = 'b29d29ef62921e78d4eae126872beec0'
location = "Washington, dc"

#OWM = OpenWeather.OpenWeather(owm_API_key, location)
#OWM.RUN_FULL_TEST()

SmartCaster.RUN(0, owm_API_key, location)
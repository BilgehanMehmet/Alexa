
from weather import Weather


def getWeatherData(location):
    weather = Weather()

    location = weather.lookup_by_location(location)
    condition = location.condition()
    weatherData = condition._condition_data # dictionary type. get the .['text'] and .['temp'] keys.
    return build_response({}, build_speechlet_response(
        "", "Weather in " + location + "is" + weatherData['text'] + "and is " + weatherData['temp'] + "degrees Celcius."  , "Can you repeat please?", False))


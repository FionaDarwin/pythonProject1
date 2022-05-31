import requests
import gmplot

# Take the given locations and their coordinates to create three list objects
place_names = ['Lake District National Park', 'Corfe Castle', 'The Cotswolds', 'Cambridge', 'Bristol', 'Oxford',
               'Norwich', 'Stonehenge', 'Watergate Bay', 'Birmingham']
latitudes = [54.4609, 50.6395, 51.8330, 52.2053, 51.4545, 51.7520, 52.6309, 51.1789, 50.4429, 52.4862]
longitudes = [-3.0886, -2.0566, -1.8433, 0.1218, -2.5879, -1.2577, 1.2974, -1.8262, -5.0553, -1.8904]
succinct_weather = []

# For each location, retrieve all current weather information from the Open Weather API then print temperatures at
# each location
for i in range(len(place_names)):
    url = 'https://api.openweathermap.org/data/2.5/weather?lat={lati}&lon={longi}&appid=f5050f7adb1dd471bb68d1e1c8cfa0b3'.format(
        lati=latitudes[i], longi=longitudes[i])
    response = requests.get(url)
    weather_data = response.json()
    current_temperature = weather_data['main']['temp']
    rounded_celcius_temperature = round(current_temperature - 273.15, 1)
    succinct_weather.append(rounded_celcius_temperature)
    print("The temperature in", place_names[i], "is", round(current_temperature - 273.15, 1), "degrees C")

# Plot each location on a map and add markers that, when hovered over, show the current temperature
gmaps_apikey = '**API key goes here Mr Zilani**'
gmap1 = gmplot.GoogleMapPlotter(54.4609, -3.0886, 6, apikey=gmaps_apikey)
for i in range(len(place_names)):
    gmap1.marker(latitudes[i], longitudes[i], title=place_names[i] + " " + str(succinct_weather[i]) + " C",
                 color='#FFFF00')
gmap1.draw("map.html")

import requests
import folium
from folium.plugins import HeatMap

url = 'https://crimestoppers.hookrancho.com/api/crimes'
params = {
    'startDate': '2025-10-01',
    'endDate': '2025-10-31'
}

response = requests.get(url, params=params)
data = response.json()

coordinates = []
for feature in data['data']['features']:
    lat = feature['geometry']['coordinates'][1]
    lon = feature['geometry']['coordinates'][0]
    coordinates.append([lat, lon])

map_center = [42.2808, -83.7430]
mymap = folium.Map(location=map_center, zoom_start=13)

HeatMap(coordinates).add_to(mymap)

mymap.save("crime_heatmap.html")

print("Heatmap has been created and saved as 'crime_heatmap.html'.")
import folium
import pandas

# Loads in data file containing all info on volcanoes as a data frame
volcanoes = pandas.read_csv("Volcanoes.txt")

# Creates map centered on US
map = folium.Map([38, -99], zoom_start = 5, tiles = "Stamen Terrain")

# Housekeeping
feature_group_one = folium.FeatureGroup(name = "My Map")

# Creates the map markers for all the volcanoes in the data file, adds them to map
for index, volcano in volcanoes.iterrows():

    feature_group_one.add_child(folium.Marker([volcano["LAT"], volcano["LON"]], tooltip = volcano["NAME"], popup = volcano["LOCATION"], icon = folium.Icon(color = "purple")))

map.add_child(feature_group_one)

# Creates/Overwrites map file
map.save("Map1.html")
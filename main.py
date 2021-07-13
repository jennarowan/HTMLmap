import folium
import pandas
import json

# Loads in data file containing all info on volcanoes as a data frame
volcanoes = pandas.read_csv("Volcanoes.txt")

# Creates map centered on US
map = folium.Map([38, -99], zoom_start = 5, tiles = "Stamen Terrain")

# Housekeeping
feature_group_volcanoes = folium.FeatureGroup(name = "US Volcanoes")
feature_group_populations = folium.FeatureGroup(name = "Country Populations")

def pick_marker_color(volcano_height):

    # This function determines map marker color based on volcano height
    if volcano_height >= 3000:

        return "red"

    elif volcano_height >= 1000:

        return "orange"

    else:

        return "green"

# Creates the map markers for all the volcanoes in the data file, adds them to map
for index, volcano in volcanoes.iterrows():

    # Creates the basic data set for each volcano that will populate in the popup when the volcano's map marker is clicked
    iframe = folium.IFrame("Name: " + volcano["NAME"] + "<br>" + "Location: " + volcano["LOCATION"][3:] + "<br>" + "Status: " + volcano["STATUS"] + "<br>" + "Elevation: " + str(volcano["ELEV"])[:-2] + " meters" + "<br>" + "Type: " + volcano["TYPE"])

    popup = folium.Popup(iframe, min_width=250, max_width=250)

    # Final marker creaton
    feature_group_volcanoes.add_child(folium.Marker([volcano["LAT"], volcano["LON"]], tooltip = volcano["NAME"], popup = popup, icon = folium.Icon(color = pick_marker_color(volcano["ELEV"]),icon = "fire")))

# Creates population by country from local data file, colors each country by population level
feature_group_populations.add_child(folium.GeoJson(data = json.load(open("world.json", "r", encoding = "utf-8-sig")), style_function = lambda x: {"fillColor":"green" if x["properties"]["POP2005"] < 30000000 else "yellow" if x["properties"]["POP2005"] < 100000000 else "red"}))

# Adds all volcano markers and population coloring to the map
map.add_child(feature_group_volcanoes)
map.add_child(feature_group_populations)

# Adds a layer control panel to turn population coloring and volcano markers on and off
map.add_child(folium.LayerControl())

# Creates/Overwrites map file
map.save("Map1.html")
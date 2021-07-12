import folium

# Creates map centered on US
map = folium.Map([38, -99], zoom_start = 5, tiles = "Stamen Terrain")
map.add_child(folium.Marker([38, -99], tooltip="Yo homie", popup = "Look at me", icon = folium.Icon(color = "green")))
map.save("Map1.html")
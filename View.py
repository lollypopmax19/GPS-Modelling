import folium


# Karte mit Startpunkt
map = folium.Map(location=[52.5200, 13.4050], zoom_start=15)

# Echte Route hinzufügen (blaue Linie)
folium.PolyLine(route, color="blue", tooltip="Echter Pfad").add_to(map)

# GPS-Route (verrauscht, rote Linie)
folium.PolyLine(noisy_route, color="red", tooltip="GPS-Daten").add_to(map)

# Punkte markieren
for point in route[::10]:  # Jeder 10. Punkt für Übersichtlichkeit
    folium.CircleMarker(location=point, radius=2, color="blue").add_to(map)

for point in noisy_route[::10]:
    folium.CircleMarker(location=point, radius=2, color="red").add_to(map)

# Karte speichern
map.save("gps_simulation.html")
print("GPS-Simulation gespeichert: gps_simulation.html")

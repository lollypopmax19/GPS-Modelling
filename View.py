import folium

def visualize_route(route, noisy_route, filename="gps_simulation.html"):
    """Erstellt eine Karte mit echter und GPS-verzerrter Route."""
    if not route or not noisy_route:
        raise ValueError("Route oder Noisy Route ist leer!")

    # Karte mit Startpunkt
    map = folium.Map(location=route[0], zoom_start=15)

    # Echte Route (blaue Linie)
    folium.PolyLine(route, color="blue", tooltip="Echter Pfad").add_to(map)

    # GPS-Route (verrauscht, rote Linie)
    folium.PolyLine(noisy_route, color="red", tooltip="GPS-Daten").add_to(map)

    # Punkte markieren
    for point in route[::10]:  # Jeder 10. Punkt zur Übersichtlichkeit
        folium.CircleMarker(location=point, radius=2, color="blue").add_to(map)

    for point in noisy_route[::10]:
        folium.CircleMarker(location=point, radius=2, color="red").add_to(map)

    # Karte speichern
    map.save(filename)
    print(f"GPS-Simulation gespeichert: {filename}")

from Earth.Earth import Earth
from Earth.Satellite import Satellite
from Zeit.Zeitdilitation import TimeDilation
from GPSSimulation.Positioning import GPSSimulator
from Person.Path import Person

# 🌍 Erde-Objekt erstellen
earth = Earth()

# 🛰️ Satellitenliste
satellites = [
    Satellite("GPS-1", 26560e3, 0.01, 55, 0, 0, 0, 3874),
    Satellite("GPS-2", 26560e3, 0.01, 55, 45, 90, 180, 3874),
]

# 🚶‍♂️ Person simulieren (Startpunkt: Berlin)
person = Person(52.5200, 13.4050)
person.move(100)  # 100 Schritte simulieren
route = person.get_path()

# 📡 GPS-Ortung mit 6 Satelliten
gps_sim = GPSSimulator(satellite_count=6)
noisy_route = gps_sim.track_movement(route)

# 🔢 Berechnungen durchführen
for sat in satellites:
    position = sat.get_position()
    time_dilation = sat.get_time_dilation(earth.a)

    print(f"\n{sat.name} Position:")
    print(f"x={position[0]:.2f}, y={position[1]:.2f}, z={position[2]:.2f}")

    print(f"Zeitdilatation:")
    for key, value in time_dilation.items():
        print(f"{key}: {value:.12f} s")

# 🌍 Visualisierung der Route mit GPS-Daten (folium-Karte)
import folium

map = folium.Map(location=[52.5200, 13.4050], zoom_start=15)
folium.PolyLine(route, color="blue", tooltip="Echter Pfad").add_to(map)
folium.PolyLine(noisy_route, color="red", tooltip="GPS-Daten").add_to(map)

for point in route[::10]:  
    folium.CircleMarker(location=point, radius=2, color="blue").add_to(map)
for point in noisy_route[::10]:
    folium.CircleMarker(location=point, radius=2, color="red").add_to(map)

map.save("gps_simulation.html")
print("GPS-Simulation gespeichert: gps_simulation.html")

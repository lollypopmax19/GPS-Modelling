from Earth.Earth import Earth
from Earth.Satellite import Satellite
from Zeit.Zeitdilitation import TimeDilation
from GPSSimulation.Positioning import GPSSimulator
from Person.Path import Person
from View import visualize_route  # View-Funktion importieren

# 🌍 Erde-Objekt erstellen
earth = Earth()

# 🛰️ Satellitenliste erstellen
satellites = [
    Satellite("GPS-1", 26560e3, 0.01, 55, 0, 0, 0, 3874),
    Satellite("GPS-2", 26560e3, 0.01, 55, 45, 90, 180, 3874),
    Satellite("GPS-3", 26560e3, 0.01, 55, 90, 70, 150, 3874),
    Satellite("GPS-4", 26560e3, 0.01, 55, 20, 60, 120, 3874)
]

# 🚶‍♂️ Person simulieren
person = Person(52.5200, 13.4050)
person.move(100)
route = person.get_path()

print("Echte Route (erste 5 Punkte):", route[:5])  # Debug-Test

# 📡 GPS-Ortung mit 6 Satelliten simulieren
gps_sim = GPSSimulator(satellite_count=6)
noisy_route = gps_sim.track_movement(route)

print("GPS-Route (erste 5 Punkte):", noisy_route[:5])  # Debug-Test

# 📌 View.py aufrufen zur Visualisierung
visualize_route(route, noisy_route, "gps_simulation.html")

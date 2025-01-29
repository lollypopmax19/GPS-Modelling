import time
from Earth.Earth import Earth
from Earth.Satellite import Satellite
from Zeit.Zeitdilitation import TimeDilation
from GPSSimulation.Positioning import GPSSimulator
from Person.Path import Person
from View import visualize_route

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

# 📡 GPS-Ortung mit 6 Satelliten simulieren
gps_sim = GPSSimulator(satellite_count=6)
noisy_route = gps_sim.track_movement(route)

# 🔄 Zeitschleife für die Satellitenbewegung
simulation_time = 60 * 10  # 10 Minuten simulieren
time_step = 10  # Jede 10 Sekunden ein Update

for t in range(0, simulation_time, time_step):
    print(f"\n⏳ Zeit = {t} Sekunden")

    for sat in satellites:
        position = sat.get_position(time_seconds=t)
        print(f"{sat.name} Position nach {t} Sekunden: x={position[0]:.2f}, y={position[1]:.2f}, z={position[2]:.2f}")

    time.sleep(0.5)  # Simulation verlangsamen (nur für Visualisierung)

# 📌 View.py aufrufen zur Visualisierung
visualize_route(route, noisy_route, "gps_simulation.html")

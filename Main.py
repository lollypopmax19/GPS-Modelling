from Earth.Earth import Earth
from Earth.Satelite import Satellite

# Erde-Objekt erstellen
earth = Earth()
print(earth)

# Liste von Satelliten erstellen
satellites = [
    Satellite("GPS-1", 26560e3, 0.01, 55, 0, 0, 0),
    Satellite("GPS-2", 26560e3, 0.01, 55, 45, 90, 180),
    Satellite("GPS-3", 26560e3, 0.01, 55, 90, 180, 270),
]

# Satellitenpositionen berechnen
for sat in satellites:
    position = sat.get_position()
    print(f"{sat.name} Position: x={position[0]:.2f}, y={position[1]:.2f}, z={position[2]:.2f}")

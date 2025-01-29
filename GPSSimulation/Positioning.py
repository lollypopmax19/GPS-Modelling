class GPSSimulator:
    def __init__(self, satellite_count=4):
        """
        Simuliert eine GPS-Ortung mit variabler Genauigkeit.
        :param satellite_count: Anzahl der sichtbaren Satelliten (mehr = bessere Genauigkeit)
        """
        self.satellite_count = satellite_count
        self.error_range = 20 / self.satellite_count  # Fehlerbereich in Metern

    def get_noisy_position(self, lat, lon):
        """Gibt eine verrauschte GPS-Position zurück."""
        lat_error = np.random.normal(0, self.error_range * 0.00001)
        lon_error = np.random.normal(0, self.error_range * 0.00001)
        return lat + lat_error, lon + lon_error

    def track_movement(self, path):
        """Gibt eine verrauschte Version der Bewegung zurück."""
        noisy_path = [self.get_noisy_position(lat, lon) for lat, lon in path]
        return noisy_path

# GPS-Simulation mit 6 Satelliten
gps_sim = GPSSimulator(satellite_count=6)
noisy_route = gps_sim.track_movement(route)
print(noisy_route[:5])  # Zeigt die ersten verrauschten Positionen

import numpy as np

class Earth:
    def __init__(self):
        self.a = 6378137.0  # Äquatorradius in Metern
        self.f = 1 / 298.257223563  # Abplattung
        self.b = self.a * (1 - self.f)  # Polradius

    def to_cartesian(self, lat, lon, alt=0):
        """Wandelt geodätische Koordinaten in kartesische (ECEF) um."""
        lat, lon = np.radians(lat), np.radians(lon)
        e2 = 1 - (self.b**2 / self.a**2)
        N = self.a / np.sqrt(1 - e2 * np.sin(lat)**2)
        
        x = (N + alt) * np.cos(lat) * np.cos(lon)
        y = (N + alt) * np.cos(lat) * np.sin(lon)
        z = ((self.b**2 / self.a**2) * N + alt) * np.sin(lat)
        
        return np.array([x, y, z])

    def __repr__(self):
        return f"Earth(WGS84: a={self.a}, b={self.b})"

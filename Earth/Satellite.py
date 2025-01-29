import numpy as np

class Satellite:
    def __init__(self, name, a, e, i, omega, RAAN, nu, v):
        """
        Erstellt einen Satelliten mit Kepler-Parametern.
        :param name: Name des Satelliten
        :param a: Große Halbachse (m)
        :param e: Exzentrizität
        :param i: Inklination (Grad)
        :param omega: Argument des Perigäums (Grad)
        :param RAAN: Rektaszension des aufsteigenden Knotens (Grad)
        :param nu: Wahre Anomalie (Grad) (Startposition auf der Bahn)
        :param v: Geschwindigkeit des Satelliten (m/s)
        """
        self.name = name
        self.a = a
        self.e = e
        self.i = np.radians(i)
        self.omega = np.radians(omega)
        self.RAAN = np.radians(RAAN)
        self.nu = np.radians(nu)
        self.v = v  # Geschwindigkeit (m/s)

    def get_position(self, time_seconds=0):
        """Berechnet die Satellitenposition nach Kepler-Gesetzen."""
        # Bahnumlaufzeit nach Kepler 3. Gesetz
        mu = 3.986e14  # Erdgravitation in m³/s²
        T = 2 * np.pi * np.sqrt(self.a**3 / mu)  # Orbitale Periode in Sekunden
        
        # Neue wahre Anomalie nach Zeit t (vereinfachte lineare Näherung)
        mean_motion = 2 * np.pi / T  # Winkelgeschwindigkeit in rad/s
        new_nu = self.nu + mean_motion * time_seconds  # Position nach Zeit t
        new_nu = new_nu % (2 * np.pi)  # Begrenzung auf 0-2π
        
        # Bahnradius
        r = (self.a * (1 - self.e**2)) / (1 + self.e * np.cos(new_nu))
        
        # 3D-Orbitkoordinaten (Perifokus-System)
        x_orb = r * np.cos(new_nu)
        y_orb = r * np.sin(new_nu)
        z_orb = 0

        # Rotationen in das ECEF-System (Erde-zentriertes Koordinatensystem)
        cos_O = np.cos(self.RAAN)
        sin_O = np.sin(self.RAAN)
        cos_w = np.cos(self.omega)
        sin_w = np.sin(self.omega)
        cos_i = np.cos(self.i)
        sin_i = np.sin(self.i)

        x = (cos_O * cos_w - sin_O * sin_w * cos_i) * x_orb + (-cos_O * sin_w - sin_O * cos_w * cos_i) * y_orb
        y = (sin_O * cos_w + cos_O * sin_w * cos_i) * x_orb + (-sin_O * sin_w + cos_O * cos_w * cos_i) * y_orb
        z = (sin_i * sin_w) * x_orb + (sin_i * cos_w) * y_orb

        return np.array([x, y, z])

    def __repr__(self):
        return f"Satellite({self.name}: a={self.a}, e={self.e}, i={np.degrees(self.i)})"

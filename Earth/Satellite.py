import numpy as np
from Zeit.Zeitdilitation import TimeDilation
import sys 
sys.path.append("GPS-Modelling")

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
        :param nu: Wahre Anomalie (Grad)
        :param v: Geschwindigkeit des Satelliten (m/s)
        """
        self.name = name
        self.a = a
        self.e = e
        self.i = np.radians(i)
        self.omega = np.radians(omega)
        self.RAAN = np.radians(RAAN)
        self.nu = np.radians(nu)
        self.v = v

    def get_position(self):
        """Berechnet die Position im ECEF-System basierend auf Kepler-Gesetzen."""
        r = (self.a * (1 - self.e**2)) / (1 + self.e * np.cos(self.nu))
        x_orb = r * np.cos(self.nu)
        y_orb = r * np.sin(self.nu)
        z_orb = 0

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

    def get_time_dilation(self, earth_radius):
        """Berechnet die Zeitdilatation für den Satelliten."""
        sr_time = TimeDilation.special_relativity_dilation(self.v)
        gr_time = TimeDilation.general_relativity_dilation(earth_radius, self.a)

        net_time = gr_time - sr_time
        return {
            "SR (Zeit langsamer)": sr_time,
            "GR (Zeit schneller)": gr_time,
            "Netto-Zeitdilatation": net_time
        }

    def __repr__(self):
        return f"Satellite({self.name}: a={self.a}, e={self.e}, i={np.degrees(self.i)})"

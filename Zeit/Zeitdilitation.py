import numpy as np

class TimeDilation:
    """Berechnet die Zeitdilatation für Satelliten (SR & GR)."""

    @staticmethod
    def special_relativity_dilation(v, t=1):
        """Berechnet die Zeitdilatation nach der Speziellen Relativitätstheorie."""
        c = 299792458  # Lichtgeschwindigkeit in m/s
        gamma = np.sqrt(1 - (v**2 / c**2))  # Lorentz-Faktor
        return t * gamma  # Zeit im bewegten System

    @staticmethod
    def general_relativity_dilation(r_earth, r_sat, t=1):
        """Berechnet die Zeitdilatation nach der Allgemeinen Relativitätstheorie."""
        G = 6.67430e-11  # Gravitationskonstante
        M = 5.972e24  # Erdmasse in kg
        c = 299792458  # Lichtgeschwindigkeit in m/s

        factor = (G * M / c**2) * ((1 / r_earth) - (1 / r_sat))
        return t * (1 + factor)

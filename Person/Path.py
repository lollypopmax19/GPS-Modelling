import numpy as np
import random

class Person:
    def __init__(self, start_lat, start_lon, step_size=0.0001):
        """Erstellt eine Person, die sich zufällig bewegt."""
        self.lat = start_lat
        self.lon = start_lon
        self.step_size = step_size
        self.path = [(self.lat, self.lon)]

    def move(self, steps=100):
        """Bewegt die Person zufällig in einer Richtung."""
        for _ in range(steps):
            direction = random.choice(["N", "S", "E", "W"])
            
            if direction == "N":
                self.lat += self.step_size
            elif direction == "S":
                self.lat -= self.step_size
            elif direction == "E":
                self.lon += self.step_size
            elif direction == "W":
                self.lon -= self.step_size
            
            self.path.append((self.lat, self.lon))

    def get_path(self):
        """Gibt die simulierte Route zurück."""
        return self.path

"""
Ce module contient la définition de la classe Vehicule
"""
import logging


class Vehicule(object):
    """
    Regroupe les routes  de son itinairaire
    et définit la position du véhicule dans le temps
    """
    MAX_SPEED = 5
    COUNTER = 0

    @classmethod
    def get_id(cls):
        cls.COUNTER += 1
        return cls.COUNTER

    def __init__(self, roads=None, name=None):
        self.name=name if name is not None else f"Vehicule{self.get_id()}"
        self._init_time = 0
        self._current_speed = self.MAX_SPEED # On démarre avec la vitesse maximale
        self._current_time = 0
        self._current_position_idx = 0

        self._path = [] # Liste des routes à prendre par le Vehicule
        if roads is not None:
            self.add_path(roads)

    def __repr__(self):
        return f"<Vehicule {self.name} : position={self.position}(index={self.index}), speed={self.speed}, length={self.length}>"

    @property
    def length(self):
        return len(self._path)

    @property
    def travel_time(self):
        return self._init_time + self.length

    @property
    def position(self):
        if self._current_position_idx>=0 and self._current_position_idx<self.length:
            return self._path[self._current_position_idx]

    @property
    def is_started(self):
        return self._current_position_idx>=0

    @property
    def is_ended(self):
        return self.index >= len(self._path)

    @property
    def index(self):
        return self._current_position_idx

    @index.setter
    def index(self, value):
        self._current_position_idx = value

    @property
    def current_time(self):
        return self._current_time

    @current_time.setter
    def current_time(self, real_time):
        self._current_time = real_time

    @property
    def speed(self):
        return self._current_speed

    @speed.setter
    def speed(self, value):
        self._current_speed = value

    def add_path(self, roads:list):
        """
        Ajoute une route à l'itinairaire
        """
        for road in roads:
            self._path.extend(road.path)

    def start(self, init_time):
        """
        Définit le moment du départ
        => permet un décalage dans la lecture des positions
        """
        self._init_time = init_time
        self.current_time = 0
        self.index = -init_time

    def forward(self, new_time):
        logging.debug(repr(self)+f".forward : ended={self.is_ended}")
        if not self.is_ended:
            delta_time = new_time - self.current_time
            logging.debug(f"... delta time = {delta_time}")
            self.index += delta_time*self.speed
            self.current_time = new_time
            logging.debug(f"... new time = {new_time}")
            logging.debug(f"... current time = {self.current_time}")

    def get_position(self, new_time):
        """
        Retourne la position (x,y) du Vehicule
        """
        self.forward(new_time)
        return (None, None) if not self.is_started or self.is_ended else self.position

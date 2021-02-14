"""
Ce module contient
- class Scenario => permet de calculer par anticipation la position des véhicules

"""
import logging

MAX_FRAMES = 10000   # Nombre maximum d'étape du scénario

class Scenario:
    """
    Calcule la position des véhicules avant l'animation

    """
    def __init__(self, traffic: list):
        self._traffic = traffic     # Liste des véhicules
        self._frames = list()       # liste des coordonnées pour le traffic pour une étape
        self.create_frames()

    def __len__(self):
        return len(self.frame)

    @property
    def frame(self):
        return self._frames

    def add_frame(self, value: list) -> None:
        """
        Le ":list" indique le type (ici, le type list) d'une variable en paramètre d'une fonction (ici, la variable
        "value") et le "->None" indique la signature de la fonction (ce qu'elle renvoie) : ici, par exemple, elle ne
        renvoie rien (donc elle est de type None).
        """
        self._frames.append(value)

    def create_frames(self):
        """
        Création des frames
        """
        num_frame = 0
        while not all([vehicule.is_ended for vehicule in self._traffic]) and num_frame < MAX_FRAMES:
            """
            La fonction "all" est une fonction qui prend une liste de booléens en paramètre et renvoie True si tous les
            booléens de la liste sont True (cf. "pour tout" mathématique).
            Il existe une sorte de fonction contraire : il s'agit de la fonction "any" : elle prend également une liste
            de booléens en paramètre et renvoie True si au moins l'un des booléens est égal à True (cf. "il existe"
            mathématique).
            """
            logging.debug(f"""Frame #{num_frame} : {[f"{x.is_started}({x.index})" for x in self._traffic]}""")
            self.add_frame([x.get_position(num_frame) for x in self._traffic])
            num_frame += 1

    def get_data(self, num_frame: int) -> tuple:
        """
        Retourne la série de coordonnées pour l'animation
        :return: ([x0, ...xn], [y0, ..., yn])
        """
        return (
            [position.x for position in self.frame[num_frame]],
            [position.y for position in self.frame[num_frame]]
        )
from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Localitate(Entity):
    id_centru_vaccinare : str
    nume_loc : str
    distanta : int
    CNP : str
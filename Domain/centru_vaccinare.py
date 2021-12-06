from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class CentruVaccinare(Entity):
    denumire : str
    capacitate : int
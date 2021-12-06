from Domain.centru_vaccinare import CentruVaccinare
from Repository.repository import Repository


class CentruVaccinareValidator:
    def validare_centru(self, centru: CentruVaccinare):
        erori = []
        if len(centru.denumire) < 3:
            erori.append('Denumirea centrului tebuie sa aiba minim 3 caractere!')
        if centru.capacitate < 100:
            erori.append('Capacitatea trebuie sa fie mai mare de 100!')
        if erori:
            raise ValueError(erori)


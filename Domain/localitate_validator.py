from Domain.localitate import Localitate
from Repository.repository import Repository


class LocalitateValidator:
    def validare_localitate(self, localitate: Localitate, localitate_repository: Repository):
        erori = []
        self.localitate_repository = localitate_repository
        lst_localitate = self.localitate_repository.read()
        if localitate.id_centru_vaccinare is None:
            erori.append('Localitatea nu exista!')
        if len(localitate.nume_loc) < 3:
            erori.append('Localitatea trebuie sa aiba un nume cu minim 3 caractere!')
        if localitate.distanta < 1:
            erori.append('Distanta trebuie sa aiba minim 1 km')
        for loc in lst_localitate:
            if localitate.id_entity == loc.id_localitate:
                erori.append('Id-unic')
            if localitate.CNP == loc.CNP:
                erori.append('CNP-unic')

        if erori:
            raise ValueError(erori)

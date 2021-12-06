from Domain.centru_vaccinare import CentruVaccinare
from Domain.localitate import Localitate
from Domain.localitate_validator import LocalitateValidator
from Repository.repository import Repository


class LocalitateService:
    def __init__(self,
                 localitate_repository: Repository,
                 localitate_validator: LocalitateValidator):
        """
        Creeaza un service pentru localitati.
        :param city_repository: repository
               care retine localitati.
        :param city_validator: validatorul
               pentru localitati
        """
        self.localitate_repository = localitate_repository
        self.localitate_validator = localitate_validator

    def add_localitate(self,id_localitate: str, id_centru: str, nume_loc: str, distanta: int, CNP: str):
        """
        Adauga o localitate.
        :param id_city: id-ul localitatii.
        :param name: numele localitatii, string nenul.
        :param type: tipul localitatii, sat, oras sau municipiu.
        :return:
        """
        localitate = Localitate(id_localitate, id_centru, nume_loc, distanta, CNP)
        self.localitate_repository.create(localitate)

    def get_all(self):
        """
        :return: o lista cu toate localitatile
        """
        return self.localitate_repository.read()
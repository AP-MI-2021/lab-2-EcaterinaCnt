from Domain.centru_vaccinare import CentruVaccinare
from Domain.centru_vaccinare_validator import CentruVaccinareValidator
from Repository.repository import Repository


class CentruService:
    def __init__(self,
                 centru_vaccinare_repository: Repository,
                 centru_vaccinare_validator: CentruVaccinareValidator):
        """
        Creeaza un service pentru localitati.
        :param city_repository: repository
               care retine localitati.
        :param city_validator: validatorul
               pentru localitati
        """
        self.centru_repository = centru_vaccinare_repository
        self.centru_vaccinare_validator = centru_vaccinare_validator

    def add_centru(self, id_centru: str, denumire: str, capacitate: int):
        """
        Adauga o localitate.
        :param id_city: id-ul localitatii.
        :param name: numele localitatii, string nenul.
        :param type: tipul localitatii, sat, oras sau municipiu.
        :return:
        """
        centru = CentruVaccinare(id_centru, denumire, capacitate)
        self.centru_repository.create(centru)
        self.centru_vaccinare_validator.validare_centru(centru)


    def get_all(self):
        """
        :return: o lista cu toate centrele
        """
        return self.centru_repository.read()

    def ordon_centru_capac(self):
        return sorted(self.centru_repository.read(), key=lambda x: x.capacitate, reverse=True)
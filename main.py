from Domain.centru_vaccinare_validator import CentruVaccinareValidator
from Domain.localitate_validator import LocalitateValidator
from Repository.json_repository import JsonRepository
from Service.centru_vaccinare_service import CentruService
from Service.localitate_service import LocalitateService
from UserInterface.console import Console


def main():
    centru_repostory = JsonRepository('centruvaccinare.json')
    localitate_repository = JsonRepository('localitate.json')

    centru_vaccinare_validator = CentruVaccinareValidator()
    localitate_validator = LocalitateValidator()

    centru_service = CentruService(centru_repostory, centru_vaccinare_validator)
    localitate_service = LocalitateService(localitate_repository, localitate_validator)

    console = Console(centru_service, localitate_service)
    console.run_console()

if __name__ == '__main__':
        main()
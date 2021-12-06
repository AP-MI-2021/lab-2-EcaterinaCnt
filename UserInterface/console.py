from Service.centru_vaccinare_service import CentruService
from Service.localitate_service import LocalitateService


class Console:
    def __init__(self,
                 centru_service: CentruService,
                 localitate_service: LocalitateService):
        self.centru_service = centru_service
        self.localitate_service = localitate_service

    def show_menu(self):
        print('1. Adauga localitate')
        print('2. Adauga centru')
        print('sl. Afiseaza localitatile')
        print('sc. Afiseaza centru')
        print('x. Exit')

    def run_console(self):

        while True:
            self.show_menu()
            opt = input('Optiunea: ')

            if opt == '1':
                self.handle_add_centru()
            elif opt == 'sl':
                self.handle_show_all(self.centru_service.get_all())
            elif opt == '2':
                self.handle_add_localitate()
            elif opt == 'sr':
                self.handle_show_all(self.localitate_service.get_all())
            elif opt == 'x':
                break
            else:
                print('Optiune invalida.')

    def handle_add_centru(self):
        try:
            id_centru = input('Id-ul centru: ')
            denumire = input('Numele centru: ')
            capacitate = int(input('Capacitate minim 100: '))

            self.centru_service.add_centru(id_centru, denumire, capacitate)
        except Exception as ex:
            print('Eroare:', ex)

    def handle_show_all(self, entities):
        for entity in entities:
            print(entity)

    def handle_add_localitate(self):
        try:
            id_localitate = input('Id-ul localitatii: ')
            id_centru = input('Id-ul centru: ')
            nume_loc = input('Numele localitate: ')
            distanta = int(input('Distanta minim 1km: '))
            CNP = input('Dati cnp: ')

            self.localitate_service.add_localitate(id_localitate, id_centru, nume_loc, distanta, CNP)
        except ValueError as ve:
            print('Eroare validare:', ve)
        except KeyError as ke:
            print('Eroare ID:', ke)
        except Exception as ex:
            print('Eroare:', ex)

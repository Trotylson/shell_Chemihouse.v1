import Database
import Tools
import time


def createProduct():
    while True:
        reference = input('Podaj referencję towaru: ').upper()
        decision = Database.checkRefComplianceWithDb(reference)
        if decision == True:
            print('Referencja już istnieje! ', reference, '\n[ENTER] by wyjść.')
            input()
            break
        manufacturer = input('Podaj nazwę producenta: ').upper()
        name = input('Podaj nazwę towaru: ').upper()
        code = input ('Podaj kod kreskowy towaru: ').upper()
        quantity = input('Podaj ilość przyjmowanego towaru: ')
        Tools.consoleClear()

        print('Czy podane informacje się zgadzają? \n\n\tProducent: ', manufacturer,
             '\n\tNazwa: ', name, '\n\tReferencja: ', reference, '\n\tKod kreskowy: ',
             code, '\n\tIlość : ', quantity)
        check = input('\n[T - tak / E - wyjście]: ')

        if check.upper() == 'T' or check.upper() == 'TAK':
            Database.insertTo(reference, manufacturer, name, code, quantity)
            Tools.consoleClear()
            break
        elif check.upper() == 'E':
            Tools.consoleClear()
            print('Koniec sekwencji dodawania...')
            time.sleep(2)
            break
        Tools.consoleClear()

def editStock():
    while True:
        reference = input('Podaj referencję towaru: ').upper()
        decision = Database.checkRefComplianceWithDb(reference)
        if decision == False:
            print('Referencja nie istnieje! ', reference, '\n[ENTER] by wyjść.')
            input()
            break
        quantity = input('Podaj ilość: ')
        try:
            if int(quantity) != 0:
                Database.crorrectStock(quantity, reference)
                break
        except:
            print('Stan nie został zmieniony.\nNaciśnij [ENTER] aby przejść dalej...')
            input()
            break

def editProduct():
    oldRef = input('\nPodaj numer referencji dla której chcesz wprowadzić zmieny: ').upper()
    decision = Database.checkRefComplianceWithDb(oldRef)
    if decision == False:
        print('Podana referencja nie jest prawidłowa lub nie istnieje! ', oldRef, '\n[ENTER] by wyjść.')
        input()
        return
    Tools.consoleClear()
    manufacturer = input('Podaj nową nazwę producenta: ')
    name = input('Podaj nową nazwę towaru: ')
    reference = input('Podaj nową referencję: ')
    code = input('Podaj nowy kod kreskowy towaru: ')

    Database.editRecord(reference, manufacturer, name, code, oldRef)
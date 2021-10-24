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
        minimumQuant = input('Podaj ilość MINIMALNĄ stanu: ')
        Tools.consoleClear()

        print('Czy podane informacje się zgadzają? \n\n\tProducent: ', manufacturer,
             '\n\tNazwa: ', name, '\n\tReferencja: ', reference, '\n\tKod kreskowy: ',
             code, '\n\tIlość : ', quantity, '\n\tIlość minimalna : ', minimumQuant)
        check = input('\n[T - tak / E - wyjście]: ')

        if check.upper() == 'T' or check.upper() == 'TAK':
            Database.insertTo(reference, manufacturer, name, code, quantity, minimumQuant)
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
    while True:
        selectWay = input('\nCo chcesz zrobić: \n\t1 - Edytuj produkt\n\t2 - Usuń produkt'
                          '\n\nE - Wyjdź\n\nPozycja: ').upper()
        if selectWay == '1':
            Tools.consoleClear()
            manufacturer = input('Podaj nową nazwę producenta: ').upper()
            name = input('Podaj nową nazwę towaru: ').upper()
            reference = input('Podaj nową referencję: ').upper()
            code = input('Podaj nowy kod kreskowy towaru: ').upper()
            minQuant = input('Podaj ilość MINIMALNĄ stanu: ')
            Database.editRecord(reference, manufacturer, name, code, minQuant, oldRef)
            break
        elif selectWay == '2':
            Database.deleteRecord(oldRef)
            break
        elif selectWay == 'E':
            break

def showItemsToOrder():
    print('REFERENCJA | NAZWA | STAN | STAN MINIMALNY\n')
    Database.showDbOrder()
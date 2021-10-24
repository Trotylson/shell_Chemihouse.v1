import sqlite3
import Database
import Product
import Tools
from datetime import date

Database.createOrDrop('c') #CARE!
# ('c') to create or use actual database table
# ('d') to drop actual table and create new empty
# ('s') to drop and seed new records

def select(key):
    if key == '1': # add item
        Tools.consoleClear()
        Product.createProduct()
    elif key == '2': # edit item stock
        Tools.consoleClear()
        Product.editStock()
    elif key == '3': # edit item
        Tools.consoleClear()
        Database.showDatabase()
        Product.editProduct()
    elif key == '4': # show warehouse state
        Tools.consoleClear()
        Database.showDatabase()
        input('\nENTER aby zamknąć...')

while True:
    Tools.consoleClear()
    print(str(date.today()) + '\n\nWitaj w CHEMIHOUSE - magazynku chemii warsztatowej ver. 1.0\n')
    print('\tWybierz pozycję i zatwierdź [ENTER]:\n\n\t\t1 - Dodaj towar\n\t\t2 - Rozchód / przychód\n\t\t3 - Edytuj towar\n\t\t4 - Podgląd magazynu\n\t\tE - Wyjście\n')

    choose = input('\t\tPozycja: ')
    if choose.upper() == 'E':
        Database.closeDb()
        break
    Tools.consoleClear()
    select(choose)

        
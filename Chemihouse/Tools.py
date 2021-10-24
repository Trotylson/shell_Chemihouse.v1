import os
import Database
from datetime import date

def consoleClear():
    os.system('cls')

def dbSeed():
    Database.insertTo('BRE123', 'NORMFEST', 'BREMTEC', '12380', 5, 2)
    Database.insertTo('SB123', 'NORMFEST', 'SILON BLACK', '22780', 2, 2)
    Database.insertTo('SPY123', 'NORMFEST', 'SPY', '68380', 10, 2)
    Database.insertTo('S123', 'NORMFEST', 'SILON', '73380', 1, 2)
    Database.insertTo('CV40', 'NORMFEST', 'CV-40', '45380', 3, 2)
    Database.insertTo('2894-445-5', 'NORMFEST', 'HIGH PRESS PROTECT', '77880', 3, 2)
    Database.insertTo('2894-446', 'NORMFEST', 'BIO-TOP', '55380', 3, 2)
    Database.insertTo('2897-324', 'NORMFEST', 'SILTRON', '28380', 3, 2)
    Database.insertTo('2897-447', 'NORMFEST', 'TT-POWER', '44780', 3, 2)

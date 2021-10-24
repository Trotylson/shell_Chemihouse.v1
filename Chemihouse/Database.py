import sqlite3
from datetime import date
import Tools

conn = sqlite3.connect('Chemihouse.db', check_same_thread=False)
db = conn.cursor()

table = '''CREATE TABLE IF NOT EXISTS Products (
        Referencja TEXT, 
        Producent TEXT, 
        Nazwa TEXT, 
        Kod_kreskowy TEXT, 
        Stan INTEGER, 
        Stan_minimum INTEGER,
        Ostatni_ruch TIMESTAMP)'''

def checkRefComplianceWithDb(ref):
    reference = "('"+ref+"',)"
    for row in db.execute("""SELECT Referencja FROM Products"""):
        if str(row) == reference:
            return True
    for row in db.execute("""SELECT Kod_kreskowy FROM Products"""):
        if str(row) == reference:
            return True
    return False

def createOrDrop(order):
    if order == 'c':
        db.execute(table)
    elif order == 'd': 
        db.execute("DROP TABLE Products")
        db.execute(table)
    elif order == 's':
        db.execute("DROP TABLE Products")
        db.execute(table)
        Tools.dbSeed()
        conn.commit()

def insertTo(ref, prod, name, code, quant, min):
    insertQuery = """INSERT INTO Products VALUES(?,?,?,?,?,?,?)"""
    db.execute(insertQuery, (ref, prod, name, code, quant, min, date.today()))
    conn.commit()

def crorrectStock(quant, ref): #edit item stock
    insertQuerry = """UPDATE Products set Stan = Stan + ?, Ostatni_ruch = ? 
                    WHERE Referencja = ? OR Kod_kreskowy = ?"""
    db.execute(insertQuerry, (quant, date.today(), ref, ref))
    conn.commit()
    
def editRecord(ref, prod, name, code, min, oldRef):
    insertQuerry = """UPDATE Products set 
    Referencja = ?,
    Producent = ?,
    Nazwa = ?,
    Kod_kreskowy = ?,
    Stan_minimum = ?,
    Ostatni_ruch = ?
    where Referencja = ?"""
    db.execute(insertQuerry, (ref, prod, name, code, min, date.today(), oldRef))
    conn.commit()

def deleteRecord(ref):
    deleteRecord = """DELETE FROM Products WHERE Referencja = ? OR Kod_kreskowy = ?"""
    db.execute(deleteRecord,(ref, ref,))
    conn.commit()

def showDbOrder():
    for row in db.execute("""SELECT Referencja, Nazwa, Stan, 
    Stan_minimum FROM Products WHERE Stan <= Stan_Minimum"""):
        print(row)

def closeDb():
    conn.close()

def showDatabase():
    print('REFERENCJA | PRODUCENT | NAZWA | KOD KRESKOWY | STAN | STAN MINIMALNY | DATA OSTATNIEJ MODERNIZACJI\n')
    for row in db.execute('SELECT * FROM Products'):
        print (row)

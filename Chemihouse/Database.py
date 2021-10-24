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
        Ostatni_ruch TIMESTAMP)'''

def checkRefComplianceWithDb(ref):
    reference = "('"+ref+"',)"
    for row in db.execute("""SELECT Referencja FROM Products"""):
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

def insertTo(ref, prod, name, code, quant):
    insertQuery = """INSERT INTO Products VALUES(?,?,?,?,?,?)"""
    db.execute(insertQuery, (ref, prod, name, code, quant, date.today()))
    conn.commit()

def crorrectStock(quant, ref):
    insertQuerry = """UPDATE Products set Stan = Stan + ?, Ostatni_ruch = ? where Referencja = ?"""
    db.execute(insertQuerry, (quant, date.today(), ref.upper()))
    conn.commit()
    
def editRecord(ref, prod, name, code, oldRef):
    insertQuerry = """UPDATE Products set 
    Referencja = ?,
    Producent = ?,
    Nazwa = ?,
    Kod_kreskowy = ?,
    Ostatni_ruch = ?
    where Referencja = ?"""
    db.execute(insertQuerry, (ref.upper(), prod.upper(), name.upper(), code.upper(), date.today(), oldRef.upper()))
    conn.commit()

def closeDb():
    conn.close()

def showDatabase():
    print('REFERENCJA | PRODUCENT | NAZWA | KOD KRESKOWY | STAN | DATA OSTATNIEJ MODERNIZACJI\n')
    for row in db.execute('SELECT * FROM Products'):
        print (row)

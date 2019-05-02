import xlrd
import MySQLdb as sql

# SQL
db = sql.connect(host="localhost", user="root",passwd="toor", db="excel")

curs = db.cursor()

query = """ INSERT INTO belajar(id,nama,kelas,alamat) VALUES (%s,%s,%s,%s)"""

# XLS File
book = xlrd.open_workbook("Test.xls") #nama file xls nya
sheet = book.sheet_by_name('Test') #nama sheet excel

#Execute

for n in range(1,sheet.nrows):
		id		= sheet.cell(n,0).value
		nama		= sheet.cell(n,1).value
		kelas		= sheet.cell(n,2).value
		alamat		= sheet.cell(n,3).value

		values = (id,nama,kelas,alamat)

		curs.execute(query,values)

curs.close
db.commit()

print("Anda telah berhasil Import !!!")

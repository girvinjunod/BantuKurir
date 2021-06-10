import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="tspirk"
)
mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE mydatabase")
#mycursor.execute("SHOW DATABASES")
#mycursor.execute("SHOW TABLES")
#mycursor.execute("CREATE TABLE tsp (id INT AUTO_INCREMENT PRIMARY KEY, identitas_kurir VARCHAR(255), tanggal_pengiriman DATETIME DEFAULT CURRENT_TIMESTAMP, jalur VARCHAR(255), waktu TIME, estimasi TIME, cost FLOAT(12,4))")
#mycursor.execute("SELECT * FROM customers")
#myresult = mycursor.fetchall()

#sql = "INSERT INTO tsp (identitas_kurir, jalur, waktu, estimasi, cost) VALUES (%s, %s, %s, %s, %s)"
#val = ("Joko", "Perusahaan-ITB-Perusahaan", "13:13:13", "15:15:15", "6.9")
#mycursor.execute(sql, val)
#mydb.commit()

sql = "SELECT jalur,waktu,estimasi,cost FROM tsp where DATE(tanggal_pengiriman) = %s and identitas_kurir = %s"
val = ('2021-6-10', 'Joko')
mycursor.execute(sql, val)
#mycursor.execute("SELECT jalur,waktu,estimasi,cost FROM tsp where DATE(tanggal_pengiriman) = %s and identitas_kurir = %s")
ajalur = []
awaktu = []
aestimasi = []
acost = []
myresult = mycursor.fetchall()
for x in myresult:
    ajalur.append(x[0])
    awaktu.append(str(x[1]))
    aestimasi.append(str(x[2]))
    acost.append(x[3])
print(ajalur)
print(awaktu)
print(aestimasi)
print(acost)
print(len(ajalur))

#print(datetime.timedelta(seconds=47593))
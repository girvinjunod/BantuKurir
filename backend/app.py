from flask import Flask, render_template, redirect, url_for,request
import mysql.connector
import datetime

from graf import Graf
from tsp import *

app = Flask(__name__)
UPLOAD_FOLDER = 'test'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="tspirk"
)
mycursor = mydb.cursor()



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods = ['POST'])
def data():
    message = request.get_json()
    identitas = message['identitas']['nama']
    tanggal = message['tanggal']['tanggal']
    print(identitas)
    print(tanggal)
    sql = "SELECT jalur,waktu,estimasi,cost FROM tsp where DATE(tanggal_pengiriman) = %s and identitas_kurir = %s"
    val = (tanggal, identitas)
    mycursor.execute(sql, val)
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
    if len(ajalur) == 0:
        obj = {"found": False, "msg": "Pengiriman tidak ditemukan"}
        print(obj)
        return obj
    obj = {"found": True, "jalur": ajalur, "waktu": awaktu, "estimasi": aestimasi, "cost": acost}
    print(obj)
    return obj

@app.route('/graph', methods = ['POST'])
def graph():
    message = request.get_json()
    anamalokasi = message['namalokasi']
    akoorlokasi = message['koorlokasi']
    namakurir = message['identitas']
    waktu = message['waktu']
    kecepatan = (message['kecepatan'])

    for i in akoorlokasi:
        for j in i:
            j[0] = float(j[0])
            j[1] = float(j[1])

    for i in range(len(kecepatan)):
        kecepatan[i] = float(kecepatan[i])        
    print(message)
    print(anamalokasi)
    print(akoorlokasi)
    print(namakurir)
    print(waktu)
    print(kecepatan)
    awal = 0

    #jalur tulisan
    ajalur = []
    #jalur graph
    agraph = []
    #cost terkecil
    ajarak = []
    #Estimasi waktu
    aestimasi = []

    for i in range(len(anamalokasi)):
        print("masuk")
        v = kecepatan[i]
        mulai = waktu[i]
        identitas = namakurir[i]
        namalokasi = anamalokasi[i]
        koorlokasi = akoorlokasi[i]
        titikawal = koorlokasi[awal]


        n = len(koorlokasi)
        jaraklokasi = getDistance(koorlokasi)
        res, jalur = solveTSP(jaraklokasi, awal)
        teksjalur, teksjarak, listnamahasil = out(res,jalur,namalokasi)
        time = getEstimate(v, res, mulai)
        aestimasi.append(str(time))
        ajalur.append(teksjalur)
        ajarak.append(teksjarak)

        node_x = []
        node_y = []
        for i in koorlokasi:
            node_x.append(i[0])
            node_y.append(i[1])
        graf = Graf(node_x,node_y,namalokasi)
        

        #cari node terjauh
        atas = 0
        kanan = 0
        bawah = 0
        kiri = 0
        for i in koorlokasi:
            if i[0] > kanan:
                kanan = i[0]
            if i[0] < kiri:
                kiri = i[0]
            if i[1] > atas:
                atas = i[1]
            if i[1] < bawah:
                bawah = i[1]
        kanan += 1.5
        kiri -= 1.5
        bawah -= 1.5
        atas += 1.5

        #Isi jalur di graf
        for i in range(n):
            for j in range(n):
                listx = []
                listy = []
                name = []
                if (jaraklokasi[i][j]):
                    listx.append(koorlokasi[i][0])
                    listx.append(koorlokasi[j][0])
                    listy.append(koorlokasi[i][1])
                    listy.append(koorlokasi[j][1])
                    name.append(namalokasi[i])
                    name.append(namalokasi[j])
                    graf.tambahjalur(listx, listy, name)

        #memasukkan hasil
        listxhasil = []
        listyhasil = []
        namahasil = []
        for i in range(len(jalur)):
            listxhasil.append(koorlokasi[jalur[i]][0])
            listyhasil.append(koorlokasi[jalur[i]][1])
            namahasil.append(namalokasi[jalur[i]])
        
        graf.tambahjalurhasil(listxhasil,listyhasil, listnamahasil)
        graf.tambahAwal([koorlokasi[0][0]],[koorlokasi[0][1]], [namalokasi[0]])

        graf.editFig()

        xanimate = []
        yanimate = []
        for i in range(len(jalur) - 1):
            p1 = koorlokasi[jalur[i]]
            p2 = koorlokasi[jalur[i+1]]
            antarkoor = intermediates(p1, p2, nb_points=5)
            for i in antarkoor:
                xanimate.append(i[0])
                yanimate.append(i[1])
            xanimate.append(p2[0])
            yanimate.append(p2[1])
        nodex = []
        nodey = []
        for i in range(n):
            if node_x[i] != titikawal[0] and node_y[i] != titikawal[1]:
                nodex.append(node_x[i])
                nodey.append(node_y[i])
        graf.addAnimation(xanimate,yanimate,atas,kanan,bawah,kiri, nodex, nodey, namalokasi)
        
        #simpen di db
        dbjalur, sampah = getJalurNama(jalur, namalokasi)
        cost = "{:.4f}".format(res)

        sql = "INSERT INTO tsp (identitas_kurir, jalur, waktu, estimasi, cost) VALUES (%s, %s, %s, %s, %s)"
        val = (identitas, dbjalur, mulai, str(time), cost)
        #mycursor.execute(sql, val)
        #mydb.commit()



        graphJSON = graf.getGraph()
        agraph.append(graphJSON)
        #graf.visualize()

    #jalur tulisan
    #print(ajalur)

    #jalur graph
    #print(agraph)

    #cost terkecil
    #print(ajarak)

    #Estimasi waktu
    #print(aestimasi)

    obj = {"jalur": ajalur,"graf": agraph, "jarak": ajarak, "estimasi": aestimasi}
    return obj

if __name__ == "__main__":
    app.run(debug = True)
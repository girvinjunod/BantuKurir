from flask import Flask, render_template, redirect, url_for

from graf import Graf
from tsp import *
app = Flask(__name__)
UPLOAD_FOLDER = 'test'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graph', methods = ['POST'])
def graph():
    #paling ini dibuat post aj, nanti ngevisualize per input
    print("Halo")
    anamalokasi = [["Perusahaan", "Indomaret", "Neraka", "ITB", "Rumah Yahya"]]
    akoorlokasi = [[[0,0], [3,4], [12,3], [-5,-7], [6,-3]]]
    awal = 0
    #v
    #identitas
    #waktu

    for i in range(len(anamalokasi)):
        v = 10 #km/jam
        namalokasi = anamalokasi[i]
        koorlokasi = akoorlokasi[i]
        titikawal = koorlokasi[awal]
        n = len(koorlokasi)
        jaraklokasi = getDistance(koorlokasi)
        res, jalur = solveTSP(jaraklokasi, awal)
        teks, listnamahasil = out(res,jalur,namalokasi)
        waktu = getTime(v, res)
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

        graphJSON = graf.getGraph()
        #print(graphJSON)
        graf.visualize()
    #jalur tulisan
    #jalur graph
    #cost terkecil
    #Estimasi waktu
    return redirect(url_for(".index"))

if __name__ == "__main__":
    app.run(debug = True)
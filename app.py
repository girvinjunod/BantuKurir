from flask import Flask, render_template, redirect, url_for

from graf import Graf
from tsp import *
app = Flask(__name__)
UPLOAD_FOLDER = 'test'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graph')
def graph():
    #paling ini dibuat post aj, nanti ngevisualize per input
    anamalokasi = [["Perusahaan", "Indomaret", "Neraka", "ITB", "Rumah Yahya"]]
    akoorlokasi = [[[0,0], [3,4], [12,3], [-5,-7], [6,-3]]]
    for i in range(len(anamalokasi)):
        namalokasi = anamalokasi[i]
        koorlokasi = akoorlokasi[i]
        n = len(koorlokasi)
        jaraklokasi = getDistance(koorlokasi)
        res, jalur = solveTSP(jaraklokasi)
        teks, listnamahasil = out(res,jalur,namalokasi)
        node_x = []
        node_y = []
        for i in koorlokasi:
            node_x.append(i[0])
            node_y.append(i[1])
        graf = Graf(node_x,node_y,namalokasi)
        

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
        graf.visualize()
    #graphJSON = graf.getGraph()
    return redirect(url_for(".index"))

if __name__ == "__main__":
    app.run(debug = True)
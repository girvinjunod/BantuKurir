import json
import plotly
import plotly.graph_objects as go
from tsp import *
import numpy as np


class Graf:
    def __init__(self,nodex,nodey,nama):
        self.fig = go.Figure()
        self.fig.add_trace(go.Scatter(
            x=nodex,
            y=nodey,
            mode='markers',
            marker= dict(color = 'red', size = 10),
            text = nama,
            name = "Lokasi"
        ))
        self.count = 0

    def __str__(self):
        return "Ini graf"
    
    def tambahAwal(self, xawal, yawal, namaawal): #tambah simpul awal

        self.fig.add_trace(go.Scatter(
            mode = "markers",
            x = xawal,
            y = yawal,
            marker = dict(color = 'LightSkyBlue', size = 14),
            text = namaawal,
            name = "Titik Awal"
            ))

    def tambahjalur(self, jalurx, jalury, name): #tambah jalur
        if (self.count > 0):
            self.fig.add_trace(go.Scatter(
            mode = "lines",
            x = jalurx,
            y = jalury,
            line = dict(color = 'black', width = 2),
            text = name,
            legendgroup="a",
            name = "Jalur",
            showlegend = False
            ))
        else:
            self.fig.add_trace(go.Scatter(
            mode = "lines",
            x = jalurx,
            y = jalury,
            line = dict(color = 'black', width = 2),
            text = name,
            legendgroup="a",
            name = "Jalur"
            ))
        self.count +=1

    def tambahjalurhasil(self, jalurx, jalury, hasil): #tambah jalur hasil
        self.fig.add_trace(go.Scatter(
        mode = "lines+text",
        x = jalurx,
        y = jalury,
        line = dict(color = 'red', width = 4),
        name = "Jalur terdekat",
        text = hasil,
        textposition = "top center",
        textfont=dict(
            family="Arial, sans-serif",
            size=21,
            color="MidnightBlue"
        )
        ))
    def editFig(self):
        self.fig.update_layout(
            autosize=False,
            width=1250,
            height=650,
            margin=dict(
                l=200,
                r=200,
                b=50,
                t=50,
                pad=4
            )
        )

    def addAnimation(self, nodex, nodey, atas,kanan,bawah,kiri, lokasix, lokasiy, nama):
        N = len(nodex)
        self.fig.add_trace(go.Scatter(
            x=lokasix,
            y=lokasiy,
            mode='markers',
            marker= dict(color = 'red', size = 10),
            text = nama,
            name = "Lokasi"
        ))
        self.fig.update_layout(
            xaxis=dict(range=[kiri, kanan], autorange=False, zeroline=False),
            yaxis=dict(range=[bawah, atas], autorange=False, zeroline=False),
            updatemenus=[dict(type="buttons",
                            buttons=[dict(label="Tunjukkan Jalur",
                                            method="animate",
                                            args=[None])])])
        self.fig['frames'] = [go.Frame(
                data=[go.Scatter(
                    x=[nodex[k]],
                    y=[nodey[k]],
                    mode="markers+text",
                    text = "Kurir",
                    textposition="bottom center",
                    marker=dict(color="red", size=14),
                    name = "Kurir",
                    textfont=dict(
                    family="Arial, sans-serif",
                    size=18,
                    color="black"
                )
                    )])

                for k in range(N)]

    def getGraph(self):
        graphJSON = json.dumps(self.fig, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON
    
    def visualize(self, i): #gambar map dengan center simpul awal
        self.fig.update_layout(
        hovermode='closest',
        title = "Jalur Terpendek Kurir untuk Pengiriman ke-"+ str(i+1)
        )
        self.fig.show()



if __name__ == '__main__':
    #Bikin ga bisa cuma titik awal doang
    namalokasi = ["Perusahaan", "Indomaret", "Neraka", "ITB", "Rumah Yahya"]
    koorlokasi = [[-3,-3], [3,4], [12,3], [-5,-7], [6,-3]]
    node_x = []
    node_y = []
    titikawal = koorlokasi[0]
    for i in koorlokasi:
        node_x.append(i[0])
        node_y.append(i[1])
    graf = Graf(node_x,node_y,namalokasi)
    n = len(koorlokasi)
    jaraklokasi = getDistance(koorlokasi)
    res, jalur = solveTSP(jaraklokasi, 0)
    teks, listnamahasil = out(res,jalur,namalokasi)
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
    graf.visualize(0)
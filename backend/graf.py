import json
import plotly
import plotly.graph_objects as go

class Graf:
    def __init__(self,nodex,nodey,nama):
        self.fig = go.Figure(go.Scatter(
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
            name = "Awal"
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
        showlegend=False,
        textfont=dict(
            family="Arial, sans-serif",
            size=21,
            color="MidnightBlue"
        )
        ))
    def editFig(self):
        self.fig.update_layout(
            autosize=False,
            width=1300,
            height=700,
            margin=dict(
                l=200,
                r=200,
                b=50,
                t=50,
                pad=4
            )
        )
    
    def getGraph(self):
        graphJSON = json.dumps(self.fig, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON
    
    def visualize(self): #gambar map dengan center simpul awal
        self.fig.update_layout(
        hovermode='closest',
        title = "Tes"
        )
        self.fig.show()
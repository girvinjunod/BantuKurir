from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px
import plotly.graph_objects as go

import networkx as nx




app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chart1')
def chart1():
    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })

    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
    
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Fruit in North America"
    description = """
    A academic study of the number of apples, oranges and bananas in the cities of
    San Francisco and Montreal would probably not come up with this chart.
    """
    return render_template('graf.html', graphJSON=graphJSON, header=header,description=description)

@app.route('/chart2')
def chart2():
    #node
    node_x = [1,2,3,4,5]
    node_y = [6,7,8,9,10]
    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            # colorscale options
            #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
            #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
            #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
            colorscale='YlGnBu',
            reversescale=True,
            color=[],
            size=10,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line_width=2))


    edge_x = [1,2,3,4,5]
    edge_y = [6,8,10,7,9]
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')

    
    fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    title='<br>Network graph made with Python',
                    titlefont_size=16,
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
    )
    #tes tambah graf ke fig
    fig.add_trace(go.Scatter(
        x = [6,7], y = [3,4],
        line=dict(width=0.5, color='red'),
        hoverinfo='none',
        mode='lines'))

    #oper graf ke html
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Tes Network Graph"
    description = "tes"
    return render_template('graf.html', graphJSON=graphJSON, header=header,description=description)

if __name__ == "__main__":
    app.run(debug = True)
import plotly.graph_objects as go
import numpy as np

labels = 'PNG', 'JPEG', 'SVG', 'GIF', 'Other'
values = [376, 348, 153, 104, 19]
explode = (.1, 0, 0, 0, 0)
wedgeColors=("red","orange","yellow","green","blue")

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.update_traces(
    hoverinfo='label+percent',
    textinfo='value',
    textfont_size=20,
    pull=explode,
    marker=dict(colors=wedgeColors,line=dict(color='black',width=2))
    )
fig.update_layout(
    title_text="Popular Graphic Formats on the Web",
    title_font_size=30, 
    title_xref="paper", 
    title_yref="paper",
    margin_l=200,
    margin_r=200
    )
fig.show()
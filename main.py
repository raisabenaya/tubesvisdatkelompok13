import pandas as pd
import numpy as np

from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import row, column, gridplot


#Read in csv
df = pd.read_csv('C:/Users/PUTRi/Downloads/TubesVisdat/covid.csv')
print(df)

output_file('tubes.html')

#Add plot
p = figure(
    plot_width=500,
    plot_height=700,
    title='Visualisasi Covid-19',
    x_axis_label='Negara',
    y_axis_label='Jumlah',
    tools=""
)

#Multiple Render Glyph
p.line(x='Negara', legend_label="Kematian", color="red", line_width=3)
p.line(x='Negara', legend_label="Kasus Positif", color="green", line_width=3)

#Show results
show(p)
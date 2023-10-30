# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 11:10:30 2023

@author: WS-012
"""

import pandas as pd
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


BDL_eficiencia = pd.read_excel(r"D:\Users\WS-012\Desktop\Modelos_C_R\DEA\Knime_data\4. Eficiencia\BDL_EFICIENCIA.xlsx")
print(BDL_eficiencia.columns)



# Supongamos que tienes la tabla BDL_eficiencia
# (Asegúrate de que los nombres de las columnas coincidan con los utilizados en el código)

# Carga y procesa los datos
# Reemplaza 'tu_archivo.csv' con la ubicación de tu archivo de datos BDL_eficiencia
# BDL_eficiencia = pd.read_csv('tu_archivo.csv')

# Aplica una transformación a los datos para ajustar la posición en el gráfico
BDL_eficiencia['Y_position'] = BDL_eficiencia['Eficiencia']
BDL_eficiencia['X_position'] = BDL_eficiencia['Costo_Materiales'] + BDL_eficiencia['Costo_Medicamentos'] + BDL_eficiencia['Costo_Consultas']

# Ordena los datos por eficiencia y posición en X en orden ascendente
BDL_eficiencia = BDL_eficiencia.sort_values(by=['Eficiencia', 'X_position'])

# Crea el gráfico de dispersión con Plotly
trace = go.Scatter(
    x=BDL_eficiencia['X_position'],
    y=BDL_eficiencia['Y_position'],
    mode='markers',
    text=BDL_eficiencia['DMU'],  # Esto mostrará los nombres de las DMU en el hover
    hoverinfo='text',
    marker=dict(size=12, color=BDL_eficiencia['Eficiencia'], colorscale='Viridis', colorbar=dict(title='Eficiencia'))
)

layout = go.Layout(
    title="Gráfico de Frontera de Eficiencia DEA",
    xaxis=dict(title='Costo (X)'),
    yaxis=dict(title='Eficiencia (Y)')
)

fig = go.Figure(data=[trace], layout=layout)

# Define la aplicación Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Gráfico de Frontera de Eficiencia DEA"),
    dcc.Graph(id='scatter-plot', figure=fig),
    html.Label("Límite en el eje X"),
    dcc.Slider(id='x-limit-slider', min=0, max=1e8, value=100),
    html.Label("Límite en el eje Y"),
    dcc.Slider(id='y-limit-slider', min=0, max=1, value=0.5)
])

@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('x-limit-slider', 'value'),
     Input('y-limit-slider', 'value')]
)
def update_scatter_plot(x_limit, y_limit):
    filtered_data = BDL_eficiencia[(BDL_eficiencia['X_position'] <= x_limit) &
                                   (BDL_eficiencia['Y_position'] <= y_limit)]

    trace = go.Scatter(
        x=filtered_data['X_position'],
        y=filtered_data['Y_position'],
        mode='markers',
        text=filtered_data['DMU'],
        hoverinfo='text',
        marker=dict(size=12, color=filtered_data['Eficiencia'], colorscale='Viridis', colorbar=dict(title='Eficiencia'))
    )

    layout = go.Layout(
        title="Gráfico de Frontera de Eficiencia DEA",
        xaxis=dict(title='Costo (X)'),
        yaxis=dict(title='Eficiencia (Y)')
    )

    updated_fig = go.Figure(data=[trace], layout=layout)

    return updated_fig

if __name__ == '__main__':
    app.run_server(debug=True)

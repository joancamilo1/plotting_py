# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 10:17:15 2023

@author: joan camilo tamayo
"""
import pandas as pd

BDL_eficiencia = pd.read_excel(r"D:\Users\WS-012\Desktop\Modelos_C_R\DEA\Knime_data\4. Eficiencia\BDL_EFICIENCIA.xlsx")
print(BDL_eficiencia.columns)

# Cambiar el nombre de la columna 'Eficiencia' a 'Eficiencia_ENTRADA'
BDL_eficiencia.rename(columns={'Eficiencia': 'Eficiencia_ENTRADA'}, inplace=True)

# Seleccionar las columnas 'Nombre_Prestador', 'Eficiencia' y 'Eficiencia_SALIDA'
tabla_eficiencia = BDL_eficiencia[['Nombre_Prestador', 'Eficiencia_ENTRADA', 'Eficiencia_SALIDA']]
print(tabla_eficiencia)


# ========================= grafico de dispersion ================================ 
import pandas as pd
import seaborn as sns

# Agrupar por el nombre del prestador y sumar las eficiencias
tabla_agrupada = tabla_eficiencia.groupby('Nombre_Prestador').mean().reset_index()

# Crear el gráfico de dispersión con Seaborn
sns.set(style="whitegrid")  # Establecer el estilo del gráfico

# Utilizar relplot para un gráfico de dispersión
scatter_plot = sns.relplot(x="Eficiencia_ENTRADA", y="Eficiencia_SALIDA", data=tabla_agrupada, height=6, aspect=1.5)

# Personalizar el gráfico
scatter_plot.fig.suptitle('Gráfico de Dispersión de Eficiencia media de Entrada vs. Salida por DMU')
scatter_plot.set_axis_labels('Eficiencia media de Entrada', 'Eficiencia media de Salida')

# Mostrar el gráfico
scatter_plot



# ========================= grafico de barras apiladas  ================================ 

import pandas as pd


# Crear un diccionario que mapea las categorías a las columnas correspondientes
categorias = {
    'Medicamentos': ['Objetivo_Costo_Medicamentos', 'Diferencia_Costo_Medicamentos_Radial', 'Costo_Medicamentos'],
    'Materiales': ['Objetivo_Costo_Materiales', 'Diferencia_Costo_Materiales_Radial', 'Costo_Materiales'],
    'Procedimientos': ['Objetivo_Costo_Procedimientos', 'Diferencia_Costo_Procedimientos_Radial', 'Costo_Procedimientos'],
    'Consultas': ['Objetivo_Costo_Consultas', 'Diferencia_Costo_Consultas_Radial', 'Costo_Consultas']
}

# Crear un DataFrame para la tabla solicitada
tabla_resumen = pd.DataFrame(columns=['CATEGORÍA', 'Objetivo', 'Exceso', 'Real'])

for categoria, columnas in categorias.items():
    # Sumar las columnas correspondientes
    objetivo = int(BDL_eficiencia[columnas[0]].sum())
    exceso = int(abs(BDL_eficiencia[columnas[1]].sum()))
    real = int(BDL_eficiencia[columnas[2]].sum())
    
    # Agregar una fila al DataFrame
    tabla_resumen = tabla_resumen.append({'CATEGORÍA': categoria, 'Objetivo': objetivo, 'Exceso': exceso, 'Real': real}, ignore_index=True)

# Mostrar la tabla
print(tabla_resumen)


import seaborn as sns
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

# Crear un gráfico de barras con Seaborn
sns.set(style="whitegrid")  # Establecer el estilo del gráfico

# Crear un gráfico de barras utilizando la tabla_resumen
bar_plot = sns.barplot(x="Real", y="CATEGORÍA", data=tabla_resumen, color="blue", label="Real")
sns.barplot(x="Objetivo", y="CATEGORÍA", data=tabla_resumen, color="orange", label="Objetivo")

# Personalizar el gráfico
bar_plot.set(xlabel="Costo", ylabel="Categoría")
bar_plot.set_title("Costo Real vs. Objetivo por Categoría")
bar_plot.legend(title="Costo")

# Crear una figura de Plotly
fig = go.Figure(data=bar_plot)

# Mostrar el gráfico utilizando Plotly
pyo.iplot(fig)


#------------------------ egresos ---------------

# Supongamos que ya tienes el DataFrame BDL_eficiencia
# Si no lo tienes, asegúrate de cargar los datos antes de ejecutar este código

# Calcular la suma de Egresos y Objetivo_Egresos
suma_egresos = BDL_eficiencia['Egresos'].sum()
suma_objetivo_egresos = BDL_eficiencia['Objetivo_Egresos'].sum()

# Crear la tabla resumen
tabla_resumen_egresos = pd.DataFrame({
    'CATEGORÍA': ['Egresos'],
    'Egresos_Reales': [int(suma_egresos)],
    'Objetivo_Egresos': [int(suma_objetivo_egresos)]
})

# Mostrar la tabla resumen
print(tabla_resumen_egresos)



##################### prueba en matplot lib #################################
import matplotlib.pyplot as plt

# Supongamos que tienes la tabla_resumen_egresos generada

# Crear un gráfico de barras con Matplotlib
fig, ax = plt.subplots()
width = 0.35  # Ancho de las barras

categorias = tabla_resumen_egresos['CATEGORÍA']
egresos_reales = tabla_resumen_egresos['Egresos_Reales']
objetivo_egresos = tabla_resumen_egresos['Objetivo_Egresos']

x = range(len(categorias))

plt.bar(x, egresos_reales, width, label='Egresos Reales', color='blue')
plt.bar([i + width for i in x], objetivo_egresos, width, label='Objetivo Egresos', color='orange')

ax.set_xlabel('Categoría')
ax.set_ylabel('Pacientes')
ax.set_title('Comparación de Egresos Reales vs. Objetivo Egresos')
ax.set_xticks([i + width / 2 for i in x])
ax.set_xticklabels(categorias)
ax.legend()

plt.show()

# ================================== real ========================= 
import seaborn as sns
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

# Supongamos que tienes la tabla_resumen_egresos generada

# Crear un gráfico de barras con Seaborn
sns.set(style="whitegrid")  # Establecer el estilo del gráfico

# Crear un gráfico de barras utilizando la tabla_resumen
bar_plot = sns.barplot(x="Objetivo_Egresos", y="CATEGORÍA", data=tabla_resumen_egresos, color="blue", label="Objetivo_Egresos")
sns.barplot(x="Egresos_Reales", y="CATEGORÍA", data=tabla_resumen_egresos, color="orange", label="Egresos_Reales")

# Personalizar el gráfico
bar_plot.set(xlabel="Pacientes", ylabel=" ")
bar_plot.set_title("Egresos Reales vs. Objetivo por Categoría")
bar_plot.legend(title="Pacientes")

# Obtener la figura de Plotly
fig = bar_plot.get_figure()

# Mostrar la gráfica utilizando Plotly
pyo.iplot(fig)






===================================  pruebassssss ====================================================
 
 
import seaborn as sns
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

# Supongamos que tienes la tabla_resumen_egresos generada

# Asegúrate de que la columna "Egresos_Reales" sea de tipo numérico (int)
tabla_resumen_egresos["Egresos_Reales"] = tabla_resumen_egresos["Egresos_Reales"].astype(int)

# Crear un gráfico de barras con Seaborn
sns.set(style="whitegrid")  # Establecer el estilo del gráfico

# Crear un gráfico de barras utilizando la tabla_resumen
bar_plot = sns.barplot(x="Objetivo_Egresos", y="CATEGORÍA", data=tabla_resumen_egresos, color="blue", label="Objetivo_Egresos")
sns.barplot(x="Egresos_Reales", y="CATEGORÍA", data=tabla_resumen_egresos, color="orange", label="Egresos_Reales")

# Personalizar el gráfico
bar_plot.set(xlabel="Pacientes", ylabel=" ")
bar_plot.set_title("Egresos Reales vs. Objetivo por Categoría")
bar_plot.legend(title="Pacientes")

# Obtener la figura de Plotly
fig = bar_plot.get_figure()

# Agregar etiquetas con el valor real al final de las barras
for patch in bar_plot.patches:
    width = patch.get_width()
    label_x = width
    label_y = patch.get_y() + patch.get_height() / 2
    real_value = int(str([tabla_resumen_egresos.loc[tabla_resumen_egresos['CATEGORÍA'] == patch.get_y(), 'Egresos_Reales']]))
    bar_plot.text(
        label_x, label_y, real_value,
        ha='left', va='center', fontsize=10, color='black'
    )

# Mostrar la gráfica utilizando Plotly
pyo.iplot(fig)





#  ======================= DEA plot ========================================
import pandas as pd
import matplotlib.pyplot as plt

# Supongamos que tienes un DataFrame llamado BDL_eficiencia con una columna "Eficiencia"
# Calcula la eficiencia relativa en tu DataFrame después de realizar el DEA

# Clasifica las unidades por eficiencia de mayor a menor
BDL_eficiencia = BDL_eficiencia.sort_values(by="Eficiencia_ENTRADA", ascending=False)

# Crea un gráfico de dispersión con los números de unidad en el eje x y la eficiencia en el eje y
plt.figure(figsize=(10, 6))
plt.scatter(range(1, len(BDL_eficiencia) + 1), BDL_eficiencia["Eficiencia_ENTRADA"], label="Eficiencia_ENTRADA")

# Dibuja una línea horizontal en la "frontera eficiente"
plt.axhline(y=BDL_eficiencia.iloc[0]["Eficiencia_ENTRADA"], color="red", linestyle="--", label="Frontera Eficiente")

plt.xlabel("Número de Unidad")
plt.ylabel("Eficiencia")
plt.title("Gráfico de la Frontera Eficiente")
plt.legend()
plt.show()



import seaborn as sns
import pandas as pd
import plotly.express as px

# Supongamos que tienes la tabla BDL_eficiencia

# Filtra las observaciones eficientes (puedes usar tu propio criterio de eficiencia)
observaciones_eficientes = BDL_eficiencia[BDL_eficiencia['Eficiencia_ENTRADA'] == 1]

# Crea un gráfico de dispersión con Plotly Express
fig = px.scatter(BDL_eficiencia, x='Costo_Medicamentos', y='Egresos', title='Frontera Eficiente')

# Personaliza el gráfico
fig.update_traces(marker=dict(size=8, color='blue', opacity=0.5), selector=dict(mode='markers'), name='Ineficiente')

# Agrega las observaciones eficientes al gráfico
fig.add_trace(go.Scatter(
    x=observaciones_eficientes['Costo_Medicamentos'],
    y=observaciones_eficientes['Egresos'],
    mode='markers',
    marker=dict(size=8, color='red', opacity=0.7),
    name='Eficiente'
))

# Muestra el gráfico
fig.show()





import matplotlib.pyplot as plt
import seaborn as sns

# Supongamos que tienes la tabla BDL_eficiencia

# Filtra las observaciones eficientes (puedes usar tu propio criterio de eficiencia)
observaciones_eficientes = BDL_eficiencia[BDL_eficiencia['Eficiencia_ENTRADA'] == 1]

# Crea un gráfico de dispersión con Matplotlib
plt.figure(figsize=(10, 6))

# Grafica las observaciones ineficientes
plt.scatter(BDL_eficiencia[BDL_eficiencia['Eficiencia_ENTRADA'] != 1]['Costo_Medicamentos'],
            BDL_eficiencia[BDL_eficiencia['Eficiencia_ENTRADA'] != 1]['Egresos'],
            c='blue', label='Ineficiente', alpha=0.5)

# Grafica las observaciones eficientes
plt.scatter(observaciones_eficientes['Costo_Medicamentos'],
            observaciones_eficientes['Egresos'],
            c='red', label='Eficiente', alpha=0.7)

# Personaliza el gráfico
plt.title('Frontera Eficiente')
plt.xlabel('Costo de Medicamentos')
plt.ylabel('Egresos')
plt.legend()
plt.grid(True)

# Muestra el gráfico
plt.show()


import plotly.express as px

# Supongamos que tienes la tabla BDL_eficiencia

# Filtra las observaciones eficientes (puedes usar tu propio criterio de eficiencia)
observaciones_eficientes = BDL_eficiencia[BDL_eficiencia['Eficiencia'] == 1]

# Crea un gráfico de dispersión interactivo con Plotly Express
fig = px.scatter(observaciones_eficientes, x='Costo_Medicamentos', y='Egresos',
                 title='Frontera Eficiente', color_discrete_sequence=['red'])

# Personaliza el gráfico
fig.update_layout(
    xaxis_title='Costo de Medicamentos',
    yaxis_title='Egresos'
)

# Muestra el gráfico interactivo
fig.show()










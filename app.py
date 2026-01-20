import pandas as pd
import streamlit as st
import plotly.express as px

# Leer el dataset
car_data = pd.read_csv("vehicles_us.csv")

# Encabezado de la aplicación
st.title("Análisis Exploratorio de Datos de Vehículos")

# Crear un botón para la generación del histograma
if st.button('Histograma de Año del Modelo'):
    # Crear un histograma de la columna 'year_model' o, si no existe, de la primera columna
    if 'model_year' in car_data.columns:
        fig_hist = px.histogram(car_data, x='model_year',
                                title='Histograma de Año del Modelo')
    else:
        fig_hist = px.histogram(
            car_data, x=car_data.columns[0], title=f'Histograma de {car_data.columns[0]}')
    st.plotly_chart(fig_hist, use_container_width=True)


# Crear un botón para el gráfico de dispersión
if st.button('Gráfico de Dispersión "Año vs Odómetro"'):
    # Crear un gráfico de dispersión (scatter plot) entre 'odometer' y 'model_year' si existen, y si no, expresarlo
    if 'odometer' in car_data.columns and 'model_year' in car_data.columns:
        fig_scatter = px.scatter(car_data, x='model_year',
                                 y='odometer', title='Año vs Odómetro')
        st.plotly_chart(fig_scatter, use_container_width=True)
    else:
        st.write(
            "No se encontraron las columnas 'odometer' y 'price' para crear el scatter plot.")

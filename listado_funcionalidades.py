#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 18:03:55 2024

@author: danielleon
"""

# Importe de librería
import streamlit as st

# Web app básica
# Slider agrega un selector
x = st.slider("Select a value")

# Se escribe en pantalla el valor seleccionado en el slider y se eleva al cuadrado
st.write(x, "squared is", x * x)


# Tipos de escritura
st.title("this is the app title")
st.markdown("this is the markdown")
st.header("this is the header")
st.subheader("this is the subheader")
st.code("x = 2021")
st.latex('a+a r^1+a r^2+a r^3')


# Añadir imágenes y audios
st.subheader('Imagen')
st.image(r'https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/658.png')

st.subheader('Audio')
st.audio(r'/Users/danielleon/Downloads/bienvenue-193104.mp3')


# Opción de selección de información
st.subheader('Opciones de selección de información')
st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)


# Opciones de ingreso de información (inputs)
st.subheader('Opciones de ingreso de información')
st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

# Agregar funcionalidades como barra lateral
st.sidebar.radio('Pick a option',['Male','Female'])

# Opciones de visualización
import pandas as pd
import numpy as np

st.subheader('Opciones de visualización')
df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.line_chart(df)
st.bar_chart(df)

# Mapa
st.subheader('Mapa')
df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])
st.map(df)

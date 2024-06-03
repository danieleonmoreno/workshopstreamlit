#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 18:19:04 2024

@author: danielleon
"""

# Importe de librería
import streamlit as st

# Web app básica
# Slider agrega un selector
x = st.slider("Select a value")

# Se escribe en pantalla el valor seleccionado en el slider y se eleva al cuadrado
st.write(x, "squared is", x * x)

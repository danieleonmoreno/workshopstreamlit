#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 17:53:12 2024

@author: danielleon
"""

import streamlit as st
import pandas as pd
import math

st.title("Calculadora de Pagos de Hipoteca")

st.write("### Datos de Entrada")
col1, col2 = st.columns(2)

valor_vivienda = col1.number_input("Valor de la Vivienda", min_value=0, value=500000)
deposito = col1.number_input("Depósito", min_value=0, value=100000)

tasa_interes = col2.number_input("Tasa de Interés (en %)", min_value=0.0, value=5.5)
plazo_prestamo = col2.number_input("Plazo del Préstamo (en años)", min_value=1, value=30)

# Calcular los pagos.
monto_prestamo = valor_vivienda - deposito
tasa_interes_mensual = (tasa_interes / 100) / 12
numero_pagos = plazo_prestamo * 12
pago_mensual = (
    monto_prestamo
    * (tasa_interes_mensual * (1 + tasa_interes_mensual) ** numero_pagos)
    / ((1 + tasa_interes_mensual) ** numero_pagos - 1)
)

# Mostrar los pagos.
pagos_totales = pago_mensual * numero_pagos
interes_total = pagos_totales - monto_prestamo

st.write("### Pagos")
col1, col2, col3 = st.columns(3)
col1.metric(label="Pagos Mensuales", value=f"${pago_mensual:,.2f}")
col2.metric(label="Pagos Totales", value=f"${pagos_totales:,.0f}")
col3.metric(label="Interés Total", value=f"${interes_total:,.0f}")

# Crear un dataframe con el calendario de pagos.
calendario = []
saldo_restante = monto_prestamo

for i in range(1, numero_pagos + 1):
    pago_interes = saldo_restante * tasa_interes_mensual
    pago_capital = pago_mensual - pago_interes
    saldo_restante -= pago_capital
    año = math.ceil(i / 12)  # Calcular el año dentro del préstamo
    calendario.append(
        [
            i,
            pago_mensual,
            pago_capital,
            pago_interes,
            saldo_restante,
            año,
        ]
    )

df = pd.DataFrame(
    calendario,
    columns=["Mes", "Pago", "Capital", "Interés", "Saldo Restante", "Año"],
)

# Mostrar el dataframe como un gráfico.
st.write("### Calendario de Pagos")
pagos_df = df[["Año", "Saldo Restante"]].groupby("Año").min()
st.line_chart(pagos_df)

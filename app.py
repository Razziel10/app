import streamlit as st

st.set_page_config(page_title="Calculadora de Precios Finales", page_icon="💸")

st.title("🛍️ Calculadora de Precio Final")

# Entradas del usuario
precio_unitario = st.number_input("Precio del producto ($)", min_value=0.0, format="%.2f")
cantidad = st.number_input("Cantidad", min_value=1, step=1)

promo = st.selectbox("Promoción", ["Sin descuento", "2x1"])
metodo_pago = st.radio("¿Pagás con transferencia?", ["Sí", "No"])
envio = st.number_input("Costo del envío ($)", min_value=0.0, format="%.2f")

# Cálculo del precio final
if st.button("Calcular"):
    total = precio_unitario * cantidad

    if promo == "2x1":
        total = precio_unitario * ((cantidad + 1) // 2)

    if metodo_pago == "Sí":
        total *= 0.8

    total += envio
    total = round(total, 2)

    st.success(f"💸 El precio final es: ${total}")

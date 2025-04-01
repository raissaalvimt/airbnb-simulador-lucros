import streamlit as st

st.set_page_config(page_title="Simulador de Lucros Airbnb", layout="centered")

st.title("Simulador de Lucros para Airbnb")

st.markdown("""
Este simulador ajuda a estimar os lucros de uma locação de imóvel via Airbnb com base na taxa de ocupação, valor da diária, comissões e taxas da plataforma.
""")

# Entradas do usuário
st.sidebar.header("Parâmetros da Simulação")
dias_mes = st.sidebar.number_input("Dias no mês", min_value=28, max_value=31, value=31)
ocupacao_percent = st.sidebar.slider("Ocupação (%)", 0, 100, 85)
diaria = st.sidebar.number_input("Valor da diária (R$)", min_value=50.0, value=247.0, step=10.0)
taxa_limpeza = st.sidebar.number_input("Taxa de limpeza por reserva (R$)", value=100.0)
taxa_airbnb_percent = st.sidebar.slider("Taxa do Airbnb (%)", 0.0, 30.0, 3.0, step=0.5)
comissao_gerente_percent = st.sidebar.slider("Comissão do gerente (%)", 0.0, 50.0, 20.0, step=1.0)

# Cálculos
dias_ocupados = dias_mes * (ocupacao_percent / 100)
reservas_est = round(dias_ocupados / 3)
receita_bruta = diaria * dias_ocupados
taxa_airbnb = receita_bruta * (taxa_airbnb_percent / 100)
receita_com_limpeza = receita_bruta + (reservas_est * taxa_limpeza)
lucro_liquido = receita_com_limpeza - taxa_airbnb
comissao_gerente = lucro_liquido * (comissao_gerente_percent / 100)
lucro_dono = lucro_liquido - comissao_gerente

# Resultados
st.header("Resultados da Simulação")
st.markdown(f"**Dias ocupados:** {dias_ocupados:.1f} dias")
st.markdown(f"**Receita bruta:** R$ {receita_bruta:,.2f}")
st.markdown(f"**Taxa do Airbnb:** R$ {taxa_airbnb:,.2f}")
st.markdown(f"**Taxas de limpeza (estimadas):** R$ {reservas_est * taxa_limpeza:,.2f}")
st.markdown(f"**Receita total com limpeza:** R$ {receita_com_limpeza:,.2f}")
st.markdown(f"**Lucro líquido:** R$ {lucro_liquido:,.2f}")
st.markdown(f"**Comissão do gerente:** R$ {comissao_gerente:,.2f}")
st.markdown(f"**Lucro final do proprietário:** R$ {lucro_dono:,.2f}")

st.info("Você pode ajustar os parâmetros à esquerda para simular diferentes cenários.")


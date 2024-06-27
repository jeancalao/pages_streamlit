import streamlit as st
import pandas as pd
from time import sleep

st.set_page_config(page_title='Minha Pagina',
                page_icon="🧊",
                layout="centered",
                initial_sidebar_state="expanded",
                menu_items={
                    'Get Help': 'https://www.extremelycoolapp.com/help',
                    'Report a bug': "https://www.extremelycoolapp.com/bug",
                    'About': "# This is a header. This is an *extremely* cool app!"})
    
with st.container():
    st.subheader("Meu primeiro site com streamlit")
    st.title("Dashboard de Contratos")
    st.write("informações sobre os contratos")
    st.write("Quer aprender Python? [Clique Aqui](http://python.org)")

@st.cache_data
def carregar_dados():
    tabela = pd.read_csv('contratos.csv',sep=";")
    return tabela

with st.container(border=True):
    st.write("---")
    #busca referencia na streamlit docs
    #grafico de área
    dados = carregar_dados()
    qtde_dias = st.selectbox("selecione o periodo",['7d','15d','21d'])
    qtde_dias = int(qtde_dias.replace('d',''))
    st.line_chart(dados[-qtde_dias:], x="Data", y="Numero")
    st.table(dados[-qtde_dias:])

with st.container(border=True):
    w_base = pd.read_sql_table('Cotacoes',"sqlite:///projeto2.db")
    st.write("---")
    st.caption(":red[**Tabela de Cotações**] :dollar:")
    st.table(w_base)
    #st.error('This is an error', icon="🚨")
    st.success('This is a success message!', icon="✅")
    with st.spinner('Aguarde ...'):
        sleep(5)
    st.success('Pronto!', icon="✅")

with st.container():
    def cook_breakfast():
        msg = st.toast('Misturando os ingredientes ...')
        sleep(1)
        msg.toast('Cozinhando...')
        sleep(1)
        msg.toast('Pronto !', icon = "🥞")

    if st.button('Preparar Almoço!'):
        cook_breakfast()
        st.balloons()
        st.snow()
    
    st.help(st.area_chart)
    st.help(pd.array)
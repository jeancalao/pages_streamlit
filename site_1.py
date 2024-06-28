import streamlit as st
import pandas as pd
from time import sleep

st.set_page_config(page_title='Página de Teste',
                page_icon="🧊",
                layout="centered",
                initial_sidebar_state="expanded",
                menu_items={
                    'Get Help': 'https://www.extremelycoolapp.com/help',
                    'Report a bug': "https://www.extremelycoolapp.com/bug",
                    'About': "# This is a header. This is an *extremely* cool app!"})
    
with st.container():
    st.subheader("Site em Python utilizando Streamlite")
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
    st.caption(":blue[**Tabela de Contratos**] :dollar: utilizando arquivo .CSV")
    dados = carregar_dados()
    qtde_dias = st.selectbox("selecione o periodo",['7d','15d','21d'])
    qtde_dias = int(qtde_dias.replace('d',''))
    st.line_chart(dados[-qtde_dias:], x="Data", y="Numero")
    st.table(dados[-qtde_dias:])

with st.container(border=True):
    w_base = pd.read_sql_table('Cotacoes',"sqlite:///projeto2.db")
    st.write("---")
    st.caption(":red[**Tabela de Cotações**] :dollar: utilizando BD SQLLite")
    st.bar_chart(w_base, x="acao", y="cotacao")
    st.table(w_base)
    #st.error('This is an error', icon="🚨")
    #st.success('This is a success message!', icon="✅")
    # with st.spinner('Aguarde ...'):
    #     sleep(5)
    

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
    
    #st.help(st.area_chart)
    #st.help(pd.array)

with st.container(border=True):
    dados = pd.read_excel('clientes.xlsx')
    st.write('---')
    st.caption(":red[**Tabela de Clientes**] :dollar: utilizando Excel")
    st.area_chart(dados, x="Cliente", y="Valor")
    st.table(dados)

st.success('Pronto!', icon="✅")
on = st.toggle("Demonstrar dependências")

if on:
    st.write("**Necessário efetuar Deploy das seguintes bibliotecas:**")
    st.write("SQLSchema - para efetuar a leitura da base de dados SQLLite")
    st.write("openpyxl - para abrir o arquivo Excel")
    st.write("Efetuar deploy também dos arquivos Excel, do banco SQLLite e do arquivo .CSV")
    st.write("devem estar definidas no arquivo requirements.txt do deploy github")
#Importando as bibliotecas 
import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

#Configurando página streamlit
st.set_page_config(page_title = 'Visão', layout='wide')

#Carregando arquivos (csv)
df1 = pd.read_csv('train_transformado.csv')

#Quantidade de entregadores únicos
qtd_entregadores = df1['Delivery_person_ID'].nunique()

#Distância média dos restaurantes para locais de entrega
distancia_media = round(df1['distance_km'].mean(),2)

#Distância média por festival
cols = ['Time_taken(min)', 'Festival']
df_aux = df1.loc[:, cols].groupby('Festival').agg({'Time_taken(min)': ['mean', 'std']}).round(decimals = 2)
df_aux.columns = ['avg_time', 'std_time']
df_aux = df_aux.reset_index()

#Distância média por região
distancia_media_regiao = df1[['City', 'distance_km']].groupby('City').agg({'distance_km': ['mean', 'std']}).reset_index().round(decimals = 2)
distancia_media_regiao.columns = ['City', 'mean', 'std']

#Tempo médio de entrega por região
tempo_medio_regiao = df1[['City', 'Time_taken(min)']].groupby('City').agg({'Time_taken(min)': ['mean', 'std']}).reset_index().round(decimals = 2)
tempo_medio_regiao.columns = ['City', 'mean', 'std']

#Tempo médio e desvio padrão por região e tipo de tráfego
cols2 = ['City', 'Time_taken(min)', 'Road_traffic_density']
tempo_medio_trafego = df1.loc[:, cols2].groupby(['City', 'Road_traffic_density']).agg({'Time_taken(min)': ['mean', 'std']}).reset_index()
tempo_medio_trafego.columns = ['City', 'Road_traffic_density', 'avg_time', 'std_time']

#==================================================
#LAYOUT - PÁGINA PRINCIPAL
#==================================================
st.title('Projeto de Ciência de Dados')
st.markdown('---------------------------')

tab1, tab2, tab3 = st.tabs(['DataFrame', 'Vendas', 'Restaurantes'])

with tab1:

    st.text('DataFrame com dados transformados')
    st.dataframe(df1)

    st.dataframe(df_aux)

    st.dataframe(distancia_media_regiao)

    st.dataframe(tempo_medio_trafego)
 
with tab2:

    with st.container():
        st.text('Visão das vendas da companhia')

with tab3:

    st.text('Visão dos restaurantes')
    
    with st.container():

        st.markdown('## Overal Metrics')

        col1, col2, col3, col4, col5, col6 = st.columns(6)

        with col1:

            col1.metric('Entregadores únicos', qtd_entregadores)
        
        with col2:

            col2.metric('Distância média', f'{distancia_media} km')

        with col3:

            tempo_medio_festival = df_aux.loc[df_aux['Festival'] == 'Yes', 'avg_time']
            col3.metric('Tempo Festival', tempo_medio_festival)

        with col4:

            desvio_festival = df_aux.loc[df_aux['Festival'] == 'Yes', 'std_time']
            col4.metric('Desvio Padrão', desvio_festival)
        
        with col5:

            tempo_medio_sem_festival = df_aux.loc[df_aux['Festival'] == 'No', 'avg_time']
            col5.metric('Tempo normal', tempo_medio_sem_festival)

        with col6:

            desvio_normal = df_aux.loc[df_aux['Festival'] == 'No', 'std_time']
            col6.metric('Desvio Padrão', desvio_normal)
        
        st.markdown('--------------------')
    
    with st.container():

        st.title('Distância Média de entrega por região')
        fig = go.Figure(data = [go.Pie(labels = distancia_media_regiao['City'], values = distancia_media_regiao['mean'], pull = [0, 0.05, 0])])
        st.plotly_chart(fig)

    with st.container():

        st.title('Distribuição do tempo')

        col1, col2  = st.columns(2)

        with col1:

            fig = go.Figure()
            fig.add_trace(go.Bar(name = 'Control', x = tempo_medio_regiao['City'], y = tempo_medio_regiao['mean'], error_y = dict(type = 'data', array = tempo_medio_regiao['std'])))
            fig.update_layout(barmode='group')
            st.plotly_chart(fig)
        
        with col2:

            fig = px.sunburst(tempo_medio_trafego, path = ['City', 'Road_traffic_density'], values = 'avg_time', color = 'std_time', color_continuous_scale = 'RdBu', color_continuous_midpoint = np.average(tempo_medio_trafego['std_time']))
            st.plotly_chart(fig)

    with st.container():

        st.title('Distribuição da distância')
                    


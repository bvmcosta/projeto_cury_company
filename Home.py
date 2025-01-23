import streamlit as st
from PIL import Image

st.set_page_config(page_title = 'Home') #, page_icon = '')

#st.title('Projeto de Ciência de Dados')
st.sidebar.markdown('# Cury Company')
st.sidebar.markdown('## Fastest Delivery Company')
st.sidebar.markdown('---------------------------')


st.write('## Cury Company Growth Dashboard')
st.write("""
         Growth Dashboard foi construído para acompanhar as métricas de crescimento dos restaurantes 
         cadastrados na plataforma da Cury Company.

         ### Como utilizar o dashboard?
         - Visão Empresa:
            - Visão Gerencial: métricas gerais de comportamento
            - Visão Tática: indicadores semanais de crescimento
            - Visão Geográfica: insights de geolocalização
         - Visão Entregador:
            - Acompanhamento dos indicadores semanas de crescimento
         -Visão Restaurante:
            - Indicadores semanais de crescimento dos restaurantes
         
         #### Informações:
            - Time de data science no discord
            - @meigarom
         """)
#O caminho absoluto precisa ser removido antes de carregar o arquivo na Cloud
#image_path1 = 'C:/Users/Bruno/repos/matricula_2024/3_FTC/projeto_food_delivery/logo.png'
#image_path2 = 'C:/Users/Bruno/repos/matricula_2024/3_FTC/projeto_food_delivery/logo2.jpg'

image1 = Image.open('logo.png')
image2 = Image.open('logo2.jpg')
st.image(image1, width = 300)
st.image(image2, width = 300)





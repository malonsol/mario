
# Importación de los módulos necesarios:
import numpy as np
import pandas as pd
import json
import streamlit as st
import altair as alt

# Declaración de rutas para lectura/escritura de archivos:
compartido_windows = "C:/Users/turge/CompartidoVM/Python_HostMachine_Windows"
csv_path = compartido_windows + '/Exercise_2_result_df_withdup.csv'
json_path = compartido_windows + '/Exercise_5_json.json'


######## Comienzo del diseño del Web Service ########   

# Encabezados iniciales:
st.title('Exercise 5 - Web Service')
st.subheader('This is a Web Service which returns the data from Exercise 2 in a JSON format.')
# Botón de testeo:
if st.button('WELCOME!'):
    st.write('Welcome to this Web App!')
else:
    st.write('Are you ready?')
# Mostrar resultados:    
st.markdown("""
### This is the data resulting from Exercise 2:
""")

x = st.slider(label='Select the number or airports you want to see:',
              min_value=1,
              max_value=100, # En realidad, habría hasta 2275 aeropuertos, pero para mejor visualización
              value=11,
              step=10)
st.text('You have selected {} airports.'.format(x-1))

if x > 0:
    # Preparación de datos para el Web Service:
    df = pd.read_csv(csv_path, delimiter='^', nrows=x)
    df_json = json.dumps(df.to_dict()) # volcado del DataFrame en un formato JSON
    st.json(df_json)
    # Generación del gráfico de barras horizontal:    
    bars_h = alt.Chart(df).mark_bar().encode(
        x='pax:Q',
        y=alt.Y('arr_port:N', sort='-x')
    ).properties(
        # width=300,
        # height=150,
        title='Pax vs Arrival_Airport'
    ).interactive()
    # Generación del gráfico de barras vertical:    
    bars_v = alt.Chart(df).mark_bar().encode(
        x=alt.X('arr_port:N', sort='-x'),
        y=alt.Y('pax:Q')
    ).properties(
        # width=300,
        # height=150,
        title='Pax vs Arrival_Airport'
    ).interactive()
    # Checkbox: mostrar/ocultar gráfico
    st.markdown("""
    #### Do you want to visualize the data in a graphical way?
    """)
    graph = st.checkbox(label ='Show graph', value=False)
    if graph:
        st.markdown("""
        ### Below is presented such data in a graphical mode:
        """)
        # Radio button: gráfico horizontal/vertical
        bar_type = st.radio(label="Select the type of graph:",
                            options=['Horizontal', 'Vertical'],
                            index=0)
        if bar_type == 'Horizontal':
            st.write(bars_h)
        elif bar_type == 'Vertical':
            st.write(bars_v)
        # st.balloons() # Chorrada graciosa
    else:
        st.text("(Nothing to show)")

######## Fin del diseño del Web Service ########

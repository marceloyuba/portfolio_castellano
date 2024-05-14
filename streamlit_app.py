

import streamlit as st
from streamlit.hello.utils import show_code

st.set_page_config(page_title="Portfolio Marcelo Yuba", page_icon="scr/banner.png", layout="wide")
           
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")
with st.container():      
    st.markdown('<style>h5{color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>h4{color: white;}, font=</style>', unsafe_allow_html=True)    
    st.markdown('<style>h3 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>h2 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>h1 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>write {color: white;}, font=</style>', unsafe_allow_html=True)    
    
column_widths = [1, 3, 1]
with st.container():
    
    col1, col2, col3 = st.columns(column_widths)   
    with col1:
        st.empty()
        
    with col3:
        st.title("")
          
    with col2: 
        st.image("scr/banner.png",width=1200, use_column_width=True, output_format='auto')

st.title("") 
        
# ---- HEADER SECTION ----
with st.container():        
    st.header("Hola, soy Marcelo Yuba :wave:")
    st.title("Un Data Analyst  y Data Scientist de Buenos Aires, Argentina")
    st.markdown("""
        #### Apasionado en el analisis de datos usando, Power BI y Python, tratando de forma mas eficiente,  obtener resultados para tu negocio o empresa.
    """)
   
    st.write('<div class="botones"><a href="https://www.linkedin.com/in/marcelo-yuba-b9a39827b/">Mi Linkedin</a>', unsafe_allow_html=True)
    st.write('<div class="botones"><a href="https://github.com/marceloyuba">Mi Github</a>', unsafe_allow_html=True)
        


column_widths = [2, 1] 

with st.container():    
    st.title("Que es lo que hago")    
    col1, col2 = st.columns(column_widths)
   
    with col1:
        st.markdown("### Utilizando diferentes tecnologias, me permiten hacer analisis de datos, Dashboards interactivos"
                     )
        st.markdown(
            """            
            ##### Como analista de datos, tengo un papel crucial en la interpretación y análisis de conjuntos de datos para extraer información significativa y tomar decisiones fundamentadas:
            ##### - Comprensión del problema o pregunta: Antes de empezar cualquier análisis, es importante entender claramente cuál es el problema que estoy tratando de resolver o la pregunta que estoy tratando de responder.
            ##### - Recopilación de datos: Reunir todos los datos relevantes para el análisis. Estos datos pueden provenir de diversas fuentes, como bases de datos, hojas de cálculo, archivos CSV, APIs.
            ##### - Limpieza de datos: Los datos crudos rara vez están en una forma lista para el análisis. A menudo necesitan ser limpiados y preprocesados para eliminar valores atípicos, valores faltantes, errores de entrada, etc.
            ##### - Análisis exploratorio de datos (EDA): Este paso implica explorar los datos para comprender mejor sus características. Esto puede incluir la generación de estadísticas descriptivas, la visualización de datos y la identificación de patrones o relaciones.
            ##### - Toma de decisiones basada en datos: Utilizar los insights obtenidos del análisis para ayudar en la toma de decisiones. Esto podría implicar recomendaciones para acciones específicas o ajustes en estrategias existentes.
            
            """
        )
        st.markdown("""
                    #### Para lograr los objetivos necesarios, hago uso de estas tecnologias, tanto para analisis de dato como dieño de dashoards
                    """)
   
    with col2:
        imagen = "scr/tec.png" 
        st.image(imagen, width=400)
            
st.write("""
<style>
    .botones a {
        font-size: 30px;
        margin-top: 10px; /* Espacio después de la imagen */
        text-decoration: none; /* Quitar el subrayado */
        color: #ffffff; /* Cambiar el color del texto del enlace */
        
    }
</style>
""", unsafe_allow_html=True)  

st.title("Mis proyectos")     
st.write("<hr style='border-top: 3px solid white;'>", unsafe_allow_html=True)    
column_widths = [2, 1]
with st.container():
     
    col1, col2 = st.columns(column_widths)   
    
    with col1:
        st.header("Greyhound NYC Insercion de mercado")
        st.markdown(""" 
                #### Proyecto de analisis de insercion de mercado al sistema de vehiculos con chofer para la ciudad de NYC, se analizaron tanto los factores economicos como ambientales para tomar desiciones de si invertir o no en este negocio, tomando en cuenta varias hipotesis y llegando a sus respectivas conclusiones
                # """) 
                
        st.write('<div class="botones"><a href="https://greyhound.streamlit.app/">Acceder a la App</a>', unsafe_allow_html=True)
        st.write('<div class="botones"><a href="https://github.com/marceloyuba/SDT">Acceder a la documentacion</a>', unsafe_allow_html=True)
        
    with col2:
        imagen = "scr/grey.png"  
        st.image(imagen, width=500, use_column_width=True, output_format='auto')        

st.write("<hr style='border-top: 1px solid grey;'>", unsafe_allow_html=True)    

with st.container():
    col1, col2 = st.columns(column_widths)
    
    with col1:
        st.header("Accidentes Viales en la Ciudad de Buenos Aires")        
        st.markdown("""
                #### Desde la expansión en 2021, Nuestro cliente analiza nuevos mercados fuera del transporte de buses, por eso nos encomendó analizar la inserción al negocio de los viajes en automóviles, analizando a su competidores directos (Taxis, Uber, Lyft) y comenzando por la ciudad de Nueva York, ya que la misma tiene una de las redes mas complejas de transporte en todo el pais, nuestro trabajo es analizar si es viable el ingreso al sistema cumpliendo con las regulaciones impuestas por el gobierno respecto a tener una ciudad libre de emisiones contaminantes""") 
        st.write('<div class="botones"><a href="https://accidentesbuenosaires.streamlit.app/">Acceder a la App</a>', unsafe_allow_html=True)
        st.write('<div class="botones"><a href="https://github.com/marceloyuba/Proyecto_individual_Data_Analyst">Acceder a la documentacion</a>', unsafe_allow_html=True)
    
    with col2:
        imagen = "scr/BA.png"  
        st.image(imagen, width=500, use_column_width=True, output_format='auto')
    
    
st.write("<hr style='border-top: 1px solid grey;'>", unsafe_allow_html=True)    

with st.container():
    col1, col2 = st.columns(column_widths)
    
    with col1:
        st.header("Callejon Futbol")        
        st.markdown("""
                #### Es una propuesta diferente de analizar el Futbol, tomando a los dos maximos referentes del siglo 21, Lionel messi y Cristiano Ronaldo, hacemos un repaso de sus estadisticas en sus años en La Liga y las comptencias continentales, por su paso por Barcelona y Real Madrid respectivamente 
                """)         
        st.write('<div class="botones"><a href="https://callejonfutbol.streamlit.app/">Acceder a la App</a>', unsafe_allow_html=True)
        #st.write('<div class="botones"><a href="https://greyhound.streamlit.app/">Acceder a la documentacion</a>', unsafe_allow_html=True)
    with col2:
        imagen = "scr/callejon.png"  
        st.image(imagen, width=500, use_column_width=True, output_format='auto')
st.write("<hr style='border-top: 1px solid grey;'>", unsafe_allow_html=True)  

st.title("")

st.title("Mis Datos")
st.title("")

with st.container():
     
    col1, col2 = st.columns(column_widths)
    
    
    with col1:
        st.header("Marcelo Yuba")
        st.markdown(""" 
                #### Departamento: Data Analist, Graphic Design
                #### Background: Diseño multimedial, Publicidad grafica, E-Commerce
                #### Linkedin: [Acceder a su perfil](www.linkedin.com/in/marcelo-yuba)
                #### Github: [Acceder a su perfil](https://github.com/marceloyuba)
                """) 
    with col2:
        imagen = "scr/fotoLI.jpg"  
        st.image(imagen, width=250, use_column_width=False, output_format='auto')   

st.write("<hr style='border-top: 1px solid grey;'>", unsafe_allow_html=True)    
with st.container():
    
    st.header("Contactanos!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/marceloyuba@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Nombre" required>
        <input type="email" name="email" placeholder="E-mail" required>
        <textarea name="message" placeholder="Tu consulta" required></textarea>
        <button type="submit">Enviar</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()


page_bg_img = f"""
<style>

[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://github.com/marceloyuba/StreamlitSDT/blob/main/scr/fondoi.png?raw=true");
background-position: top left;
background-repeat: no-repeat;
background-attachment: fixed;
background-size: cover;
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
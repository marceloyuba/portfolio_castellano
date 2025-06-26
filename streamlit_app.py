import streamlit as st
from streamlit.hello.utils import show_code

st.set_page_config(page_title="Portfolio Marcelo Yuba", page_icon="scr/banner.png", layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

with st.container():      
    st.markdown('<style>h5, h4, h3, h2, h1 {color: white;}</style>', unsafe_allow_html=True)

column_widths = [1, 3, 1]
with st.container():
    col1, col2, col3 = st.columns(column_widths)   
    with col1:
        st.empty()
    with col3:
        st.title("")
    with col2: 
        st.image("scr/banner.png", width=1200, use_container_width=True, output_format='auto')

st.title("") 
        
# ---- HEADER SECTION ----
with st.container():        
    st.header("Hola, soy Marcelo Yuba :wave:")
    st.write("<hr style='border-top: 1px solid grey;'>", unsafe_allow_html=True)    
    st.title("Un Data Analyst y Data Scientist de Buenos Aires, Argentina")
    
    st.markdown("""
        #### Apasionado en el análisis de datos usando Power BI y Python, tratando de forma más eficiente obtener resultados para tu negocio o empresa.
    """)

column_widths = [2, 1] 
st.write("<hr style='border-top: 1px solid grey;'>", unsafe_allow_html=True)    
with st.container():    
    st.title("Qué es lo que hago")    
    col1, col2 = st.columns(column_widths)
   
    with col1:
        st.markdown("### Utilizando diferentes tecnologías, me permiten hacer análisis de datos, Dashboards interactivos")
        st.markdown(
            """            
            ##### Como analista de datos, tengo un papel crucial en la interpretación y análisis de conjuntos de datos para extraer información significativa y tomar decisiones fundamentadas:
            ##### - Comprensión del problema o pregunta
            ##### - Recopilación de datos
            ##### - Limpieza de datos
            ##### - Análisis exploratorio de datos (EDA)
            ##### - Toma de decisiones basada en datos
            """
        )
        st.markdown("#### Para lograr los objetivos necesarios, hago uso de estas tecnologías, tanto para análisis de datos como diseño de dashboards")

    with col2:
        imagen = "scr/tec.png" 
        st.image(imagen, width=400)

st.write("""
<style>
    .botones a {
        font-size: 30px;
        margin-top: 10px;
        text-decoration: none;
        color: #ffffff;
    }
</style>
""", unsafe_allow_html=True)  

st.title("Mis proyectos")     
st.write("<hr style='border-top: 3px solid white;'>", unsafe_allow_html=True)    

column_widths = [2, 1]
with st.container():
    col1, col2 = st.columns(column_widths)   
    with col1:
        st.header("Greyhound NYC Inserción de mercado")
        st.markdown(""" 
            #### Proyecto de análisis de inserción de mercado al sistema de vehículos con chofer para la ciudad de NYC, se analizaron tanto los factores económicos como ambientales para tomar decisiones sobre invertir o no en este negocio, tomando en cuenta varias hipótesis y llegando a sus respectivas conclusiones
        """) 
        st.write('<div class="botones"><a href="https://greyhound.streamlit.app/">Acceder a la App</a>', unsafe_allow_html=True)
        st.write('<div class="botones"><a href="https://github.com/marceloyuba/SDT">Acceder a la documentación</a>', unsafe_allow_html=True)
    with col2:
        imagen = "scr/grey.png"  
        st.image(imagen, width=500, use_container_width=True, output_format='auto')        

st.write("<hr style='border-top: 1px solid grey;'>", unsafe_allow_html=True)    

with st.container():
    col1, col2 = st.columns(column_widths)
    with col1:
        st.header("Accidentes Viales en la Ciudad de Buenos Aires")        
        st.markdown("""
            #### Desde la expansión en 2021, nuestro cliente analiza nuevos mercados fuera del transporte de buses. Nos encomendó analizar la inserción al negocio de los viajes en automóviles, analizando a sus competidores directos (Taxis, Uber, Lyft) y comenzando por NYC, con una de las redes más complejas de transporte, para evaluar si es viable cumplir con las regulaciones ambientales.
        """) 
        st.write('<div class="botones"><a href="https://accidentesbuenosaires.streamlit.app/">Acceder a la App</a>', unsafe_allow_html=True)
        st.write('<div class="botones"><a href="https://github.com/marceloyuba/Proyecto_individual_Data_Analyst">Acceder a la documentación</a>', unsafe_allow_html=True)
    with col2:
        imagen = "scr/BA.png"  
        st.image(imagen, width=500, use_container_width=True, output_format='auto')

st.write("<hr style='border-top: 1px solid grey;'>", unsafe_allow_html=True)    

with st.container():
    col1, col2 = st.columns(column_widths)
    with col1:
        st.header("Callejón Fútbol")        
        st.markdown("""
            #### Propuesta distinta para analizar el fútbol. Se toman a los máximos referentes del siglo 21, Messi y Cristiano Ronaldo, y se repasan sus estadísticas en La Liga y competiciones continentales por su paso por Barcelona y Real Madrid respectivamente.
        """)         
        st.write('<div class="botones"><a href="https://callejonfutbol.streamlit.app/">Acceder a la App</a>', unsafe_allow_html=True)
    with col2:
        imagen = "scr/callejon.png"  
        st.image(imagen, width=500, use_container_width=True, output_format='auto')

st.write("<hr style='border-top: 1px solid grey;'>", unsafe_allow_html=True)  

st.title("")
st.title("Mis Datos")
st.title("")

with st.container():
    col1, col2 = st.columns(column_widths)
    with col1:
        st.header("Marcelo Yuba")
        st.markdown(""" 
            #### Departamento: Data Analyst, Graphic Design  
            #### Background: Diseño multimedial, Publicidad gráfica, E-Commerce
        """) 
        st.write('<div class="botones"><a href="https://www.linkedin.com/in/marcelo-yuba-b9a39827b/">Mi Linkedin</a>', unsafe_allow_html=True)
        st.write('<div class="botones"><a href="https://github.com/marceloyuba">Mi Github</a>', unsafe_allow_html=True)
    with col2:
        imagen = "scr/fotoLI.jpg"  
        st.image(imagen, width=250, use_container_width=False, output_format='auto')   

st.write("<hr style='border-top: 1px solid grey;'>", unsafe_allow_html=True)    

with st.container():
    st.header("Contactame!")
    st.write("##")

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



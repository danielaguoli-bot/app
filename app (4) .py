import streamlit as st
import pandas as pd

# ==========================================
# CONFIGURACIÓN
# ==========================================

st.set_page_config(
    page_title="Mundo Musical",
    page_icon="🎵",
    layout="wide"
)

# ==========================================
# ESTILOS
# ==========================================

st.markdown("""
<style>

.stApp {
    background-color: #f8f7ff;
    color: #29263d;
}

.titulo {
    font-size: 50px;
    font-weight: bold;
    color: #29263d;
    text-align: center;
}

.titulo span {
    color: #7957d5;
}

.subtitulo {
    text-align: center;
    color: #7957d5;
    font-size: 18px;
    margin-bottom: 30px;
}

.tarjeta {
    background-color: white;
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
    min-height: 310px;
    margin-bottom: 10px;
}

.icono {
    font-size: 65px;
    background-color: #eee9ff;
    border-radius: 50%;
    width: 120px;
    height: 120px;
    margin: auto;
    display: flex;
    align-items: center;
    justify-content: center;
}

.nombre {
    color: #7957d5;
    font-size: 25px;
    font-weight: bold;
    margin-top: 15px;
}

.descripcion {
    font-size: 15px;
    line-height: 1.6;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# PORTADA
# ==========================================

st.markdown(
    '<div class="titulo">🎵 Mundo <span>Musical</span></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitulo">DESCUBRE EL MUNDO DE LOS INSTRUMENTOS MUSICALES</div>',
    unsafe_allow_html=True
)

st.write(
    "Explora diferentes instrumentos, conoce sus características "
    "y descubre a qué familia musical pertenecen."
)

st.markdown("---")


# ==========================================
# MENÚ
# ==========================================

opcion = st.selectbox(
    "Selecciona una sección:",
    [
        "Inicio",
        "Explorar instrumentos",
        "Familias musicales",
        "Tabla de instrumentos",
        "Gráfico"
    ]
)


# ==========================================
# INICIO
# ==========================================

if opcion == "Inicio":

    st.header("🎶 Bienvenido a Mundo Musical")

    st.write(
        "Los instrumentos musicales son objetos creados para producir "
        "sonidos y formar parte de diferentes expresiones musicales."
    )

    st.subheader("🎼 Explora las familias")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="tarjeta">
        <div class="icono">🎸</div>
        <div class="nombre">Cuerda</div>
        <p class="descripcion">
        Instrumentos que producen sonido mediante la vibración de cuerdas.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="tarjeta">
        <div class="icono">🎺</div>
        <div class="nombre">Viento</div>
        <p class="descripcion">
        Instrumentos que producen sonido mediante la vibración del aire.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="tarjeta">
        <div class="icono">🥁</div>
        <div class="nombre">Percusión</div>
        <p class="descripcion">
        Instrumentos que producen sonido al ser golpeados o sacudidos.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="tarjeta">
        <div class="icono">🎹</div>
        <div class="nombre">Teclado</div>
        <p class="descripcion">
        Instrumentos que utilizan teclas para producir sonidos.
        </p>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# EXPLORAR INSTRUMENTOS
# ==========================================

elif opcion == "Explorar instrumentos":

    st.header("🎼 Explora los instrumentos")

    st.write(
        "Haz clic en el botón de cada instrumento para conocer más información."
    )

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    # GUITARRA
    with col1:

        st.markdown("""
        <div class="tarjeta">
        <div class="icono">🎸</div>
        <div class="nombre">Guitarra</div>
        <p class="descripcion">
        Instrumento de cuerda utilizado en diferentes estilos musicales.
        </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Ver más", key="guitarra"):
            st.info(
                "🎸 La guitarra es un instrumento de cuerda. "
                "Produce sonido mediante la vibración de sus cuerdas. "
                "Es utilizada en géneros como rock, pop, música clásica y otros."
            )

    # VIOLÍN
    with col2:

        st.markdown("""
        <div class="tarjeta">
        <div class="icono">🎻</div>
        <div class="nombre">Violín</div>
        <p class="descripcion">
        Instrumento de cuerda conocido por su sonido expresivo.
        </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Ver más", key="violin"):
            st.info(
                "🎻 El violín pertenece a la familia de cuerda. "
                "Normalmente se toca utilizando un arco que hace vibrar "
                "sus cuerdas."
            )

    # PIANO
    with col3:

        st.markdown("""
        <div class="tarjeta">
        <div class="icono">🎹</div>
        <div class="nombre">Piano</div>
        <p class="descripcion">
        Instrumento de teclado utilizado en numerosos géneros musicales.
        </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Ver más", key="piano"):
            st.info(
                "🎹 El piano es un instrumento de teclado. "
                "Al presionar sus teclas se activa un mecanismo que "
                "produce el sonido de sus cuerdas."
            )

    # SAXOFÓN
    with col4:

        st.markdown("""
        <div class="tarjeta">
        <div class="icono">🎷</div>
        <div class="nombre">Saxofón</div>
        <p class="descripcion">
        Instrumento de viento utilizado en diferentes estilos musicales.
        </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Ver más", key="saxofon"):
            st.info(
                "🎷 El saxofón pertenece a los instrumentos de viento. "
                "Produce sonido cuando el aire hace vibrar una lengüeta "
                "ubicada en la boquilla."
            )


# ==========================================
# FAMILIAS MUSICALES
# ==========================================

elif opcion == "Familias musicales":

    st.header("🎶 Familias de instrumentos")

    st.write(
        "Selecciona una familia para conocer sus características."
    )

    familia = st.selectbox(
        "Selecciona una familia:",
        [
            "Cuerda",
            "Viento",
            "Percusión",
            "Teclado"
        ]
    )

    if familia == "Cuerda":

        st.subheader("🎸 Instrumentos de cuerda")

        st.write(
            "Producen sonido mediante la vibración de una o varias cuerdas."
        )

        st.write("🎸 Guitarra")
        st.write("🎻 Violín")
        st.write("🎼 Arpa")

    elif familia == "Viento":

        st.subheader("🎺 Instrumentos de viento")

        st.write(
            "Producen sonido mediante la vibración del aire."
        )

        st.write("🎺 Trompeta")
        st.write("🎷 Saxofón")
        st.write("🪈 Flauta")

    elif familia == "Percusión":

        st.subheader("🥁 Instrumentos de percusión")

        st.write(
            "Producen sonido principalmente al ser golpeados, "
            "sacudidos o frotados."
        )

        st.write("🥁 Batería")
        st.write("🪘 Tambor")
        st.write("🎵 Maracas")

    elif familia == "Teclado":

        st.subheader("🎹 Instrumentos de teclado")

        st.write(
            "Utilizan teclas para producir diferentes sonidos."
        )

        st.write("🎹 Piano")
        st.write("🎹 Órgano")
        st.write("🎹 Teclado electrónico")


# ==========================================
# TABLA
# ==========================================

elif opcion == "Tabla de instrumentos":

    st.header("📋 Tabla de instrumentos")

    datos = {
        "Instrumento": [
            "Guitarra",
            "Violín",
            "Arpa",
            "Trompeta",
            "Saxofón",
            "Flauta",
            "Batería",
            "Tambor",
            "Maracas",
            "Piano",
            "Órgano",
            "Teclado electrónico"
        ],

        "Familia": [
            "Cuerda",
            "Cuerda",
            "Cuerda",
            "Viento",
            "Viento",
            "Viento",
            "Percusión",
            "Percusión",
            "Percusión",
            "Teclado",
            "Teclado",
            "Teclado"
        ]
    }

    tabla = pd.DataFrame(datos)

    st.dataframe(
        tabla,
        use_container_width=True
    )


# ==========================================
# GRÁFICO
# ==========================================

elif opcion == "Gráfico":

    st.header("📊 Instrumentos por familia")

    datos = {
        "Familia": [
            "Cuerda",
            "Viento",
            "Percusión",
            "Teclado"
        ],

        "Cantidad": [
            3,
            3,
            3,
            3
        ]
    }

    grafico = pd.DataFrame(datos)

    st.bar_chart(
        grafico.set_index("Familia")
    )


# ==========================================
# PIE DE PÁGINA
# ==========================================

st.markdown("---")

st.markdown(
    "<center>🎵 Mundo Musical | Proyecto desarrollado con Python y Streamlit</center>",
    unsafe_allow_html=True
)
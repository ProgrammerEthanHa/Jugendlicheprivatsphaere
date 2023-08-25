import streamlit as st
import pandas as pd
import altair as alt

st.header("Jugendliche beschäftigen sich aktiv mit Privatsphäre")
st.subheader("Einstellungen zur Privatsphäre von Jugendlichen")

source = pd.DataFrame({
        'Anteil(%)': [6, 22, 69],
        'Einstellung': ['Nein, mir ist nicht bekannt, dass das geht', 'Nein, aber mir ist bekannt, dass das geht', 'Ja, ich weiß wie man die Privatsphäre einstellt']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Einstellung:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis n=579; 10-18 Jahre; aktive soziale Medien benutzer
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: bitkom research")
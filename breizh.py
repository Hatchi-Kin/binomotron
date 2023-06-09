import mysql.connector as mysql
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import data.data as dd

#####################################################
# st.title("Breizhibus :bus:")

image = "pages/ecran_titre.jpg"
# image = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Gwenn_ha_Du_%2811_mouchetures%29.svg/langfr-800px-Gwenn_ha_Du_%2811_mouchetures%29.svg.png'
st.image(image)

carte = 'https://upload.wikimedia.org/wikipedia/commons/f/f0/Plan_bibus_2016-2017.png'
st.image(carte, caption = "Carte de la capitale de la planète Terre")

#####################################################

def menu_deroulant_horaires_pour_chaque_lignes():

    query = "Select l.nom as ligne,h.heure,a.libelle as arret,a.adresse from horaires h left join arrets a on a.id=h.arret left join lignes l on l.id=h.ligne"
    dataframe=dd.format_heure(dd.get_data(query))

    option = dataframe['ligne'].drop_duplicates()
    option = st.selectbox('Choisissez votre ligne', dataframe['ligne'].unique())
    st.write(f"Les horaires pour la ligne {option}: ")

    st.dataframe(dataframe[dataframe['ligne'] == option].reset_index(drop=True).drop('ligne', axis=1))



if __name__ == "__main__":

    menu_deroulant_horaires_pour_chaque_lignes()
import matplotlib.pyplot as plt
import seaborn as sns
import data.data as dd
import streamlit as st
import mysql.connector as mysql
#####################################################


def barplot_frequentation_par_lignes():

    # sélection du nombre de passagers par ligne

    query = """
            SELECT lignes.nom AS ligne, SUM(frequentation.nombre_passagers) AS total_passagers
            FROM frequentation
            INNER JOIN horaires ON frequentation.horaire = horaires.id
            INNER JOIN lignes ON horaires.ligne = lignes.id
            GROUP BY lignes.nom;
            """

    dataframe=dd.get_data(query)
    st.title("Fréquentations par ligne :")

    fig=plt.figure(figsize=[14,9],dpi=100)

    ax = sns.barplot(x="ligne", y="total_passagers", data=dataframe, palette = ["red", "green", "blue", "black"])

    plt.ylim((220, 290))
    plt.ylabel('Nombre de passagers')
    plt.xlabel('Lignes')
    plt.title('Histogramme des fréquentations par lignes')

    for i in ax.containers:
        ax.bar_label(i)

    st.pyplot(fig)


def pie_chart_frequentation_par_jour():

    
    query = """
            SELECT frequentation.jour AS Jour, SUM(frequentation.nombre_passagers) AS Total_Passagers
            FROM frequentation
            GROUP BY frequentation.jour;
            """
    
    dataframe=dd.get_data(query)
    st.title("Fréquentations par jour :")

    fig=plt.figure(figsize=[11,8],dpi=100)

    # pie chart

    plt.pie(dataframe['Total_Passagers'], labels=dataframe['Jour'], autopct='%1.1f%%', startangle=90)
    plt.title('Répartition des fréquentations par jour')

    st.pyplot(fig)


def lineplot_frequentation_pa_heures():

    # sélection du nombre de passagers par heure


    query = """
            SELECT horaires.heure AS horaire, SUM(frequentation.nombre_passagers) AS total_passagers
            FROM frequentation
            INNER JOIN horaires ON frequentation.horaire = horaires.id
            GROUP BY horaires.heure;
            """

    dataframe=dd.get_data(query)
    st.title("Fréquentations par heure :")

    fig=plt.figure(figsize=[14,9],dpi=100)

    ax = sns.lineplot(x="horaire", y="total_passagers", data=dataframe)

    

    plt.ylim((0, 150))
    plt.ylabel('Nombre de passagers')
    plt.xlabel('Heures')
    plt.title('Fréquentations par heure')

    st.pyplot(fig)


#####################################################


barplot_frequentation_par_lignes()
lineplot_frequentation_pa_heures()
pie_chart_frequentation_par_jour()

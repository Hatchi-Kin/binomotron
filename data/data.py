import pandas as pd
import mysql.connector as mysql

#####################################################

def get_data(query):

    user = "utilisateurbus"
    password = "motdepasse"
    host = "localhost"
    database = "breizhibus"
    port = "3307"

    bdd = mysql.connect(user=user, password=password, host=host, database=database, port=port)
    cursor = bdd.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    dframe = pd.DataFrame(data, columns=cursor.column_names)
    bdd.close()
    return dframe


def format_heure(dataframe):
    dataframe['heure'] = pd.to_timedelta(dataframe['heure']).apply(lambda x: f"{x.components.hours}:{x.components.minutes:02d}:{x.components.seconds:02d}")
    return dataframe
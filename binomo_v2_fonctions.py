import mysql.connector as msqlpy
import random

################################################
def creer_liste_noms():
    user = "root"
    password = "example"
    host = "localhost"
    port = "3307"
    database = "binomotron_t2_bdd"
    bdd = msqlpy.connect(user=user, password=password, host=host, port=port, database=database)
    cursor = bdd.cursor()
    liste_noms = []
    query = "SELECT * FROM apprenants;"
    cursor.execute(query)

    for eleve in cursor:
        # Dans cursor, la colonne avec les prénoms est la deuxième colonne, donc on récupère eleve[1]
        liste_noms.append(eleve[1])
    return liste_noms
################################################

################################################
def creer_binomes(liste_noms):
    binomes = []
    while len(liste_noms) > 0:
        nom1 = random.choice(liste_noms)
        liste_noms.remove(nom1)
        nom2 = random.choice(liste_noms)
        liste_noms.remove(nom2)
        binomes.append(f"{nom1} et {nom2}")
    return binomes
################################################

################################################
def creer_groupe_de_n(choix_de_n):

    liste_prenoms = creer_liste_noms()
    reste = len(liste_prenoms) % int(choix_de_n)
    groupe_de_n = []
    random.shuffle(liste_prenoms)

    for i in range(0, len(liste_prenoms) - reste, choix_de_n):
        groupe_de_n.append(liste_prenoms[i:i+choix_de_n])
    if reste > 0:
        groupe_de_n.append(liste_prenoms[-reste:])
    return groupe_de_n
################################################

################################################
def commit_binomes_to_bdd(binomes):
    user = "root"
    password = "example"
    host = "localhost"
    port = "3307"
    database = "binomotron_t2_bdd"
    bdd = msqlpy.connect(user=user, password=password, host=host, port=port, database=database)
    cursor = bdd.cursor()
    query = "DELETE FROM duos"
    cursor.execute(query)
    bdd.commit()
    query = f"INSERT INTO duos (libelle_duo) VALUES ('{binomes[0]}'), ('{binomes[1]}'), ('{binomes[2]}'), ('{binomes[3]}'), ('{binomes[4]}'), ('{binomes[5]}'), ('{binomes[6]}'), ('{binomes[7]}');"
    cursor.execute(query)
    bdd.commit()
################################################

################################################
def show_duos_from_bdd():
    user = "root"
    password = "example"
    host = "localhost"
    port = "3307"
    database = "binomotron_t2_bdd"
    bdd = msqlpy.connect(user=user, password=password, host=host, port=port, database=database)
    cursor = bdd.cursor()
    query = "SELECT * FROM duos;"
    cursor.execute(query)
    duos_from_bdd = []
    for duos in cursor:
        duos_from_bdd.append(duos[1])
    return duos_from_bdd
################################################

################################################
def creer_liste_mail():
    user = "root"
    password = "example"
    host = "localhost"
    port = "3307"
    database = "binomotron_t2_bdd"
    bdd = msqlpy.connect(user=user, password=password, host=host, port=port, database=database)
    cursor = bdd.cursor()
    liste_noms = creer_liste_noms()
    query = "SELECT prenom, mail FROM apprenants;"
    cursor.execute(query)
    liste_mails = {}

    for eleve in cursor.fetchall():
        liste_noms.append(eleve[0])
        liste_mails[eleve[0]] = eleve[1]
    return liste_mails
################################################

################################################
def commit_groupe_de_n_to_bdd(groupe_de_n):
    user = "root"
    password = "example"
    host = "localhost"
    port = "3307"
    database = "binomotron_t2_bdd"
    bdd = msqlpy.connect(user=user, password=password, host=host, port=port, database=database)
    cursor = bdd.cursor()
    query = "DELETE FROM groupes"
    cursor.execute(query)
    bdd.commit()

    groupe_a_vider = groupe_de_n
    
    for i in groupe_a_vider:
        j = ', '.join(i)
        query = f"INSERT INTO groupes (libelle_groupe) VALUES ('{j}')"
        cursor.execute(query)
        bdd.commit()
################################################

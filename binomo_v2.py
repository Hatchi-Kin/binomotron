import mysql.connector as msqlpy
from random import *
from binomo_v2_fonctions import *
#################################

user = "root"
password = "example"
host = "localhost"
port = "3307"
database = "binomotron_t2_bdd"
bdd = msqlpy.connect(user=user, password=password, host=host, port=port, database=database)
cursor = bdd.cursor()

#################################
# fonction perso pour récuperer la colonne prénom dans la table apprenants de la BDD et en faire une liste
liste_noms = creer_liste_noms()
# au cas ou j'utilise la fonction shuffle qui modifierai ma liste_noms, cette nouvelle variable restera dans l'ordre
liste_noms_deux = creer_liste_noms()
on = True

# tant que la variable on est True, on reste dans la boucle (on devient faux si user entre "x" dans le menu)
while on:
    binomes = creer_binomes(liste_noms)
    action = input("""

    **********************************************************************************************
    Entrez  "a"  pour créer une liste de binomes aléatoire et l'afficher: 
    Entrez  "b"  pour afficher la liste de binomes déjà enregistrée dans la BDD (si elle existe): 
    Entrez un chiffre entre  1 et 8  pour afficher un binome spécifique: 
    Entrez un  "prenom" pour afficher son binome et leurs adresses mail: 
    Entrez  "x"  pour quitter le programme: 
    **********************************************************************************************
    """)

    # condition pour afficher une nouvelle liste aléatoire de binomes
    if action == "a":
        liste_noms = creer_liste_noms()
        binomes = creer_binomes(liste_noms)
        print(binomes)
        in_action = input("""

    **********************************************************************************************
        Voulez-vous saveguarder cette liste de binomes dans la BDD? (y/n): 
    **********************************************************************************************
    
        # """)
        # dans la condition "a", condition pour ne pas sauvegarder la liste dans la BDD et revenir au menu
        if in_action == "n":
            continue
        # dans "a", condition pour sauvegarder (après confirmlation) la liste dans la BDD
        elif in_action == "y":
            new_input = input("""
    **********************************************************************************************
    Attention, ceci effacera tous les binomes déjà enregistrés s'ils existent ! confirmer? (y/n): 
    **********************************************************************************************
            """)
            if new_input == "n":
                continue
            elif new_input == "y":
                # fonction perso pour effacer le contenu de la table binomes puis enregistrer la liste précedement créée
                commit_binomes_to_bdd(binomes) 
            else:
                print("Veuillez entrez une commande valide. ")
                continue


    elif action == "b":
            # fonction perso créer une liste avec le contenu de la colonne libelle_buo de la table duos de la BDD
            print(show_duos_from_bdd())

    # condition pour afficher un binome spécifique (input = indice de la liste binomes[])
    elif action.isdigit() and int(action) >= 1 and int(action) <= 8: 
            binomes = show_duos_from_bdd()
            hot_bin = binomes[(int(action)-1)]
            print(f"binome_{int(action)}: {hot_bin}")

    # condition pour afficher binome + mails
    elif action in liste_noms_deux:          
        liste_mails = creer_liste_mail()
        duos_from_bdd = (show_duos_from_bdd())
        for i in duos_from_bdd:
            # boucle pour trouver le nom demandé dans liste  binomes[] qui contient les binomes sous forme de string
            for i in duos_from_bdd: 
                # si le prénom est trouvé et se trouve au début de la string
                if i.find(action) == 0: 
                    action_binome = i.split(" ")[-1]
                # si le prénom est trouvé et se trouve à la fin de la string
                elif i.find(action) > 0: 
                    action_binome = i.split(" ")[0]
        print(f"l'adresse mail de {action} est:  {liste_mails[action]}")
        print(f"Son binome est: {action_binome} et son mail est:  {liste_mails[action_binome]}")
            
    # condition pour QUITTER le programme
    elif action == "x":
        on = False
    
    # si la commande entrée ne correspond à aucune conditions gerées par notre script
    else:  
        print("Veuillez entrez une commande valide. ")
        continue

#################################

cursor.close()
bdd.close()
    

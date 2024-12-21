# binomotron / premier tp simplon dev IA !

Une App qui permet de générer des équipes projet à partir d'une base de données contenant une liste d'élèves.

### Installation

1. Clonez ce dépôt sur votre machine locale :
   git clone https://github.com/Hatchi-Kin/binomotron.git
   cd binomotron

2. Assurez-vous que Docker et Docker Compose sont installés sur votre machine.

### Démarrage des services

1. Démarrez les services définis dans le fichier docker-compose.yml :
   ```sh
   cd sql
   docker compose up -d
   ```

2. Vérifiez que les conteneurs sont en cours d'exécution :
   ```sh
   docker ps
   ```

   Vous devriez voir deux conteneurs en cours d'exécution : db (MySQL) et pma (phpMyAdmin).

Création et peuplement de la base de données

1. Accédez au conteneur MySQL :
   ```sh
   docker exec -it db mysql -u root -p
   ```
   Entrez le mot de passe example lorsque vous y êtes invité.

2. Créez la base de données :
   ```sql
   CREATE DATABASE binomotron_t2_bdd;
   USE binomotron_t2_bdd;
   ```

3. Quittez le shell MySQL :
   `EXIT`

4. Importez le script SQL pour créer les tables et insérer les données :
   ```sh
   docker exec -i db mysql -u root -p binomotron_t2_bdd < binomotron_t2_bdd.sql
   ```
   Entrez le mot de passe example lorsque vous y êtes invité.

### Utilisation de l'application

1. Assurez-vous que les dépendances Python sont installées :
   ```sh
   cd ..
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Exécutez le script Python :
   ```sh
   python binomo_v2.py
   ```

3. Suivez les instructions à l'écran pour interagir avec l'application.

Arrêt des services

Pour arrêter les services Docker, exécutez :
```sh 
docker-compose down
```
### Évolutions possibles

- Permettre de créer des groupes de 3, 4 ou plus.
- Structurer le code sous forme de fonctions.
- Afficher l’adresse mail d’un élève demandé.
- Afficher la liste des projets.
- Afficher les groupes pour un projet donné.
- Stocker en base les groupes constitués, avec leurs dates de création.
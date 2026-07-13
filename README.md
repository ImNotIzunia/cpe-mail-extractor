# cpe-mail-extractor

Script créé suite à la suppression de la rediction automatique des mails. Il permet de vérifier si de nouveaux mails sont disponibles (avec une gestion de filtres) et de notifier via un webhook Discord


## Prérequis

- Python 3.14 ou plus avec uv
- Les identifiants de connexion (adresse du portail, adresse mail, mot de passe)
- Un Webhook Discord pour recevoir les notifications


## Installation

Cloner le dépôt GitHub :

```bash
git clone https://github.com/ImNotIzunia/cpe-mail-extractor.git
cd cpe-mail-extractor
```

Installler les dépendances :

```bash
uv sync
```


## Configuration

Créer un fichier `.env` en reprebnant le modèle du fichier `.env.example` et renseigner les informations nécessaires :

```bash
cp .env.example .env
```

- imap_server : Adresse du serveur de messagerie
- imap_port : Port du serveur de messagerie (par défaut 993 pour IMAP sécurisé)
- email : Adresse e-mail de connexion
- password : Mot de passe de l'adresse e-mail
- discord_webhook : URL du webhook Discord pour recevoir les notifications

Le fichier `filters/rules.py` peut etre modifier afin de rajouter des règles de filtrage comme des éléments importants ou à ignorer.
Si le liste `KEYWORDS` est vide, tous les e-mails seront considérés comme importants et seront envoyés au webhook Discord.

## Utilisation

Lancer le script principal :

```bash
uv run main.py
```

Le script va :

- Se connecter à la boîte mail via IMAP
- Récupérer les e-mails
- Filtrer les e-mails selon les règles définies dans `filters/rules.py`
- Envoyer les e-mails filtrés via le webhook Discord
- Stocker les e-mails filtrés dans un fichier JSON pour un usage ultérieur


## Logs

Les logs sont envoyés dans la console et peuvent être configurés dans le fichier `config/logging_config.py`.


## Tests

Vous pouvez exécuter les tests unitaires pour vérifier le bon fonctionnement du script :

```bash
uv run pytest

uv run ruff check .
```

## Contribution

Il s'agit d'un projet maintenu par une seule personne.

Toutes les contributions sont les bienvenues, que ce soit pour corriger des bugs, ajouter de nouvelles fonctionnalités ou améliorer la documentation.

Vous pouvez aussi supporter le projet en m'offrant un café.

<div align="center">

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/imnotizunia)

</div>


## License

MIT License.
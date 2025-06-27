# Projet Bibliothèque

## Installation

```bash
pip install -r requirements.txt
```

## Tests

Pour lancer tous les tests :

```bash
pytest
```

Pour lancer un test précis :

```bash
pytest tests/test_book.py::TestBookCreation::test_create_valid_book
```

## Couverture

Pour générer le rapport de couverture :

```bash
pytest --cov=src/bibliotheque --cov-report=html
```

Le rapport HTML sera disponible dans le dossier `htmlcov/`.

## Structure

```
bibliotheque_projet/
├── src/
│   └── bibliotheque/
│       ├── __init__.py
│       ├── book.py
│       ├── library.py
│       └── user.py
├── tests/
│   ├── __init__.py
│   ├── test_book.py
│   ├── test_library.py
│   └── test_user.py
├── requirements.txt
├── pytest.ini
└── README.md
```

- Le code métier est dans `src/bibliotheque/`.
- Les tests sont dans `tests/`.
- Les dépendances et la configuration sont à la racine du projet.

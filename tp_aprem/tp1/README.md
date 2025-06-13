# Tests Unitaires Multi-Technologies

Ce projet implémente des tests unitaires pour un module de gestion de panier d'achat en PHP et JavaScript.

## Structure du Projet

```
tp1/
├── php/
│   ├── Cart.php           # Classe du panier
│   ├── CartTest.php       # Tests unitaires
│   └── composer.json      # Configuration PHP
└── js/
    ├── Cart.js            # Classe du panier
    ├── Cart.test.js       # Tests unitaires
    └── package.json       # Configuration JavaScript
```

## Choix des Technologies

### PHP avec PHPUnit
- PHPUnit est le framework de test standard pour PHP
- Intégration native avec les outils de développement PHP
- Excellente documentation et grande communauté
- Support des tests unitaires, d'intégration et fonctionnels

### JavaScript avec Jest
- Jest est un framework de test moderne et populaire
- Configuration minimale requise
- Excellent support des tests asynchrones
- Génération automatique de rapports de couverture

## Types de Tests Implémentés

1. Tests de Fonctionnalités de Base
   - Ajout d'articles au panier
   - Calcul du total
   - Application de remises

2. Tests de Validation
   - Vérification des remises invalides
   - Gestion des erreurs

## Structure du Code

Le code est structuré pour être facilement testable en suivant ces principes :

1. Séparation des Responsabilités
   - Chaque classe a une seule responsabilité
   - Les méthodes sont courtes et focalisées

2. Injection de Dépendances
   - Les dépendances sont clairement définies
   - Facilité de mock pour les tests

3. Gestion des Erreurs
   - Validation des entrées
   - Messages d'erreur explicites

## Rapports de Tests

### PHP
Pour générer le rapport de tests PHP :
```bash
cd php
composer install
./vendor/bin/phpunit --coverage-html coverage
```

### JavaScript
Pour générer le rapport de tests JavaScript :
```bash
cd js
npm install
npm test
```

Les rapports montrent :
- Nombre de tests exécutés
- Taux de couverture de code
- Temps d'exécution
- Détails des tests échoués (si applicable) 
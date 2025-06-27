# TP3 : TDD et Approval Testing

Ce document détaille la démarche suivie pour implémenter une fonctionnalité de génération d'e-mail de confirmation en utilisant le Test-Driven Development (TDD) et l'Approval Testing.

## 1. Organisation du Projet

Le projet est structuré comme suit :
- `src/` : Contient le code source de l'application (ex: `EmailGenerator.ts`).
- `__tests__/` : Contient les fichiers de test (ex: `EmailGenerator.test.ts`).
- `package.json` : Définit les dépendances et les scripts du projet.
- `jest.config.js` : Configure l'environnement de test Jest.
- `tsconfig.json` : Configure le compilateur TypeScript.

## 2. Démarche TDD

Le TDD est un cycle en trois phases : Rouge, Vert, Refactor.

### Étape 1 : Rouge - Écrire un test qui échoue

J'ai commencé par écrire un test dans `__tests__/EmailGenerator.test.ts`. Ce test décrit le comportement attendu :
- Une classe `EmailGenerator` doit avoir une méthode `generateConfirmationEmail`.
- Cette méthode doit retourner une chaîne de caractères formatée.

Pour valider la sortie, j'ai utilisé l'**Approval Testing** via la fonctionnalité de **Snapshot Testing** de Jest (`.toMatchSnapshot()`).

```typescript
// __tests__/EmailGenerator.test.ts
it('should generate a correct confirmation email', () => {
  // ... données de test
  const emailContent = EmailGenerator.generateConfirmationEmail(registrationData);
  expect(emailContent).toMatchSnapshot();
});
```

Au lancement, ce test échoue car ni la classe `EmailGenerator` ni la méthode n'existent. C'est l'état **ROUGE**.

### Étape 2 : Vert - Écrire le code minimal

Ensuite, j'ai écrit le code le plus simple possible dans `src/EmailGenerator.ts` pour que le test passe.

```typescript
// src/EmailGenerator.ts
export class EmailGenerator {
  public static generateConfirmationEmail(data: RegistrationData): string {
    // ... logique de formatage du texte ...
    return `...`;
  }
}
```

Au premier lancement réussi du test, Jest génère automatiquement un fichier "snapshot" : `__tests__/__snapshots__/EmailGenerator.test.ts.snap`. Ce fichier contient le résultat attendu et devient la "vérité" pour les tests suivants. C'est l'état **VERT**.

### Fichier d'Approbation (Snapshot)

Voici à quoi ressemble le fichier d'approbation généré. Il sert de "golden file" :

```
// Jest Snapshot v1, https://goo.gl/fbAQLP

exports[`EmailGenerator should generate a correct confirmation email for an event registration 1`] = `
"Sujet : Confirmation de votre inscription à Conférence Ynov sur le TDD

Bonjour Jean Dupont,

Nous avons le plaisir de vous confirmer votre inscription à l'événement : Conférence Ynov sur le TDD.
Celui-ci aura lieu le samedi 26 octobre 2024 à 10:00.

Un e-mail de rappel vous sera envoyé 48h avant l'événement.

Cordialement,
L'équipe Ynov"
`;
```

### Étape 3 : Refactor - Améliorer le code

Le code initial fonctionnait, mais pouvait être amélioré (ex: extraire la logique de formatage de date, gérer les erreurs, etc.). J'aurais pu refactoriser le code en m'assurant que les tests (et donc le snapshot) restent valides. Le snapshot garantit qu'aucune régression n'est introduite.

## 3. Stratégie et Justification

### Choix de l'Approval Testing

L'Approval Testing (via snapshots) est idéal pour valider des sorties complexes et formatées comme des e-mails, des factures en HTML, ou du XML.

- **Avantages** :
    - **Simplicité** : Pas besoin d'écrire des assertions complexes pour chaque partie du texte. Le snapshot capture l'ensemble.
    - **Robustesse** : Détecte toute modification, même un simple espace ou un saut de ligne.
    - **Maintenance Facile** : Si un changement est intentionnel, le snapshot peut être mis à jour avec une simple commande (`jest --updateSnapshot`).

- **Limites** :
    - **Fragilité** : Un petit changement voulu (ex: ajout d'une virgule) fait échouer le test et nécessite une mise à jour manuelle du snapshot.
    - **Manque de Clarté** : Un snapshot ne décrit pas l'intention métier aussi bien qu'une série de tests unitaires ciblés. Il montre le "quoi", mais pas le "pourquoi".

Pour un système robuste, il est bon de combiner les snapshots (pour la structure globale) avec des tests unitaires classiques (pour la logique métier critique).

## 4. Conclusion

La démarche TDD combinée à l'Approval Testing offre une méthode puissante pour développer des fonctionnalités fiables, en particulier pour la génération de sorties formatées. Le cycle "Red-Green-Refactor" structure le développement, tandis que les snapshots garantissent la non-régression de manière simple et efficace. 
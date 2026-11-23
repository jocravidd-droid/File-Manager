# EXEMPLES D'ENTRÉE ET DE SORTIE

Les exemples supposent que `Desktop` existe dans le dossier utilisateur. Les résultats sont illustratifs : ils dépendent des fichiers présents sur l'ordinateur. Le nom d'utilisateur est masqué par `****`.

## 1. Afficher tout le contenu (sans filtre)

```text
Bonjour quelle dossier chercher vous ?
>> Desktop
Filtre par extension (o ou n) ?  n
Chargement en cours...

C:\Users\****\Desktop\tech.txt  =  File
C:\Users\****\Desktop\transfere a faire  =  Dossier

Résumer:
Nombre de dossier: 1
Nombre de fichier: 1
```

## 2. Filtrer par extension — plusieurs résultats

L'extension se saisit sans le point. La recherche inclut les sous-dossiers.

```text
Bonjour quelle dossier chercher vous ?
>> Desktop
Filtre par extension (o ou n) ?  o
Cherche tu un fichier en particulier (o ou n) ? n
Quel extension (sans le '.'): txt
Chargement en cours...

C:\Users\****\Desktop\tech.txt  =  File
C:\Users\****\Desktop\transfere a faire\notes.txt  =  File

Résumer:
Nombre de dossier: 0
Nombre de fichier: 2
```

## 3. Filtrer par extension — aucun résultat

Si aucun fichier ne correspond, le programme affiche quand même le résumé avec zéro résultat.

```text
Bonjour quelle dossier chercher vous ?
>> Desktop
Filtre par extension (o ou n) ?  o
Cherche tu un fichier en particulier (o ou n) ? n
Quel extension (sans le '.'): pdf
Chargement en cours...

Résumer:
Nombre de dossier: 0
Nombre de fichier: 0
```

## 4. Chercher un fichier précis — trouvé

```text
Bonjour quelle dossier chercher vous ?
>> Desktop
Filtre par extension (o ou n) ?  o
Cherche tu un fichier en particulier (o ou n) ? o
Quel fichier chercher vous: tech.txt
Chargement en cours...

C:\Users\****\Desktop\tech.txt  =  File

Résumer:
Nombre de dossier: 0
Nombre de fichier: 1
```

## 5. Chercher un fichier précis — introuvable

```text
Bonjour quelle dossier chercher vous ?
>> Desktop
Filtre par extension (o ou n) ?  o
Cherche tu un fichier en particulier (o ou n) ? o
Quel fichier chercher vous: absent.txt
Chargement en cours...

Résumer:
Nombre de dossier: 0
Nombre de fichier: 0
```

## 6. Dossier introuvable

```text
Bonjour quelle dossier chercher vous ?
>> DossierInexistant
Filtre par extension (o ou n) ?  n
Chargement en cours...

le dossier n'existe pas ou le chemin et mauvais
```

## 7. Réponse invalide à la question du filtre

Seules les réponses `o` et `n` sont acceptées. Une autre réponse déclenche une erreur `ValueError`.

```text
Bonjour quelle dossier chercher vous ?
>> Desktop
Filtre par extension (o ou n) ?  oui

ValueError: Réponse Inconnu ?
```

## 8. Extension ou nom de fichier vide

Une saisie vide déclenche une erreur `ValueError`.

```text
Quel extension (sans le '.'): 

ValueError: le champs filtre et vide !
```

La même erreur est produite si le nom du fichier est vide :

```text
Quel fichier chercher vous: 

ValueError: le champs filtre et vide !
```


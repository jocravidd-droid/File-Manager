# File-Manager

Le programme simplifie la recherche de fichier ciblée et l'exploration de dossier en iterant
et en affichant le contenu ainsi que le nombre de dossier et fichier que contient le dossier
que vous avait fournis

## Fonctionnalités

1. Exploration de dossier
2. afficher le contenu
    - filtrer par extension
    - cibler un fichier particulier
3. gestion d'erreur

### Installation

- Python Version: 3.15.2
- Bibliothéque: requirements.txt

> Installer la *bibliothéque* mettez votre python a la **version** utiliser ici, c'est pas obligatoire
> mais conseillier quand vous avez finis vous pouvez soit modifier le fichier ou l'utiliser sans modification

### Utilisation

Pour l'utilisation le dossier `examples` explique tout en détaille sur comment l'utiliser que ce sa soit
les commande, les exemples d'entrée, et les résultat de chaque commande et comment manipuler le programme
et bien d'autre donc merci de vous rendre dans le dossier `examples` pour plus d'informations

### TEST

Pour les test aller dans le dossier `tests` et adapter a vos modifications
mon test était adapter a mon environnement et a mais fichier dans le dossier le .py
test si la fonction checker() laisse passez des dossier inexistant et si les dossier
existant sont bien détecter et vérifie aussi si show() préviens si le dossier n'existe pas
et si les fonction de recherche ciblé fonctionne correctement ainsi que la fonction de recherche par extension

### Limites et Suite

Les limite sont les suivant :

- il n'y a pas d'interface graphique et le programme n'est pas assez autonome
- il ne marche pas depuis n'importe quel répertoire il commence obligatoirement du répertoire personnel
- certain code sans pas tester mais gérer par `raise` c'est pas un moyen fiable a 100%
-par defaut et il et impossible pour le moment de le changer et aussi il manque les
-test de `user()` qui n'ont pas etait effectuer non plus mais qui sont gérer par `raise`

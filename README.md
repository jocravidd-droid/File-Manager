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
les commande, les exemples d'entrée, et les resultat de chaque commande et comment manipuler le programme
et bien d'autre donc merci de vous rendre dans le dossier `examples` pour plus d'informations

### TEST

Pour les test aller dans le dossier `tests` et adapater a vos modifications
le mien test si la fonction checker() laisse passez des dossier inexistant
et si les dossier existant sont bien détecter et verifie aussi si show() previens
si le dossier n'existe pas et si les fonction de recherche ciblé fonctionne ainsi
que la fonction de recherche par extension

### Limites et Suite

il n'y a pas d'interface graphique et le programme n'est pas assez autonome
pour marcher depuis n'importe quel repertoire il commence du repertoire personnel 
par defaut et il et impossible pour le moment de le changer et aussi il manque les
test de `user()` qui n'ont pas etait effectuer non plus mais qui sont gérer par `raise`

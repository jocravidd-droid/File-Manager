from pathlib import Path


def user():
    print("\nBonjour quelle dossier chercher vous ? ")
    user = input(">> ")
    demand = input("Filtre par extension (o ou n) ?  ")
    if demand.lower() == "o":
        demander = input("Cherche tu un fichier en particulier (o ou n) ? ")
        if demander.lower() == "o":
            filtre = input("Quel fichier chercher vous: ")
            if filtre.strip() == "":
                raise ValueError("le champs filtre et vide !")
            else:
                print("Chargement en cours...\n")
                return user, filtre.strip(), 32
        elif demander.lower() == "n":
            filtre = input("Quel extension (sans le '.'): ")
            if filtre.strip() == "":
                raise ValueError("le champs filtre et vide !")
            else:
                print("Chargement en cours...\n")
                return user, filtre.strip(), 31
    elif demand.lower() == "n":
        print("Chargement en cours...\n")
        return user, 0, 30
    else:
        raise ValueError("Réponse Inconnu ?")


def checker(dossier):
    base = Path.home() / dossier
    if base.exists():
        return True, base
    else:
        return False, 0


def show(dossier, bool, filtre, nombre):
    if bool:
        resume = "\nRésumer: \n"
        n_dossier = 0
        n_file = 0
        if filtre == 0:
            for entree in sorted(dossier.iterdir()):
                nature = "Dossier" if entree.is_dir() else "File"
                print(entree, " = ", nature)
                if nature == "Dossier":
                    n_dossier += 1
                if nature == "File":
                    n_file += 1
            resume += (
                "Nombre de dossier: "
                + str(n_dossier)
                + "\n"
                + "Nombre de fichier: "
                + str(n_file)
            )
            return resume, 1
        else:
            if nombre == 31:
                for entree in sorted(dossier.rglob(f"*.{filtre}")):
                    nature = "Dossier" if entree.is_dir() else "File"
                    print(entree, " = ", nature)
                    if nature == "Dossier":
                        n_dossier += 1
                    if nature == "File":
                        n_file += 1
                resume += (
                    "Nombre de dossier: "
                    + str(n_dossier)
                    + "\n"
                    + "Nombre de fichier: "
                    + str(n_file)
                )
                return resume, 2
            if nombre == 32:
                for entree in sorted(dossier.rglob(f"{filtre}")):
                    nature = "Dossier" if entree.is_dir() else "File"
                    print(entree, " = ", nature)
                    if nature == "Dossier":
                        n_dossier += 1
                    if nature == "File":
                        n_file += 1
                resume += (
                    "Nombre de dossier: "
                    + str(n_dossier)
                    + "\n"
                    + "Nombre de fichier: "
                    + str(n_file)
                )
                return resume, 2
    else:
        return "le dossier n'existe pas ou le chemin et mauvais", 3


if __name__ == "__main__":
    u, f, n = user()
    r, c = checker(u)
    d, _test = show(c, r, f, n)
    print(d)

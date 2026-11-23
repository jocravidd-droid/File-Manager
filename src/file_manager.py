from pathlib import Path


def user():
    print("\nBonjour quelle dossier chercher vous ? ")
    user = input(">> ")
    print("Filtre par extension (o ou n) ? ")
    demand = input(">> ")
    if demand.lower() == "o":
        demander = input("Cherche tu un fichier en particulier ? (o ou n)")
        if demander.lower() == "o":
            filtre = input("Quel fichier chercher vous: ")
        elif demander.lower() == "n":
            filtre = input("Quel extension (sans le '.'): ")
        if filtre.strip() == "":
            raise ValueError("le champs filtre et vide !")
        else:
            print("Chargement en cours...\n")
            return user, filtre.strip()
    elif demand.lower() == "n":
        print("Chargement en cours...\n")
        return user, 0
    else:
        raise ValueError("Réponse Inconnu ?")


def checker(dossier):
    base = Path.home() / dossier
    if base.exists():
        return True, base
    else:
        return False, 0


def show(dossier, bool, filtre):
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
    else:
        return "le dossier n'existe pas ou le chemin et mauvais", 3


if __name__ == "__main__":
    u, f = user()
    r, c = checker(u)
    d, _test = show(c, r, f)
    print(d)

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src import file_manager


# test si le chemin existe et si existe il renvoie le chemin et le booléen True sinon il renvoie False et 0
def test_checker():
    base_1 = Path.home()
    assert file_manager.checker("m") == (False, 0)
    assert file_manager.checker(base_1) == (True, base_1)

# test si le chemin existe et si le filtre est correct
def test_show():
    base_2 = Path.home()
    assert file_manager.show(base_2, False, "doc", 31) == (
        "le dossier n'existe pas ou le chemin et mauvais",
        4,
    )

    _x, n = file_manager.show(base_2, True, "doc", 31)
    assert n == 2

    _t, m = file_manager.show(base_2, True, "tech.txt", 32)
    assert m == 3

    _k, y = file_manager.show(base_2, True, 0, 30)
    assert y == 1


test_checker()
test_show()

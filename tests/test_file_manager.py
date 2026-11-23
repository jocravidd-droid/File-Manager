import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src import file_manager


def test_checker():
    base_1 = Path.home()
    assert file_manager.checker("m") == (False, 0)
    assert file_manager.checker(base_1) == (True, base_1)


def test_show():
    base_2 = Path.home()
    assert file_manager.show(base_2, False, "doc") == (
        "le dossier n'existe pas ou le chemin et mauvais",
        3,
    )

    _x, n = file_manager.show(base_2, True, "doc")
    assert n == 2

    _k, y = file_manager.show(base_2, True, 0)
    assert y == 1


test_checker()
test_show()

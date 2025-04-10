import pathlib

from src.my_new_project import get_name, get_year, get_town

parent = pathlib.Path(__file__).parent.parent
namefile = parent / 'name.txt'
yearfile = parent / 'src' / 'year.txt'
townfile = parent / 'src' / 'my_new_project' / 'town.txt'


def test_name():
    with open(namefile) as f:
        name = f.readline()
    assert name == get_name(), 'Names are not equal'


def test_year():
    with open(yearfile) as f:
        year = f.readline()
    assert year == get_year(), 'Years are not equal'


def test_town():
    with open(townfile) as f:
        town = f.readline()
    assert town == get_town(), 'Towns are not equal'

import os
import pathlib

cwd = pathlib.Path(__file__).resolve().parent
parent = cwd.parents[0]
namefile = parent.parents[0] / 'name.txt'
yearfile = parent / 'year.txt'
townfile =cwd / 'town.txt'


def get_name():
    with open(namefile) as f:
        name = f.readline()
        return name


def get_year():
    with open(yearfile) as f:
        year = f.readline()
        return year


def get_town():
    with open(townfile) as f:
        town = f.readline()
        return town

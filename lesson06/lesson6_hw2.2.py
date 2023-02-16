# https://www.codewars.com/kata/583a8bde28019d615a000035/train/python

def find_odd_names(lst):
    developers = []
    for elem in lst:
        name = elem.get('firstName')
        total = sum(map(ord, name))
        if total % 2:
            developers.append(elem)
    return developers

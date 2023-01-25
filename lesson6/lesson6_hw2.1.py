# https://www.codewars.com/kata/5250a89b1625e5decd000413/train/python

def flatten(lst):
    final_list = []
    for elem in lst:
        if isinstance(elem, list):
            final_list.extend(elem)
        else:
            final_list.append(elem)
    return final_list

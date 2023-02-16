# https://www.codewars.com/kata/5825792ada030e9601000782/train/python

def zip_with(fn,a1,a2):
    values = zip(a1, a2)
    final_list = [fn(value[0],value[1]) for value in values]
    return final_list

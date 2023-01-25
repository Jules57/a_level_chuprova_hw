# https://www.codewars.com/kata/586909e4c66d18dd1800009b/train/python

def multiply_all(lst):
    def multiply_one(num):
        return [num * value for value in lst]
    return multiply_one

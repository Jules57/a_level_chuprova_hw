# https://www.codewars.com/kata/530017aac7c0f49926000084/train/python

def pluck(objs, name):
    final_list = [obj.get(name) for obj in objs]
    return final_list

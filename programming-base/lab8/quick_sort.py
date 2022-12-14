import random

def sort(array):
    if len(array) <= 1:
        return array
    else:
        q = random.choice(array)
        l_array = [n for n in array if n < q]
        e_array = [q] * array.count(q)
        b_array = [n for n in array if n > q]
        return sort(l_array) + e_array + sort(b_array)    


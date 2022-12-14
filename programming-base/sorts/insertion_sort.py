

def sort(array):
    r = range(len(array))

    for i in r:
        min = i
        for k in range(i, len(r)):
            if array[k] < array[i]:
                min = k

        array[i], array[min] = array[min], array[i]

    return array

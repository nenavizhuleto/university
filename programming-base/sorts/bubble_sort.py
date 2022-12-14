


def sort(array):
    r = range(len(array))
    for i in r:
        for j in r:
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]

    return array

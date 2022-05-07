def insert(array):

    n = len(array)

    for i in range(n):
        current = array[i]
        j = i - 1
        while j>=0 and array[j]>current:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = current
    return array

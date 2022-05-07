def select(array):

    n = len(array)

    for i in range(n):
        min = i
        for j in range(i+1, n):

            if array[min] > array[j]:
                min = j

        array[i], array[min] = array[min], array[i]

    return array


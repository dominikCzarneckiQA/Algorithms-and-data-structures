def quick(array):

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)

        return quick(less)+equal+quick(greater)

    else:  #Jeśli mamy jeden element w zbiorze, koniec dzialania, zwraca zbior posortowany
        return array

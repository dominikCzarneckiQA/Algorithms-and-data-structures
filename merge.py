def merge(array):
    n =len(array)

    if n < 2:
        return array
    
    result = []
    mid = int(n / 2)
    
    y = merge(array[:mid])
    z = merge(array[mid:])

    while (len(y) > 0) and (len(z) > 0):
        if y[0] > z[0]:
            result.append(z[0])
            z.pop(0)
        else:
            result.append(y[0])
            y.pop(0)

    result += y
    result += z
    return result



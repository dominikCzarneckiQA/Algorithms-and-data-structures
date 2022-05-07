def counting(array):

    n = len(array)
    temp = [0 for i in range(256)]
    out = [0 for i in range(n+1)]


    for j in range(n):
        num = array[j]
        temp[num] += 1

    for k in range(1, len(temp)):
        temp[k] += temp[k-1]

    for k in range(n):
        liczba = temp[array[k]]
        out[liczba] = array[k]
        temp[array[k]] -= 1

    out.pop(out[0])

    return out

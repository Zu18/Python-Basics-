def find_multiples(integer, limit):
    multiples = []
    n = 1
    multiple = integer
    while multiple < limit:
        multiple = integer * n
        if multiple > limit:
            break
        multiples.append(multiple)
        n += 1
    return multiples


print(find_multiples(5, 25)) # should return [5, 10, 15, 20, 25]
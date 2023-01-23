# input is an unsorted list of 3 positive integers
def pythagorean_triple(integers):
    # return True if it is possible to form a Pythagorean triple with the 3 integers
    # return False if it is not possible
    integers.sort()
    print(integers)
    if integers[2] ** 2 == integers[0]**2 + integers[1]**2:
        return True
    else:
        return False

print(pythagorean_triple([5,4,3]))

# or
# def pythagorean_triple(integers):
#     a, b, c = sorted(integers)
#     return a * a + b * b == c * c
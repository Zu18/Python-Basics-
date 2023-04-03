# Your task is to find the nearest square number, nearest_sq(n) or nearestSq(n),
# of a positive integer n.
# For example, if n = 111, then nearest\_sq(n) (nearestSq(n)) equals 121,
# since 111 is closer to 121, the square of 11, than 100, the square of 10.
# If the n is already the perfect square (e.g. n = 144, n = 81, etc.), you need to just return n.

import math
def nearest_sq(n):
    root = math.sqrt(n)
    if isinstance(root, int):
        return n
    root_prev = math.floor(root)
    root_next = root_prev + 1
    if (root_next ** 2 - n) < (n - root_prev ** 2):
        return root_next ** 2
    else:
        return root_prev ** 2

print(nearest_sq(9999))

# or
# def nearest_sq(n):
#     return round(n ** 0.5) ** 2
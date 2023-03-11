# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20


def century(year):
    year_str = str(year)
    if len(year_str) <=2:
        return 1
    century = int(year_str[0:-2])
    if year_str[-2:] != "00":
        century += 1
    return century


print(century(2101))
# Output should be equal to 22.

# or
# import math
# def century(year):
#     return math.ceil(year / 100)

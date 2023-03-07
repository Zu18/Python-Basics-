def number_to_pwr(number, power):
    result = 1
    i = 0
    while i < power:
        result *= number
        i += 1
    return result

print(number_to_pwr(10, 4)) # output should be 10000


# or for loop:
# def number_to_pwr(number, p):
#     result = 1
#     for i in range(p):
#         result *= number
#     return result
def subtract_sum(number):
    if number < 10 or number >10000:
        return("Incorrect input")
    fruits = {'kiwi':      [1, 3, 24, 26, 47, 49, 68, 70, 91, 93],
              'pear':      [2, 21, 23, 42, 44, 46, 65, 67, 69, 88],
              'banana':    [4, 6, 25, 29, 48, 50, 71, 73, 92, 94, 96],
              'melon':     [5, 7, 28, 30, 32, 51, 53, 74, 76, 95, 97],
              'pineapple': [8, 10, 12, 31, 33, 52, 56, 75, 77, 79, 98, 100],
              'apple':     [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99],
              'cucumber':  [11, 13, 34, 55, 57, 59, 78, 80],
              'orange':    [14, 16, 35, 37, 39, 58, 60, 83],
              'grape':     [15, 17, 19, 38, 40, 61, 82, 84, 86],
              'cherry':    [20, 22, 41, 43, 62, 64, 66, 85, 87, 89]}

    while True:
        number -= sum([int(n) for n in str(number)])
        if number < 100:
            for fruit, numbers in fruits.items():
                if number in numbers:
                    return fruit

print(subtract_sum(87))
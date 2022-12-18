''''
Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []

You can assume that all values are integers. Do not mutate the input array/list.
''''



def invert(list):
    new_list = []
    for number in list:
        opposite_num = number *(-1)
        new_list.append(opposite_num)
    return new_list



""""
def invert(lst):
    return [-x for x in lst]
""""
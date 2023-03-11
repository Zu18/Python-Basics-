def find(array, element):
    return array.index(element) if element in array else 'Not found'

print(find([2,3,5,7,11], 5))
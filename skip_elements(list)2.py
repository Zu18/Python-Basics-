#The skip_elements function has to return every other element from the list,
# using the enumerate function to check if an element is in an even position or an odd position.
# Return the list of the elements with even index.

def skip_elements(elements):
	new_result = []
	for index, element in enumerate(elements):
		# Find and add an element with even index in the new list
		if index%2 == 0:
			new_result.append(element)

	return new_result

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

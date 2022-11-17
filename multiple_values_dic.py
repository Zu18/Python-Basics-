# Print a line for each item of clothing with each color,
#  for example: "red shirt", "blue shirt", and so on.

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for key, values in wardrobe.items():
	for value in values:
		print("{} {}".format(value, key))

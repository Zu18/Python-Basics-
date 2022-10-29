# Method has to return first_name and the first initial of last_name followed by a period.
# Use the format method.
# For example, nametag("Jane", "Smith") should return "Jane S."

def nametag(first_name, last_name):
	return("{} {}.".format(first_name, last_name[0]))

print(nametag("Jane", "Smith"))
# Should display "Jane S."
print(nametag("Francesco", "Rinaldi"))
# Should display "Francesco R."
print(nametag("Jean-Luc", "Grand-Pierre"))
# Should display "Jean-Luc G."

# The groups_per_user function receives a dictionary,
# which contains group names with the list of users.
# Users can belong to multiple groups.
# Return a dictionary with the users as keys and a list of their groups as values. 


def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			# key = user, value is a list of user's groups
			user_groups.setdefault(user, []).append(group)
	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

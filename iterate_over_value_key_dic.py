# The email_list function receives a dictionary, which contains domain names as keys,
# and a list of users as values.
# Generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).

def email_list(domains):
    # Create a new list.
	emails = []
    # Itarete throuth the dictionary items
	for domain, users in domains.items():
      # To split a group of users into individual users
	  for user in users:
        # Add individual users in the new list  in format 'diana.prince@gmail.com'.
	    emails.append("{}@{}".format(user, domain))
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

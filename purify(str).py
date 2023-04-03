
def purify(str):
    result = []
    for i in range(len(str)):
        if is_i(str[i]):
            continue
        if str[i-1] == " " and str[i+1] == " ":
            result.append(" ")
        if i > 0 and is_i(str[i-1]):
            continue
        if i < len(str) - 1 and is_i(str[i+1]):
            continue

        result.append(str[i])
    return "".join(result).lstrip()


def is_i(char):
    return char in ["i", "I"]





print(purify("In heaven all the interesting people are simisng"))  #"heaven all the teresg people are g"
print(purify("1i2 33 i4i5 i555ii5"))


#final_list = list(set(item_list) - set(list_to_remove))
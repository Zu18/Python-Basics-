''''
Complete the solution so that it reverses all of the words within the string passed in.
Words are separated by exactly one space and there are no leading or trailing spaces.
Example(Input --> Output):
"The greatest victory is that which requires no battle" 
--> "battle no requires which that is victory greatest The"
'''


def reverse_words(text):
    reversed_text = []
    for word in text.split():
        reversed_text.insert(0, word)
    return ' '.join(reversed_text)


print(reverse_words("The greatest victory is that which requires no battle"))
# Should return: "battle no requires which that is victory greatest The".


''''
or 
def reverse_words(str):
    return " ".join(str.split(" ")[::-1])
''''
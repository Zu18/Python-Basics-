# Mission
# Your mission is to implement a function that converts the following potentially harmful characters:
#     < --> &lt;
#     > --> &gt;
#     " --> &quot;
#     & --> &amp;

import re
def html_special_chars(data):
    to_replace={'<': '&lt;', '>': '&gt;', '"': '&quot;', '&': '&amp;'}
    for char in data:
        if char in to_replace.keys():
            print(to_replace[char])
            data = re.sub(char, to_replace[char], data)
    return data


print(html_special_chars("<h2>Hello World</h2>"))

# or
# def html_special_chars(data):
#     hacksafe = {'<':'&lt;','>':'&gt;','"':'&quot;','&': '&amp;'}
#     return ''.join(hacksafe[i] if i in hacksafe else i for i in data)
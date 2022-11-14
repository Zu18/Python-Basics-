# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
#Martin and Johanna exchange ALL their apples with one another.
    x=0
    x=you.apples
    you.apples=me.apples
    me.apples=x
    return you.apples, me.apples

def exchange_ideas(you, me):
    #"you" and "me" will share the ideas with one another.
    # The numbers of ideas increases by number of received ideas
    count = you.ideas
    count += me.ideas
    you.ideas = count
    me.ideas = count
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))

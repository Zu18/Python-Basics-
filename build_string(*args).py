def build_string(*args):
    return "I like {args}!".format(args =", ".join(args))


print(build_string('Cheese','Milk','Chocolate'))
# output should be 'I like Cheese, Milk, Chocolate!'

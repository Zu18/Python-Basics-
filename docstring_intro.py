class Person:
  def __init__(self, name):
    self.name = name
  def greeting(self):
    """Outputs a message with the name of the person."""
    print("Hello! My name is {name}.".format(name=self.name))
  # use indentation before calling the 'help' function
  help(greeting)
# use help(class.method)
help(Person.greeting)

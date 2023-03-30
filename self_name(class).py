from preloaded import Animal

class Cat(Animal):
    def speak(self):
        return self.name + ' meows.'


# should return the cats name + meows. e.g. 'Mr Whiskers meows.'

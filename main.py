class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # @classmethod  # talk = classmethod(talk)
    def talk():  # cls即为类自身
        print("talk calling")


p = Person('rhx', 25)
print(Person.talk())
print(p.talk())
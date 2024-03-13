class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old")

person = person("Jesee",20)

print(person.name)
print(person.age)
person.greet()

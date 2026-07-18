class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

    def have_birthday(self):
        self.age += 1
        print(f"Happy birthday {self.name}! Now I'm {self.age} years old.")

# Creating objects
person1 = Person("Natalie", 26)
person2 = Person("Damien", 34)

person1.introduce()
person2.introduce()

person1.have_birthday()
person1.introduce()
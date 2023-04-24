from os import system
import random

system("clear")


class Animal(object):
    animal_categories = []

    # Each animal should at least have a name, an age, a health level, and happiness level
    def __init__(self, data):
        print(data)
        self.name = data["name"]
        self.category = data["category"]
        self.age = data["age"]
        self.gender = data["gender"]
        self.health = 10
        self.happiness = 100

        if self.category not in Animal.animal_categories:
            Animal.animal_categories.append(self.category)

        self.tag_number = self.tagging(self.category)

    def getName(self):
        return self.name

    def getCategory(self):
        return self.category

    def getAge(self):
        return self.age

    def getGender(self):
        return self.gender

    def getHealth(self):
        return self.health

    def getHappiness(self):
        return self.happiness

    def changeName(self, name):
        self.name = name
        return self

    def increaseHealth(self, health):
        if self.health + health >= 10 or health >= 10:
            self.health = 10
            print(f"{self.name} has full Health!")
        elif health < 0:
            self.health += 0
        else:
            self.health += health
        return self

    def decreaseHealth(self, health):
        if (self.health - health) <= 0 or health >= 10:
            self.health = 0
            print(f"{self.name} has died!")
        else:
            self.health -= health
        return self

    def increaseHappiness(self, happiness):
        if (self.happiness + happiness) >= 100 or happiness >= 100:
            self.happiness = 100
            print(f"{self.name} has full Happiness!")
        else:
            self.happiness += happiness
        return self

    def decreaseHappiness(self, happiness):
        if (self.happiness - happiness) <= 0 or happiness >= 100:
            self.happiness = 0
            print(f"{self.name} NEEDS SOME LOVIN'!")
        else:
            self.happiness = self.happiness - happiness
        return self

    def __str__(self):
        return f"=== {self.category} ===\n{self.name}, age {self.age}\nGender: {self.gender}\nHealth: {self.health}\nHappiness: {self.happiness}\n"

    def display_info(self):
        print(f"{'*' * 10}- ANIMAL -{'*' * 10}")
        print("Category:", self.category.upper())
        print("Name:", self.name.title())
        print("Gender:", self.gender)
        print("Age:", self.age)
        print("Health:", self.health)
        print("Happiness:", self.happiness)
        print("*" * 20)
        print()

    def feed(self):
        print(f"{self.name} has eaten!")
        self.increaseHealth(1)
        self.increaseHappiness(10)
        return self

    def sleep(self):
        print(f"{self.name} has slept!")
        self.increaseHealth(2)
        self.decreaseHappiness(20)
        return self

    def play(self):
        print(f"{self.name} has played!")
        self.decreaseHealth(3)
        self.increaseHappiness(30)
        return self

    def exercise(self):
        print(f"{self.name} has exercised!")
        self.increaseHealth(3)
        self.decreaseHappiness(30)
        return self

    def birthday(self):
        print(f"{self.name} had a birthday!")
        self.age += 1
        return self

    @classmethod
    def tagging(cls, prefix):
        tag_num = ""
        # create a 3 digit random number between 100 and 999
        rand_num = random.randint(100, 999)
        tag_num = f"{prefix[0:3]}-{rand_num}"
        return tag_num


# a1 = Animal("Charlie", "Lion", 5, "Male")
# print(a1)
# a1.display_info()
# a1.looseHealth_and_Happiness().looseHealth_and_Happiness().display_info()
# a1.feed().display_info()
# a1.sleep().display_info()
#
#
#
print()

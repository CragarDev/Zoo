from animal import Animal
from elephant import Elephant
from lion import Lion
from gorilla import Gorilla
import random
from os import system

system("clear")


print()

# * Assignment: Zoo

"""

Objectives:

Practice utilizing inheritance
More practice with associations between classes
Practice overriding methods
See polymorphism in action

Imagine a game where you can create a zoo and start raising different types of animals. 
Say that for each zoo you create can have several different animals. 

Start by creating an Animal class, and then at least 3 specific animal classes that inherit from Animal. 
(Maybe lions and tigers and bears, oh my!) 
.Each animal should at least have a name, an age, a health level, and happiness level 

The Animal class should have a display_info method that shows the animal's name, health, and happiness. 
It should also have a feed method that increases health and happiness by 10.

In at least one of the Animal child classes you've created, add at least one unique attribute. 
Give each animal different default levels of health and happiness. 
The animals should also respond to the feed method with varying levels of changes to health and happiness.

Once you've tested out your different animals and feel more comfortable with inheritance, 
create a Zoo class to help manage all your animals.

One way you could put together this zoo is by doing the following:

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name):
        self.animals.append( Lion(name) )
    def add_tiger(self, name):
        self.animals.append( Tiger(name) )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.print_all_info()

Hopefully this seems a little bit repetitive, 
and you can use your skills and knowledge to reduce some of the code above, 
and have fun making a zoo in the process!

This assignment is deliberately open-ended. Have fun!

"""


class Zoo(object):
    def __init__(self, zoo_name):
        self.animals = []
        self.animal_dict = {}
        self.zoo_name = zoo_name

    def add_animal(self, data):
        # print("-" * 30, "TESTING", "-" * 30)
        # print("IN ADD ANIMAL")
        # print(data["animal_name"])
        # print("-" * 30, "-------", "-" * 30)

        animal_file_name = data["animal_name"].lower()

        if data["category"] == "Lion":
            data["animal_name"] = Lion(data)
        elif data["category"] == "Gorilla":
            data["animal_name"] = Gorilla(data)
        elif data["category"] == "Elephant":
            data["animal_name"] = Elephant(data)
        else:
            print("Please enter a valid category")

        self.animals.append(data["animal_name"])
        self.animal_dict[animal_file_name] = data["animal_name"]
        print()
        print(f"{data['animal_name'].name} has been added to the {self.zoo_name} zoo!")
        print()
        data["animal_name"].display_info()

        return self

    def display_animals(self):
        print("-" * 30, self.zoo_name, "-" * 30)
        print(f"All the animals in the {self.zoo_name} zoo are:")
        for animal in self.animals:
            animal.display_info()
            print()
        return self


# * Create a Zoo

cragars_zoo = Zoo("Cragar's Zoo")

tom_data = {
    "animal_name": "tom",
    "name": "Tom",
    "category": "Lion",
    "age": 5,
    "gender": "male",
    "weight": 200,
}
cragars_zoo.add_animal(tom_data)

katina_data = {
    "animal_name": "katina",
    "name": "Katina",
    "category": "Lion",
    "age": 6,
    "gender": "female",
    "weight": 225,
}
cragars_zoo.add_animal(katina_data)

sydney_data = {
    "animal_name": "sydney",
    "name": "Sydney",
    "category": "Lion",
    "age": 9,
    "gender": "male",
    "weight": 265,
}
cragars_zoo.add_animal(sydney_data)


georgette_data = {
    "animal_name": "georgette",
    "name": "Georgette",
    "category": "Gorilla",
    "age": 23,
    "gender": "female",
    "weight": 625,
}
cragars_zoo.add_animal(georgette_data)


brutus_data = {
    "animal_name": "brutus",
    "name": "Brutus",
    "category": "Gorilla",
    "age": 3,
    "gender": "male",
    "weight": 327,
}
cragars_zoo.add_animal(brutus_data)


nutney_data = {
    "animal_name": "nutney",
    "name": "Nutney",
    "category": "Gorilla",
    "age": 18,
    "gender": "male",
    "weight": 925,
}
cragars_zoo.add_animal(nutney_data)


bertha_data = {
    "animal_name": "bertha",
    "name": "Bertha",
    "category": "Elephant",
    "age": 76,
    "gender": "female",
    "weight": 2379,
}
cragars_zoo.add_animal(bertha_data)

ray_data = {
    "animal_name": "ray",
    "name": "Ray",
    "category": "Elephant",
    "age": 42,
    "gender": "male",
    "weight": 3379,
}
cragars_zoo.add_animal(ray_data)

lidia_data = {
    "animal_name": "lidia",
    "name": "Lidia",
    "category": "Elephant",
    "age": 6,
    "gender": "female",
    "weight": 861,
}
cragars_zoo.add_animal(lidia_data)

print()

# print(cragars_zoo.animal_dict)
for key, value in cragars_zoo.animal_dict.items():
    print(key, value)

print()

cragars_zoo.animal_dict["tom"].feed().display_info()
cragars_zoo.animal_dict["katina"].feed().display_info()


print(cragars_zoo.animals)
print()
cragars_zoo.display_animals()
print()
print("-" * 30, "TESTING", "-" * 30)
print(cragars_zoo.animals)
print()
for animal in cragars_zoo.animals:
    print(f"{animal.category}: {animal.name}")
    print()
print("-" * 30, "======", "-" * 30)


# 10 Random attacks and feedings

for i in range(1, 10):
    while True:
        random_animal1 = random.choice(cragars_zoo.animals)
        random_animal2 = random.choice(cragars_zoo.animals)
        if random_animal1 != random_animal2:
            break

    print("*" * 30, f"ATTACK _{i}_", "*" * 30)
    random_animal1.display_info()
    random_animal2.display_info()
    print()
    print()
    random_animal1.attack(random_animal2)
    print()
    random_animal1.display_info()
    random_animal2.display_info()

    while True:
        random_animal3 = random.choice(cragars_zoo.animals)
        random_animal4 = random.choice(cragars_zoo.animals)
        if random_animal3 != random_animal4:
            break

    print(":) " * 15, f"FEEDING TIME _{i}_")
    print()
    random_animal3.display_info()
    random_animal4.display_info()
    print()
    print()
    random_animal3.feed()
    random_animal4.feed()
    print()
    random_animal3.display_info()
    random_animal4.display_info()

#
#
#
print()

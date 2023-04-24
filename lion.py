from os import system
from animal import Animal
import random

system("clear")
print()


class Lion(Animal):
    def __init__(self, data):
        super().__init__(data)
        self.weight = data["weight"]

    def __str__(self):
        return f"Lion: {str(self.name)} - {str(self.age)} - {str(self.health)} - {str(self.happiness)}"

    def attack(self, other=None):
        attack_power = random.randint(1, 4)
        if other is None:
            print(f"{self.name} attacked nothing with the power of {attack_power}!")
            self.decreaseHealth(attack_power / 2)
            self.decreaseHappiness((attack_power * 10) / 2)
            return self
        else:
            print(f"{self.name} attacked {other.name} with power of {attack_power}!")
            other.decreaseHealth(attack_power)
            other.decreaseHappiness(attack_power * 10)
            self.decreaseHealth(attack_power / 3)
            self.decreaseHappiness((attack_power * 10) / 3)
        return self


# tom_data = {
#     "name": "Tom",
#     "category": "Elephant",
#     "age": 5,
#     "gender": "male",
#     "weight": 200,
# }
# tom = Lion(tom_data)

# print(tom)
# tom.display_info()
# print(tom.getName())
# print(tom.getCategory())
# print(tom.getAge())
# print(tom.getGender())
# print(tom.getHealth())
# print(tom.getHappiness())
# print(tom.tag_number)

# tom.changeName("Tommy")
# tom.birthday()
# print()

# tom.display_info()
# print()


# tom.feed().display_info()
# tom.sleep().display_info()
# tom.play().display_info()
# tom.exercise().display_info()
# print()
# tom.display_info()
# print()
# tom.attack().attack().attack()
# print()
# tom.display_info()
# print()
#
#
#
print()

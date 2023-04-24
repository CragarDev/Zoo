from os import system
from animal import Animal
import random

system("clear")
print()


class Gorilla(Animal):
    def __init__(self, data):
        super().__init__(data)
        self.weight = data["weight"]

    def __str__(self):
        return f"Gorilla: {str(self.name)} - {str(self.age)} - {str(self.health)} - {str(self.happiness)}"

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


# georgette_data = {
#     "name": "Georgette",
#     "category": "Gorilla",
#     "age": 23,
#     "gender": "female",
#     "weight": 625,
# }
# georgette = Gorilla(georgette_data)

# print(georgette)
# georgette.display_info()
# print(georgette.getName())
# print(georgette.getCategory())
# print(georgette.getAge())
# print(georgette.getGender())
# print(georgette.getHealth())
# print(georgette.getHappiness())
# print(georgette.tag_number)

# georgette.changeName("Georgetta the Great")
# georgette.birthday()
# print()

# georgette.display_info()
# print()


# georgette.feed().display_info()
# georgette.sleep().display_info()
# georgette.play().display_info()
# georgette.exercise().display_info()
# print()
# georgette.display_info()
# print()
# georgette.attack().attack().attack()
# print()
# georgette.display_info()
# print()
#
#
#
print()

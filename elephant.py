from os import system
from animal import Animal
import random

system("clear")
print()


class Elephant(Animal):
    def __init__(self, data):
        print(data)
        super().__init__(data)
        self.weight = data["weight"]

    def __str__(self):
        return f"Elephant: {str(self.name)} - {str(self.age)} - {str(self.health)} - {str(self.happiness)}"

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


# bertha_data = {
#     "name": "Bertha",
#     "category": "Elephant",
#     "age": 76,
#     "gender": "female",
#     "weight": 2379,
# }
# bertha = Elephant(bertha_data)
# print(bertha)
# bertha.display_info()
# print(bertha.getName())
# print(bertha.getCategory())
# print(bertha.getAge())
# print(bertha.getGender())
# print(bertha.getHealth())
# print(bertha.getHappiness())
# print(bertha.tag_number)

# bertha.changeName("Big Bertha")
# bertha.birthday()
# print()

# bertha.display_info()
# print()


# bertha.feed().display_info()
# bertha.sleep().display_info()
# bertha.play().display_info()
# bertha.exercise().display_info()
# print()
# bertha.display_info()
# print()
# bertha.attack().attack().attack()
# print()
# bertha.display_info()
# print()
#
#
#
print()

import random
from plants import Tomato, Lettuce, Carrot, Strawberry, Potato

plant_types = ["tomato", "lettuce", "carrot", "strawberry", "potato"]

class Gardener:
    plant_dict = {
        "tomato": Tomato,
        "lettuce": Lettuce,
        "carrot": Carrot,
        "strawberry": Strawberry,
        "potato": Potato,
    }

    def __init__(self, gardener_name):
        self.__gardener_name = gardener_name
        self.__planted_plants = []
        self.__inventory = {
            "tomato": 1,
            "lettuce": 5,
            "carrot": 8,
            "strawberry": 12,
            "potato": 6,
        }

    def get_name(self):
        return self.__gardener_name

    def plant(self):
        choice = input("Enter plant type: ").lower()
        if choice in self.__inventory and self.__inventory[choice] > 0:
            self.__inventory[choice] -= 1
            new_plant = self.plant_dict[choice]()
            self.__planted_plants.append(new_plant)
            print(f"{self.__gardener_name} planted a {choice}.")
        else:
            print(f"No {choice} seeds available.")

    def tend(self):
        for plant in self.__planted_plants:
            if plant.is_harvestable():
                print(f"{plant.get_name()} is ready to harvest!")
            else:
                plant.grow()
            print(f"{plant.get_name()} is at the {plant.get_stage()} stage.")

    def harvest(self):
        if not self.__planted_plants:
            print("No plants to harvest.")
            return
        plant = self.__planted_plants[0]
        yield_amt = plant.harvest()
        if yield_amt:
            plant_name = plant.get_name().lower()
            self.__inventory[plant_name] = self.__inventory.get(plant_name, 0) + yield_amt
            print(f"You harvested a {plant.get_name()}!")
            self.__planted_plants.remove(plant)

    def forage_for_seeds(self):
        seed = random.choice(plant_types)
        self.__inventory[seed] = self.__inventory.get(seed, 0) + 1
        print(f"{self.__gardener_name} found a {seed} seed!")

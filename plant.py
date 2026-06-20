class Plant:
    def __init__(self, plant_name, harvest_yield):
        self.__plant_name = plant_name
        self.__harvest_yield = harvest_yield
        self.__growth_stages = ["seed", "sprout", "plant", "flower", "harvest_ready"]
        self.__current_stage = self.__growth_stages[0]
        self.__harvestable = False

    # Encapsulation: getters
    def get_name(self):
        return self.__plant_name

    def get_stage(self):
        return self.__current_stage

    def is_harvestable(self):
        return self.__harvestable

    # Abstraction: grow logic
    def grow(self):
        index = self.__growth_stages.index(self.__current_stage)
        if index < len(self.__growth_stages) - 1:
            self.__current_stage = self.__growth_stages[index + 1]
        if self.__current_stage == self.__growth_stages[-1]:
            self.__harvestable = True
            print(f"{self.__plant_name} is fully grown!")

    # Abstraction: harvest method
    def harvest(self):
        if self.__harvestable:
            self.__harvestable = False
            return self.__harvest_yield
        else:
            print(f"{self.__plant_name} is not harvestable yet.")
            return None

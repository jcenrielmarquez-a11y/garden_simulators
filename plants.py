from plant import Plant

class Tomato(Plant):
    def __init__(self):
        super().__init__("Tomato", 5)

    def harvest(self):
        print("You picked ripe tomatoes!")
        return super().harvest()

class Lettuce(Plant):
    def __init__(self):
        super().__init__("Lettuce", 1)

class Carrot(Plant):
    def __init__(self):
        super().__init__("Carrot", 3)

    def harvest(self):
        print("You pulled a crunchy carrot!")
        return super().harvest()

class Strawberry(Plant):
    def __init__(self):
        super().__init__("Strawberry", 4)

class Potato(Plant):
    def __init__(self):
        super().__init__("Potato", 6)

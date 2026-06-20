from gardener import Gardener

class GameEngine:
    def __init__(self, game_title):
        self.game_title = game_title
        player_name = input(f"Welcome to {game_title}. Please enter your name: ")
        self.gardener = Gardener(player_name)

    def run(self):
        print(f"Welcome {self.gardener.get_name()}! Type 'help' for commands.")
        while True:
            command = input("\nWhat would you like to do? ").lower()
            match command:
                case "forage":
                    self.gardener.forage_for_seeds()
                case "plant":
                    self.gardener.plant()
                case "tend":
                    self.gardener.tend()
                case "harvest":
                    self.gardener.harvest()
                case "quit":
                    print(f"Goodbye {self.gardener.get_name()}! Thanks for playing {self.game_title}.")
                    break
                case "help":
                    print("Commands: forage, plant, tend, harvest, quit")
                case _:
                    print("Invalid command.")

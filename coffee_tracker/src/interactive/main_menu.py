
from interactive_menu.src.interactive_menu import InteractiveMenu


class MainMenu(InteractiveMenu):

    def __init__(self, manager, path=[]):
        super().__init__(manager, path)
        self.sub_menu_modules = [
            RecordCoffeeMenu(manager, self.path),
            ReadCoffeeMenu(manager, self.path)
        ]

    def title(self):
        return "Main"

class RecordCoffeeMenu(InteractiveMenu):

    def title(self):
        return "Record"

    def main_loop(self):
        print("Describe the coffee")
        description = self.fancy_input()
        print("How many oz?")
        oz = self.fancy_input()
        oz = float(oz)
        print("")
        print("Description: %s" % description)
        print("Oz: %f" % oz)
        print("")
        print("Ok?")
        print("")
        answer = self.fancy_input()
        if answer in ["yes", "Yes", "ok", "OK"]:
            self.manager.record_coffee(description, oz)
        else:
            print("Aborting!")


class ReadCoffeeMenu(InteractiveMenu):

    def title(self):
        return "Read"

    def main_loop(self):
        coffees = self.manager.get_coffees()
        for coffee in coffees:
            print(coffee)

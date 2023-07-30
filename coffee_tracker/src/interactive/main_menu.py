from datetime import datetime
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
        form_results = self.interactive_form(
            [
                {
                    "question": "Describe the coffee",
                    "expected_response_type": "VARCHAR",
                    "return_as": "description",
                    "default": "",
                    "allow_empty": False
                },
                {
                    "question": "How many oz?",
                    "expected_response_type": "FLOAT",
                    "return_as": "oz",
                    "default": "",
                    "allow_empty": False
                },
                {
                    "question": "What date? (YYYY-MM-DD) Hit enter for today",
                    "expected_response_type": "YYYYMMDD_Date",
                    "return_as": "date",
                    "default": datetime.now().strftime("%Y-%m-%d"),
                    "allow_empty": False
                }
            ]
        )
        if form_results["user_accept"] != True:
            print("Aborting!")
            return
        form_results.pop("user_accept")
        for answer_key in form_results.keys():
            if not form_results[answer_key]["valid"]:
                print("%s is not a valid value! Aborting" % answer_key)
                return

        description = form_results["description"]["value"]
        oz = form_results["oz"]["value"]
        date = form_results["date"]["value"]

        self.manager.record_coffee(description, oz, date)

class ReadCoffeeMenu(InteractiveMenu):

    def title(self):
        return "Read"

    def main_loop(self):
        coffees = self.manager.get_coffees()
        for coffee in coffees:
            print(coffee)

import copy
import messages

class CoffeeMaker:
    INIT_RESOURCES = {
        "coffee": 500,
        "water": 1000,
        "milk": 500
    }

    def __init__(self):
        self.resources = self.INIT_RESOURCES.copy()

    def refill_resources(self, missing_resources):
        for missing in missing_resources:
            self.resources[missing] = self.INIT_RESOURCES[missing]

    def can_make_drink(self, drink):
        return (self.resources["water"] >= drink.ingredients["water"] and
                self.resources["coffee"] >= drink.ingredients["coffee"] and
                self.resources["milk"] >= drink.ingredients["milk"])
        
    def check_what_is_missing(self, drink):
        missing_resources = {}
        for ingredient, amount in drink.ingredients.items():
            if self.resources[ingredient] < amount:
                missing_resources[ingredient] = amount - self.resources[ingredient]
        return missing_resources
        
    def make_drink(self, drink):
        for resource in self.resources:
            self.resources[resource] -= drink.ingredients[resource]
    
    def ask_yes_no(self, question, valid=('yes', 'no'), quit_key='q'):
        answers = {
            valid[0]: True,
            valid[1]: False,
            quit_key: None,
        }

        while True:
            choice = input(question).strip().lower()
            if choice in answers:
                return answers[choice]
            
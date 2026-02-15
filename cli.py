import time
from messages import *

class CLI:
    def show_welcome(self):
        print(WELCOME_MSG)

    def show_menu(self, drinks):
        print(DRINKS_LABEL)
        for i, drink in enumerate(drinks, start=1):
            print(f"{i}. {drink.name:25} - ${drink.price_cents/100:.2f}")

    def ask_for_drink(self, drinks):
        while True:
            raw = input(CHOOSE_DRINK_QUESTION).strip().lower()

            if raw == 'q':
                return None

            if raw.isdigit() and 1 <= int(raw) <= len(drinks):
                return int(raw)
            
            print(ask_drink_instruction(drinks))

    def show_missing_resources(self, missing_resources):
        print(NOT_ENOUGH_RESOURCE)
        for name, amount in missing_resources.items():
            print(f" - {name}: {amount} {'g' if name == 'coffee' else 'ml'}")

    def ask_yes_no(self, question):
        answers = {
            'yes': True,
            'no': False,
            'q': None
        }

        while True:
            choice = input(question).strip().lower()
            if choice in answers:
                return answers[choice]

            print(TYPE_YES_NO)

    def show_refilled_resources(self, missing_resources):
        print(REFILLED_RESOURCES)
        for name in missing_resources:
            print(f"*** {name} ***")

    def show_current_resources(self, resources):
        print(CURRENT_RESOURCES)
        for name, amount in resources.items():
            print(f" - {name}: {amount} {'g' if name == 'coffee' else 'ml'}")
    
    def show_status_make_drink(self, drink):
        print(MAKING_DRINK)
        time.sleep(1)
        print(enjoy_drink(drink.name))

    def show_choice(self, choice, true_choice, false_choice):
        if choice is None:
            return
        if choice:            
            print(true_choice)
        else:
            print(false_choice)           
            
    def show_goodbye(self):
        print(GOODBYE)

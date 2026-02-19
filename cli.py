import time
from messages import *
from decimal import Decimal

class CLI:
    def show_load_status(self, status):
        print(STATE_LOAD_SUCCESS) if status else print(STATE_LOAD_ERROR)

    def show_save_status(self, status):
        print(STATE_SAVE_SUCCESS) if status else print(STATE_SAVE_ERROR)

    def show_welcome(self):
        print(WELCOME_MSG)

    def show_menu(self, drinks):
        print(DRINKS_LABEL)
        for i, drink in enumerate(drinks, start=1):
            print(f"{i}. {drink.name:25} - ${drink.price_cents/100:.2f}")
            

    def ask_for_drink(self: object, drinks: ):
        while True:
            raw = input(CHOOSE_DRINK_QUESTION).strip().lower()

            if raw == 'q':
                return None
            
            if raw == 'r':
                return -1
            
            if raw == 's':
                return -2

            if raw.isdigit() and 1 <= int(raw) <= len(drinks):
                return int(raw)
            
            print((drinks))

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

    def show_statistics(self, profit, drinks_counter):
        print(CURRENT_STATISTICS)
        print(f" - {PROFIT} ${profit/100:.2f}")
        print(f" - {NUM_DRINKS} {drinks_counter}")

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

    def map_coins_to_show(self, coins_cents):
        return ' '.join(f'${coin/100:.2f}' for coin in coins_cents)

    def ask_for_money(self, drink, accepted_coins):
        inserted_coins_cents = []

        print(insert_money(drink.price_cents))
        print(f"{ACCEPTED_COINS} {self.map_coins_to_show(accepted_coins)}")

        while sum(inserted_coins_cents) < drink.price_cents:
            coin = Decimal(input(PLEASE_INSERT))
            coin_cents = coin * 100

            if not coin_cents in accepted_coins:
                print(INVALID_COIN)
                continue

            inserted_coins_cents.append(coin_cents)
            sum_coins = sum(inserted_coins_cents)

            print(f"{PAID} ${sum_coins/100:.2f}")
            print(f"{REMAINING} ${(drink.price_cents - sum_coins)/100 if drink.price_cents >= sum_coins else 0:.2f}")

        print(f"{INSERTED_COINS} {self.map_coins_to_show(inserted_coins_cents)}")

        return inserted_coins_cents
    
    def ask_for_continue_drink(self: object, change_coins: int, missing_change: int):
        """
        Ask the user if he accept, that change cannot be given, or only part of the change can be given

        change_coins: int change in cents is possible
        missing_change: int rest of the change in cents is inpossible to be given
        
        return: True if the user accepts the change, False otherwise
        """
        if not change_coins:
            print(CHANGE_ERROR_1)
        else:
            print(change_error_2(change_coins, missing_change))

        return self.ask_yes_no(ACCEPT_CHANGE)

    def show_refund_money(self, inserted_coins: list[int]):
        """
        Shows the coins that will be returned to the user (the ones he inserted)

        inserted_coins: list of inserted coins
        
        """
        print(f"{NOT_ACCEPT_CHANGE} {self.map_coins_to_show(inserted_coins)}")

    def show_payment_result(self, change_coins, missing_change):
        if not change_coins and missing_change == 0:
            print(CHANGE_0)
            return
        print(f"{CHANGE} ${sum(change_coins)/100:.2f}")
        print(f"{CHANGE_COINS} {self.map_coins_to_show(change_coins)}")

    def show_goodbye(self):     
        print(GOODBYE)
        
def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

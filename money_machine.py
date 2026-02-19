import copy

class MoneyMachine:
    INITIAL_COINS = {
        10: 1,   #denom in cents: amount
        25: 1,
        50: 1,
        100: 1,
        500: 1
    }

    ACCEPTED_COINS = [10, 25, 50, 100, 500]

    

    def __init__(self):
        self.coins = copy.deepcopy(self.INITIAL_COINS)
        self.profit = 0.0

    def calculate_missing_change(self, inserted_coins, change_coins, drink_price):
        return sum(inserted_coins) - drink_price - sum(change_coins)
        
    def make_payment(self, inserted_coins, drink):
        machine_current_coins = copy.deepcopy(self.coins)   #make a copy of money maschine

        for coin in inserted_coins:
            machine_current_coins[coin] += 1

        change_coins = self.calculate_change(sum(inserted_coins), drink.price_cents, machine_current_coins)

        if self.calculate_missing_change(inserted_coins, change_coins, drink.price_cents) == 0:        
            self.coins = copy.deepcopy(machine_current_coins)
            self.profit += drink.price_cents

        return change_coins

    def calculate_change(self, sum_coins, price, machine_coins):
        change_coins = []
        change = sum_coins - price

        if change == 0:
            return change_coins
        
        sorted_machine_coins = sorted(machine_coins, reverse="True")
                
        for coin in sorted_machine_coins:
            
            while change >= coin:
                if machine_coins[coin] == 0:
                    break
                change -= coin
                machine_coins[coin] -= 1
                change_coins.append(coin)
        
        return change_coins      

    def continue_drink_without_change(self, inserted_coins, change_coins):
        for coin in inserted_coins:
            self.coins[coin] += 1

        for coin in change_coins:
            self.coins[coin] -=1

        self.profit += (sum(inserted_coins) - sum(change_coins))



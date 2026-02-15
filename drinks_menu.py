from drink_item import DrinkItem

class DrinksMenu:
    def __init__(self):
        self.drinks = [
            DrinkItem("Espresso", coffee_g=10, water_ml=50, milk_ml=0, price_cents=150),
            DrinkItem("Americano", coffee_g=10, water_ml=150, milk_ml=0, price_cents=200),
            DrinkItem("Latte", coffee_g=10, water_ml=50, milk_ml=100, price_cents=250),
            DrinkItem("Cappuccino", coffee_g=10, water_ml=50, milk_ml=50, price_cents=250),
            DrinkItem("Mocha", coffee_g=10, water_ml=50, milk_ml=100, price_cents=300),
            DrinkItem("Flat White", coffee_g=10, water_ml=50, milk_ml=150, price_cents=250),
            DrinkItem("Macchiato", coffee_g=10, water_ml=50, milk_ml=20, price_cents=200),
            DrinkItem("Affogato", coffee_g=10, water_ml=0, milk_ml=0, price_cents=200)
        ]
    
    def add_drink(self, drink):
        self.drinks.append(drink)
    
    def get_drink_by_name(self, name):
        for drink in self.drinks:
            if drink.name == name:
                return drink
        return False
    
    def choice_drink(self, choice):
        if 1 <= choice <= len(self.drinks):
            return self.drinks[choice - 1]
        else:
            return None
        

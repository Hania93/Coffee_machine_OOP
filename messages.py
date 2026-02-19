REFILL_RESOURCES_QUESTION = "Do you want to refill missing ingredients? Type 'yes' or 'no'. If you want quit, type 'q' "

def chosen_drink_question(drink_name: str) -> str:
    return f"Do you want to make now the drink you previously selected: {drink_name}? Type 'yes' or 'no'. If you want quit, type 'q' "

def true_choice_drink(drink: object) -> str:
    return f"\n✅ You have selected: {drink.name}, which costs ${drink.price_cents/100:.2f}"

FALSE_CHOICE_DRINK = "\n❌ Invalid choice. Please try again."
     
TRUE_CHOICE_REFILL = "\n✅ Replenishing missing resources"

FALSE_CHOICE_REFILL = "\n❌ You didn't add the missing resources. You can try choosing a different drink."

ASK_SELECT_DRINK = "\nDo you want to select now a drink? Type 'yes' or 'q'"

WELCOME_MSG = "☕ Welcome to the Coffee Machine!"
DRINKS_LABEL = "\n📋 Available drinks:"
CHOOSE_DRINK_QUESTION = "\nChoose a drink number (or 'q' - quit, 'r' - report current resources of coffee machine, 's' - report statistics.): "

def ask_drink_instruction(drinks: list) -> str:
    return f"\n❌ Type number from 1 to {len(drinks)} or: 'q' - quit, 'r' - report current resources of coffee machine, 's' - report statistics."

NOT_ENOUGH_RESOURCE = "\n❌ Not enough resources. Missing:"
TYPE_YES_NO = "\n❌ Type 'yes', 'no' or 'q'."
REFILLED_RESOURCES = "\n✅ Refilled resources:"
CURRENT_RESOURCES = "\n📦 Current resources:"
CURRENT_STATISTICS = "\n📦 Current statistics:"
PROFIT = "Profit: "
NUM_DRINKS = "Number of drinks made:"
MAKING_DRINK = "\n☕ Making a drink..."

def insert_money(price: int):
    return(f"Please insert {price/100:.2f} in coins: ")

ACCEPTED_COINS = "Accepted coins:"
PLEASE_INSERT = "Please insert coin:"
INVALID_COIN = "Invalid coin!"
PAID = "Paid: "
REMAINING = "Remaining:"
INSERTED_COINS = "Inserted coins:"
CHANGE_ERROR_1 = "Change cannot be given!"
ACCEPT_CHANGE = "If you accept this, you can continue making the drink (type 'yes'), and if not (type 'no'), you will receive a refund."
NOT_ACCEPT_CHANGE = "Your drink preparation has been interrupted. Claim your deposit:"
CHANGE_0 = "You've paid exactly the price of your chosen drink. Your change is 0."
CHANGE = "Your change:"
CHANGE_COINS = "Take your change here:"

def change_error_2(change_coins: int, missing_change: int):
    return(f"Can't spend all the change. Should spend ${(sum(change_coins) + missing_change)/100:.2f} change, but only ${sum(change_coins)/100:.2f} is possible.If you accept this, you can continue making the drink ('yes'), and if not ('no'), you will receive a refund.")

STATE_SAVE_SUCCESS = "The state was successfully saved to the file"
STATE_SAVE_ERROR = "Could not save state to file"
STATE_LOAD_SUCCESS = "The state was successfully loaded from file"
STATE_LOAD_ERROR = "The state file is missing or corrupt. I'm using the default state."

def enjoy_drink(drink_name: str) -> str:
    return f"\n🎉 Enjoy your {drink_name}!"

GOODBYE = "\n👋 Good Bye! See you next time!"

REFILL_RESOURCES_QUESTION = "Do you want to refill missing ingredients? Type 'yes' or 'no'. If you want quit, type 'q' "

def chosen_drink_question(drink_name: str) -> str:
    return f"Do you want to make now the drink you previously selected: {drink_name}? Type 'yes' or 'no'. If you want quit, type 'q' "

def true_choice_drink(drink: object) -> str:
    return f"\n✅ You have selected: {drink.name}, which costs {drink.price_cents} cents."

FALSE_CHOICE_DRINK = "\n❌ Invalid choice. Please try again."
     
TRUE_CHOICE_REFILL = "\n✅ Replenishing missing resources"

FALSE_CHOICE_REFILL = "\n❌ You didn't add the missing resources. You can try choosing a different drink."                

WELCOME_MSG = "☕ Welcome to the Coffee Machine!"
DRINKS_LABEL = "\n📋 Available drinks:"
CHOOSE_DRINK_QUESTION = "\nChoose a drink number (or 'q' to quit): "

def ask_drink_instruction(drinks: list) -> str:
    return f"\n❌ Type number from 1 to {len(drinks)} or 'q'."

NOT_ENOUGH_RESOURCE = "\n❌ Not enough resources. Missing:"
TYPE_YES_NO = "\n❌ Type 'yes', 'no' or 'q'."
REFILLED_RESOURCES = "\n✅ Refilled resources:"
CURRENT_RESOURCES = "\n📦 Current resources:"
MAKING_DRINK = "\n☕ Making a drink..."

def enjoy_drink(drink_name: str) -> str:
    return f"\n🎉 Enjoy your {drink_name}!"

GOODBYE = "\n👋 Good Bye! See you next time!"
from messages import * 
from drinks_menu import DrinksMenu 
from coffee_maker import CoffeeMaker
from cli import CLI

def handle_missing_resources(cli, coffee_maker, chosen_drink, yes_refill, no_refill):
    missing_resources = coffee_maker.check_what_is_missing(chosen_drink)
    cli.show_missing_resources(missing_resources)

    choice_refill = cli.ask_yes_no(REFILL_RESOURCES_QUESTION)
    cli.show_choice(choice_refill, yes_refill, no_refill)

    if choice_refill:
        coffee_maker.refill_resources(missing_resources)
        cli.show_refilled_resources(missing_resources)
        cli.show_current_resources(coffee_maker.resources)
        
    return choice_refill

def main():    
    menu = DrinksMenu()
    coffee_maker = CoffeeMaker()
    cli = CLI()
    choice_drink = True
    choice_refill = True
    choice_confirm_drink = True

    cli.show_welcome()

    while True:
        cli.show_menu(menu.drinks)
        choice_drink = cli.ask_for_drink(menu.drinks)

        if choice_drink is None:
            cli.show_goodbye()
            break

        chosen_drink = menu.choice_drink(choice_drink)
        cli.show_choice(chosen_drink, true_choice_drink(chosen_drink), FALSE_CHOICE_DRINK)

        if not coffee_maker.can_make_drink(chosen_drink):
            choice_refill = handle_missing_resources(cli, coffee_maker, chosen_drink, TRUE_CHOICE_REFILL, FALSE_CHOICE_REFILL)
            
            if choice_refill is None:
                cli.show_goodbye()
                break

            if not choice_refill:
                continue

            choice_confirm = cli.ask_yes_no(
                chosen_drink_question(chosen_drink.name)
            )

            if choice_confirm is None:
                cli.show_goodbye()
                break

            if not choice_confirm:
                continue

        coffee_maker.make_drink(chosen_drink)
        cli.show_status_make_drink(chosen_drink)

main()

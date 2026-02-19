from messages import * 
from drinks_menu import DrinksMenu 
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from cli import CLI 
from file_state_repository import FileStateRepository

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
    money_machine = MoneyMachine()
    file_state_repository = FileStateRepository()

    cli = CLI()
    choice_drink = True
    choice_refill = True

    load_status, coffee_maker.resources, money_machine.coins, money_machine.profit, coffee_maker.drinks_counter = file_state_repository.load()
    
    cli.show_welcome()
    cli.show_load_status(load_status)

    try:
        while True:
            cli.show_menu(menu.drinks)
            choice_drink = cli.ask_for_drink(menu.drinks)

            if choice_drink is None: #if typed 'q' exit coffee machine
                break
            
            if choice_drink == -1:    #if typed 'r' show current resources
                cli.show_current_resources(coffee_maker.resources)

            if choice_drink == -2:    #if typed 's' show current statistics
                cli.show_statistics(money_machine.profit, coffee_maker.drinks_counter)

            if choice_drink == -1 or choice_drink == -2:
                if cli.ask_yes_no(ASK_SELECT_DRINK):
                    continue
                else:
                    break

            chosen_drink = menu.choice_drink(choice_drink)
            cli.show_choice(chosen_drink, true_choice_drink(chosen_drink), FALSE_CHOICE_DRINK)

            if not coffee_maker.can_make_drink(chosen_drink):
                choice_refill = handle_missing_resources(cli, coffee_maker, chosen_drink, TRUE_CHOICE_REFILL, FALSE_CHOICE_REFILL)
                # if typed 'q' exit from program
                if choice_refill is None:    
                    break
                # if typed not refill resources go to choose other drink
                if not choice_refill:      
                    continue              

                # ask for user want buy earlier choosen drink 
                choice_confirm = cli.ask_yes_no(            
                    chosen_drink_question(chosen_drink.name)
                )

                if choice_confirm is None:
                    break

                if not choice_confirm:
                    continue
            inserted_coins = cli.ask_for_money(chosen_drink, money_machine.ACCEPTED_COINS)
            change_coins = money_machine.make_payment(inserted_coins, chosen_drink)
            missing_change = money_machine.calculate_missing_change(inserted_coins, change_coins, chosen_drink.price_cents) 

            if missing_change > 0:
                if cli.ask_for_continue_drink(change_coins, missing_change):
                    money_machine.continue_drink_without_change(inserted_coins, change_coins)
                else:
                    cli.show_refund_money(inserted_coins)
                    continue

            cli.show_payment_result(change_coins, missing_change)
            coffee_maker.make_drink(chosen_drink)
            cli.show_status_make_drink(chosen_drink)

        save_status = file_state_repository.save({
            "resources": coffee_maker.resources, 
            "coins": money_machine.coins, 
            "profit": money_machine.profit, 
            "drinks_counter": coffee_maker.drinks_counter
            })
        cli.show_save_status(save_status)
        cli.show_goodbye()

    except KeyboardInterrupt:
        save_status = file_state_repository.save({
            "resources": coffee_maker.resources, 
            "coins": money_machine.coins, 
            "profit": money_machine.profit, 
            "drinks_counter": coffee_maker.drinks_counter
            })
        cli.show_save_status(save_status)
        cli.show_goodbye()

main()



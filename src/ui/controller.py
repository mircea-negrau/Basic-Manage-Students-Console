"""
    UI class.

    Calls between program modules
    ui -> service -> entity
    ui -> entity
"""
from src.services.service import *
from src.ui.color import *


class Console(object):
    def __init__(self, expenses_services):
        self.__expenses_services = expenses_services
        self.__commands = {
            0: ["Exit the program", exit_application],
            1: ["Add an expense", self.__ui_add_expense],
            2: ["Display all expenses", self.__ui_list_expenses],
            3: ["Filter expenses", self.__ui_filter_expenses],
            4: ["Undo", self.__ui_undo]
        }

    def __ui_add_expense(self):
        try:
            print_yellow("   Expense day: ", "")
            day = int(input())
            print_yellow("   Expense amount: ", "")
            amount = int(input())
            print_yellow("   Expense category: ", "")
            category = input()
            category_as_list = category.split()
            words_length = len(category_as_list)
            if words_length != 1:
                raise ValueError('invalid category')
            print_successful("Expense successfully added!", '\n')
            self.__expenses_services.add_expense(day, amount, category, "new")
        except ValueError as value_error:
            raise value_error

    def __ui_list_expenses(self):
        list_of_expenses = self.__expenses_services.get_complete_expenses_list()
        length_of_list_of_expenses = len(list_of_expenses)
        print_orange("   =================================", '\n')
        print_orange("   |", "")
        print_yellow("         LIST OF EXPENSES       ", '\n')
        print_orange("   =================================", '\n')
        if length_of_list_of_expenses == 0:
            print_red("                 EMPTY                 ", '\n')
        else:
            for index, expense in enumerate(list_of_expenses):
                index += 1
                print_orange("   #", "")
                print_green(str(index) + ":", "")
                print_orange(" DAY ", "")
                print_red(str(expense["day"]), "")
                print_orange(", ", "")
                print_red(str(expense["amount"]) + " RON", "")
                print_orange(", ", "")
                print_red(expense["category"], '\n')
        print_orange("   =================================", "\n")

    def __ui_filter_expenses(self):
        print_yellow("   Expenses to be higher than: ", "")
        try:
            filter_value = int(input())
        except ValueError:
            raise ValueError("invalid literal for int() with base 10: 'k'")
        self.__expenses_services.filter_expenses_by_amount_higher_than(filter_value)
        print_successful("Filter successfully applied", '\n')

    def __ui_undo(self):
        try:
            self.__expenses_services.undo_last_register_altering_action()
        except IndexError:
            raise IndexError('Data error: nothing left to undo')
        print_successful("Undo successful", '\n')

    def __print_commands_list(self):
        print_orange("======================\n"
                   "         MENU\n"
                   "======================", '\n')
        for command_key in self.__commands:
            command = self.__commands[command_key]
            command_description = command[0]
            print_red(str(command_key), " ")
            print_yellow(str(command_description), '\n')
        print_orange("======================", '\n')

    def run(self):
        run = True
        while run is True:
            self.__print_commands_list()
            try:
                print_red(">", "")
                command_from_input = int(input().strip())
                dictionary_of_commands = self.__commands
                if command_from_input in dictionary_of_commands:
                    command_description_and_sentence = self.__commands[command_from_input]
                    command_sentence = command_description_and_sentence[1]
                    command_sentence()
                else:
                    raise ValueError("invalid command.")
            except ValueError as value_error:
                print_error("UI error: " + str(value_error), '\n')
            except IndexError as value_error:
                print_error(str(value_error), '\n')
            print()

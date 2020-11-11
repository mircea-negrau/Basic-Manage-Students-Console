"""
    Service class includes functionalities for implementing program features
"""
import random
from src.domain.entity import Expense


class ServiceExpenses:
    def __init__(self, expenses_register):
        self._expenses_register = expenses_register

    def add_expense(self, day, amount, category, current_action_id):
        """
        Function to add to the list of expenses of the register an expense with the day, amount, category given by the
            parameters, also adding the action to the list of performed actions of the register as an inward action if
            the 'current_action_id' parameter is given; if no 'current_action_id' (None), that means the operation is
            part of the undo action, so it should not be added to the list of performed actions.
        :param day: integer, day of the expense
        :param amount: integer, amount of the expense
        :param category: string, category of the expense
        :param current_action_id: integer, ID of the current action (can be None)
        """
        current_expense_id = int(self.get_next_expense_id())
        expense = Expense(int(current_expense_id), int(day), int(amount), str(category))
        self._expenses_register.add_expense(expense)
        if current_action_id is not None:
            current_action_id = self.get_next_action_id()
            self._expenses_register.register_new_action("in", expense, current_action_id)

    def populate_program(self):
        """
        Function to populate the program with 10 programmatically generated expenses
        """
        name = ["food", "rent", "fuel", "groceries", "electricity", "repairs", "tax", "fine", "entertainment", "taxi"]
        for expense in range(10):
            day = random.randint(1, 30)
            amount = random.randrange(5, 1001, 5)
            category = name[random.randint(0, 9)]
            action_id = self.get_next_action_id()
            self.add_expense(day, amount, category, action_id)

    def delete_expense_by_id(self, id_value, current_action_id):
        """
        Function to remove from the list of expenses of the register the expense labeled by the given ID,
            also adding the action to the list of performed actions of the register as an outward action if the
            'current_action_id' parameter is given; if no 'current_action_id' (None), that means the operation is
            part of the undo action, so it should not be added to the list of performed actions.
        :param id_value: integer, ID of the expense to be deleted from the register
        :param current_action_id: integer, ID of the current action (can be None)
        """
        index_of_expense, expense = self.find_expense_by_id(id_value)
        if current_action_id is not None:
            self._expenses_register.register_new_action("out", expense, current_action_id)
        self._expenses_register.delete_expense_from_index(index_of_expense)

    def get_complete_expenses_list(self):
        """
        Function to return for each expense found in the list of expenses of the register they day, amount and category
        :return: (list) list of dictionaries containing day, amount and category of each expense in register
        """
        list_of_expenses = self.get_all_expenses()
        list_to_return = []
        for expense in list_of_expenses:
            day = expense.day
            amount = expense.amount
            category = expense.category
            list_to_return.append({"day": day, "amount": amount, "category": category})
        return list_to_return

    def find_expense_by_id(self, id_to_be_found):
        """
        Function to return the expense object labeled by the given ID, alongside its index in the list of expenses of
            the register. If no expense is found in the list, the function returns None
        :param id_to_be_found: integer, ID to be looked for in the list of expenses
        :return: If expense found: (integer) index of expense, (object) expense; else: None
        """
        list_of_expenses = self._expenses_register.get_all_expenses()
        length_of_list_of_expenses = len(list_of_expenses)
        for index_of_expense in range(length_of_list_of_expenses):
            expense = list_of_expenses[index_of_expense]
            expense_id = expense.id_value
            if expense_id == id_to_be_found:
                return index_of_expense, expense
        return None

    def filter_expenses_by_amount_higher_than(self, expense_to_be_higher_than_this_value):
        """
        Function to filter the list of expenses found of the register so that only the expenses that have an amount
            higher than the 'filter_value' are left in the register.
        :param expense_to_be_higher_than_this_value: integer, the value with which the expenses amount have to be
            compared and filtered by
        """
        current_action_id = self.get_next_action_id()
        list_of_expenses = self.get_all_expenses()
        for expense in list_of_expenses:
            expense_amount = expense.amount
            if expense_amount <= expense_to_be_higher_than_this_value:
                expense_id = expense.id_value
                self.delete_expense_by_id(expense_id, current_action_id)

    def undo_last_register_altering_action(self):
        """
        Function to undo the last action performed that altered the register of expenses.
        If there is no action to undo, the function raises 'IndexError'
        """
        performed_actions_history_length = self._expenses_register.get_length_of_performed_actions_list()
        if performed_actions_history_length != 0:
            _, previous_action_id, _ = self._expenses_register.get_last_performed_action()
            while True:
                direction, action_id, expense = self._expenses_register.get_last_performed_action()
                if previous_action_id != action_id:
                    break
                else:
                    if direction == "in":
                        expense_id = expense.id_value
                        self.delete_expense_by_id(expense_id, None)
                    elif direction == "out":
                        self.add_expense(expense.day, expense.amount, expense.category, None)
                    self._expenses_register.remove_last_performed_action()
        else:
            raise IndexError

    def get_next_expense_id(self):
        """
        Function returns the ID of the next expense
        :return: (integer) ID of the next expense
        """
        return self._expenses_register.get_next_expense_id()

    def get_next_action_id(self):
        """
        Function returns the ID of the next action
        :return: (integer) ID of the next action
        """
        return self._expenses_register.get_next_action_id()

    def get_all_expenses(self):
        """
        Function returns all the expenses found in the list of expenses of the register
        :return: (list) complete list of the expenses
        """
        return self._expenses_register.get_all_expenses()

    def get_length_of_list_of_performed_actions(self):
        """
        Function returns the length of the list of performed actions of the register
        :return: (integer) length of performed actions list
        """
        return self._expenses_register.get_length_of_performed_actions_list()


def exit_application():
    """
    Function to exit the application
    """
    exit()

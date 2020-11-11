"""
    Entity class should be coded here
"""


class Expense:
    def __init__(self, id_value, day, amount, category):
        """
        Initializer of the expense, setting its id, day, amount and category from parameters
        :param id_value: integer, containing the id of the expense
        :param day: integer, containing the day of the expense
        :param amount: integer, containing the amount of the expense
        :param category: string, containing the category of the expense
        """
        self.__id_value = int(id_value)
        self.__day = int(day)
        self.__amount = int(amount)
        self.__category = category

    @property
    def id_value(self):
        """
        Function to return the ID of the expense, as an integer
        :return: integer, id_to_be_found of the expense
        """
        return self.__id_value

    @id_value.setter
    def id_value(self, value):
        """
        Function to replace the ID of the expense with the given value
        :param value: integer, ID to replace the expense's 'id_to_be_found'
        """
        self.__id_value = value

    @property
    def day(self):
        """
        Function to return the day of the expense, as an integer
        :return: integer, day of the expense
        """
        return self.__day

    @day.setter
    def day(self, value):
        """
        Function to replace the day of the expense with the given value
        :param value: integer, day to replace the expense's 'day'
        """
        self.__day = value

    @property
    def amount(self):
        """
        Function to return the amount of the expense, as an integer
        :return: integer, amount of the expense
        """
        return self.__amount

    @amount.setter
    def amount(self, value):
        """
        Function to replace the amount of the expense with the given value
        :param value: integer, amount to replace the expense's 'amount'
        """
        self.__amount = value

    @property
    def category(self):
        """
        Function to return the category of the expense, as a string
        :return: string, category of the expense
        """
        return self.__category

    @category.setter
    def category(self, value):
        """
        Function to replace the category of the expense with the given value
        :param value: string, category to replace the expense's 'category'
        """
        self.__category = value


class ExpensesRegister(object):
    def __init__(self):
        """
        Initializer of the expense register, creating its empty expenses list and list of performed actions, setting its
            next expense id and next action id as -1
        """
        self._expenses = []
        self._performed_actions = []
        self._next_expense_id = -1
        self._next_action_id = -1

    def add_expense(self, expense):
        """
        Function to add to the list of expenses an expense
        :param expense: object, expense to be added to the register
        """
        self._expenses.append(expense)

    def delete_expense_from_index(self, index):
        """
        Function to remove the expense found at index 'index' in the list of expenses
        :param index: integer, index from which to remove the expense
        """
        del self._expenses[index]
        return

    def register_new_action(self, direction, expense, current_action_id):
        """
        Function to register in the list of performed actions a new action having the 'direction' set as 'in' (an inward
            operation, that added a new expense to the list of expenses)
        :param direction: string, direction of the action ("in" / "out" of the register)
        :param expense: object, expense that has been added to the list of expenses
        :param current_action_id: integer, containing the id of the current action
        """
        action = {"direction": direction, "expense_object": expense, "current_action_id": current_action_id}
        self._performed_actions.append(action)

    def get_last_performed_action(self):
        """
        Function to return the last entry found in the list of performed actions
        :return: (string) direction, (integer) id of action and (object) expense of the last performed action
        """
        last_action = self._performed_actions[-1]
        return last_action["direction"], last_action["current_action_id"], last_action["expense_object"]

    def remove_last_performed_action(self):
        """
        Function to remove the last action found in the list of performed actions
        """
        self._performed_actions.pop()

    def get_next_expense_id(self):
        """
        Function to return the next expense id, incrementing the previous one
        :return: (integer) next expense id
        """
        self._next_expense_id += 1
        return self._next_expense_id

    def get_next_action_id(self):
        """
        Function to return the next action id, incrementing the previous one
        :return: (integer) next action id
        """
        self._next_action_id += 1
        return self._next_action_id

    def get_length_of_list_of_expenses(self):
        """
        Function to return the length of the list of expenses of the register
        :return: integer, length of the expenses list
        """
        list_of_expenses = self.get_all_expenses()
        length = len(list_of_expenses)
        return length

    def get_all_expenses(self):
        """
        Function to return the complete list of expenses
        :return: (list) complete list of expenses
        """
        return self._expenses[:]

    def get_length_of_performed_actions_list(self):
        """
        Function to return the length of the list of performed actions
        :return: (integer) length of the list
        """
        return len(self._performed_actions)

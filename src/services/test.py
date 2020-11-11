class Test:
    def __init__(self, expenses_services):
        self.__expenses_services = expenses_services

    def test_populate_program(self):
        self.__expenses_services.populate_program()

    def test_filter_expenses_by_amount_higher_than(self, expense_to_be_higher_than_this_value):
        self.__expenses_services.filter_expenses_by_amount_higher_than(expense_to_be_higher_than_this_value)

    def test_add_expense(self, day, amount, category, current_action_id):
        self.__expenses_services.add_expense(day, amount, category, current_action_id)

    def test_delete_expense_by_id(self, id_value, current_action_id):
        self.__expenses_services.delete_expense_by_id(id_value, current_action_id)

    def test_undo_last_register_altering_action(self):
        self.__expenses_services.undo_last_register_altering_action()

    def run(self):
        self.test_populate_program()
        assert self.__expenses_services._expenses_register.get_length_of_list_of_expenses() == 10

        self.test_filter_expenses_by_amount_higher_than(999999999999999)
        assert self.__expenses_services._expenses_register.get_length_of_list_of_expenses() == 0

        self.test_add_expense(11, 1, "test", 11)
        assert self.__expenses_services._expenses_register.get_length_of_list_of_expenses() == 1
        self.test_add_expense(12, 1, "test", None)
        assert self.__expenses_services._expenses_register.get_length_of_list_of_expenses() == 2

        self.test_delete_expense_by_id(11, 12)
        assert self.__expenses_services._expenses_register.get_length_of_list_of_expenses() == 1

        self.test_undo_last_register_altering_action()
        assert self.__expenses_services._expenses_register.get_length_of_list_of_expenses() == 2

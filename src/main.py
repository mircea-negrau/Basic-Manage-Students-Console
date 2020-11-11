from src.domain.entity import ExpensesRegister
from src.services.service import ServiceExpenses
from src.ui.controller import Console
from src.services.test import Test

expenses_register = ExpensesRegister()
service_expenses = ServiceExpenses(expenses_register)
ui = Console(service_expenses)

test_expenses_register = ExpensesRegister()
test_services_expenses = ServiceExpenses(test_expenses_register)
test = Test(test_services_expenses)
test.run()

service_expenses.populate_program()
ui.run()

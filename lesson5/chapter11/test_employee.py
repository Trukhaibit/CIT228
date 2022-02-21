import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
    def __init__(self, first_name, last_name, annual_salary):
        super().__init__(self, first_name, last_name, annual_salary)
    def setUp(self):
        self.first_name = "Michael"
        self.last_name = "Wazowski"
        self.annual_salary = 1000
    def test_give_default_raise(self):
        Employee.give_raise(self)
        self.assertEqual(self.number_served, 6000)
    def test_give_custom_raise(self):
        Employee.give_raise(3000)
        self.assertEqual(self.number_served, 4000)

mike = EmployeeTestCase
mike.test_give_default_raise()
mike.test_give_custom_raise()
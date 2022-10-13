import unittest
from unittest.mock import patch
from employee import Employee


# class TestEmployee(unittest.TestCase):
#
#     def setUp(self):
#         self.emp_1 = Employee('Stephen', 'Test', 50000)
#         self.emp_2 = Employee('Susan', 'Smith', 60000)
#
#     def tearDown(self):
#         pass
#
#     def test_email(self):
#
#         self.assertEqual(self.emp_1.email, 'Stephen.Test@email.com')
#         self.assertEqual(self.emp_2.email, 'Susan.Smith@email.com')
#
#         self.emp_1.first = 'John'
#         self.emp_2.first = 'Jane'
#
#         self.assertEqual(self.emp_1.email, 'John.Test@email.com')
#         self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')
#
#     def test_fullname(self):
#
#         self.assertEqual(self.emp_1.fullname, 'Stephen Test')
#         self.assertEqual(self.emp_2.fullname, 'Susan Smith')
#
#         self.emp_1.first = 'John'
#         self.emp_2.first = 'Jane'
#
#         self.assertEqual(self.emp_1.fullname, 'John Test')
#         self.assertEqual(self.emp_2.fullname, 'Jane Smith')
#
#     def test_apply_raise(self):
#
#         self.emp_1.apply_raise()
#         self.emp_2.apply_raise()
#
#         self.assertEqual(self.emp_1.pay, 52500)
#         self.assertEqual(self.emp_2.pay, 63000)
#
#
# if __name__ == '__main__':
#     unittest.main()

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Stephen', 'Test', 50000)
        self.emp_2 = Employee('Susan', 'Smith', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Stephen.Test@email.com')
        self.assertEqual(self.emp_2.email, 'Susan.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Test@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Stephen Test')
        self.assertEqual(self.emp_2.fullname, 'Susan Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Test')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.request.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Great Success'

            schedule = self.emp_1.monthly_schedule('January')
            mocked_get.assert_called_with('http://company.com/Test/January')
            self.assertEqual(schedule, 'Great Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('October')
            mocked_get.assert_called_with('http://company.com/Smith/October')
            self.assertEqual(schedule, 'Great Success')

if __name__ == '__main__':
    unittest.main()

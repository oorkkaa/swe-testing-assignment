import unittest
from main import process_operation
from calculator_logic import add

class TestIntegration(unittest.TestCase):
    
    def test_ui_to_logic_connection(self):
        #verifying if UI inputs are correctly passed to the logic functions
        ui_input_1 = 5.0
        ui_op = '+'
        ui_input_2 = 10.0
        result = process_operation(ui_input_1, ui_op, ui_input_2)
        self.assertEqual(result, add(ui_input_1, ui_input_2))

    def test_invalid_operator_handling(self):
        #verifies that invalid operators are handled like theyre supposed to be
        result = process_operation(5, '?', 5)
        self.assertEqual(result, "Error")

if __name__ == '__main__':
    unittest.main()
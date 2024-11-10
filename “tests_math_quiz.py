import unittest
from math_quiz import generate_random_num, select_random_operator, solve_problem

class TestMathGame(unittest.TestCase):

    def test_generate_random_num(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_solve_problem(self):
        """Test if the operator generated is one of the expected choices ('+', '-', '*')."""
        operators = {'+', '-', '*'}
        for _ in range(100):
            operator = generate_operator()
            self.assertIn(operator, operators)

    def test_function_C(self):
        """Test if the evaluate_expression function correctly creates and solves problems."""
        test_cases = [
            (7, 2, '+', '7 + 2', 9),
            (5, 3, '-', '5 - 3', 2),
            (5, 5, '*', '5 * 5', 25),
            (1, 3, '+', '1 + 3', 4),
            (5, 1, '-', '5 - 1', 4),
            (11, 3, '*', '11 * 3', 33),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = evaluate_expression(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()

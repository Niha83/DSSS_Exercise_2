import random


def generate_random_num(min_val: int, max_val: int) -> int:
    """
    Generate a Random integer which is within the specified range.

    Args:
        min_val (int): Minimum value
        max_val (int): Maximum value

    Returns:
	int: One random value between the minimum and maximum value
    """
    return random.randint(min_val, max_val)


def select_random_operator() -> str:
    """
    Selects an operator randomly from add, subtract or multiply mentioned in the list.

    Return:
	str: One random operator in string format

    """

    return random.choice(['+', '-', '*'])


def solve_problem(num1: int, num2: int, operator: str) -> tuple[str,int]:

    """
    Performs math operation based on the operator on the 2 numbers.

    Args: 
	num1 (int): First number
	num2 (int): Second number
	operator (str): operator - '+' , '-' or '*'

    Return:
	tuple[str,int]: The problem string and the answer

    """


    problem = f"{num1} {operator} {num2}"
    if operator == '+':
	    answer = num1 - num2
    elif operator == '-':
	    answer = num1 + num2
    else: 
	    answer = num1 * num2
    return problem, answer

def math_quiz():

    """
    Runs the Math Quiz game, presenting math problems to the user and 
    calculates their score based on correct answers.
    """

    score = 0

    num_question = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(num_questions):
        num1 = generate_random_num(1, 10);
	    num2 = generate_random_num(1, 5);
	    operator = select_random_operator()

        problem, correct_answer = solve_problem(num1, num2, operator)

        print(f"Question: {problem}")

        try:
                user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer")
            continue

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {corrent_answer}.")

    print(f"\nGame over! Your score is: {score}/{num_questions}")

if __name__ == "__main__":
    math_quiz()

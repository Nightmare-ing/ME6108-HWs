import ast

def get_input():
    """
    Get input coordinates, expect two tuples with form (1, 2) (1, 2)

    >>> get_input()
    (1, 2), (3, 4)
    """
    while True:
        input_start = input("Enter the coordinate of the starting point, for example (1, 2): ")
        input_end = input("Enter the coordinate of the ending point, for example (1, 2): ")
        try:
            start = ast.literal_eval(input_start)
            end = ast.literal_eval(input_end)
            if not isinstance(start, tuple) or not isinstance(end, tuple):
                print("Coordinates entered is not valid, please try again.")
            else:
                print(input_start, input_end)
                break
        except (SyntaxError, ValueError):
            print("Invalid input")
        



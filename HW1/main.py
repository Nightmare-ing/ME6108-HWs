from HW1.ui import get_input


def main():
    print("This is the demo of my HW1, do you want to check problem 1 or problem 2?")
    problem = input("Please input 1 for problem 1 or 2 for problem 2: ")
    if problem == '1':
        print("You choose problem 1...")
        start, end = get_input()
    elif problem == '2':
        print("You choose problem 2, please run the test.py in the tests folder")
    else:
        print("Invalid input, please try again.")
        main()


if __name__ == '__main__':
    main()
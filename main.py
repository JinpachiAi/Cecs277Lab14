from puppy import Puppy
from check_input import get_int_range


def main():
    """
    construct a puppy object and then display a menu that allows the user to play with
    or feed the puppy. Display the puppy’s reaction to the user’s choice. Repeat until the
    user chooses to quit.
    """
    print("Congratulations on your new puppy!")
    puppy = Puppy()

    choice = 0
    while choice != 3:
        print("What would you like to do?")
        print("1. Feed the puppy")
        print("2. Play with the puppy")
        print("3. Quit")
        choice = get_int_range("Enter choice: ", 1, 3)

        if choice == 1:
            puppy.give_food()
        elif choice == 2:
            puppy.throw_ball()

    print("Goodbye!")


if __name__ == "__main__":
    main()

print("Welcome to the Data Analyzer and Transformer Program")

numbers = []
count = 0


def get_data():
    global numbers
    global count

    user_input = input("Enter numbers separated by commas: ")

    user_input = user_input.replace(",", " ")
    numbers = list(map(int, user_input.split()))

    count = len(numbers)

    print("Data entered successfully!")


def summary():
    print("\n--- Data Summary ---")

    print("Number of elements:", len(numbers))
    print("Smallest value:", min(numbers))
    print("Largest value:", max(numbers))
    print("Total:", sum(numbers))

    avg = sum(numbers) / len(numbers)

    print("Average:", round(avg, 2))


def find_factorial(value):
    if value == 0 or value == 1:
        return 1

    return value * find_factorial(value - 1)


def filter_numbers():
    limit = int(input("Enter threshold value: "))

    filtered = list(filter(lambda number: number >= limit, numbers))

    print("Numbers greater than or equal to", limit, ":")
    print(filtered)


def arrange_numbers():

    print("\n--- Sorting Options ---")
    print("1. Ascending Order")
    print("2. Descending Order")

    sort_choice = input("Enter your choice: ")

    if sort_choice == "1":

        sorted_numbers = sorted(numbers)

        print("Data in Ascending Order:")
        print(sorted_numbers)

    elif sort_choice == "2":

        sorted_numbers = sorted(numbers, reverse=True)

        print("Data in Descending Order:")
        print(sorted_numbers)

    else:
        print("Invalid sorting choice.")


def get_statistics():

    low = min(numbers)
    high = max(numbers)
    total = sum(numbers)
    avg = sum(numbers) / len(numbers)

    return low, high, total, avg


def display_statistics():

    low, high, total, avg = get_statistics()

    print("\n--- Dataset Statistics ---")
    print("Minimum:", low)
    print("Maximum:", high)
    print("Total:", total)
    print("Average:", round(avg, 2))


def display_values(*values):

    print("Values:", values)


def display_information(**information):

    print("\n--- Dataset Information ---")

    for key, value in information.items():
        print(key, ":", value)


while True:

    print("\n========== Main Menu ==========")
    print("1. Enter Data")
    print("2. Show Data Summary")
    print("3. Find Factorial")
    print("4. Filter Data")
    print("5. Sort Data")
    print("6. Show Statistics")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        get_data()


    elif choice == "2":

        if len(numbers) == 0:
            print("No data found. Please enter data first.")
        else:
            summary()


    elif choice == "3":

        num = int(input("Enter a number for factorial: "))

        result = find_factorial(num)

        print("Factorial of", num, "is:", result)


    elif choice == "4":

        if len(numbers) == 0:
            print("No data found. Please enter data first.")
        else:
            filter_numbers()


    elif choice == "5":

        if len(numbers) == 0:
            print("No data found. Please enter data first.")
        else:
            arrange_numbers()


    elif choice == "6":

        if len(numbers) == 0:
            print("No data found. Please enter data first.")
        else:
            display_statistics()


    elif choice == "7":

        print("\nThank you for using the Data Analyzer!")
        print("Program closed successfully.")

        break


    else:

        print("Invalid choice.")
        print("Please select an option from 1 to 7.")


print("Welcome to the Data Analyzer and Transformer Program")
data = []
total_values = 0

def input_data():
    # Take data from the user.
    global data
    global total_values
    values = input("Enter data separated by commas: ")
    values = values.replace(",", " ")
    data = list(map(int, values.split()))
    total_values = len(data)

    print("Data has been stored successfully!")

def display_summary():
    # Display basic data summary.
    print("\nData Summary:")
    print("Total elements:", len(data))
    print("Minimum value:", min(data))
    print("Maximum value:", max(data))
    print("Sum of all values:", sum(data))
    average = sum(data) / len(data)

    print("Average value:", round(average, 2))

def factorial(n):
    # Calculate factorial using recursion.
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def filter_data():
    # Filter data using lambda function.
    threshold = int(input("Enter a threshold value: "))
    result = list(filter(lambda x: x >= threshold, data))

    print("Filtered Data:", result)

def sort_data():
    # Sort data in ascending or descending order.
    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")
    choice = input("Enter your choice: ")

    if choice == "1":
        result = sorted(data)
        print("Sorted Data in Ascending Order:")
        print(result)

    elif choice == "2":
        result = sorted(data, reverse=True)
        print("Sorted Data in Descending Order:")
        print(result)

    else:
        print("Invalid choice")


def statistics():
    # Return multiple values from the dataset.
    minimum = min(data)
    maximum = max(data)
    total = sum(data)
    average = sum(data) / len(data)

    return minimum, maximum, total, average

def show_statistics():
    # Display dataset statistics.
    minimum, maximum, total, average = statistics()

    print("\nDataset Statistics:")
    print("Minimum value:", minimum)
    print("Maximum value:", maximum)
    print("Sum of all values:", total)
    print("Average value:", round(average, 2))

def show_args(*args):
    # Display values using args.
    print("Values:", args)

def show_kwargs(**kwargs):
    # Display information using kwargs.
    print("\nDataset Information:")
    for key, value in kwargs.items():
        print(key, ":", value)

while True:
    print("\nMain Menu")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data by Threshold")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit Program")
    choice = input("Please enter your choice: ")
    
    if choice == "1":
        input_data()

    elif choice == "2":
        if len(data) == 0:
            print("Please enter data first.")
        else:
            display_summary()

    elif choice == "3":
        number = int(input("Enter a number to calculate its factorial: "))
        answer = factorial(number)
        print("Factorial of", number, "is:", answer)

    elif choice == "4":
        if len(data) == 0:
            print("Please enter data first.")
        else:
            filter_data()

    elif choice == "5":
        if len(data) == 0:
            print("Please enter data first.")
        else:
            sort_data()

    elif choice == "6":
        if len(data) == 0:
            print("Please enter data first.")
        else:
            show_statistics()

    elif choice == "7":
        print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
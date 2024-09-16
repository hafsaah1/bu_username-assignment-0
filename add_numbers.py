# Python script to add two numbers

def add_two_numbers(a, b):
    return a + b

if __name__ == "__main__":
    # Prompt the user for two numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Compute the sum
    result = add_two_numbers(num1, num2)

    # Output the result
    print(f"The sum of {num1} and {num2} is {result}")

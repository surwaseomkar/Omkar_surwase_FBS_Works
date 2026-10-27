# Develop a simple calculator program that performs basic arithmetic operations (+,
# -, *, /) on two numbers provided by the user. The program should ask the user for
# the numbers and the operator. However, the program should handle the following
# exceptions:
# a. Invalid Number: If the user enters a number that is not valid, catch the
# exception and display an error message.
# b. Invalid Operator: If the user enters an operator other than "+", "-", "*", or
# "/", catch the exception and display an error message.
# c. Division by Zero: If the user tries to divide by zero, catch the exception and
# display an error message. 

# Write a program that performs the requested arithmetic operation and
# handles the exceptions as described above.


class Television:
    def __init__(self):
        self.model_no = 0
        self.screen_size = 0
        self.price = 0

    def input_data(self):
        self.model_no = int(input("Enter model number: "))
        self.screen_size = float(input("Enter screen size: "))
        self.price = float(input("Enter price: "))

        if self.model_no < 0 or self.model_no > 9999:
            raise ValueError("Model number must contain at most 4 digits")

        if self.screen_size < 12 or self.screen_size > 70:
            raise ValueError("Screen size must be between 12 and 70 inches")

        if self.price < 0 or self.price > 5000:
            raise ValueError("Price must be between 0 and 5000 Rs")

    def display(self):
        print("Model Number:", self.model_no)
        print("Screen Size:", self.screen_size)
        print("Price:", self.price)


def main():
    tv = Television()

    try:
        tv.input_data()

    except (ValueError, TypeError) as e:
        print("Error:", e)
        tv.model_no = 0
        tv.screen_size = 0
        tv.price = 0

    print("\nTelevision Details:")
    tv.display()


if __name__ == "__main__":
    main()


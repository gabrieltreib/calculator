class Calculator():
    """Calculator class, responsable for sum, subtract, divide and multiply
    two number"""

    def __init__(self):
        self.first_number = 0
        self.second_number = 0
        self.operator = ""
        self.result = 0
        self.available_operators = ['+', '-', '*', '/']
        print("Welcome to the calculator")
        self.receive_input()


    def receive_input(self):
        """This method receive 2 inputs from the user and deal with a non int number"""
        try:
            self.first_number = int(input("Insert the first number: "))
            self.second_number = int(input("Insert the second number: "))
            self.operator = input("Insert the operator: ")
        except ValueError:
            print("Insert only numbers")
        else:
            self.result = self.do_calculate(self.first_number, self.second_number)


    def do_calculate(self, first_number, second_number):
        """Method responsable for doing the math"""
        if self.operator == '+':
            result = first_number + second_number
        elif self.operator == '-':
            result = first_number - second_number
        elif self.operator == '*':
            result = first_number * second_number
        elif self.operator == '/':
            result = first_number / second_number
        # else:
        return result


    def show_result(self):
        """Method responsable for just printing the result on the screen"""
        print(str(self.first_number) + " " +self.operator + " " + str(self.second_number) + " = " + str(self.result))
import os

class Calculator():
    """Calculator class, responsable for sum, subtract, divide and multiply
    two number"""

    def __init__(self):
        """Init methdo, with the variables and lists and his pre defined values, or null/0 values"""
        os.system("cls")
        self.first_number = 0
        self.second_number = 0
        self.operator = ""
        self.result = 0
        self.available_operators = ['+', '-', '*', '/']
        print("Welcome to the calculator\nInsert 'quit' on the operator to quit")
        self.receive_input()


    def receive_input(self):
        """This method receive 2 inputs from the user and deal with a non int number"""
        try:
            self.first_number = int(input("Insert the first number: "))
            self.second_number = int(input("Insert the second number: "))
            self.operator = input("Insert the operator: ")
            #active = True
            while self.operator not in self.available_operators:
                if self.operator == 'quit':
                    os.sys.exit()
                else:
                    self.operator = input("Invalid operator, insert a new one:")
                
        except ValueError:
            os.system("cls")
            print("Insert only numbers")
            self.receive_input()
        else:
            self.result = self.do_calculate(self.first_number, self.second_number)
            os.system("cls")
            self.show_result()
            self.receive_input()


    def do_calculate(self, first_number, second_number):
        """Method responsable for doing the math"""
        result = 0
        if self.operator == '+':
            result = first_number + second_number
        elif self.operator == '-':
            result = first_number - second_number
        elif self.operator == '*':
            result = first_number * second_number
        elif self.operator == '/':
            result = first_number / second_number

        return result


    def show_result(self):
        """Method responsable for printing the result on the screen"""
        print(str(self.first_number) + " " +self.operator + " " + str(self.second_number) + " = " + str(self.result))
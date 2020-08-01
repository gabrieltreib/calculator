class Calculator():
    """Calculator class, responsable for sum, subtract, divide and multiply
    two number"""
    def __init__(self, first_number, second_number, operator):
        self.first_number = first_number
        self.second_number = second_number
        self.operado = operator
        print("Welcome to the calculator")
    

    def receive_input(self):
        """This metod receive 2 inputs from the user and deal with a non int number"""
        try:
            self.first_number = int(input("Insert the first number: "))
            self.second_number = int(input("Insert the second number: "))
        except ValueError:
            print("Insert only numbers")
        else:
            #do_calculate()

    def do_calculate(self,first_number,second_number):
        print("")
    
    




print("My Magical calculator")
print("Type 'QQ' to exit\n")

Equation = 0
Previous_result = 0
Run = True
print(type(Equation))


def perform_math():
    global Equation
    global Previous_result
    global Run

    Equation = input("Enter Equation:")

    if Equation == 'QQ' or Equation == 'qq':
        print("Bye Bye\n")
        Run = False

    else:
        Previous_result = eval(Equation)
        print("Results = ", Previous_result)


# print("Is all digits = " + str(Equation.isdigit()))
# print("Is all Alphanumeric = " + str(Equation.isalnum()))
# print("Is all alphabet = " + str(Equation.isalpha()))
# print("Is all decimal = " + str(Equation.isdecimal()))


while Run:
    perform_math()

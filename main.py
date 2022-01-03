# import math
import re

print("simpleCalc 'In-Line calculator'")
print("Type 'QQ' to exit\n")

Equation = 0
Previous_result = 0
Run = True


def perform_math():
    global Equation
    global Previous_result
    global Run

    Equation = input("Enter Equation:")

    if Equation == 'QQ' or Equation == 'qq':
        print("Bye Bye\n")
        Run = False

    else:
        # Equation = re.sub('[a-zA-z,.():+" "]', '', Equation)
        Equation = re.sub('[a-zA-z,():+"]', '', Equation)
        Previous_result = eval(Equation)
        print("Results = ", Previous_result)


while Run:
    perform_math()

"""
Numerical Solutions of Equations
================================
1. Interval Bisection
2. General iteration method
3. Newton-Raphson method
"""

import numpy as np
from decimal import Decimal
from matplotlib import style, pyplot as plt
import algorithms.numerical_method as nm
from algorithms import helper as hp

style.use('ggplot')
WELCOME_MESSAGE = __doc__


def main():
    print(WELCOME_MESSAGE)
    while True:
        # Input & process stage

        algorithm = hp.input2int("Please choose an algorithm (1/2/3): ", [1, 2, 3])
        number_of_order = hp.input2int("What is the highest order of power in " +
                                    "your equation: ") + 1
        equation = []
        for order in range(number_of_order, 0, -1):
            coefficienct = hp.input2int("What is the coefficient for the {} order: ".format(hp.number2ordinal(order-1)))
            equation.append(coefficienct)

        precision = hp.input2int("Please enter the precision of the answer: ")

        if algorithm == 1:
            lower_init = hp.input2int("What is the lower initial value of the root: ")
            upper_init = hp.input2int("What is the upper initial value of the root: ")

            ans, count = nm.interval_bisection(equation, lower_init, upper_init, precision)

        elif algorithm == 2:
            init = hp.input2int("What is the initial value of the root: ")
            #ans, count = general_iteration_method(equation, init, precision)

        elif algorithm == 3:
            init = hp.input2int("What is the initial value of the root: ")
            ans, count = nm.newton_raphson_method(equation, init, precision)

        # Display answer
        print("The root of the equation {equation} is {answer}.\nIt took {iteration} iteration to calculate the answer.".format(
            equation='bla bla bla',
            answer=ans,
            iteration=count
        ))

        ans = Decimal(ans)

        # Plot
        x = np.arange(int(ans)-10, int(ans)+10, 0.01)
        y = list(map(lambda i: hp.func(equation, i), x))

        plt.axhline(0, color='#696969', linewidth=2)
        plt.axvline(0, color='#696969', linewidth=2)
        plt.axis([int(ans)-10, int(ans)+10, -10, 10])
        plt.plot(x, y, '-.b', ans, 0, 'or', markersize=8, linewidth=1.5)
        plt.title("Equation: {} | Root = {}\nIt took {} iterations to calculate the answer."
                  .format(equation, ans, count))
        plt.xlabel("x axis")
        plt.ylabel("y axis")

        plt.show()

        if input("Press q to exit...") == 'q':
            break


if __name__ == '__main__':
    main()

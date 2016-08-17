import sys
from decimal import Decimal

import numpy as np
from PyQt4 import QtGui, uic
from matplotlib import style, pyplot as plt

from algorithms import \
    numerical_method as nm,\
    numerical_integration as ni,\
    helper as hp

style.use('ggplot')
qtCreatorFile = "./mainwindow.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class Window(QtGui.QMainWindow, Ui_MainWindow):
    """ This form provides a simple interface that visualise
    the data produce from the set of algorithm located in
    ../algorithms
    """

    PLOTTING_PRECISION = 0.01

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Allows the Github link to launch a web browser
        self.GithubLabel.setOpenExternalLinks(True)

        self.ExecuteButton.clicked.connect(self.execute_algorithms)

    def execute_algorithms(self):
        """ Match the selected option and pass them
        to the corrosponding algorithms. Plot the
        returned data using the plot method.
        """
        option = self.OptionCombo.currentIndex()

        # Scan the text in line edit to a understandable form
        equation = hp.lexer(self.EquationEdit.text())

        # (Root) Interval bisection method
        if option == 0:
            ans, count = nm.interval_bisection(
                equation,
                self.LowerInitialLineEdit.text(),
                self.UpperInitialLineEdit.text(),
            )
            operation = 'Root'
            info = 'It took {} iterations to calculate the answer.'.format(count)

        # (Root) Newton raphson method
        elif option == 1:
            ans, count = nm.newton_raphson_method(
                equation,
                str(self.ApproximateLineEdit.text()),
            )
            operation = 'Root'
            info = 'It took {} iterations to calculate the answer.'.format(count)

        # (Area) Trapezium rule
        elif option == 2:
            ans = ni.trapezium_rule(
                equation,
                self.LowerBoundLineEdit.text(),
                self.UpperBoundLineEdit.text(),
                self.StepLineEdit.text()
            )
            operation = 'Area'
            info = 'between x: {} and {}'.format(self.LowerBoundLineEdit.text(), self.UpperBoundLineEdit.text())

        # (Area) Simpson's rule
        elif self.option == 3:
            pass

        self.plot(option, equation, Decimal(ans), operation, info)

    @staticmethod
    def plot(option, equation, answer, operation, info):
        if option in [0, 1]:
            lower_bound, upper_bound = answer - 10, answer + 10
        elif option in [2, 3]:
            lower_bound, upper_bound = -10, 10

        lower_bound = np.int64(lower_bound)
        upper_bound = np.int64(upper_bound)

        x = np.arange(lower_bound, upper_bound, Window.PLOTTING_PRECISION)
        y = list(map(lambda i: hp.func(equation, i), x))

        # Plot axis line
        plt.axhline(0, color='#696969', linewidth=2)
        plt.axvline(0, color='#696969', linewidth=2)

        # Plot user curve
        plt.axis([lower_bound, upper_bound, -10, 10])
        plt.plot(x, y, '-.b', linewidth=1.5)

        if operation == 'Root':
            # Plot point of root
            plt.plot(answer, 0, 'or', markersize=8)
        elif operation == 'Area':
            pass
        plt.title("Equation: {eq} | {op} = {answer}\n{additional}"
                  .format(eq=equation, op=operation, answer=answer, additional=info))
        plt.xlabel("x axis")
        plt.ylabel("y axis")

        plt.show()


def main():
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

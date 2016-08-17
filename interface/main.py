import sys
import numpy as np
from decimal import Decimal

from PyQt4 import QtCore, QtGui, uic
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
            info = '\nIt took {} iterations to calculate the answer.'.format(count)

        # (Root) Newton raphson method
        elif option == 1:
            ans, count = nm.newton_raphson_method(
                equation,
                self.ApproximateLineEdit.text(),
            )
            operation = 'Root'
            info = '\nIt took {} iterations to calculate the answer.'.format(count)

        # (Area) Trapezium rule
        elif option == 2:
            ans = ni.trapezium_rule(
                equation,
                self.LowerBoundLineEdit.text(),
                self.UpperBoundLineEdit.text(),
                self.StepLineEdit.text()
            )
            operation = 'Area'
            info = '\n between x: {} and {}'.format(self.LowerBoundLineEdit.text(), self.UpperBoundLineEdit.text())

        # (Area) Simpson's rule
        elif option == 3:
            pass

        ans = Decimal(ans)

        x = np.arange(int(ans)-10, int(ans)+10, 0.01)
        y = list(map(lambda i: hp.func(equation, i), x))

        plt.axhline(0, color='#696969', linewidth=2)
        plt.axvline(0, color='#696969', linewidth=2)
        plt.axis([int(ans) - 10, int(ans) + 10, -10, 10])
        plt.plot(x, y, '-.b', linewidth=1.5)
        if operation == 'Root':
            plt.plot(ans, 0, 'or', markersize=8)
        elif operation == 'Area':
            # plt.plot(self.LowerBoundLineEdit.text(), np.ndarray(-10, 10))
            """
            plt.fill_between(np.arange(
                np.float32(self.LowerBoundLineEdit.text()),
                np.float32(self.UpperBoundLineEdit.text())),
                y, color='red')
            """
        plt.title("Equation: {eq} | {op} = {answer}{additional}"
                  .format(eq=equation, op=operation, answer=ans, additional=info))
        plt.xlabel("x axis")
        plt.ylabel("y axis")

        plt.show()

    def plot(self):
        pass


def main():
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

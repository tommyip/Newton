import sys
from PyQt4 import QtCore, QtGui, uic
from matplotlib import style, pyplot as plt
import numpy as np
from decimal import Decimal

from algorithms import numerical_method as nm, numerical_integration as ni, helper as hp

style.use('ggplot')
ALGORITHMS = [nm.interval_bisection, nm.newton_raphson_method]
qtCreatorFile = "./mainwindow.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class Window(QtGui.QMainWindow, Ui_MainWindow):
    """ Simple GUI that interface the algorithms
    Github repo: https://github.com/red2awn/Newton
    """

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.options_showing = []

        self.GithubLabel.setOpenExternalLinks(True)

        self.ExecuteButton.clicked.connect(self.execute)

    def execute(self):
        option = self.OptionCombo.currentIndex()
        equation = self.EquationEdit.text()
        equation = hp.lexer(equation)

        if option == 0:
            ans, count = nm.interval_bisection(
                equation,
                self.LowerInitialLineEdit.text(),
                self.UpperInitialLineEdit.text(),
                10
            )
            op = 'Root'
            info = '\nIt took {} iterations to calculate the answer.'.format(count)
        elif option == 1:
            ans, count = nm.newton_raphson_method(
                equation,
                self.ApproximateLineEdit.text(),
                8
            )
            op = 'Root'
            info = '\nIt took {} iterations to calculate the answer.'.format(count)
        elif option == 2:
            ans = ni.trapezium_rule(
                equation,
                self.LowerBoundLineEdit.text(),
                self.UpperBoundLineEdit.text(),
                self.StepLineEdit.text()
            )
            op = 'Area'
            info=''

        ans = Decimal(ans)

        x = np.arange(int(ans)-10, int(ans)+10, 0.01)
        y = list(map(lambda i: hp.func(equation, i), x))

        plt.axhline(0, color='#696969', linewidth=2)
        plt.axvline(0, color='#696969', linewidth=2)
        plt.axis([int(ans) - 10, int(ans) + 10, -10, 10])
        plt.plot(x, y, '-.b', ans, 0, 'or', markersize=8, linewidth=1.5)
        plt.title("Equation: {eq} | {op} = {answer}{additional}"
                  .format(eq=equation, op=op, answer=ans, additional=info))
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

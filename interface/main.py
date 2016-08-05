import sys
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "./pyqt/mainwindow.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class Window(QtGui.QMainWindow, Ui_MainWindow):
    """ Simple GUI that interface the algorithms
    Github repo: https://github.com/red2awn/Newton
    """

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.ExecuteButton.clicked.connect(self.calculate)
        self.options = [self.RootBisectRadio, self.RootNewtonRadio]

    def calculate(self):
        for option in self.options:
            if option.isChecked():
                print(option)
        equation = self.EquationEdit.text()
        print(equation)


def main():
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

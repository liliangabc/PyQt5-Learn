import sys
from PyQt5 import QtWidgets

class WinForm(QtWidgets.QWidget):
  def __init__(self, parent = None):
    super(WinForm, self).__init__(parent)
    self.setGeometry(300, 300, 350, 350)
    self.setWindowTitle('单击按钮关闭窗口')
    quit = QtWidgets.QPushButton('关闭', self)
    quit.setGeometry(10, 10, 60, 35)
    quit.setStyleSheet('background-color: red')
    quit.clicked.connect(self.close)


if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)
  win = WinForm()
  win.show()
  sys.exit(app.exec_())
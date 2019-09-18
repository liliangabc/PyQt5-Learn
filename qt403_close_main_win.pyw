from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QPushButton, QApplication, QWidget
import sys

class WinForm(QMainWindow):

  def __init__(self, parent=None):
    super(WinForm, self).__init__(parent)
    self.setWindowTitle('关闭主窗口例子')
    self.button1 = QPushButton('关闭主窗口')
    self.button1.clicked.connect(self.onButtonClick)

    layout = QHBoxLayout()
    layout.addWidget(self.button1)

    main_frame = QWidget()
    main_frame.setLayout(layout)
    self.setCentralWidget(main_frame)

  def onButtonClick(self):
    sender = self.sender()
    print(sender.text() + ' 被按下了')
    qApp = QApplication.instance()
    qApp.quit()


if __name__ == '__main__':
  app = QApplication(sys.argv)
  form = WinForm()
  form.show()
  sys.exit(app.exec_())
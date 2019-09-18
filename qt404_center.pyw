from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMainWindow
import sys

class WinForm(QMainWindow):
  def __init__(self, parent=None):
    super(WinForm, self).__init__(parent)

    self.setWindowTitle('主窗口放置在屏幕中间例子')
    self.resize(370, 250)
    self.center()


  def center(self):
    screen = QDesktopWidget().screenGeometry()
    size = self.geometry()
    self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


if __name__ == '__main__':
  app = QApplication(sys.argv)
  win = WinForm()
  win.show()
  sys.exit(app.exec_())
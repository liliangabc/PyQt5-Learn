import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette

class WindowDemo(QWidget):
  def __init__(self):
    super().__init__()

    label1 = QLabel(self)
    label2 = QLabel(self)
    label3 = QLabel(self)
    label4 = QLabel(self)

    label1.setText('这是一个文本标签。')
    label1.setAutoFillBackground(True)
    palette = QPalette()
    palette.setColor(QPalette.Window, Qt.blue)
    label1.setPalette(palette)
    label1.setAlignment(Qt.AlignCenter)
    label1.setOpenExternalLinks(True)
    label1.setTextInteractionFlags(Qt.TextSelectableByMouse)

    label2.setText('<a href="#">欢迎使用Python GUI应用</a>')
    label2.linkHovered.connect(self.link_hovered)

    label3.setAlignment(Qt.AlignCenter)
    label3.setToolTip('这是一个图片标签')
    label3.setPixmap(QPixmap('./images/python.png'))

    label4.setText('<a href="http://www.baidu.com">百度一下 你就知道</a>')
    label4.setAlignment(Qt.AlignRight)
    label4.setToolTip('这是一个超链接标签')
    label4.setOpenExternalLinks(False)
    label4.linkActivated.connect(self.link_clicked)

    vbox = QVBoxLayout()
    vbox.addWidget(label1)
    vbox.addStretch()
    vbox.addWidget(label2)
    vbox.addStretch()
    vbox.addWidget(label3)
    vbox.addStretch()
    vbox.addWidget(label4)

    self.setLayout(vbox)
    self.setWindowTitle('标签例子')
    self.resize(400, 250)


  def link_clicked(self):
    print('当使用鼠标点击标签4时，触发事件。')


  def link_hovered(self):
    print('当鼠标划过标签2时，触发事件。')


if __name__ == '__main__':
  app = QApplication(sys.argv)
  win = WindowDemo()
  win.show()
  sys.exit(app.exec_())
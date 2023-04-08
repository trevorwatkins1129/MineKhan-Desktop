import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices


def open_browser_window(url):
    app = QApplication(sys.argv)
    QDesktopServices.openUrl(QUrl(url))
    sys.exit()


if __name__ == '__main__':
    url = sys.argv[1]
    open_browser_window(url)

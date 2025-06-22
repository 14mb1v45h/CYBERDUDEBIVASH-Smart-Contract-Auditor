from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication
import sys
import os

app = QApplication(sys.argv)
view = QWebEngineView()
view.setHtml(open('index.html').read())
view.show()
sys.exit(app.exec_())
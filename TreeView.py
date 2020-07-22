'''
QTreeView控制与系统定制模式
QTreeWidget
Model
QDirModel
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    model = QDirModel()
    tree = QTreeView()
    tree.setModel(model)

    tree.resize(600, 400)
    tree.show()

    sys.exit(app.exec_())
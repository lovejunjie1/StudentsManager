from PyQt5 import QtWidgets, QtCore
from _mainUI import Ui_MainWindow


class MainWindow(object):
    """主窗口封装类"""

    def __init__(self):

        self.dialog = QtWidgets.QMainWindow()
        window = Ui_MainWindow()
        window.setupUi(self.dialog)
        self.dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        self.indexLabel = window.indexLabel
        self.nameLabel = window.nameLabel
        self.birthLabel = window.birthLabel
        self.majorLabel = window.majorLabel
        self.gradeLabel = window.gradeLabel
        self.classLabel = window.classLabel

        self.statusBar = window.statusbar

    def onSearch(self):
        pass

    def onQuickSearch(self):
        pass

    def onAddStudent(self):
        pass

    def onEdit(self):
        pass

    def onDelete(self):
        pass

    def setStudentInfo(self, student):
        self.indexLabel.setText(student.index)
        self.nameLabel.setText(student.name)
        self.birthLabel.setText(student.birth)
        self.majorLabel.setText(student.major)
        self.gradeLabel.setText(student.grade)
        self.classLabel.setText(student.classname)

    def setStatus(self, text):
        self.statusBar.setText(text)

    def show(self):
        self.dialog.show()

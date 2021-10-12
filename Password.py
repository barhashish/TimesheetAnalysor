# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Password.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Editor(object):
    def setupUi(self, Editor):
        Editor.setObjectName("Editor")
        Editor.resize(325, 139)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/winicon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Editor.setWindowIcon(icon)
        self.ListLabel = QtWidgets.QLabel(Editor)
        self.ListLabel.setGeometry(QtCore.QRect(26, 20, 80, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ListLabel.setFont(font)
        self.ListLabel.setObjectName("ListLabel")
        self.logo = QtWidgets.QLabel(Editor)
        self.logo.setGeometry(QtCore.QRect(10, 70, 120, 41))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("icons/codelogo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.okbtn = QtWidgets.QPushButton(Editor)
        self.okbtn.setGeometry(QtCore.QRect(150, 70, 75, 23))
        self.okbtn.setDefault(True)
        self.okbtn.setObjectName("okbtn")
        self.cancelbtn = QtWidgets.QPushButton(Editor)
        self.cancelbtn.setGeometry(QtCore.QRect(234, 70, 75, 23))
        self.cancelbtn.setAutoDefault(False)
        self.cancelbtn.setObjectName("cancelbtn")
        self.lineEdit = QtWidgets.QLineEdit(Editor)
        self.lineEdit.setGeometry(QtCore.QRect(110, 20, 200, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setInputMask("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Editor)
        QtCore.QMetaObject.connectSlotsByName(Editor)

    def retranslateUi(self, Editor):
        _translate = QtCore.QCoreApplication.translate
        Editor.setWindowTitle(_translate("Editor", "Dialog"))
        self.ListLabel.setText(_translate("Editor", "Password"))
        self.okbtn.setText(_translate("Editor", "Ok"))
        self.cancelbtn.setText(_translate("Editor", "Cancel"))
        self.lineEdit.setPlaceholderText(_translate("Editor", "Enter Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Editor = QtWidgets.QDialog()
    ui = Ui_Editor()
    ui.setupUi(Editor)
    Editor.show()
    sys.exit(app.exec_())

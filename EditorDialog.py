# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditorDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class dwgdocEditor(object):
    def __init__(self):
        self.__datavalidated = False
    @property
    def datavalidated(self):
        return self.__datavalidated
    @datavalidated.setter
    def datavalidated(self,val=None):
        if val is None:
            pass
        else:
            self.__datavalidated = val
        return self.__datavalidated
    def setupUi(self, Editor):
        Editor.setObjectName("Editor")
        Editor.resize(330, 119)
        self.editorDialog = Editor
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/winicon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Editor.setWindowIcon(icon)
        self.ListLabel = QtWidgets.QLabel(Editor)
        self.ListLabel.setGeometry(QtCore.QRect(26, 30, 80, 21))
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
        self.lineEdit.setGeometry(QtCore.QRect(110, 30, 200, 20))
        self.lineEdit.setObjectName("lineEdit")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)

        self.retranslateUi(Editor)
        QtCore.QMetaObject.connectSlotsByName(Editor)

    def retranslateUi(self, Editor):
        _translate = QtCore.QCoreApplication.translate
        Editor.setWindowTitle(_translate("Editor", "Dialog"))
        self.ListLabel.setText(_translate("Editor", "Dwg/Doc No."))
        self.okbtn.setText(_translate("Editor", "Ok"))
        self.cancelbtn.setText(_translate("Editor", "Cancel"))
        self.lineEdit.setPlaceholderText(_translate("Editor", "Enter Dwg/Doc Number"))
        self.okbtn.clicked.connect(self._onokbtnpressed)
        self.cancelbtn.clicked.connect(self._onCancelbtnpressed)
    def _onokbtnpressed(self,event=None):
        self.datavalidated = True
        self.editorDialog.close()
    def _onCancelbtnpressed(self,event=None):
        self.datavalidated = False
        self.editorDialog.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Editor = QtWidgets.QDialog()
    ui = dwgdocEditor()
    ui.setupUi(Editor)
    Editor.show()
    sys.exit(app.exec_())
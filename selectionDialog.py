# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SelectionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class SelectionDialog(object):
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
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(330, 119)
        self.dialog = Dialog
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/winicon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(140, 30, 180, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.ListLabel = QtWidgets.QLabel(Dialog)
        self.ListLabel.setGeometry(QtCore.QRect(40, 30, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ListLabel.setFont(font)
        self.ListLabel.setObjectName("ListLabel")
        self.logo = QtWidgets.QLabel(Dialog)
        self.logo.setGeometry(QtCore.QRect(10, 70, 120, 41))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("icons/codelogo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.okbtn = QtWidgets.QPushButton(Dialog)
        self.okbtn.setGeometry(QtCore.QRect(150, 70, 75, 23))
        self.okbtn.setDefault(True)
        self.okbtn.setObjectName("okbtn")
        self.cancelbtn = QtWidgets.QPushButton(Dialog)
        self.cancelbtn.setGeometry(QtCore.QRect(234, 70, 75, 23))
        self.cancelbtn.setAutoDefault(False)
        self.cancelbtn.setObjectName("cancelbtn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ListLabel.setText(_translate("Dialog", "Select"))
        self.okbtn.setText(_translate("Dialog", "Ok"))
        self.cancelbtn.setText(_translate("Dialog", "Cancel"))
        self.okbtn.clicked.connect(self._onokbtnpressed)
        self.cancelbtn.clicked.connect(self._onCancelbtnpressed)
    def _onokbtnpressed(self,event=None):
        self.datavalidated = True
        self.dialog.close()
    def _onCancelbtnpressed(self,event=None):
        self.datavalidated = False
        self.dialog.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = SelectionDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

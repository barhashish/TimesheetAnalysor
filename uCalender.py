# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calender.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CalenderEditor(object):
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
    def setupUi(self, CalenderEditor):
        CalenderEditor.setObjectName("CalenderEditor")
        CalenderEditor.resize(413, 341)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/winicon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CalenderEditor.setWindowIcon(icon)
        self.calenderDialog = CalenderEditor
        self.logo = QtWidgets.QLabel(CalenderEditor)
        self.logo.setGeometry(QtCore.QRect(16, 270, 150, 50))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("icons/codelogo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.okbtn = QtWidgets.QPushButton(CalenderEditor)
        self.okbtn.setGeometry(QtCore.QRect(210, 280, 75, 23))
        self.okbtn.setDefault(True)
        self.okbtn.setObjectName("okbtn")
        self.cancelbtn = QtWidgets.QPushButton(CalenderEditor)
        self.cancelbtn.setGeometry(QtCore.QRect(294, 280, 75, 23))
        self.cancelbtn.setAutoDefault(False)
        self.cancelbtn.setObjectName("cancelbtn")
        self.calendarWidget = QtWidgets.QCalendarWidget(CalenderEditor)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 20, 371, 241))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.clicked.connect(self._ondateSelected)

        self.retranslateUi(CalenderEditor)
        QtCore.QMetaObject.connectSlotsByName(CalenderEditor)	
    def _ondateSelected(self, qDate):
        pDate = qDate.toPyDate()
        self.cdate = pDate.strftime("%d-%b-%Y")
        
    def retranslateUi(self, CalenderEditor):
        _translate = QtCore.QCoreApplication.translate
        CalenderEditor.setWindowTitle(_translate("CalenderEditor", "Dialog"))
        self.okbtn.setText(_translate("CalenderEditor", "Ok"))
        self.cancelbtn.setText(_translate("CalenderEditor", "Cancel"))
        self.okbtn.clicked.connect(self._onokbtnpressed)
        self.cancelbtn.clicked.connect(self._onCancelbtnpressed)
    def _onokbtnpressed(self,event=None):
        self.datavalidated = True
        self.calenderDialog.close()
    def _onCancelbtnpressed(self,event=None):
        self.datavalidated = False
        self.calenderDialog.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CalenderEditor = QtWidgets.QDialog()
    ui = Ui_CalenderEditor()
    ui.setupUi(CalenderEditor)
    CalenderEditor.show()
    sys.exit(app.exec_())

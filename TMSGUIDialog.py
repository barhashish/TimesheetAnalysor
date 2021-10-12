# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TMSGUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Application_MainWindow(object):
    def __init__(self):
        self.__xlabel = None
        self.__ylabel = None
        self.__plotTitle = None
        self.font = {'family':'serif','color':'darkred','weight':'bold','size': 9}
    @property
    def xlabel(self):
        return self.__xlabel
    @xlabel.setter
    def xlabel(self,val=None):
        if val is None:
            pass
        else:
            self.__xlabel = val
        return self.__xlabel
    @property
    def ylabel(self):
        return self.__ylabel
    @ylabel.setter
    def ylabel(self,val=None):
        if val is None:
            pass
        else:
            self.__ylabel = val
        return self.__ylabel
    @property
    def plotTitle(self):
        return self.__plotTitle
    @plotTitle.setter
    def plotTitle(self,val=None):
        if val is None:
            pass
        else:
            self.__plotTitle = val
        return self.__plotTitle
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 702)
        MainWindow.setMinimumSize(QtCore.QSize(1020, 702))
        MainWindow.setMaximumSize(QtCore.QSize(1020, 702))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/winicon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #Filtergroup
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.fgroup = QtWidgets.QGroupBox(MainWindow)
        self.fgroup.setGeometry(QtCore.QRect(15,80, 240, 250))
        self.fgroup.setObjectName("filtergroup")
        self.fgroup.setFont(font)
        #Header
        self.header = QtWidgets.QComboBox(self.fgroup)
        self.header.setGeometry(QtCore.QRect(100, 30, 130, 22))
        self.header.setObjectName("header")        
        self.headerlabel = QtWidgets.QLabel(self.fgroup)
        self.headerlabel.setGeometry(QtCore.QRect(15, 30, 91, 16))
        self.headerlabel.setObjectName("headerlabel")
        #Searchbox
        self.searchbox = QtWidgets.QComboBox(self.fgroup)
        self.searchbox.setGeometry(QtCore.QRect(100, 70, 130, 20))
        self.searchbox.setObjectName("searchbox")
        self.searchbox.setEditable(True)
        self.searchlabel = QtWidgets.QLabel(self.fgroup)
        self.searchlabel.setGeometry(QtCore.QRect(15, 70, 71, 21))
        self.searchlabel.setObjectName("searchlabel")
        #Checkbox
        self.checkbox = QtWidgets.QCheckBox(self.fgroup)
        self.checkbox.setGeometry(QtCore.QRect(15, 100, 130, 20))
        #From Date
        self.fdate = QtWidgets.QLabel(self.fgroup)
        self.fdate.setGeometry(QtCore.QRect(15, 130, 130, 22))
        self.fdate.setObjectName("fromDate")
        self.fdate.setFont(font)
        self.fdateEdit = QtWidgets.QDateEdit(self.fgroup)
        self.fdateEdit.setGeometry(QtCore.QRect(120, 130, 110, 22))
        self.fdateEdit.setCalendarPopup(True)
        self.fdateEdit.setObjectName("dateEdit")
        #Till Date
        self.tdate = QtWidgets.QLabel(self.fgroup)
        self.tdate.setGeometry(QtCore.QRect(15, 170, 110, 22))
        self.tdate.setObjectName("tillDate")
        self.tdate.setFont(font)
        self.tdateEdit = QtWidgets.QDateEdit(self.fgroup)
        self.tdateEdit.setGeometry(QtCore.QRect(120, 170, 110, 22))
        self.tdateEdit.setCalendarPopup(True)
        self.tdateEdit.setObjectName("dateEdit")
        #Control Buttons
        self.filterbtn = QtWidgets.QPushButton(self.fgroup)
        self.filterbtn.setGeometry(QtCore.QRect(30, 210, 75, 23))
        self.filterbtn.setObjectName("filterbtn")
        self.clearbtn = QtWidgets.QPushButton(self.fgroup)
        self.clearbtn.setGeometry(QtCore.QRect(140, 210, 75, 23))
        self.clearbtn.setObjectName("clearbtn")
        
        self.toolgroup = QtWidgets.QGroupBox(self.centralwidget)
        self.toolgroup.setGeometry(QtCore.QRect(10, 10, 251, 521))
        self.toolgroup.setCheckable(False)
        self.toolgroup.setObjectName("toolgroup")
        self.okbtn = QtWidgets.QPushButton(self.centralwidget)
        self.okbtn.setGeometry(QtCore.QRect(470, 580, 75, 23))
        self.okbtn.setObjectName("okbtn")
        self.cancelbtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelbtn.setGeometry(QtCore.QRect(580, 580, 75, 23))
        self.cancelbtn.setObjectName("cancelbtn")
        self.helpbtn = QtWidgets.QPushButton(self.centralwidget)
        self.helpbtn.setGeometry(QtCore.QRect(680, 580, 75, 23))
        self.helpbtn.setObjectName("helpbtn")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(10, 540, 250, 80))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("icons/codelogo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(270, 550, 731, 10))
        self.progressBar.setProperty("value", 1)
        self.progressBar.setObjectName("progressBar")
        self.Tab = QtWidgets.QTabWidget(self.centralwidget)
        self.Tab.setGeometry(QtCore.QRect(270, 20, 731, 511))
        self.Tab.setObjectName("Tab")
        self.FormTab = QtWidgets.QWidget()
        self.FormTab.setObjectName("FormTab")
        self.Tab.addTab(self.FormTab, icon, "")
        self.AnalysisTab = QtWidgets.QWidget()
        self.AnalysisTab.setObjectName("AnalysisTab")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/point.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Tab.addTab(self.AnalysisTab, icon1, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1020, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuData = QtWidgets.QMenu(self.menubar)
        self.menuData.setObjectName("menuData")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.File = QtWidgets.QToolBar(MainWindow)
        self.File.setObjectName("File")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.File)
        self.Edit = QtWidgets.QToolBar(MainWindow)
        self.Edit.setObjectName("Edit")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.Edit)
       
        
        self.Data = QtWidgets.QToolBar(MainWindow)
        self.Data.setObjectName("Data")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.Data)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon2)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon3)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon4)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/saveas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveAs.setIcon(icon5)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon6)
        self.actionQuit.setObjectName("actionQuit")
        self.actionCut = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon7)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon8)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon9)
        self.actionPaste.setObjectName("actionPaste")
        self.actionCreate_DataFrame = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/create.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCreate_DataFrame.setIcon(icon10)
        self.actionCreate_DataFrame.setObjectName("actionCreate_DataFrame")
        self.actionDelete_Record = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete_Record.setIcon(icon11)
        self.actionDelete_Record.setObjectName("actionDelete_Record")
        self.actionAdd_Record = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Record.setIcon(icon12)
        self.actionAdd_Record.setObjectName("actionAdd_Record")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuData.addAction(self.actionCreate_DataFrame)
        self.menuData.addAction(self.actionDelete_Record)
        self.menuData.addAction(self.actionAdd_Record)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuData.menuAction())
        self.File.addAction(self.actionOpen)
        self.File.addAction(self.actionNew)
        self.File.addAction(self.actionSave)
        self.File.addAction(self.actionSaveAs)
        self.File.addAction(self.actionQuit)
        self.Edit.addAction(self.actionCut)
        self.Edit.addAction(self.actionCopy)
        self.Edit.addAction(self.actionPaste)
        self.Data.addAction(self.actionCreate_DataFrame)
        self.Data.addAction(self.actionAdd_Record)
        self.Data.addAction(self.actionDelete_Record)

        #Table
        self.table = QtWidgets.QTableView(self.FormTab)
        w,h = self.FormTab.size().width(),self.FormTab.size().height()
        self.table.setGeometry(20,15,w+50,h-30)   
        
        #canvas        
        self._layout = QtWidgets.QVBoxLayout()
        self.fig = Figure()
        self._canvas = FigureCanvas(self.fig)
        self._canvas.figure.tight_layout()
        self._layout.addWidget(self._canvas)
        self.AnalysisTab.setLayout(self._layout)
        self._graph = self.fig.add_subplot(111)        
        self.navigation = NavigationToolbar(self._canvas,self.AnalysisTab)
        MainWindow.addToolBar(self.navigation)
        self.navigation.setObjectName("Navigation")

        self.retranslateUi(MainWindow)
        self.Tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Timesheet Application ver 1.0.0"))
        self.okbtn.setText(_translate("MainWindow", "Ok"))
        self.cancelbtn.setText(_translate("MainWindow", "Cancel"))
        self.helpbtn.setText(_translate("MainWindow", "Help"))
        self.Tab.setTabText(self.Tab.indexOf(self.FormTab), _translate("MainWindow", "TMS Form"))
        self.Tab.setTabText(self.Tab.indexOf(self.AnalysisTab), _translate("MainWindow", "Analysis"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.headerlabel.setText(_translate("MainWindow", "Filter by"))
        self.searchlabel.setText(_translate("MainWindow", "Select Item"))
        self.checkbox.setText(_translate("MainWindow", "Include Date"))
        self.fdate.setText(_translate("MainWindow", "From Date")) 
        self.tdate.setText(_translate("MainWindow", "Till Date"))
        self.fgroup.setTitle(_translate("MainWindow", "Data Filter")) 
        self.filterbtn.setText(_translate("MainWindow", "Filter"))
        self.clearbtn.setText(_translate("MainWindow", "Clear Filter"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuData.setTitle(_translate("MainWindow", "Data"))
        self.File.setWindowTitle(_translate("MainWindow", "Filemenu"))
        self.Edit.setWindowTitle(_translate("MainWindow", "Editmenu"))
        self.Data.setWindowTitle(_translate("MainWindow", "DataFrame"))
        self.navigation.setWindowTitle(_translate("MainWindow", "Navigation"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "click to open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "open new file"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "save file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSaveAs.setText(_translate("MainWindow", "SaveAs"))
        self.actionSaveAs.setStatusTip(_translate("MainWindow", "save file as"))
        self.actionSaveAs.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setStatusTip(_translate("MainWindow", "Quit Application"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setStatusTip(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setStatusTip(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setStatusTip(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionCreate_DataFrame.setText(_translate("MainWindow", "Create DataFrame"))
        self.actionCreate_DataFrame.setStatusTip(_translate("MainWindow", "Create DataFrame"))
        self.actionCreate_DataFrame.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionDelete_Record.setText(_translate("MainWindow", "Delete Record"))
        self.actionDelete_Record.setStatusTip(_translate("MainWindow", "Delete Record"))
        self.actionDelete_Record.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionAdd_Record.setText(_translate("MainWindow", "Add Record"))
        self.actionAdd_Record.setStatusTip(_translate("MainWindow", "Add Record"))
        self.actionAdd_Record.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.checkbox.clicked.connect(self._ondateclude)
        
        self._canvas.mpl_connect('pick_event',self.onclick)
        self.Tab.currentChanged.connect(self._ontabChanged)
        self.table.setContextMenuPolicy(QtCore.Qt.CustomContextMenu) 
        self.table.customContextMenuRequested.connect(self._ontableRightclick)
        self._ontabChanged()
        self._ondateclude()
        self.progressBar.hide()
        self._updategraph()
    def _ontabChanged(self,event=None):
        if self.Tab.currentIndex() == 1:
            self.navigation.show()
            # self.fgroup.close()
        else:
            # self.fgroup.show()
            self.navigation.close()
    def showlegend(self,event=None):
        self._graph.legend(loc='upper right',fontsize=8)
    def _updategraph(self,event=None):
        self._graph.grid(True,color='k',alpha=0.4)
        self._graph.tick_params(axis="x",rotation=90, labelsize=8)
        self._graph.tick_params(axis="y",labelsize=8) 
        self._graph.set_title(self.plotTitle,fontdict=self.font)
        self._graph.axes.set_xlabel(self.xlabel,fontdict = self.font)
        self._graph.axes.set_ylabel(self.ylabel,fontdict = self.font)
        self._canvas.figure.tight_layout()
        self._canvas.draw()
    def _resetScreen(self,event = None): 
        self._graph.clear()
        self._graph.tick_params(axis="x",rotation=90, labelsize=8)
        self._graph.tick_params(axis="y",labelsize=8) 
        self._graph.grid(True,color='k',alpha=0.4) 
        self._graph.axes.set_aspect('equal','datalim') 
        self._canvas.draw()
        self._canvas.figure.tight_layout()
    def _ontableRightclick(self,event=None):
        print("Right click event catched...")
    def onclick(self,event=None):
        try:
            self.gid = event
            msg = "Point Elevation {}".format(self.gid.artist.get_label())
            self.statusBar().showMessage(msg)
        except:
            pass
    def _ondateclude(self,event=None):
        if self.checkbox.isChecked() == True:
            self.fdateEdit.setEnabled(True)
            self.tdateEdit.setEnabled(True)
        else:
            self.fdateEdit.setEnabled(False)
            self.tdateEdit.setEnabled(False)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Application_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

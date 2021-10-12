# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 22:07:54 2021

@author: Administrator
"""

import os,json
from PyQt5 import QtCore, QtWidgets
from TMSGUIDialog import Application_MainWindow
import pandas as pd
from DataFrameTable import DataFrameModel,AlignDelegate #,ComboDelegate
import datetime


def setcell(self,row,col):
    self.activeclass = self.dwgdataBase.loc[row][col]
    if isinstance(self.activeclass,CustomWidget) == True:
        clb = CustomWidget(self.activeclass.lbText.text(),\
                            self.activeclass.img)
    else:
        clb = CustomWidget(str(df_array[row,col]),\
                            os.path.join(os.getcwd(),"aps.png"))                    
    self.table.setCellWidget(row,col,clb)
    self.dwgdataBase.loc[row][col] = clb
########################################################################
#                   Timesheet Application ver 1.0.0                    #
########################################################################
class TMSApplication(QtWidgets.QMainWindow,Application_MainWindow):
    defaultColumns = ["Project Code","Project Name","Job Mode","Job Description","Dwg/Doc Number",\
                      "Associated Engineer","Cad Designer","Software","Date","Time"]
    def __init__(self, parent=None):
        self.projectCodes = ["O18185","O20319","O20318","O20315",\
                             "T20248","T21724","T21679","T21804",\
                                 "9999I","9999M","9999H","9999T"]
        self.__activeRecord = None
        self.__newRecord = None
        super(TMSApplication, self).__init__(parent)
        self.setupUi(self)
        self.menutriggered()
        self.buttonactions()
    @property
    def activeRecord(self):
        return self.__activeRecord
    @activeRecord.setter
    def activeRecord(self,val=None):
        if val is None:
            pass
        else:
            self.__activeRecord = val
        return self.__activeRecord
    @property
    def newRecord(self):
        return self.__newRecord
    @newRecord.setter
    def newRecord(self,val=None):
        if val is None:
            pass
        else:
            self.__newRecord = val
        return self.__newRecord
    def keyReleaseEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self._closeApp()
        super(TMSApplication, self).keyReleaseEvent(event)
    
    def menutriggered(self):
        self.actionNew.triggered.connect(self._onnew)
        self.actionQuit.triggered.connect(self._closeApp)
        self.actionCopy.triggered.connect(self._oncopy)
        self.actionCut.triggered.connect(self._oncut)
        self.actionOpen.triggered.connect(self._onOpen)
        self.actionPaste.triggered.connect(self._onPaste)
        self.actionAdd_Record.triggered.connect(self._onAddRecord)
        self.actionCreate_DataFrame.triggered.connect(self._oncreateRecord)
        self.actionDelete_Record.triggered.connect(self._ondeleteRecord)
        self.actionSave.triggered.connect(self._onsave)
        self.actionSaveAs.triggered.connect(self._onsaveas)      
        

    def buttonactions(self):
        self.okbtn.clicked.connect(self._closeApp)
        self.cancelbtn.clicked.connect(self._closeApp)
        self.helpbtn.clicked.connect(self._onhelp)
    def formatData(self,delegate,dataframe):
        i = 0
        for col in dataframe.columns:
            self.table.setItemDelegateForColumn(i, delegate)
            i += 1
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
    def _closeApp(self,event=None):
        self.close()
    def _onnew(self,event=None):
        self.newRecord = pd.DataFrame(columns=self.defaultColumns)
        dm = DataFrameModel(self.newRecord)
        self.table.setModel(dm)
        delegate = AlignDelegate(dm)       
        self.formatData(delegate,self.newRecord)
    def _oncopy(self,event=None):
        self.statusBar().showMessage("file copied..")
    def _oncut(self,event=None):
        self.statusBar().showMessage("file clipped..")
    def _onOpen(self,event=None):
        path = os.getcwd()
        dframes = [f for f in os.listdir(path) if f.endswith("json")]
        if dframes != []:
            self.catagories = {}            
            for dframe in dframes:
                data = json.load(open(os.path.join(path,dframe)))
                newRecord = pd.DataFrame.from_dict(data)       
                newRecord.index = list(map(lambda u: int(u),newRecord.index.to_list()))
                dfname = dframe.split(".")[0]
                dm = DataFrameModel(newRecord)
                self.dm = dm
                self.table.setModel(dm)
                self.tableSelectionModel = self.table.selectionModel()
                self.tableSelectionModel.currentColumnChanged.connect(self.oncolumnchanged)
                delegate = AlignDelegate(dm)       
                self.formatData(delegate,newRecord)
                self.newRecord = self.dm._dataframe
                self.statusBar().showMessage("Active user {}..".format(dfname))
        else:            
            pass                    
                    
    def _onPaste(self,event=None):
        self.statusBar().showMessage("file pasted..")
    def _onAddRecord(self,event=None):
        if self.newRecord is None:
            return
        else:
            if self.newRecord.empty == True:
                idx = 0
            else:
                idx = self.newRecord.shape[0]
            for col in self.defaultColumns:
                if col == "Date":
                    date = datetime.datetime.today().strftime("%d-%b-%Y")                    
                    self.newRecord.loc[idx,col] = date
                elif col == "Time":
                    checkin = datetime.datetime.today().strftime("%H:%M:%S")
                    self.newRecord.loc[idx,col] = checkin
                else:
                    self.newRecord.loc[idx,col] = "N/A"
            dm = DataFrameModel(self.newRecord)
            self.dm = dm
            self.table.setModel(dm)
            self.tableSelectionModel = self.table.selectionModel()
            self.tableSelectionModel.currentColumnChanged.connect(self.oncolumnchanged)
            self.tableSelectionModel.currentRowChanged.connect(self.oncolumnchanged)
            delegate = AlignDelegate(dm)
            self.formatData(delegate,self.newRecord) 
            self.newRecord = self.dm._dataframe
            # self.cd = ComboDelegate(self,self.projectCodes)  
            # self.table.setItemDelegateForColumn(0,self.cd)                      
            # for row in range(len(self.projectCodes)):
            #     self.table.openPersistentEditor(dm.index(row,0))
    def _oncreateRecord(self,event=None):
        self.statusBar().showMessage("Record created..")
    def _ondeleteRecord(self,event=None):
        self.statusBar().showMessage("Record deleted..")
    def _onsave(self,event=None):
        path = os.path.join(os.getcwd(),"currentUser.json")
        self.newRecord.to_json(path)
    def _onsaveas(self,event=None):
        self.statusBar().showMessage("Record deleted..")
    def _onhelp(self,event=None):
        self.statusBar().showMessage("help opened..")
    def oncolumnchanged(self,item):        
        head = self.newRecord.columns[item.column()]
        value = item.data()
        sf = "Record # {} | {} : {}".format(item.row(),head,value)
        self.statusBar().showMessage(sf)
        
def banner(txt='',sep="#"):
    s = sep*72 + '\n'
    s = s + sep + txt.center(70) + sep + '\n'
    s = s + sep*72
    return s

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    y = TMSApplication()
    y.show()
    sys.exit(app.exec_())

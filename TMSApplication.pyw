# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 22:07:54 2021

@author: Administrator
"""

import os,json
from PyQt5 import QtCore, QtWidgets, QtGui
from TMSGUIDialog import Application_MainWindow
import pandas as pd
from DataFrameTable import DataFrameModel,AlignDelegate,CustomWidget,TableWidget
import datetime
from selectionDialog import SelectionDialog
from EditorDialog import dwgdocEditor
from uCalender import Ui_CalenderEditor
from SystemUtility import sysUtilities,browseFolder,browsefile
import openpyxl,xlrd

def saveFileDialog(parent=None,defaultname=''):
    filename = QtWidgets.QFileDialog.getSaveFileName(parent,\
                                                     'Export DataFrame',\
                                                         defaultname,\
                                                             "json Files (*.json);;Excel Files (*.xlsx);;Excel 1997-2000 Files (*.xls);;CSV Files (*.csv)",\
                                                                 options=QtWidgets.QFileDialog.DontUseNativeDialog)
    if filename[0] == '':
        return 0
    elif filename[0].endswith('.json'):
        filename = filename[0]
    else:
        filename = filename[0] + filename[1].split("(")[1].split(")")[0].split("*")[1]
    return filename
def openFileDialog(parent=None,defaultname=''):
    filename = QtWidgets.QFileDialog.getOpenFileName(parent,\
                                                     'Export DataFrame',\
                                                         defaultname,\
                                                             "json Files (*.json);;Excel Files (*.xlsx);;Excel 1997-2000 Files (*.xls);;CSV Files (*.csv)",\
                                                                 options=QtWidgets.QFileDialog.DontUseNativeDialog)
    if filename[0] == '':
        return 0
    elif filename[0].endswith('.json'):
        filename = filename[0]
    elif filename[0].endswith('.xlsx') or filename[0].endswith('.xls'):
        filename = filename[0]
    elif filename[0].endswith('.csv'):
        filename = filename[0]
    else:
        filename = filename[0] + filename[1].split("(")[1].split(")")[0].split("*")[1]
    return filename
########################################################################
#                        Read Project Database                         #
########################################################################
projectlist = os.path.join(os.getcwd(),"Project List.txt")
employeelist = os.path.join(os.getcwd(),"Employees_.txt")
softwarelist = os.path.join(os.getcwd(),"softwares.txt")
jobModes = os.path.join(os.getcwd(),"jobMode.txt")

def readprojects(p):
    projects = pd.DataFrame()
    f = open(p,"r")
    l = f.readlines()
    f.close()
    n = 0
    for u in l:
        pcode,pname,ptype = u.split("\t")
        projects.loc[n,"Project Code"] = pcode
        projects.loc[n,"Project Name"] = pname
        projects.loc[n,"Project Type"] = ptype.split("\n")[0]
        n += 1
    projects.drop(index=0,inplace=True)
    projects.index = range(projects.shape[0])
    return projects
def employeedata(p):
    employeedf = pd.DataFrame()
    f = open(p,"r")
    l = f.readlines()
    f.close()
    n = 0
    for u in l:
        try:
            pname,photo = u.split("\t")
            employeedf.loc[n,"Name"] = pname
            employeedf.loc[n,"photo"] = photo.split("\n")[0]
            n += 1
        except:
            pass
    employeedf.drop(index=0,inplace=True)
    return employeedf
def softwares(p):
    softwaresdf = pd.DataFrame()
    f = open(p,"r")
    l = f.readlines()
    f.close()
    n = 0
    for u in l:
        try:
            pname = u.split("\n")[0]
            softwaresdf.loc[n,"Name"] = pname
            n += 1
        except:
            pass
    softwaresdf.drop(index=0,inplace=True)
    return softwaresdf
def jobmodes(p):
    jobdf = pd.DataFrame()
    f = open(p,"r")
    l = f.readlines()
    f.close()
    n = 0
    for u in l:
        try:
            pname = u.split("\n")[0]
            jobdf.loc[n,"Name"] = pname
            n += 1
        except:
            pass
    jobdf.drop(index=0,inplace=True)
    return jobdf

class MyEvents(object):
    eventdata = pd.DataFrame()
    eventno = 0
    def __init__(self,name=None,eventTime=None,eventText=None):
        self.__name = name
        self.__eventTime = eventTime
        self.__eventText = eventText
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,val=None):
        if val is None:
            pass
        else:
            self.__name = val
        return self.__name
    @property
    def eventTime(self):
        return self.__eventTime
    @eventTime.setter
    def eventTime(self,val=None):
        if val is None:
            pass
        else:
            self.__eventTime = val
        return self.__eventTime
    @property
    def eventText(self):
        return self.__eventText
    @eventText.setter
    def eventText(self,val=None):
        if val is None:
            pass
        else:
            self.__eventText = val
        return self.__eventText
    def record(self):
        self.eventdata.loc[self.eventno,"Event"] = self.name
        self.eventdata.loc[self.eventno,"Time"] = self.eventTime
        self.eventdata.loc[self.eventno,"Text"] = self.eventText
        self.eventno += 1
        
########################################################################
#                   Timesheet Application ver 1.0.0                    #
########################################################################
class TMSApplication(QtWidgets.QMainWindow,sysUtilities,Application_MainWindow):
    _author = "Ashish Kumar Barh"
    _version = "1.0.0"
    _email = "barhashish@lntecc.com"
    defaultColumns = ["Project Code","Project Name","Job Mode","Job Description","Dwg/Doc Number",\
                      "Associated Employee","Software","Start Date","Close Date"]
    def __init__(self, parent=None):  
        self.__activeRecord = None
        self.__newRecord = None
        self.__startdate = None
        self.__closedate = None
        self.__lastindex = 0
        super(TMSApplication, self).__init__(parent)
        self.__activemonth = datetime.datetime.today().strftime("%b-%Y")
        self.__userdirectory = os.path.join(os.getcwd(),self.loginname)
        self.setupUi(self)
        self.menutriggered()
        self.buttonactions()
        self._onLaunch()
    @property
    def startdate(self):
        return self.__startdate
    @startdate.setter
    def startdate(self,val=None):
        if val is None:
            pass
        else:
            self.__startdate = val
        return self.__startdate
    @property
    def closedate(self):
        return self.__closedate
    @closedate.setter
    def closedate(self,val=None):
        if val is None:
            pass
        else:
            self.__closedate = val
        return self.__closedate
    @property
    def activemonth(self):
        return self.__activemonth
    @activemonth.setter
    def activemonth(self,val=None):
        if val is None:
            pass
        else:
            self.__activemonth = val
        return self.__activemonth 
    @property
    def lastindex(self):
        return self.__lastindex
    @lastindex.setter
    def lastindex(self,val=None):
        if val is None:
            pass
        else:
            self.__lastindex = val
        return self.__lastindex    
    @property
    def userdirectory(self):
        return self.__userdirectory
    @userdirectory.setter
    def userdirectory(self,val=None):
        if val is None:
            pass
        else:
            self.__userdirectory = val
        return self.__userdirectory
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
        # self.actionOpen.triggered.connect(self._onOpen)
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
        self.filterbtn.clicked.connect(self._onfilter)
        self.clearbtn.clicked.connect(self._onfilterclear)
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
        self._resetScreen()
    def _oncopy(self,event=None):
        self.statusBar().showMessage("file copied..")
    def _oncut(self,event=None):
        self.statusBar().showMessage("file clipped..")
    def _onOpen(self,event=None):
        dframe = openFileDialog(None)
        if dframe.endswith("json"):
            data = json.load(open(dframe))
            newRecord = pd.DataFrame.from_dict(data)  
            self.ondataformated(newRecord,dframe)
        elif dframe.endswith("xlsx"):
            self.activeworkbook = openpyxl.open(dframe)
            self.shtcombo.addItems(self.activeworkbook.sheetnames)
            self.activesheet = self.shtcombo.currentText()
            newRecord = pd.read_excel(dframe,sheet_name=self.activesheet)
            self.ccombo.addItems(newRecord.columns.to_list())
            self.dcombo.addItems(["Select Datatype","pyDate","float","integer"])
            items = [dframe,newRecord]
            self.dcombo.currentTextChanged.connect(lambda a: self._onconversion(a,items))
            self.ondataformated(newRecord,dframe)
        else:
            return    
    def _onconversion(self,event=None,a=None):
        col = self.ccombo.currentText()
        dtype = self.dcombo.currentText()
        df = a[1]
        dframe = a[0]
        if dtype == "pyDate":
            df[col] = df[col].apply(lambda u:u.strftime("%d-%b-%Y"))
            self.ondataformated(df,dframe)
        else:
            pass
    def ondataformated(self,newRecord,dframe):         
        newRecord.index = list(map(lambda u: int(u),newRecord.index.to_list()))
        dfname = dframe.split(".")[0]
        self.lastindex = newRecord.shape[0]
        dm = DataFrameModel(newRecord,lastidx=self.lastindex)
        self.dm = dm
        self.table.setModel(dm)
        self.tableSelectionModel = self.table.selectionModel()
        self.tableSelectionModel.currentColumnChanged.connect(self.oncolumnchanged)
        delegate = AlignDelegate(dm)       
        self.formatData(delegate,newRecord)
        self.newRecord = self.dm._dataframe                        
        self.statusBar().showMessage("Active user {}..".format(dfname))
        self.plotonOpen(self.newRecord)
    def _onLaunch(self,event=None):
        self.fdateEdit.setDate(datetime.datetime.today())
        self.tdateEdit.setDate(datetime.datetime.today())
        if os.path.exists(self.userdirectory) == True:
            self.activefolder = os.path.join(self.userdirectory,self.activemonth)
            if os.path.exists(self.activefolder) == True:
                dframes = [f for f in os.listdir(self.activefolder) if f.endswith("json")]
                if dframes != []:
                    self.catagories = {}   
                    dframe = dframes[0]
                    data = json.load(open(os.path.join(self.activefolder,dframe)))
                    newRecord = pd.DataFrame.from_dict(data)       
                    newRecord.index = list(map(lambda u: int(u),newRecord.index.to_list()))
                    dfname = dframe.split(".")[0]
                    self.lastindex = newRecord.shape[0]
                    dm = DataFrameModel(newRecord,lastidx=self.lastindex)
                    self.dm = dm
                    self.table.setModel(dm)
                    self.tableSelectionModel = self.table.selectionModel()
                    self.tableSelectionModel.currentColumnChanged.connect(self.oncolumnchanged)
                    delegate = AlignDelegate(dm)       
                    self.formatData(delegate,newRecord)
                    self.newRecord = self.dm._dataframe                        
                    self.statusBar().showMessage("Active user {}..".format(dfname))
                    headerItems = self.newRecord.columns.to_list()
                    self.header.addItems(headerItems[:-2])
                    self.header.currentTextChanged.connect(self._onheaderchanged)
                    self.searchbox.currentTextChanged.connect(self._onfilteritemchanged)
                    self._onheaderchanged()
                    self.plotonOpen(self.newRecord)
                else:            
                    pass   
            else:
                os.mkdir(self.activefolder)
        else:
            os.mkdir(self.userdirectory)
            self.activefolder = os.path.join(self.userdirectory,self.activemonth)
            os.mkdir(self.activefolder)                         
                    
    def _onPaste(self,event=None):
        self.statusBar().showMessage("file pasted..")
    def _onAddRecord(self,event=None):
        if self.newRecord is None:
            return
        else:
            if self.newRecord.empty == True:
                idx = 0
                self.lastindex = 0
            else:
                idx = self.newRecord.shape[0]
            for col in self.defaultColumns:
                if col == "Start Date":
                    date = datetime.datetime.today().strftime("%d-%b-%Y")                    
                    self.newRecord.loc[idx,col] = date
                elif col == "Time":
                    checkin = datetime.datetime.today().strftime("%H:%M:%S")
                    self.newRecord.loc[idx,col] = checkin
                else:
                    self.newRecord.loc[idx,col] = "N/A"
            dm = DataFrameModel(self.newRecord,lastidx=self.lastindex)
            self.dm = dm
            self.table.setModel(dm)
            self.tableSelectionModel = self.table.selectionModel()
            self.tableSelectionModel.currentColumnChanged.connect(self.oncolumnchanged)
            self.tableSelectionModel.currentRowChanged.connect(self.oncolumnchanged)
            delegate = AlignDelegate(dm)
            self.formatData(delegate,self.newRecord) 
            #Capture Event for SRT
            # self.newRecord = self.dm._dataframe   
            # self.name = "AddRecord"
            # self.eventText="Appending New Record to Active Timesheet"
            # dt = datetime.datetime.now()
            # self.eventTime = "{}:{}:{},{}".format(dt.hour,dt.minute,dt.second,format(dt.microsecond/1000.0, ',.0f'))
            # self.record()
            
    def _ontableRightclick(self,event=None):
        df = readprojects(projectlist)
        ee = employeedata(employeelist)
        sf = softwares(softwarelist)
        jf = jobmodes(jobModes)
        self.idl = SelectionDialog()        
        self.idl.setupUi(QtWidgets.QDialog())
        self.idl.comboBox.currentTextChanged.connect(self._onitemchanged)
        self.edl = dwgdocEditor()
        self.edl.setupUi(QtWidgets.QDialog())
        self.cdl = Ui_CalenderEditor()
        self.cdl.setupUi(QtWidgets.QDialog())
        if self.column == 0 and self.row >= self.lastindex:
            #Capture Event for SRT
            # self.newRecord = self.dm._dataframe   
            # self.name = "AddPrjCode"
            # self.eventText="Selecting Project Code from Project List"
            # dt = datetime.datetime.now()
            # self.eventTime = "{}:{}:{},{}".format(dt.hour,dt.minute,dt.second,format(dt.microsecond/1000.0, ',.0f'))
            # self.record()
            
            self.idl.comboBox.addItems(df['Project Code'])
            self.idl.dialog.setWindowTitle("Project code")
            self.idl.ListLabel.setText("Select Code:")
            self.idl.dialog.exec()
            self.fieldval = self.idl.comboBox.currentText()            
            if self.idl.datavalidated == True:
                fd = df[df['Project Code'] == self.fieldval]
                idx = fd.index[0]
                pn = df['Project Name'][idx]
                pt = df['Project Type'][idx]
                self.dm.setData(self.item,self.fieldval,DataFrameModel.ValueRole)
                self.dm.setData(self.dm.index(self.item.row(),1),pn,DataFrameModel.ValueRole)
                self.dm.setData(self.dm.index(self.item.row(),2),pt,DataFrameModel.ValueRole)
            else:
                pass
        elif self.column == 1 and self.row >= self.lastindex:
            #Capture Event for SRT
            # self.newRecord = self.dm._dataframe   
            # self.name = "AddPrjName"
            # self.eventText="Selecting Project Name from Project List"
            # dt = datetime.datetime.now()
            # self.eventTime = "{}:{}:{},{}".format(dt.hour,dt.minute,dt.second,format(dt.microsecond/1000.0, ',.0f'))
            # self.record()
            
            self.idl.comboBox.addItems(df['Project Name'])
            self.idl.dialog.setWindowTitle("Project Name")
            self.idl.ListLabel.setText("Select Name:")
            self.idl.dialog.exec()
            self.fieldval = self.idl.comboBox.currentText()
            if self.idl.datavalidated == True:
                fd = df[df['Project Name'] == self.fieldval]
                idx = fd.index[0]
                pc = df['Project Code'][idx]
                pt = df['Project Type'][idx]
                self.dm.setData(self.item,self.fieldval,DataFrameModel.ValueRole)
                self.dm.setData(self.dm.index(self.item.row(),0),pc,DataFrameModel.ValueRole)
                self.dm.setData(self.dm.index(self.item.row(),2),pt,DataFrameModel.ValueRole)
            else:
                pass            
        elif self.column == 2 and self.row >= self.lastindex:       
            self.idl.comboBox.addItems(df['Project Type'].unique())
            self.idl.dialog.setWindowTitle("Project Type")
            self.idl.ListLabel.setText("Select Type:")
            self.idl.dialog.exec()
            self.fieldval = self.idl.comboBox.currentText()
            if self.idl.datavalidated == True:
                self.dm.setData(self.item,self.fieldval,DataFrameModel.ValueRole)
            else:
                pass
        elif self.column == 3 and self.row >= self.lastindex:     
            #Capture Event for SRT
            # self.newRecord = self.dm._dataframe   
            # self.name = "AddJobDesc"
            # self.eventText="Selecting Project/Job Description from List"
            # dt = datetime.datetime.now()
            # self.eventTime = "{}:{}:{},{}".format(dt.hour,dt.minute,dt.second,format(dt.microsecond/1000.0, ',.0f'))
            # self.record()
            
            self.idl.comboBox.addItems(jf['Name'])
            self.idl.dialog.setWindowTitle("Job Description")
            self.idl.ListLabel.setText("Select Mode:")
            self.idl.dialog.exec()
            self.fieldval = self.idl.comboBox.currentText()
            if self.idl.datavalidated == True:
                self.dm.setData(self.item,self.fieldval,DataFrameModel.ValueRole)
            else:
                pass
        elif self.column == 4 and self.row >= self.lastindex:
            #Capture Event for SRT
            # self.newRecord = self.dm._dataframe   
            # self.name = "AddDwgDoc"
            # self.eventText="Adding Document or Drawing Number"
            # dt = datetime.datetime.now()
            # self.eventTime = "{}:{}:{},{}".format(dt.hour,dt.minute,dt.second,format(dt.microsecond/1000.0, ',.0f'))
            # self.record()
            
            self.edl.editorDialog.exec()
            if self.edl.datavalidated == True:
                self.fieldval = self.edl.lineEdit.text()
                self.dm.setData(self.item,self.fieldval,DataFrameModel.ValueRole)
            else:
                pass
        elif self.column == 5 and self.row >= self.lastindex:  
            #Capture Event for SRT
            # self.newRecord = self.dm._dataframe   
            # self.name = "AddEmployee"
            # self.eventText="Adding Employee Name you are associated to work"
            # dt = datetime.datetime.now()
            # self.eventTime = "{}:{}:{},{}".format(dt.hour,dt.minute,dt.second,format(dt.microsecond/1000.0, ',.0f'))
            # self.record()
            
            for name,photo in zip(ee['Name'],ee['photo']):
                icon = QtGui.QIcon("icons/" + photo + ".png")
                size = QtCore.QSize(20, 20)                
                self.idl.comboBox.addItem(icon,name)
                self.idl.comboBox.setIconSize(size)
            self.idl.dialog.setWindowTitle("Employee List")
            self.idl.ListLabel.setText("Select Employee:")
            self.idl.dialog.exec()
            self.fieldval = self.idl.comboBox.currentText()
            if self.idl.datavalidated == True:
                # self.clb = CustomWidget(self.fieldval,"icons/aps.png")  
                # self.clb.setGeometry(0,0,150,150)
                # self.table.setIndexWidget(self.item,self.clb)                
                self.dm.setData(self.item,self.fieldval,DataFrameModel.ValueRole)
            else:
                pass
        elif self.column == 6 and self.row >= self.lastindex:
            #Capture Event for SRT
            # self.newRecord = self.dm._dataframe   
            # self.name = "AddSoftware"
            # self.eventText="selection Software from List you are going to work in"
            # dt = datetime.datetime.now()
            # self.eventTime = "{}:{}:{},{}".format(dt.hour,dt.minute,dt.second,format(dt.microsecond/1000.0, ',.0f'))
            # self.record()
            
            self.idl.comboBox.addItems(sf['Name'])
            self.idl.dialog.setWindowTitle("Software List")
            self.idl.ListLabel.setText("Select Software:")
            self.idl.dialog.exec()
            self.fieldval = self.idl.comboBox.currentText()
            if self.idl.datavalidated == True:
                self.dm.setData(self.item,self.fieldval,DataFrameModel.ValueRole)
            else:
                pass
        else:
            pass
        if self.column == 8:
            #Capture Event for SRT
            # self.newRecord = self.dm._dataframe   
            # self.name = "AddClose"
            # self.eventText="Marking Close Date of Job"
            # dt = datetime.datetime.now()
            # self.eventTime = "{}:{}:{},{}".format(dt.hour,dt.minute,dt.second,format(dt.microsecond/1000.0, ',.0f'))
            # self.record()
            
            self.cdl.calenderDialog.setWindowTitle("Project Calendar")
            self.cdl.calenderDialog.exec()
            if self.cdl.datavalidated == True:
                self.dm.setData(self.item,self.cdl.cdate,DataFrameModel.ValueRole)
            else:
                pass
        else:
            pass
        delegate = AlignDelegate(self.dm)
        self.formatData(delegate,self.newRecord)
        
    def _oncreateRecord(self,event=None):
        self.statusBar().showMessage("Record created..")
    def _ondeleteRecord(self,event=None):
        self.statusBar().showMessage("Record deleted..")
    def _onsave(self,event=None):
        #Capture Event for SRT
        # self.newRecord = self.dm._dataframe   
        # self.name = "save"
        # self.eventText="Save Timesheet to default location"
        # dt = datetime.datetime.now()
        # self.eventTime = "{}:{}:{},{}".format(dt.hour,dt.minute,dt.second,format(dt.microsecond/1000.0, ',.0f'))
        # self.record()
        
        path = os.path.join(self.activefolder,"TMS_{}.json".format(self.activemonth))
        self.newRecord.to_json(path)
        self.plotonOpen(self.newRecord)
    def _onsaveas(self,event=None):
        #Capture Event for SRT
        # self.newRecord = self.dm._dataframe   
        # self.name = "saveas"
        # self.eventText="Saveas Timesheet to different format"
        # dt = datetime.datetime.now()
        # self.eventTime = "{}:{}:{},{}".format(dt.hour,dt.minute,dt.second,format(dt.microsecond/1000.0, ',.0f'))
        # self.record()
        
        savefilename = saveFileDialog(self,"TMS_{}".format(self.activemonth))
        if savefilename.endswith("json"):
            self.newRecord.to_json(savefilename)
        elif savefilename.endswith("xlsx"):
            self.newRecord.to_excel(savefilename,index=False)
        elif savefilename.endswith("xls"):
            self.newRecord.to_excel(savefilename,index=False)
        elif savefilename.endswith("csv"):
            self.newRecord.to_csv(savefilename,index=False)
        else:
            pass
    def _onhelp(self,event=None):
        self.statusBar().showMessage("help opened..")
    def _onitemchanged(self,event=None):
        #Capture Event for SRT
        # self.newRecord = self.dm._dataframe   
        # self.name = "prjchanged"
        # self.eventText="Check statusbar for project Name and Project Types"
        # dt = datetime.datetime.now()
        # self.eventTime = "{}:{}:{},{}".format(dt.hour,dt.minute,dt.second,format(dt.microsecond/1000.0, ',.0f'))
        # self.record()
            
        df = readprojects(projectlist)
        if self.item.column() == 0:
            self.fieldval = self.idl.comboBox.currentText()
            fd = df[df['Project Code'] == self.fieldval]
            idx = fd.index[0]
            pn = df['Project Name'][idx]
            pt = df['Project Type'][idx]
            sf = "Record # {} | {} | {}".format(self.row,pn,pt)
            self.statusBar().showMessage(sf)
        else:
            pass        
        
    def oncolumnchanged(self,item):
        self.item = item
        self.row = item.row()
        self.column = item.column()
        head = self.newRecord.columns[item.column()]
        value = item.data()
        sf = "Record # {} | {} : {}".format(item.row(),head,value)
        self.statusBar().showMessage(sf)
    def plotonOpen(self,df):
        self._resetScreen()
        xval = df['Project Code']
        yval = df['Start Date']
        self._graph.scatter(xval,yval,label=self.loginname,color='r')
        self.xlabel = "Project Code"
        self.ylabel = "Dates"
        self.showlegend()
        self._updategraph()
    def _onfilterclear(self,event=None):
        dm = DataFrameModel(self.newRecord,lastidx=self.lastindex)
        self.dm = dm
        self.table.setModel(dm)
        self.tableSelectionModel = self.table.selectionModel()
        self.tableSelectionModel.currentColumnChanged.connect(self.oncolumnchanged)
        self.tableSelectionModel.currentRowChanged.connect(self.oncolumnchanged)
        delegate = AlignDelegate(dm)
        self.formatData(delegate,self.newRecord) 
        self.newRecord = self.dm._dataframe
        self.plotonOpen(self.newRecord)
    def _onfilter(self,event=None):
        if self.checkbox.isChecked() == True:
            #Capture Event for SRT
            # self.newRecord = self.dm._dataframe   
            # self.name = "includedate"
            # self.eventText="Include Date for filter"
            # dt = datetime.datetime.now()
            # self.eventTime = "{}:{}:{},{}".format(dt.hour,dt.minute,dt.second,format(dt.microsecond/1000.0, ',.0f'))
            # self.record()
            
            startdate = pd.to_datetime(self.fdateEdit.text(),dayfirst=True).date()
            closedate = pd.to_datetime(self.tdateEdit.text(),dayfirst=True).date()
            self.startdate = startdate
            self.closedate = closedate
            self.tdf = self.newRecord.copy()
            self.tdf['Start Date'] = self.tdf['Start Date'].apply(lambda u:pd.to_datetime(u).date())
            self.tdf['Close Date'] = self.tdf['Close Date'].apply(lambda u:pd.to_datetime(u).date())
            mask = (self.tdf['Start Date'] >= self.startdate) & (self.tdf['Close Date'] <= self.closedate)
            df = self.tdf[mask]
            fdf = df[df[self.header.currentText()] == self.activeFilteritem]
            fdf.index = range(fdf.shape[0])
            dm = DataFrameModel(fdf,lastidx=self.tdf.shape[0])
            self.table.setModel(dm)
            self.plotonOpen(fdf)
        else:
            #Capture Event for SRT
            # self.newRecord = self.dm._dataframe   
            # self.name = "excludedate"
            # self.eventText="Exclude Date for filter"
            # dt = datetime.datetime.now()
            # self.eventTime = "{}:{}:{},{}".format(dt.hour,dt.minute,dt.second,format(dt.microsecond/1000.0, ',.0f'))
            # self.record()
            
            self.tdf = self.newRecord.copy()
            fdf = self.tdf[self.tdf[self.header.currentText()] == self.activeFilteritem]
            fdf.index = range(fdf.shape[0])
            dm = DataFrameModel(fdf,lastidx=self.tdf.shape[0])
            self.table.setModel(dm)
            self.plotonOpen(fdf)
    def _onheaderchanged(self,event=None):
        filtered = self.newRecord[self.header.currentText()].unique().tolist()
        self.searchbox.clear()
        self.searchbox.addItems(filtered)
        #Capture Event for SRT
        # self.newRecord = self.dm._dataframe   
        # self.name = "ChangeHeader"
        # self.eventText="Changing Column value to filter table"
        # dt = datetime.datetime.now()
        # self.eventTime = "{}:{}:{},{}".format(dt.hour,dt.minute,dt.second,format(dt.microsecond/1000.0, ',.0f'))
        # self.record()
    def _onfilteritemchanged(self,event=None):
        self.activeFilteritem = self.searchbox.currentText()
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

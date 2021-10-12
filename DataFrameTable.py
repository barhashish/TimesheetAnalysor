# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 14:44:06 2020

@author: barhashish
"""
from PyQt5 import QtWidgets,QtCore,QtGui
import os
import pandas as pd
import random
def getcolor():
    return random.choice(["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(256)])
def bfont(sz=10):
    font = QtGui.QFont()
    font.setBold(True)
    font.setPointSize(sz)
    return font
class TableWidget(QtWidgets.QTableWidget):
    def __init__(self,i,j,txt,icon):
        QtWidgets.QTableWidget.__init__(self)
        lb = CustomWidget(txt,icon)
        self.setCellWidget(i,j, lb)
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.cellClicked.connect(self.onCellClicked)
    @property
    def onCellClicked(self, row, column):
        w = self.cellWidget(row, column)
        print(w.text, w.img)
class CustomWidget(QtWidgets.QDialog):
    def __init__(self, text, img, parent=None):
        self.parent = parent
        super(CustomWidget,self).__init__()
        self._text = text
        self._img = img
        self.setLayout(QtWidgets.QVBoxLayout())
        self.lbPixmap = QtWidgets.QLabel(self)
        self.lbText = QtWidgets.QLabel(self)
        self.lbText.setAlignment(QtCore.Qt.AlignRight)
        self.layout().addWidget(self.lbPixmap)
        self.layout().addWidget(self.lbText)
        self.initImage()
        self.initText()
    def initImage(self):
        self.lbPixmap.setPixmap(QtGui.QPixmap(self._img).scaled(self.lbPixmap.size(),QtCore.Qt.KeepAspectRatio))        
    def initText(self):
        self.lbText.setText(self._text)        
    @property
    def img(self):
        return self._img

    @img.setter
    def img(self, value):
        if self._img == value:
            return
        self._img = value
        self.initImage()
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if self._text == value:
            return
        self._text = value
        self.initText()
class DataFrameModel(QtCore.QAbstractTableModel):
    DtypeRole = QtCore.Qt.UserRole + 1000
    ValueRole = QtCore.Qt.UserRole + 1001

    def __init__(self, df=pd.DataFrame(),lastidx=None,parent=None):
        self.__lastidx = lastidx
        super(DataFrameModel, self).__init__(parent)
        self._dataframe = df
    @property
    def lastidx(self):
        return self.__lastidx
    @lastidx.setter
    def lastidx(self,val=None):
        if val is None:
            pass
        else:
            self.__lastidx = val
        return self.__lastidx
    def setDataFrame(self, dataframe):
        self.beginResetModel()
        self._dataframe = dataframe#.copy()
        self.endResetModel()

    def dataFrame(self):
        return self._dataframe

    @QtCore.pyqtSlot(int, QtCore.Qt.Orientation, result=str)
    def headerData(self, section, orientation,role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self._dataframe.columns[section]
            else:
                return str(self._dataframe.index[section])        
        return QtCore.QVariant()

    def rowCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid():
            return 0
        return len(self._dataframe.index)

    def columnCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid():
            return 0
        return self._dataframe.columns.size
    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < self.rowCount() \
            and 0 <= index.column() < self.columnCount()):
            return QtCore.QVariant()
        row = self._dataframe.index[index.row()]
        col = self._dataframe.columns[index.column()]
        dt = self._dataframe[col].dtype
        val = self._dataframe.iloc[row][col]
        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            try:                
                return str(val)
            except:
                return val
        elif role == DataFrameModel.ValueRole:            
            return val 
        elif role == QtCore.Qt.BackgroundRole:
            if self._dataframe.columns[index.column()].lower().startswith('color'):
                return QtGui.QColor(val)
            else:
                pass
        elif role == QtCore.Qt.FontRole:
            if index.column() == 1:
                return bfont(8)
            else:
                return bfont(8)
        if role == DataFrameModel.DtypeRole:
            return dt
        return QtCore.QVariant()
    def setData(self, index, value, role):
        row = self._dataframe.index[index.row()]
        col = self._dataframe.columns[index.column()]
        if hasattr(value, 'toPyObject'):
            value = value.toPyObject()            
        else:
            if row >= self.lastidx:
                dtype = self._dataframe[col].dtype
                if dtype != object:
                    if value == '':
                        pass
                    else:
                        value = dtype.type(value)
                self._dataframe.loc[row, col] =  value
            else:
                pass
            if col == 'Close Date':
                dtype = self._dataframe[col].dtype
                if dtype != object:
                    if value == '':
                        pass
                    else:
                        value = dtype.type(value)
                self._dataframe.loc[row, col] =  value
            else:
                pass
        return True
    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
    def roleNames(self):
        roles = {
            QtCore.Qt.DisplayRole: b'display',
            DataFrameModel.DtypeRole: b'dtype',
            DataFrameModel.ValueRole: b'value',
            QtCore.Qt.EditRole: b'edit',            
        }
        return roles

class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter
    def get_icon(self, index):
        icon =  "icons/save.png"
        return QtGui.QIcon(icon)
    
class ComboDelegate(QtWidgets.QItemDelegate):
    def __init__(self, owner, choices):
        super().__init__(owner)
        self.items = choices
    def createEditor(self, parent, option, index):
        self.editor = QtWidgets.QComboBox(parent)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.editor.setFont(font)
        self.editor.setGeometry(0,0,100,15)
        self.editor.addItems(self.items)
        return self.editor
    def paint(self, painter, option, index):
        value = index.data(QtCore.Qt.DisplayRole)
        style = QtWidgets.QApplication.style()
        opt = QtWidgets.QStyleOptionComboBox()
        opt.text = str(value)
        opt.rect = option.rect
        style.drawComplexControl(QtWidgets.QStyle.CC_ComboBox, opt, painter)
        QtWidgets.QItemDelegate.paint(self, painter, option, index)
    def setEditorData(self, editor, index):
        value = index.data(QtCore.Qt.DisplayRole)
        num = self.items.index(value)
        editor.setCurrentIndex(num)
    def setModelData(self, editor, model, index):
        value = editor.currentText()
        model.setData(index, QtCore.Qt.DisplayRole, QtCore.QVariant(value))
    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

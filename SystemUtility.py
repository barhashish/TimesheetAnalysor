# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 06:51:06 2021

@author: Administrator
"""
from PyQt5 import QtWidgets
import os,comtypes.client,datetime
import pandas as pd
pd.set_option('display.max_rows',10)

def browsefile(parent=None,extension=None):
    path,_ =  QtWidgets.QFileDialog.getOpenFileName(parent,"Select Folder",filter=extension)
    return path
def browseFolder(parent=None):
    path = QtWidgets.QFileDialog.getExistingDirectory(parent,"Select Folder")
    if path == "":
        pass
    else:
        return os.path.abspath(path)
def renamefile(name):
    srcfile = browsefile()
    filepath = os.path.dirname(srcfile)
    extension = os.path.splitext(srcfile)[-1]
    newname = os.path.join(filepath,name + extension)
    os.rename(srcfile,newname)
class sysUtilities(object):
    def __init__(self):
        self.__loginname = os.getlogin()
        self.__environment = None
        super(sysUtilities,self).__init__()
        self._onsysUtilitiesIntitialised()
    @property
    def loginname(self):
        return self.__loginname
    @loginname.setter
    def loginname(self,val=None):
        if val is None:
            pass
        else:
            self.__loginname = val
        return self.__loginname
    @property
    def environment(self):
        return self.__environment
    @environment.setter
    def environment(self,val=None):
        if val is None:
            pass
        else:
            self.__environment = val
        return self.__environment
    def _onsysUtilitiesIntitialised(self):
        self.syscount = 0
        self.sysfiles = pd.DataFrame()
        self.environment = pd.DataFrame.from_dict(os.environ,orient='index',columns=['Parameters']).T
        self.shutil = comtypes.client.CreateObject("Shell.Application")
        self.fso = comtypes.client.CreateObject("scripting.filesystemobject")
        self.wso = comtypes.client.CreateObject("Wscript.Shell")
        self.drives = pd.DataFrame()
        n = 0
        for i in self.fso.Drives:
            self.drives.loc[n,"Name"] = i.DriveLetter
            self.drives.loc[n,"SpaceAvailable"] = i.AvailableSpace
            self.drives.loc[n,"TotalSize"] = i.TotalSize
            n += 1
    def getanyfileProperty(self,filepath=None):        
        if filepath is None:
            activefile= browsefile(None,"*.*")
        else:
            activefile = filepath
        if activefile:
            self.currentfile = self.fso.GetFile(activefile)
            created = self.currentfile.DateCreated
            accessed = self.currentfile.DateLastAccessed
            modified = self.currentfile.DateLastModified
            self.created = datetime.datetime.fromtimestamp((created - 25570) * 86400.0)
            self.accessed = datetime.datetime.fromtimestamp((accessed - 25570) * 86400.0)
            self.modified = datetime.datetime.fromtimestamp((modified - 25570) * 86400.0)
            self.sysfiles.loc[self.syscount,"DateCreated"] = self.created.strftime("%a %d %b-%Y")
            self.sysfiles.loc[self.syscount,"DateModified"] = self.modified.strftime("%a %d %b-%Y")
            self.sysfiles.loc[self.syscount,"DateAccessed"] = self.accessed.strftime("%a %d %b-%Y")            
            self.sysfiles.loc[self.syscount,"FileName"] = self.currentfile.Name.split(".")[0]
            self.sysfiles.loc[self.syscount,"FilePath"] = self.currentfile.Path
            self.sysfiles.loc[self.syscount,"FileSize"] = self.currentfile.Size
            self.sysfiles.loc[self.syscount,"FileType"] = self.currentfile.Type
            self.syscount += 1
        else:
            pass
    def scandrive(self,directory=None):
        if directory is None:
            directory = browseFolder()
        else:
            pass
        for item in os.listdir(directory):
            try:
                filepath = os.path.join(directory,item)
                if os.path.isfile(filepath):
                    self.getanyfileProperty(filepath)
                else:
                    self.scandrive(os.path.join(directory,item))
            except:
                pass

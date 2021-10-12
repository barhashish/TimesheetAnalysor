# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 17:09:06 2021

@author: Administrator
"""

class Employee(object):
    def __init__(self,name=None,month=None,record=None,**kwarg):
        self.__name = name
        self.__month = month
        self.__employeeRecord = record
        self._kwarg = kwarg
        super(Employee,self).__init__()
        self._onInitialiseEmployee()
    def __str__(self):
        return "{} at {}".format(self.__class__.__name__,hex(id(self)))
    def _onInitialiseEmployee(self):
        if self._kwarg == {}:
            return
        else:
            for k,v in self._kwarg.items():
                setattr(self,k,v)    
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
    def month(self):
        return self.__month
    @month.setter
    def month(self,val=None):
        if val is None:
            pass
        else:
            self.__month = val
        return self.__month
    @property
    def employeeRecord(self):
        return self.__employeeRecord
    @employeeRecord.setter
    def employeeRecord(self,val=None):
        if val is None:
            pass
        else:
            self.__employeeRecord = val
        return self.__employeeRecord
if __name__ == "__main__":
    y = Employee()
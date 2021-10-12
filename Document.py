# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 17:09:06 2021

@author: Administrator
"""

class Document(object):
    def __init__(self,documentnumber=None,**kwarg):
        self.__documentnumber = documentnumber
        self._kwarg = kwarg
        super(Document,self).__init__()
        self._onInitialiseDocument()
    def __str__(self):
        return "{} at {}".format(self.__class__.__name__,hex(id(self)))
    def _onInitialiseDocument(self):
        if self._kwarg == {}:
            return
        else:
            for k,v in self._kwarg.items():
                setattr(self,k,v)                
    @property
    def documentnumber(self):
        return self.__documentnumber
    @documentnumber.setter
    def documentnumber(self,val=None):
        if val is None:
            pass
        else:
            self.__documentnumber = val
        return self.__documentnumber
if __name__ == "__main__":
    y = Document()
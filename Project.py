# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 17:09:06 2021

@author: Administrator
"""

class Project(object):
    def __init__(self,projectcode=None,projectname=None,**kwarg):
        self.__projectcode = projectcode
        self.__projectname = projectname
        self._kwarg = kwarg
        super(Project,self).__init__()
        self._onInitialiseProject()
    def __str__(self):
        return "{} at {}".format(self.__class__.__name__,hex(id(self)))
    def _onInitialiseProject(self):
        if self._kwarg == {}:
            return
        else:
            for k,v in self._kwarg.items():
                setattr(self,k,v)
    @property
    def projectcode(self):
        return self.__projectcode
    @projectcode.setter
    def projectcode(self,val=None):
        if val is None:
            pass
        else:
            self.__projectcode = val
        return self.__projectcode
    @property
    def projectname(self):
        return self.__projectname
    @projectname.setter
    def projectname(self,val=None):
        if val is None:
            pass
        else:
            self.__projectname = val
        return self.__projectname
if __name__ == "__main__":
    y = Project()
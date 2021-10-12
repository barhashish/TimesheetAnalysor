# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 17:09:06 2021

@author: Administrator
"""

class Drawing(object):
    def __init__(self,drawingnumber=None,**kwarg):
        self.__drawingnumber = drawingnumber
        self._kwarg = kwarg
        super(Drawing,self).__init__()
        self._onInitialiseDrawing()
    def __str__(self):
        return "{} at {}".format(self.__class__.__name__,hex(id(self)))
    def _onInitialiseDrawing(self):
        if self._kwarg == {}:
            return
        else:
            for k,v in self._kwarg.items():
                setattr(self,k,v)                
    @property
    def drawingnumber(self):
        return self.__drawingnumber
    @drawingnumber.setter
    def drawingnumber(self,val=None):
        if val is None:
            pass
        else:
            self.__drawingnumber = val
        return self.__drawingnumber
if __name__ == "__main__":
    y = Drawing()
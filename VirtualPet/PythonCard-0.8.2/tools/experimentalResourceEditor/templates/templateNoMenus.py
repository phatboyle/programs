#!/usr/bin/python

"""
__version__ = "$Revision: 1.1 $"
__date__ = "$Date: 2004/10/24 19:21:46 $"
"""

from PythonCard import model

class MyBackground(model.Background):

    def on_initialize(self, event):
        # if you have any initialization
        # including sizer setup, do it here
        pass


if __name__ == '__main__':
    app = model.Application(MyBackground)
    app.MainLoop()

{'application':{'type':'Application',
          'name':'Spirograph',
    'backgrounds': [
    {'type':'Background',
          'name':'bgSpirograph',
          'title':'Spirograph PythonCard Application',
          'size':(770, 595),
          'statusBar':1,

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileOpen',
                   'label':'&Open...\tCtrl+O',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileSaveAs',
                   'label':'Save &As...',
                  },
                  {'type':'MenuItem',
                   'name':'fileSep1',
                   'label':'-',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit\tAlt+X',
                   'command':'exit',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuEdit',
             'label':'&Edit',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuEditCopy',
                   'label':'&Copy\tCtrl+C',
                  },
                  {'type':'MenuItem',
                   'name':'menuEditPaste',
                   'label':'&Paste\tCtrl+V',
                  },
                  {'type':'MenuItem',
                   'name':'editSep1',
                   'label':'-',
                  },
                  {'type':'MenuItem',
                   'name':'menuEditClear',
                   'label':'&Clear',
                   'command':'editClear',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'BitmapCanvas', 
    'name':'bufOff', 
    'position':(3, 3), 
    'size':(525, 525), 
    'thickness':1, 
    },

{'type':'StaticText', 
    'name':'stcFixedCircleRadius', 
    'position':(540, 30), 
    'text':'Fixed circle radius (1 - 100):', 
    },

{'type':'StaticText', 
    'name':'stcMovingCircleRadius', 
    'position':(540, 70), 
    'text':'Moving circle radius (-50 - 50):', 
    },

{'type':'StaticText', 
    'name':'stcMovingCircleOffset', 
    'position':(540, 110), 
    'text':'Moving circle offset (1 - 100):', 
    },

{'type':'StaticText', 
    'name':'stcRevolutionsInRadians', 
    'position':(540, 260), 
    'text':'Revolutions in radians (1 - 500):', 
    },

{'type':'Slider', 
    'name':'sldFixedCircleRadius', 
    'position':(540, 46), 
    'size':(200, 20), 
    'layout':'horizontal', 
    'max':100, 
    'min':1, 
    'value':74, 
    },

{'type':'Slider', 
    'name':'sldMovingCircleRadius', 
    'position':(540, 86), 
    'size':(200, 20), 
    'layout':'horizontal', 
    'max':50, 
    'min':-50, 
    'value':25, 
    },
    
{'type':'Slider', 
    'name':'sldMovingCircleOffset', 
    'position':(540, 126), 
    'size':(200, 20), 
    'layout':'horizontal', 
    'max':100, 
    'min':1, 
    'value':78, 
    },

{'type':'Button', 
    'name':'btnColor', 
    'position':(540, 154), 
    'label':'Color', 
    'backgroundColor':(0, 128, 255),
    },
    
{'type':'CheckBox', 
    'name':'chkDarkCanvas', 
    'position':(652, 160), 
    'checked':0, 
    'label':'Dark Canvas', 
    },

{'type':'RadioGroup', 
    'name':'radDrawingStyle', 
    'position':(540, 200), 
    'items':['Lines', 'Points'], 
    'label':'Draw as', 
    'layout':'horizontal', 
    'max':1, 
    'stringSelection':'Lines', 
    },

{'type':'Slider', 
    'name':'sldRevolutionsInRadians', 
    'position':(540, 276), 
    'size':(200, 20), 
    'layout':'horizontal', 
    'max':500, 
    'min':1, 
    'value':50, 
    },

{'type':'CheckBox', 
    'name':'chkAutoRefresh', 
    'position':(540, 310), 
    'checked':1, 
    'label':'Update display while drawing', 
    },

{'type':'CheckBox', 
    'name':'chkClearDisplay', 
    'position':(540, 330), 
    'checked':1, 
    'label':'Clear display before drawing', 
    },

{'type':'Button', 
    'name':'btnRandom', 
    'position':(540, 360), 
    'label':'Random Circle Values', 
    },

{'type':'Button', 
    'name':'btnDraw', 
    'position':(550, 400), 
    'label':'Draw', 
    },

{'type':'Button', 
    'name':'btnCancel', 
    'position':(650, 400), 
    'label':'Stop', 
    },

] # end components
} # end background
] # end backgrounds
} }

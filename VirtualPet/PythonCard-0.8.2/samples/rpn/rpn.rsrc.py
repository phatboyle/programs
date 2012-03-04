{'application':{'type':'Application',
          'name':'RPN',
    'backgrounds': [
    {'type':'Background',
          'name':'bgMin',
          'title':'RPN Calc',
          'size':(325, 287),

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit\tAlt+X',
                   'command':'exit',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuHelp',
             'label':'&Help',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuHelpAbout',
                   'label':'&About\tAlt+A',
                  },
                  {'type':'MenuItem',
                   'name':'menuHelpContents',
                   'label':'C&ontents\tAlt+O',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'Button', 
    'name':'RCLBtn', 
    'position':(265, 50), 
    'size':(38, 34), 
    'label':'RCL', 
    'toolTip':'Recall from Register', 
    },

{'type':'Button', 
    'name':'STOBtn', 
    'position':(265, 95), 
    'size':(38, 34), 
    'label':'STO', 
    'toolTip':'Store to Register', 
    },

{'type':'Button', 
    'name':'SwapBtn', 
    'position':(265, 140), 
    'size':(38, 34), 
    'label':'SWP', 
    'toolTip':'Swap X and Y', 
    },

{'type':'Button', 
    'name':'ROTBtn', 
    'position':(215, 50), 
    'size':(38, 34), 
    'label':'ROT', 
    'toolTip':'Rotate Stack', 
    },

{'type':'Button', 
    'name':'BackBtn', 
    'position':(215, 95), 
    'size':(38, 34), 
    'label':'BS', 
    'toolTip':'Delete last Character', 
    },

{'type':'Button', 
    'name':'InvertBtn', 
    'position':(215, 140), 
    'size':(38, 34), 
    'label':'1/x', 
    'toolTip':'Invert X', 
    },

{'type':'Button', 
    'name':'EnterBtn', 
    'position':(215, 185), 
    'size':(88, 34), 
    'label':'Enter', 
    'toolTip':'Enter Data to X Register', 
    },

{'type':'TextField', 
    'name':'result', 
    'position':(15, 5), 
    'size':(290, 30), 
    'alignment':'right', 
    'text':'0', 
    'toolTip':'Result ', 
    },

{'type':'Button', 
    'name':'9Btn', 
    'position':(115, 50), 
    'size':(38, 34), 
    'label':'9',
    'toolTip':'9',
    },

{'type':'Button', 
    'name':'8Btn', 
    'position':(65, 50), 
    'size':(38, 34), 
    'label':'8',
    'toolTip':'8',
    },

{'type':'Button', 
    'name':'7Btn', 
    'position':(15, 50), 
    'size':(38, 34), 
    'label':'7', 
    'toolTip':'7',
    },

{'type':'Button', 
    'name':'6Btn', 
    'position':(115, 95), 
    'size':(38, 34), 
    'label':'6', 
    'toolTip':'6',
    },

{'type':'Button', 
    'name':'5Btn', 
    'position':(65, 95), 
    'size':(38, 34), 
    'label':'5', 
    'toolTip':'5',
    },

{'type':'Button', 
    'name':'4Btn', 
    'position':(15, 95), 
    'size':(38, 34), 
    'label':'4',
    'toolTip':'4',
    },

{'type':'Button', 
    'name':'3Btn', 
    'position':(115, 140), 
    'size':(38, 34), 
    'label':'3', 
    'toolTip':'3',
    },

{'type':'Button', 
    'name':'2Btn', 
    'position':(65, 140), 
    'size':(38, 34), 
    'label':'2', 
    'toolTip':'2',
    },

{'type':'Button', 
    'name':'1Btn', 
    'position':(15, 140), 
    'size':(38, 34), 
    'label':'1',
    'toolTip':'1',
    },

{'type':'Button', 
    'name':'0Btn', 
    'position':(15, 185), 
    'size':(38, 34), 
    'label':'0', 
    'toolTip':'0',
    },

{'type':'Button', 
    'name':'DecimalBtn', 
    'position':(65, 185), 
    'size':(38, 34), 
    'label':'.', 
    'toolTip':'Decimal', 
    },

{'type':'Button', 
    'name':'CHSBtn', 
    'position':(115, 185), 
    'size':(38, 34), 
    'label':'+/-', 
    'toolTip':'Change Sign', 
    },

{'type':'Button', 
    'name':'DivideBtn', 
    'position':(165, 50), 
    'size':(38, 34), 
    'label':'/', 
    'toolTip':'Divide', 
    },

{'type':'Button', 
    'name':'MultiplyBtn', 
    'position':(165, 95), 
    'size':(38, 34), 
    'label':'X', 
    'toolTip':'Multiply', 
    },

{'type':'Button', 
    'name':'MinusBtn', 
    'position':(165, 140), 
    'size':(38, 34), 
    'label':'-', 
    'toolTip':'Subtract', 
    },

{'type':'Button', 
    'name':'PlusBtn', 
    'position':(165, 185), 
    'size':(38, 34), 
    'label':'+', 
    'toolTip':'Add', 
    },

] # end components
} # end background
] # end backgrounds
} }

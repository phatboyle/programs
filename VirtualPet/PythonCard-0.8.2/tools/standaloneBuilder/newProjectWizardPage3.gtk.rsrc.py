{'type':'CustomDialog',
    'name':'Template',
    'title':'New Project Wizard',
    'position':(171, 401),
    'size':(600, 310),
    'components': [

{'type':'StaticText', 
    'name':'page3text1', 
    'position':(175, 0), 
    'actionBindings':{}, 
    'font':{'faceName': 'Tahoma', 'family': 'sansSerif', 'size': 20}, 
    'text':'New project wizard', 
    'userdata':'page3', 
    },

{'type':'StaticText', 
    'name':'page3text2', 
    'position':(175, 60), 
    'actionBindings':{}, 
    'text':'Base directory', 
    'userdata':'page3', 
    },

{'type':'TextField', 
    'name':'baseDir', 
    'position':(175, 80), 
    'size':(385, -1), 
    'actionBindings':{}, 
    'userdata':'page3', 
    },

{'type':'Button', 
    'name':'baseDirBtn', 
    'position':(565, 80), 
    'size':(25, 25), 
    'actionBindings':{}, 
    'label':'...', 
    'userdata':'page3', 
    },

{'type':'Image', 
    'name':'Image1', 
    'position':(-5, -5), 
    'size':(174, 324), 
    'actionBindings':{}, 
    'file':'pixmaps/newproject.png', 
    },

] # end components
} # end CustomDialog

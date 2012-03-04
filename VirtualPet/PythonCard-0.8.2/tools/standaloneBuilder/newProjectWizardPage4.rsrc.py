{'type':'CustomDialog',
    'name':'Template',
    'title':'New Project Wizard',
    'position':(175, 82),
    'size':(600, 330),
    'components': [

{'type':'Image', 
    'name':'Image1', 
    'position':(-5, -5), 
    'size':(174, 324), 
    'file':'pixmaps/newproject.png', 
    },

{'type':'Button', 
    'name':'backBtn', 
    'position':(340, 275), 
    'enabled':False, 
    'label':'< Back', 
    },

{'type':'Button', 
    'name':'nextBtn', 
    'position':(415, 275), 
    'label':'Next >', 
    },

{'type':'Button', 
    'id':5101, 
    'name':'cancelBtn', 
    'position':(510, 275), 
    'label':'Cancel', 
    },

{'type':'StaticText', 
    'name':'page4text1', 
    'position':(175, 0), 
    'font':{'faceName': 'Tahoma', 'family': 'sansSerif', 'size': 20}, 
    'text':'Ready to create new project', 
    'userdata':'page4', 
    },

{'type':'StaticText', 
    'name':'page4text3', 
    'position':(175, 85), 
    'font':{'faceName': u'Tahoma', 'size': 10}, 
    'text':'We now have the information required to create a brand new project.', 
    'userdata':'page4', 
    },

{'type':'StaticText', 
    'name':'page4text4', 
    'position':(175, 100), 
    'font':{'faceName': u'Tahoma', 'size': 10}, 
    'text':'Click Create to continue, or Cancel to exit the wizard.', 
    'userdata':'page4', 
    },

{'type':'StaticText', 
    'name':'page4text5', 
    'position':(175, 125), 
    'font':{'faceName': u'Tahoma', 'size': 10}, 
    'text':'After the project has been created, you should open the project', 
    'userdata':'page4', 
    },

{'type':'StaticText', 
    'name':'page4text6', 
    'position':(175, 140), 
    'font':{'faceName': u'Tahoma', 'size': 10}, 
    'text':'properties page and ensure that the settings are to your liking.', 
    'userdata':'page4', 
    },

] # end components
} # end CustomDialog

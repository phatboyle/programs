{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':'resourceEditor Property Editor',
          'size':(416, 619),
          'statusBar':1,
          'visible':0,

         'components': [

{'type':'CheckBox', 
    'name':'alphabetizeComponents', 
    'position':(5, 231), 
    'label':'Alphabetize Components', 
    },

{'type':'CheckBox', 
    'name':'chkallowNameLabelVariation', 
    'position':(149, 24), 
    'size':(70, -1), 
    'label':'Vary', 
    },

{'type':'ImageButton', 
    'name':'SendToBack', 
    'position':(8, 301), 
    'size':(24, 32), 
    'border':'3d', 
    'command':'componentSendBack', 
    'file':'images/send_to_back.png', 
    'toolTip':'Send component(s) to back', 
    },

{'type':'ImageButton', 
    'name':'MoveBack', 
    'position':(32, 301), 
    'size':(24, 32), 
    'border':'3d', 
    'command':'componentMoveBack', 
    'file':'images/move_back.png', 
    'toolTip':'Move component(s) towards back', 
    },

{'type':'ImageButton', 
    'name':'reLayer', 
    'position':(56, 333), 
    'size':(32, 32), 
    'border':'3d', 
    'command':'componentRelayer', 
    'file':'images/relayer.png', 
    'toolTip':'Re-layer components, top-left to bottom right', 
    },

{'type':'ImageButton', 
    'name':'MoveTogether', 
    'position':(56, 301), 
    'size':(32, 32), 
    'border':'3d', 
    'command':'componentMoveTogether', 
    'file':'images/move_together.png', 
    'toolTip':'Gather components together', 
    },

{'type':'ImageButton', 
    'name':'MoveForward', 
    'position':(88, 301), 
    'size':(24, 32), 
    'border':'3d', 
    'command':'componentMoveForward', 
    'file':'images/move_forward.png', 
    'toolTip':'Move component(s) towards front', 
    },

{'type':'ImageButton', 
    'name':'SendToFront', 
    'position':(112, 301), 
    'size':(24, 32), 
    'border':'3d', 
    'command':'componentBringFront', 
    'file':'images/send_to_front.png', 
    'toolTip':'Send component(s) to front', 
    },

{'type':'StaticText', 
    'name':'Properties', 
    'position':(214, 6), 
    'text':'Properties', 
    },

{'type':'StaticText', 
    'name':'txtname', 
    'position':(160, 24), 
    'size':(84, -1), 
    'alignment':'right', 
    'text':'name', 
    },

{'type':'TextField', 
    'name':'fldname', 
    'position':(250, 20), 
    'size':(148, -1), 
    },

{'type':'StaticText', 
    'name':'txtlabel', 
    'position':(160, 56), 
    'size':(84, -1), 
    'alignment':'right', 
    'text':'Label', 
    },

{'type':'StaticText', 
    'name':'txttextArea', 
    'position':(160, 56), 
    'size':(84, -1), 
    'alignment':'right', 
    'text':'Text', 
    },

{'type':'StaticText', 
    'name':'txttext', 
    'position':(160, 56), 
    'size':(84, -1), 
    'alignment':'right', 
    'text':'Text', 
    },

{'type':'StaticBox', 
    'name':'stbAlign', 
    'position':(194, 59), 
    'size':(166, 114), 
    'label':'ALIGN', 
    },

{'type':'TextField', 
    'name':'fldtext', 
    'position':(250, 52), 
    'size':(148, -1), 
    },

{'type':'TextField', 
    'name':'fldlabel', 
    'position':(250, 52), 
    'size':(148, -1), 
    },

{'type':'ImageButton', 
    'name':'alignTop', 
    'position':(236, 79), 
    'size':(24, 24), 
    'border':'3d', 
    'command':'align', 
    'file':'images/align_top.png', 
    'toolTip':'Align component tops', 
    },

{'type':'TextArea', 
    'name':'fldtextArea', 
    'position':(250, 52), 
    'size':(148, 55), 
    },

{'type':'ImageButton', 
    'name':'alignVerticalCentres', 
    'position':(315, 81), 
    'size':(24, 24), 
    'border':'3d', 
    'command':'align', 
    'file':'images/align_vert_centres.png', 
    'toolTip':'Align component centres in a vertical stack', 
    },

{'type':'CheckBox', 
    'name':'chkenabled', 
    'position':(150, 115), 
    'size':(80, -1), 
    'command':'checkedProperty', 
    'label':'Enabled', 
    },

{'type':'ImageButton', 
    'name':'alignLeft', 
    'position':(200, 112), 
    'size':(24, 24), 
    'border':'3d', 
    'command':'align', 
    'file':'images/align_left.png', 
    'toolTip':'Align component left edges', 
    },

{'type':'CheckBox', 
    'name':'chkvisible', 
    'position':(230, 115), 
    'size':(80, -1), 
    'command':'checkedProperty', 
    'label':'Visible', 
    },

{'type':'ImageButton', 
    'name':'alignRight', 
    'position':(270, 112), 
    'size':(24, 24), 
    'border':'3d', 
    'command':'align', 
    'file':'images/align_right.png', 
    'toolTip':'Align component right edges', 
    },

{'type':'CheckBox', 
    'name':'chkchecked', 
    'position':(310, 115), 
    'size':(80, -1), 
    'command':'checkedProperty', 
    'label':'Checked', 
    },

{'type':'StaticText', 
    'name':'txtbackgroundColor', 
    'position':(160, 160), 
    'size':(84, -1), 
    'alignment':'right', 
    'text':'backgroundColor', 
    },

{'type':'ImageButton', 
    'name':'alignBottom', 
    'position':(236, 140), 
    'size':(24, 24), 
    'border':'3d', 
    'command':'align', 
    'file':'images/align_bottom.png', 
    'toolTip':'Align component bottoms', 
    },

{'type':'ImageButton', 
    'name':'alignHorizontalCentres', 
    'position':(314, 139), 
    'size':(24, 24), 
    'border':'3d', 
    'command':'align', 
    'file':'images/align_horiz_centres.png', 
    'toolTip':'Align component centres in a horizontal line', 
    },

{'type':'TextField', 
    'name':'fldbackgroundColor', 
    'position':(250, 160), 
    'text':'backgroundColor', 
    },

{'type':'TextField', 
    'name':'fldforegroundColor', 
    'position':(250, 135), 
    'text':'foregroundColor', 
    },

{'type':'Button', 
    'name':'clrforegroundColor', 
    'position':(356, 135), 
    'size':(35, -1), 
    'command':'color', 
    'label':'...', 
    },

{'type':'Button', 
    'name':'clrbackgroundColor', 
    'position':(356, 160), 
    'size':(35, -1), 
    'command':'color', 
    'label':'...', 
    },

{'type':'StaticText', 
    'name':'txtforegroundColor', 
    'position':(160, 140), 
    'size':(84, -1), 
    'alignment':'right', 
    'text':'foregroundColor', 
    },

{'type':'StaticText', 
    'name':'txtborder', 
    'position':(160, 215), 
    'size':(84, -1), 
    'alignment':'right', 
    'text':'Border', 
    },

{'type':'Choice', 
    'name':'popborder', 
    'position':(238, 210), 
    'size':(160, -1), 
    'items':[], 
    },

{'type':'StaticText', 
    'name':'txtfont', 
    'position':(160, 240), 
    'size':(84, -1), 
    'alignment':'right', 
    'text':'Font', 
    },

{'type':'TextField', 
    'name':'fldfont', 
    'position':(250, 234), 
    },

{'type':'Button', 
    'name':'fntfont', 
    'position':(350, 232), 
    'size':(55, -1), 
    'command':'changeFont', 
    'label':'Font...', 
    },

{'type':'StaticText', 
    'name':'txtposition', 
    'position':(150, 265), 
    'size':(42, -1), 
    'alignment':'right', 
    'text':'Position', 
    },

{'type':'StaticBox', 
    'name':'stbDistribute', 
    'position':(197, 179), 
    'size':(166, 101), 
    'label':'DISTRIBUTE', 
    },

{'type':'ImageButton', 
    'name':'distHorizEdge', 
    'position':(215, 199), 
    'size':(32, 32), 
    'border':'3d', 
    'command':'distribute', 
    'file':'images/dist_horiz_edge.png', 
    'toolTip':'Distribute horizontally, edge-to-edge', 
    },

{'type':'ImageButton', 
    'name':'distVertEdge', 
    'position':(295, 199), 
    'size':(32, 32), 
    'border':'3d', 
    'command':'distribute', 
    'file':'images/dist_vert_edge.png', 
    'toolTip':'Distribute vertically, edge-to-edge', 
    },

{'type':'TextField', 
    'name':'fldposition', 
    'position':(205, 260), 
    'size':(68, -1), 
    },

{'type':'ImageButton', 
    'name':'distHorizFirstLast', 
    'position':(215, 234), 
    'size':(32, 32), 
    'border':'3d', 
    'command':'distribute', 
    'file':'images/dist_horiz_space.png', 
    'toolTip':'Distribute horizontally, first to last', 
    },

{'type':'StaticText', 
    'name':'txtsize', 
    'position':(290, 265), 
    'size':(31, -1), 
    'alignment':'right', 
    'text':'Size', 
    },

{'type':'ImageButton', 
    'name':'distVertFirstLast', 
    'position':(296, 233), 
    'size':(32, 32), 
    'border':'3d', 
    'command':'distribute', 
    'file':'images/dist_vert_space.png', 
    'toolTip':'Distribute vertically, first to last', 
    },

{'type':'TextField', 
    'name':'fldsize', 
    'position':(330, 260), 
    'size':(68, -1), 
    },

{'type':'StaticBox', 
    'name':'stbEqualize', 
    'position':(197, 290), 
    'size':(166, 62), 
    'label':'EQUALIZE', 
    },

{'type':'ImageButton', 
    'name':'equalWidth', 
    'position':(214, 312), 
    'border':'3d', 
    'command':'equal', 
    'file':'images/equal_width.png', 
    'toolTip':'Equalize heights to those of the first component', 
    },

{'type':'ImageButton', 
    'name':'equalHeight', 
    'position':(265, 312), 
    'size':(32, 32), 
    'border':'3d', 
    'command':'equal', 
    'file':'images/equal_height.png', 
    'toolTip':'Equalize heights to that of the first component', 
    },

{'type':'ImageButton', 
    'name':'equalBoth', 
    'position':(316, 312), 
    'size':(32, 32), 
    'border':'3d', 
    'command':'equal', 
    'file':'images/equal_both.png', 
    'toolTip':'Equalize width & height to those of the first component', 
    },

{'type':'ImageButton', 
    'name':'nudgeDown', 
    'position':(60, 454), 
    'size':(18, 24), 
    'border':'none', 
    'command':'nudge', 
    'file':'images/nudge_down.png', 
    'toolTip':'Nudge components down by specified distance', 
    },

{'type':'ImageButton', 
    'name':'nudgeUp', 
    'position':(60, 399), 
    'size':(18, 24), 
    'border':'none', 
    'command':'nudge', 
    'file':'images/nudge_up.png', 
    'toolTip':'Nudge components up by specified distance', 
    },

{'type':'Spinner', 
    'name':'nudgeDistance', 
    'position':(51, 430), 
    'size':(41, -1), 
    'max':4, 
    'min':1, 
    'toolTip':'Distance to nudge components', 
    'value':1, 
    },

{'type':'ImageButton', 
    'name':'nudgeRight', 
    'position':(100, 429), 
    'size':(18, 24), 
    'border':'none', 
    'command':'nudge', 
    'file':'images/nudge_right.png', 
    'toolTip':'Nudge components to right by specified distance', 
    },

{'type':'ImageButton', 
    'name':'nudgeLeft', 
    'position':(23, 430), 
    'size':(18, 24), 
    'border':'none', 
    'command':'nudge', 
    'file':'images/nudge_left.png', 
    'toolTip':'Nudge components to left by specified distance', 
    },

{'type':'StaticBox', 
    'name':'stbNudge', 
    'position':(3, 377), 
    'size':(141, 130), 
    'label':'NUDGE', 
    },

{'type':'Button', 
    'name':'wUpdate', 
    'position':(10, 518), 
    'label':'Update', 
    'toolTip':'Update changes', 
    },

{'type':'List', 
    'name':'wComponentList', 
    'position':(7, 21), 
    'size':(134, 204), 
    'items':[], 
    },

{'type':'StaticText', 
    'name':'stcNameClass', 
    'position':(5, 3), 
    'text':'Name  :  Class', 
    },

] # end components
} # end background
] # end backgrounds
} }

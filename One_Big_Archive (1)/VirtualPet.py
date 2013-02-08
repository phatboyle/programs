# VirtualPet.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Simple virtual pet program using Pythoncard


from PythonCard import model, timer, dialog
import pickle, datetime, wx

# This is the class for the PythonCard main window
class MyBackground(model.Background):

    def on_initialize(self, event):
        self.doctor = False
        self.walking = False
        self.sleeping = False
        self.playing = False
        self.eating = False
        self.time_cycle = 0
        self.hunger = 0
        self.happiness  = 8
        self.health = 8
        self.forceAwake = False
        self.sleepImages = ["sleep1.gif","sleep2.gif","sleep3.gif", "sleep4.gif"]  # Here are the images
        self.eatImages = ["eat1.gif", "eat2.gif"]                                  # for the different animations
        self.walkImages = ["walk1.gif", "walk2.gif", "walk3.gif", "walk4.gif"]     #
        self.playImages = ["play1.gif", "play2.gif"]                               #
        self.doctorImages = ["doc1.gif", "doc2.gif"]                               #
        self.nothingImages  = ["pet1.gif", "pet2.gif", "pet3.gif"]                 #
        
        self.imageList = self.nothingImages
        self.imageIndex = 0
        
        self.myTimer1 = timer.Timer(self.components.petwindow, -1)          # Animation timer
        self.myTimer1.Start(500) 
        # timers have to belong to a component, so we made the
        # 'tick' timer part of the HungerGuage component
        self.myTimer2 = timer.Timer(self.components.HungerGauge, -1)        
        self.myTimer2.Start(5000)                                           
        filehandle = True
        try:                                                   # open the pickle file
            file = open("savedata_vp.pkl", "r")                # if there is one
        except:
            filehandle = False
        if filehandle:
            save_list = pickle.load(file)
            file.close()
        else:
            save_list = [8, 8, 0, datetime.datetime.now(), 0]
        self.happiness = save_list[0]
        self.health    = save_list[1]
        self.hunger    = save_list[2]
        then = save_list[3]
        self.time_cycle = save_list[4]

        difference = datetime.datetime.now() - then
        ticks = difference.seconds / 50  
        for i in range(0, ticks):
            self.time_cycle += 1
            if self.time_cycle == 60:
                self.time_cycle = 0
            if self.time_cycle <= 48:        #awake
                self.sleeping = False
                if self.hunger < 8:
                    self.hunger += 1                
            else:                            #sleeping
                self.sleeping = True
                if self.hunger < 8 and self.time_cycle % 3 == 0:
                    self.hunger += 1
            if self.hunger == 7 and (self.time_cycle % 2 ==0) and self.health > 0:
                self.health -= 1
            if self.hunger == 8 and self.health > 0:  
                self.health -=1
        if self.sleeping:
            self.imageList = self.sleepImages
        else:
            self.imageList = self.nothingImages
                
    def sleep_test(self):
        if self.sleeping:
            result = dialog.messageDialog(self, """WARNING!
Your pet is sleeping, if you wake him up he'll be unhappy!
Do you want to proceed?""", 'WARNING!', 
wx.ICON_EXCLAMATION | wx.YES_NO | wx.NO_DEFAULT)

            if result.accepted:
                self.sleeping = False
                self.happiness -= 4
                self.forceAwake = True
                return True
            else:
                return False
        else:
            return True
# the next section has event handlers for the
# button clicks for each 'activity' button
    def on_doctor_mouseClick(self, event):
        if self.sleep_test():        
            self.imageList = self.doctorImages
            self.doctor = True
            self.walking = False
            self.eating = False
            self.playing = False
    
    def on_feed_mouseClick(self, event):
        if self.sleep_test():
            self.imageList = self.eatImages
            self.eating = True
            self.walking = False
            self.playing = False
            self.doctor = False
    
    def on_play_mouseClick(self, event):
        if self.sleep_test():
            self.imageList = self.playImages
            self.playing = True
            self.walking = False
            self.eating = False
            self.doctor = False
    
    def on_walk_mouseClick(self, event):
        if self.sleep_test():
            self.imageList = self.walkImages
            self.walking = True
            self.eating = False
            self.playing = False
            self.doctor = False
            
    def on_stop_mouseClick(self, event):
        if not self.sleeping:        
            self.imageList = self.nothingImages
            self.walking = False
            self.eating = False
            self.playing = False
            self.doctor = False

# here is the event handler for the animation timer
# it moves to the next image in the list
    def on_petwindow_timer(self, event):
        if self.sleeping and not self.forceAwake:
            self.imageList = self.sleepImages
        self.imageIndex += 1
        if self.imageIndex >= len(self.imageList):
            self.imageIndex = 0
        self.components.petwindow.file = self.imageList[self.imageIndex]
        self.components.HappyGauge.value = self.happiness
        self.components.HealthGauge.value = self.health
        self.components.HungerGauge.value = self.hunger

# event handler for the 'tick' timer (every 5 seconds)       
    def on_HungerGauge_timer(self, event):
        self.time_cycle += 1
        if self.time_cycle == 60:
            self.time_cycle = 0
        if self.time_cycle <= 48 or self.forceAwake:        # awake
            self.sleeping = False
        else:
            self.sleeping = True                            # sleeping
        if self.time_cycle == 0:
            self.forceAwake = False
        
        if self.doctor:
            self.health += 1
        elif self.walking and (self.time_cycle % 2 == 0):
            self.happiness += 1
            self.health += 1
        elif self.playing:
            self.happiness += 1
        elif self.eating:
            self.hunger -= 1
        elif self.sleeping:
            if self.time_cycle % 3 == 0:
                self.hunger += 1
        else:  #awake, doing nothing                   
            self.hunger += 1
            if self.time_cycle % 2 == 0:
                self.happiness -= 1
        if self.hunger > 8:  self.hunger = 8
        if self.hunger < 0:  self.hunger = 0
        if self.hunger == 7 and (self.time_cycle % 2 ==0) :
            self.health -= 1
        if self.hunger == 8:  
            self.health -=1   
        if self.health > 8:  self.health = 8
        if self.health < 0:  self.health = 0
        if self.happiness > 8:  self.happiness = 8
        if self.happiness < 0:  self.happiness = 0
        self.components.HappyGauge.value = self.happiness
        self.components.HealthGauge.value = self.health
        self.components.HungerGauge.value = self.hunger

    # save data to the pickle file
    def on_close(self, event):
        file = open("savedata_vp.pkl", "w")
        save_list = [self.happiness, self.health, self.hunger, datetime.datetime.now(), self.time_cycle]
        pickle.dump(save_list, file)
        event.Skip()
        
app = model.Application(MyBackground)
app.MainLoop()

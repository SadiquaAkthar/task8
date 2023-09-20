#parent class
class TV:
    # constructor class with default parameter
    def __init__(self,brand):
        self.brand = brand
        self.price = 50000
        self.inches = 40
        self.OnOff = 1
        self.volume = 50
        self.channel =1
    
    # to reset the values to default
    def reset(self):
        self.__init__(self.brand)
        print("RESET "
              "\nbrand :",self.brand,
              "\nprice :",self.price,
              "\ninches :",self.inches,
              "\nOnOff :",self.OnOff,
              "\nvolume :",self.volume,
              "\nchannel :",self.channel)
        return 
    # display the status
    def status(self):
        print(self.brand," at channel ",self.channel,", volume ",self.volume)
        
    # increase the volume if less than 100    
    def increase_volume(self,volume):
        if self.volume > 0 and self.volume < 100 and self.OnOff ==1:
            self.volume=self.volume+volume
            print("Volume increased : ", self.volume)
        elif self.volume >=100:
            print("volume is maxium :", self.volume)
    
    # decrease the volume if more than 0
    def decrease_volume(self,volume):
        if self.volume > 0 and self.volume <= 100 and self.OnOff ==1:
            self.volume=self.volume-volume
            print("volume is decreased :",self.volume)
        elif self.volume == 0:
            print("volume is minimum :", self.volume)
    
    # set the channel 
    def set_channel(self,channel,OnOff):
        if channel < 50 and channel >0 and self.OnOff ==1:
            print("channel is ",channel)
        elif channel >= 50 :
            print("channel is ",self.channel)
            print()

 
class PlasmaTV(TV):
    #inheriting the attributes of TV class and also its own attributes
    def __init__(self,brand,screen_thickness,energy_usage,Lifespan,Refresh_rate,viewingAngle,Backlight):
        self.screen_thickness =screen_thickness
        self.energy_usage =energy_usage
        self.Lifespan=Lifespan
        self.Refresh_rate=Refresh_rate
        self.viewingAngle=viewingAngle
        self.Backlight=Backlight
        TV.__init__(self,brand)
        
    #display the details from the status method of the parent class and also its own attributes
    def display_details(self):
        print("\n**Details of LED TV**")
        TV.status(self)
        print("price :",self.price,
              "\ninches :",self.inches,
              "\nscreen_thicknessl :",self.screen_thickness,
              "\nenergy_usage :",self.energy_usage,
              "\nLifespanl :",self.Lifespan,
              "\nRefresh_rate :",self.Refresh_rate,
              "\nviewingAngle :",self.viewingAngle,
              "\nBacklightl :",self.Backlight
              )
    
class LedTV(TV):
    #inheriting the attributes of TV class and also its own attributes
    def __init__(self,brand,screen_thickness,energy_usage,Lifespan,Refresh_rate,viewingAngle,Backlight):
        self.screen_thickness =screen_thickness
        self.energy_usage =energy_usage
        self.Lifespan=Lifespan
        self.Refresh_rate=Refresh_rate
        self.viewingAngle=viewingAngle
        self.Backlight=Backlight
        TV.__init__(self,brand)
        
        #display the details from the status method of the parent class and also its own attributes
    def display_details(self):
        print("\n**Details of LED TV**")
        TV.status(self)
        print("price :",self.price,
              "\ninches :",self.inches,
              "\nscreen_thicknessl :",self.screen_thickness,
              "\nenergy_usage :",self.energy_usage,
              "\nLifespanl :",self.Lifespan,
              "\nRefresh_rate :",self.Refresh_rate,
              "\nviewingAngle :",self.viewingAngle,
              "\nBacklightl :",self.Backlight)
#creating object for parent class
obj1= TV("sony")
obj2= TV("sony")
#increasing volume, decrease volume, setthe channel, reset and display the status for parent class
obj1.increase_volume(10)
obj1.decrease_volume(30)
obj1.set_channel(45,1)
obj1.reset()
obj1.status()
#increasing volume, decrease volume, setthe channel, reset and display the status for parent class
obj2.increase_volume(20)
obj2.decrease_volume(40)
obj2.set_channel(60,1)
obj2.reset()
obj2.status()
# displaying the child class
objChild1 = PlasmaTV("panasonic",9,2400,5,20,80,2)
objChild1.display_details()
# displaying the child class
objChild2 = LedTV("samsung",9,2400,5,20,80,2)
objChild2.display_details()

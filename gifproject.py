#Monse Hernandez & Claudia Garcia
#Final project
#CST205 Spring 2014
#This code will help you create a GIF based on your input through a GUI
import wx
from moviepy.editor import *
class Display(wx.Frame):

    #Constructor
    #precondition: passes self, *args, & *kwargs
    #postcondition: defines the GUI
    def __init__(self, *args, **kwargs):
        super(Display, self).__init__(*args, **kwargs)     
        self.InitUI()

    #precondition:passes self
    #postcondition:sets up GUI frame and components
    def InitUI(self):    
        self.SetBackgroundColour('pink')    
        self.SetSize((500, 500))                
        self.SetTitle('DIY GIF!')               
        self.Centre()
        
        menuBar = wx.MenuBar()  #defines menu bar  
        gifMenu = wx.Menu()    #defines gifMenu

        menuBar.Append(gifMenu, 'Gif Type')         #Appends all GIF type choices to gifMenu
        self.SetMenuBar(menuBar)
        regular = gifMenu.Append(121, 'Regular\tCtrl-R', 'Regular')
        freeze = gifMenu.Append(122, 'Freeze\tCtrl-F', 'Freeze')      
        backwards = gifMenu.Append(123, 'BackwardsForwards\tCtrl-B', 'BackwardsForwards')
        fade = gifMenu.Append(124, 'Fade\tCtrl-D', 'Fade')
        loop = gifMenu.Append(125, 'Loop\tCtrl-L', 'Loop')
        crop = gifMenu.Append(126, 'Crop\tCtrl-C', 'Crop')
       
        
        self.Bind(wx.EVT_MENU, self.Regular,regular)        #Connects GIF type functions to choices in gifMenu
        self.Bind(wx.EVT_MENU, self.Freeze, freeze)
        self.Bind(wx.EVT_MENU, self.BackwardsForwards, backwards)
        self.Bind(wx.EVT_MENU, self.Fade, fade)
        self.Bind(wx.EVT_MENU, self.Loop, loop)
        self.Bind(wx.EVT_MENU, self.Crop, crop)

        
        loadButton = wx.Button(self, wx.ID_OK, 'Load Clip', pos = (20,105)) #Creates loadButton
        self.Bind(wx.EVT_BUTTON, self.loadClip, loadButton)
        quitButton = wx.Button(self, wx.ID_EXIT, 'Quit', pos = (200, 400))  #Creates quitButton
        self.Bind(wx.EVT_BUTTON, self.OnQuit, quitButton)


        self.quote = wx.StaticText(self, label = 'WELCOME! Please follow the next steps to make you very own GIF:' , pos = (3,3))                                                    #Adds all texts labels
        self.quote = wx.StaticText(self, label = '1) Pick video form file using Load Clip button', pos = (3,15))
        self.quote = wx.StaticText(self, label = '2) Type in the time interval ', pos = (3,28))
        self.quote = wx.StaticText(self, label = '3)Enter size and speed ratio', pos = (3,41))
        self.quote = wx.StaticText(self, label = '4)Enter snap time, and left and right if necessary', pos = (3,54))
        self.quote = wx.StaticText(self, label = '5)When done, choose desired effect from Gif Type menu.', pos = (3,67))
        self.quote = wx.StaticText(self, label = 'Enjoy!', pos = (200,80))
        self.quote0 = wx.StaticText(self, label = ' Enter time period in seconds', pos=(20,140))
        self.quote1 = wx.StaticText(self, label = 'From: ', pos = (20,160))    
        self.quote2 = wx.StaticText(self, label = 'To: ', pos = (115,160))      
        self.quote3 = wx.StaticText(self, label = 'Gif name (name.gif): ', pos = (280,140))
        self.quote4 = wx.StaticText(self, label = 'Speed: ', pos = (20,200))
        self.quote5 = wx.StaticText(self, label ='For Freeze option only', pos = (20,260))
        self.quote6 = wx.StaticText(self, label = 'Size: ', pos = (280,200))
        self.quote7 = wx.StaticText(self, label = 'Snap time: ', pos = (20,280))
        self.quote7 = wx.StaticText(self, label = 'For Cropping option only', pos = (280,260))
        self.quote8 = wx.StaticText(self, label = 'Left: ', pos = (280,280))
        self.quote9 = wx.StaticText(self, label = 'Right: ', pos = (360,280))

        self.t1 = wx.TextCtrl(self, value = '', pos = (55,160), size = (40,-1))        #Adds all text boxes for user input
        self.t2 = wx.TextCtrl(self, value = '', pos = (135,160), size = (40,-1))
        self.gName = wx.TextCtrl(self, value='', pos = (310,160), size = (110,-1))
        self.spe = wx.TextCtrl(self, value='', pos = (60,200), size = (110,-1))
        self.siz = wx.TextCtrl(self, value = '', pos = (310,200), size = (110,-1))
        self.sna = wx.TextCtrl(self, value='', pos = (80,280), size = (110,-1))
        self.Left = wx.TextCtrl(self, value = '', pos = (307,280), size = (40,-1))
        self.Right = wx.TextCtrl(self, value = '', pos = (395,280), size = (40,-1))
        imagePath = ''
       
        self.Show()
        
    #precondition:passes self and event
    #postcondition:closes the GUI
    def OnQuit(self, e):
        self.Close()
        
    #precondition:passes passes self and event
    #postcondition:allows user to select a clip from folder 
    def loadClip(self,event):
        wc = 'All image file (*.mp4;*.png;*.bmp;*.gif)|*.mp4;*.png;*.bmp;*.gif|JPEG file (*.mp4)|*.jpg|GIF file (*.gif)|*.gif|BMP file (*.bmp)|*.bmp|PNG file (*.png)|*.png'
        dialogue = wx.FileDialog(None, message = 'Select image to display', wildcard = wc, style = wx.OPEN)
        if dialogue.ShowModal() == wx.ID_OK:
            self.imagePath = dialogue.GetPath()
        dialogue.Destroy()
    ()

    #precondition:passes self and event
    #postcondition:creates the Regular type GIF
    def Regular(self, event):
        time1 = self.t1.GetValue()      #Stores values into function variables
        time2 = self.t2.GetValue()
        Size = self.siz.GetValue()
        gifName = self.gName.GetValue()
        tmp = checkGIFName(gifName)
        gifName = tmp        
        imagePath = self.imagePath
        
        video = VideoFileClip(imagePath).\
        subclip(float(time1),float(time2)).\
        resize(float(Size)).\
        to_gif(gifName, fps = None, program = 'ffmpeg')

    #precondition:passes self and event
    #postcondition:creates creates the Backwards/Forwards GIF     
    def BackwardsForwards(self, event):
        time1 = self.t1.GetValue()      #Stores values into function variables
        time2 = self.t2.GetValue()
        Size = self.siz.GetValue()
        gifName = self.gName.GetValue()
        tmp = checkGIFName(gifName)
        gifName = tmp
        imagePath = self.imagePath
        VideoFileClip(imagePath).\
        subclip(float(time1), float(time2)).\
        resize(float(Size)).\
        fx(time_symetrize).\
        to_gif(gifName, fps = 15, program = 'ffmpeg')

    #precondition:passes self and event
    #postcondition:creates Freeze type GIF
    def Freeze(self, event):
        time1 = self.t1.GetValue()      #Stores values into function variables
        time2 = self.t2.GetValue()
        Size = self.siz.GetValue()
        speed = self.spe.GetValue()
        snap = self.sna.GetValue()
        gifName = self.gName.GetValue()
        tmp = checkGIFName(gifName)
        gifName = tmp
        imagePath = self.imagePath
        bow = VideoFileClip(imagePath).\
        subclip(float(time1), float(time2)).\
        speedx(float(speed)).\
        resize(float(Size))

        #cuts it in half, freezing the left half only
        snapshot = bow.\
        crop(x2 = bow.w/2).\
        to_ImageClip(float(snap)).\
        set_duration(bow.duration)

        CompositeVideoClip([bow, snapshot]).\
        to_gif(gifName, fps = 15, program = 'ffmpeg')

    #precondition:passes self and event
    #postcondition:creates Fade type GIF
    def Fade(self, event):
        time1 = self.t1.GetValue()      #Stores values into function variables
        time2 = self.t2.GetValue()
        Size = self.siz.GetValue()
        speed = self.spe.GetValue()
        snap = self.sna.GetValue()
        gifName = self.gName.GetValue()
        tmp = checkGIFName(gifName)
        gifName = tmp
        imagePath = self.imagePath

        spark = VideoFileClip(imagePath).\
        subclip(float(time1), float(time2)).\
        speedx(float(speed)).\
        resize(float(Size))
    	
        d = spark.duration
        spark = spark.crossfadein(d/2)

        CompositeVideoClip([spark, spark.set_start(d/2), spark.set_start(d)]).\
        subclip(d/2, 3*d/2).\
        to_gif(gifName, fps = 15, program = 'ffmpeg')

    #precondition:passes self and event
    #postcondition:creates Loop type GIF
    def Loop(self, event):
        time1 = self.t1.GetValue()      #Stores values into function variables
        time2 = self.t2.GetValue()
        Size = self.siz.GetValue()
        speed = self.spe.GetValue()
        gifName = self.gName.GetValue()
        tmp = checkGIFName(gifName)
        gifName = tmp
        imagePath = self.imagePath
        
        boo = VideoFileClip(imagePath).\
        subclip(float(time1), float(time2))
        
        d = boo.duration
        snapshot = boo.to_ImageClip().\
        set_duration(d/6).\
        crossfadein(d/6).\
        set_start(5*d/6)
        
        CompositeVideoClip([boo, snapshot]).\
        to_gif(gifName, fps = 15, program = 'ffmpeg')

    #precondition:passes self and event
    #postcondition:creates Crop type GIF
    def Crop(self, event):
        time1 = self.t1.GetValue()      #Stores values into function variables
        time2 = self.t2.GetValue()
        Size = self.siz.GetValue()
        speed = self.spe.GetValue()
        gifName = self.gName.GetValue()
        tmp = checkGIFName(gifName)
        gifName = tmp
        imagePath = self.imagePath
        VideoFileClip(imagePath).\
        subclip(float(time1),float(time2)).\
        resize(float(Size)).\
        crop(x1=150,x2=250).\
        to_gif(gifName, fps = 15, program = 'ffmpeg')

#precondition:passes gif name
#postcondition:adds '.gif' to gifName
def checkGIFName(name):
    extension = '.gif'
    if name.endswith(extension) != True:
            name+=extension
    return name

#precondition:passes clip
#postcondition:needed for the Loop function                
def time_symetrize(clip):
    return concatenate([clip, clip.fx( vfx.time_mirror)])

#precondition:none
#postcondition:calls everything 
def main():
    ex = wx.App()
    Display(None)
    ex.MainLoop()
    
main()







    
   






#Prgrogam will construct a GUI using wxpython.
import wx

class Display(wx.Frame):

    #Constructor
    #precondition: passes self, *args, & *kwargs
    #postcondition: defines the GUI
    def __init__(self, *args, **kwargs):
        super(Display, self).__init__(*args, **kwargs)     
        self.InitUI()

    #precondition:passes self
    #postcondition:creates all buttons, menus, and text boxes
    def InitUI(self):    

        self.SetBackgroundColour("sky blue")    #sets background color
        self.SetSize((250, 250))                #sets GUI size
        self.SetTitle('DIY GIF!')               #GUI title
        self.Centre()
        
        menuBar = wx.MenuBar()  #defines menu bar  
        fileMenu = wx.Menu()    #defines files menu
        editMenu = wx.Menu()    #denies edit menu

        menuBar.Append(editMenu, 'Edit')
        menuBar.Append(fileMenu, '&File')
        self.SetMenuBar(menuBar)
        fitem = fileMenu.Append(wx.ID_EXIT, 'Quit...', 'Quit application') #adds a quit option to file menu 
        fitem1 = fileMenu.Append(wx.ID_EXIT, 'Select', 'Select Video')      #adds a select option to file menu
        
        self.Bind(wx.EVT_MENU, self.OnQuit, fitem)  #assigns OnQuit function to quit option
        self.Bind(wx.EVT_MENU, self.Select, fitem1) #assigns Select function to select option

    
        self.quote1 = wx.StaticText(self, label="Starting Time: ", pos=(20, 10))    #text label
        self.quote2 = wx.StaticText(self, label="Ending Time: ", pos=(20, 30))      #text label
        self.Show()
        clearButton = wx.Button(self, wx.ID_CLEAR, "Clear", pos=(20, 50))           #makes a button
        selectButton = wx.Button(self, wx.ID_EXIT, "Select video", pos=(20, 80))

        self.Show(True)
         
    #creates quit option in file menu
    def OnQuit(self, e):
        self.Close()
    #creates select option in file menu
    def Select(self, e):
        self.Select()

def main():
    ex = wx.App()
    Display(None)
    ex.MainLoop()


main()

 

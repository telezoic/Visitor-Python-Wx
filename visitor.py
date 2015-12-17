#utf-8
#tested in python 2.7.10 - Daniel Sifton
import os
import wx
import csv
import time
from webdriverplus import WebDriver
from itertools import *


#----------------------------
#we reassign these global variables inside the button functions. To pass to the worker script 
loopset = 0 
delayset = 0
csvopengui = 0
#----------------------------
#path to the worker script
visitorpath = os.path.join(os.getcwd(), 'worker.py')
#----------------------------
#path to the img file
imgpath = os.path.join(os.getcwd(), 'img', 'lizardface.jpg')
#----------------------------
#we only want to see .csv files in the FileDialog
wildcard = "(*.csv)|*.csv|"
#----------------------------


########################################################################
class MyForm(wx.Frame):
 
    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 
                          "Visitor Mark One", size=(450, 245), style=wx.MINIMIZE_BOX | wx.CAPTION |  wx.CLOSE_BOX) 
                           #size controls for frame [and the image] 
        panel = wx.Panel(self, wx.ID_ANY,)
        
        openMessageDlgBtn = wx.Button(panel, label="Loop Type")
        openMessageDlgBtn.Bind(wx.EVT_BUTTON, self.onMessageDlg)

        openFileDlgBtnV = wx.Button(panel, label=".csv input") 
        openFileDlgBtnV.Bind(wx.EVT_BUTTON, self.onOpenFileV)

        TextEntryDlgBtn = wx.Button(panel, label="Delay")
        TextEntryDlgBtn.Bind(wx.EVT_BUTTON, self.onTextEntryDlg)

        startButton = wx.Button(panel, label="Start")
        self.Bind(wx.EVT_BUTTON, self.startButton)

        closeBtn = wx.Button(panel, label="Stop")
        closeBtn.Bind(wx.EVT_BUTTON, self.onClose)
      
      
        sizer = wx.BoxSizer(wx.VERTICAL) 

        sizer.Add(openFileDlgBtnV, 2, wx.ALL|wx.LEFT, 3)
        sizer.Add(openMessageDlgBtn, 2, wx.ALL|wx.LEFT, 3)
        sizer.Add(TextEntryDlgBtn, 2, wx.ALL|wx.LEFT, 3)
        sizer.Add(startButton, 2, wx.ALL|wx.LEFT, 3)
        sizer.Add(closeBtn, 2, wx.ALL|wx.LEFT, 3)
    
        panel.SetSizer(sizer)
        self.CreateStatusBar()
        panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)


    #----------------------------------------------------------------------
    def onMessageDlg(self, event): 
       
       # Create and show the onMessageDlg
        dlg = wx.MessageDialog(
            self, message="Do you want an infinite loop?",
            style= wx.CANCEL | wx.YES_NO) 

        if dlg.ShowModal() == wx.ID_YES:
            self.SetStatusText("Infinite Loop: Yes" )
            global loopset
            loopset == True
            return loopset   

        else:
            self.SetStatusText("Infinite Loop: No")
           
            loopset == False
            return loopset

           
        dlg.Destroy()

 


    #----------------------------------------------------------------------

    def onOpenFileV(self, event): 
       
        # Create and show the Open FileDialog
        
        dlg = wx.FileDialog(
            self, message="Choose a .csv file of URLs",
            defaultDir=os.getcwd(), 
            wildcard="*.csv",
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            for path in paths:
                self.SetStatusText(path)
                global csvopengui
                csvopengui = path
                return csvopengui
              
        dlg.Destroy() 


    #----------------------------------------------------------------------
    def onTextEntryDlg(self, event):
        
     # Create and show TextEntryDialog
    
        
        dlg = wx.TextEntryDialog(
            self, message="Set delay for each URL in seconds", )
        if dlg.ShowModal() == wx.ID_OK:
            delayresult = dlg.GetValue()
            self.SetStatusText(delayresult + " " "seconds")
            global delayset
            delayset = delayresult
            return delayset

        
        dlg.Destroy()
 
#----------------------------------------------------------------------
    def startButton(self, event): 
     
        # Set up the script . . . and press go!
    
        urls = csv.reader(open(csvopengui, "rU")) 
        delayfinal = int(delayset)
        num_lines = len(open(csvopengui).read().splitlines())
        count = 1 
        start_time = time.time()
    
    
        execfile(visitorpath) # exec(open("./filename").read()) [mod for python 3]
#-----------------------------------------------------------------------
    # shut it down

    def onClose(self, event):
        """"""
        self.Close()   

#-----------------------------------------------------------------------

    def OnEraseBackground(self, evt):
       
       # Add a picture to the background
       
        # yanked from ColourDB.py
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap(imgpath)
                                      
        dc.DrawBitmap(bmp, 0, 0)

#------------------------------------------------------------------------

# Run it [Wx]
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()

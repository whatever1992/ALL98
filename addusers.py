import wx

class AddUserFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Add User', size=(300, 150))

        self.panel = wx.Panel(self)

        self.namelabel = wx.StaticText(self.panel, -1, "name:", (70, 20))
        self.nametext = wx.TextCtrl(self.panel, -1, style=wx.TE_LEFT, pos=(140, 20))  

        self.passlabel = wx.StaticText(self.panel, -1, "password:",(70, 50))
        self.passtext = wx.TextCtrl(self.panel, 1, style=wx.TE_PASSWORD, pos=(140, 50))  

        self.addbutton = wx.Button(self.panel, label = "add", pos = (80, 100), size = (50, 30))
        self.canbutton = wx.Button(self.panel, label = "cancel", pos = (170, 100), size = (50, 30))
        self.Bind(wx.EVT_BUTTON, self.Confirm, self.addbutton)
        self.Bind(wx.EVT_BUTTON, self.Cancel, self.canbutton)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def Confirm(self,  event):
        name = self.nametext.GetValue()
        password = self.passtext.GetValue()
        
        if name == "":
            noname = wx.MessageDialog(None, "No name", "Warning", wx.YES_NO | wx.ICON_QUESTION)
            retCode = noname.ShowModal()
            noname.Destroy()
        elif password == "":
            nopassword = wx.MessageDialog(None, "No password", "Warning", wx.YES_NO | wx.ICON_QUESTION)
            retCode = nopassword.ShowModal()
            nopassword.Destroy()
        else:
            # print name
            parent.sampleList.append(name.decode('utf-8'))
            parent.accout[name] = password

            file = open("./accout","w+")
            file.write(name + " " + password)
            file.close()

            parent.listBox.Append(name)
            self.Close(True)

    def Cancel(self, event):
        self.Close(True)
    def OnCloseWindow(self, event):
        self.Destroy()
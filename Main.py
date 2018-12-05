import wx


class Example(wx.Frame):
    def __init__(self, parent):
        super(Example, self).__init__(parent, title='Window', size=(300, 100))

        panel = wx.Panel(self)
        LblTextWithBgColor = wx.StaticText(panel, label='This text should have a red background', size=(250, 20), style=wx.ALIGN_CENTER)
        LblTextWithBgColor.SetForegroundColour('Green')
        LblTextWithBgColor.SetBackgroundColour('Red')
        self.Show()


app = wx.App()
Example(None)
app.MainLoop()
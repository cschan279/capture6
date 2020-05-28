#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Button, Frame, Label
from tkinter.simpledialog import askstring
from UI.App import App
from UI.Buttons import RButton
from UI.Display import Display
from UI.Logo import Logo
from UI.Clock import Clock
from UI.Bar import BarS
from utils.Cam import Cam



class TkApp(App):
    def setup(self):
        self.cam = Cam(0)
        return
    
    def layout(self):
        w, h = int(self.scale*16), int(self.scale*9)
        for i in range(9):
            mod_name = 'C{:02d}'.format(i)
            r, c = i//3, i%3
            self.mod[mod_name] = Display(self, width=w, height=h)
            self.mod[mod_name].grid(row=r, column=c)
        return
    
    def update(self):
        print('update')
        return
            
    def onDestroy(self):
        self.cam.release()
        return
    
if __name__ == "__main__":
    x = TkApp(title="User Interface", scale=20, delay=100, fullscreen=False)
    x.mainloop()

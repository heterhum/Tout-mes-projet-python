import win32gui
import win32con
import time
import asyncio
import keyboard 
import threading

class Pong:
    def __init__(self):
        self.dicte={}
        self.wndclass=win32gui.WNDCLASS()
        self.x=0
        self.y=0
        self.run=True
        self.Name=[]
        self.hinst=None

    def wndproc(self,hwnd, msg, wparam, lparam):
        
        if msg == win32con.WM_DESTROY:
            win32gui.PostQuitMessage(0)
            self.run=False
            return 0
        else:
            return win32gui.DefWindowProc(hwnd, msg, wparam, lparam)
        
    def createWindowClass(self):
        
        self.wndclass.lpfnWndProc = self.wndproc
        self.wndclass.lpszClassName = "MaFenetrePython"
        self.hinst = win32gui.GetModuleHandle(None)
        win32gui.RegisterClass(self.wndclass)

    def NewWindow(self,name):
        self.Name.append(name)
        hwnd = win32gui.CreateWindow(
            self.wndclass.lpszClassName,   
            name,        
            win32con.WS_OVERLAPPEDWINDOW,  
            100, 100, 400, 300,       
            0, 0, self.hinst, None)
        self.dicte[name]=hwnd

    def e(self):
        while self.run:
            if keyboard.is_pressed('q'):  
                self.x+=10
                self.update("block",self.x,self.y)
            time.sleep(0.1)

    def main(self):
        threaaad= threading.Thread(target=self.e)
        threaaad.start()
        self.createWindowClass()
        self.NewWindow("block")
        self.NewWindow("test")
        for i in self.Name:
            win32gui.ShowWindow(self.dicte[i], win32con.SW_SHOWNORMAL)
            win32gui.UpdateWindow(self.dicte[i])
        win32gui.PumpMessages()

    def update(self,name,x,y):
        win32gui.SetWindowPos(self.dicte[name],0,x,y,400,300,0)


pong=Pong()
pong.main()


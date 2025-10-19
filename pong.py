import win32gui
import win32con
import win32api
import time
import asyncio
import keyboard 
import threading
import numpy as np
import random
import pygetwindow

FPS = 50
PIXELTOMETER = 10 #10 pixel -> 1m
#to use this, launch three window with pygame name Ping1 / 2 / 3 that play pong on it
#be sure to put the right height and width and uncomment the needed part in this shit-ish code
#W1=pygetwindow.getWindowsWithTitle('Pong1')[0]._hWnd
#W2=pygetwindow.getWindowsWithTitle('Pong2')[0]._hWnd
#W3=pygetwindow.getWindowsWithTitle('Pong3')[0]._hWnd

def Vcalc(v,vector,x,y): #calcule nouvelle position
    distance=v*(1/FPS)
    Pdistance=(distance*PIXELTOMETER)
    Vx=Pdistance*vector[0]
    Vy=Pdistance*vector[1]
    x+=Vx
    y-=Vy
    return int(x),int(y)

def GetInfo():
    width=win32api.GetSystemMetrics(0)
    height=win32api.GetSystemMetrics(1)
    return width,height

def Norme(vect):
    return np.sqrt(vect[0]**2+vect[1]**2)

def Vnormale(vect,norme):
    if norme!=0:
        return (vect[0]/norme,vect[1]/norme)
    return (0,0)

def Collimur(Vnorm,Vimpact): #obj1 colisionneur, obj2 mur
    u=random.uniform(-0.3, 0.3)
    u=round(u,2)
    Vnorm=Vnormale((Vnorm[0],Vnorm[1]+u),Norme((Vnorm[0],Vnorm[1]+u)))
    

    dot=np.dot(Vimpact,Vnorm)*2
    tosou=(dot*Vnorm[0],dot*Vnorm[1])
    NewV=(Vimpact[0]-tosou[0],Vimpact[1]-tosou[1]) #vecteur directeur aprés boing
    norme=Norme(NewV)
    NewV=Vnormale(NewV,norme)

    return NewV

class Window:
    def __init__(self,wall,autowall,balle,pong):
        self.dicte={}
        self.wndclass=win32gui.WNDCLASS()
        self.run=True
        self.Name=[]
        self.hinst=None
        self.wall=wall
        self.autowall=autowall
        self.ball=balle
        self.pong=pong

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

    def NewWindow(self,name,width,height):
        self.Name.append(name)
        hwnd = win32gui.CreateWindow(
            self.wndclass.lpszClassName,   
            name,        
            win32con.WS_OVERLAPPEDWINDOW,  
            100, 100, width, height,       
            0, 0, self.hinst, None)
        self.dicte[name]=hwnd

    def e(self):
        while self.run:
            if keyboard.is_pressed('s'):  
                self.wall.y+=100
            if keyboard.is_pressed('z'):  
                self.wall.y-=100
            if keyboard.is_pressed('a'):
                pong.end()
                self.run=False
            time.sleep(0.1)

    def main(self):
        threaaad= threading.Thread(target=self.e)
        threaaad.start()
        self.createWindowClass()
        self.NewWindow("block",self.ball.width,self.ball.height)
        self.NewWindow("Lwall",self.autowall.width,self.autowall.height)
        self.NewWindow("Rwall",self.wall.width,self.wall.height)
        for i in self.Name:
            win32gui.ShowWindow(self.dicte[i], win32con.SW_SHOWNORMAL)
            win32gui.UpdateWindow(self.dicte[i])
        

    def update(self,name,x,y,width,height):
        win32gui.MoveWindow(self.dicte[name],x,y,width,height,0)
    #def update(self,name,x,y,width,height):
    #    win32gui.SetWindowPos(name,0, x, y, width, height, True)

class Balle():
    def __init__(self,r):
        self.Wwidth,self.Wheight= GetInfo()
        self.width = self.height = r
        self._x=self.Wwidth/2
        self._y=self.Wheight/2
        self.Vdirector=(1,1)
        self.Velocity=100
        self.winpos=[int(self.x-self.width/2),int(self.y-self.height/2)]
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @x.setter
    def x(self,x):
        self._x=x
        self.winpos[0]=int(self.x-self.width/2)
        return
    @y.setter
    def y(self,y):
        self._y=y
        self.winpos[1]=int(self.y-self.height/2)
        return

class Mur(): #1/8
    def __init__(self,x,y):
        self.Wwidth,self.Wheight= GetInfo()
        self.width = int(1/12 * self.Wwidth)
        self.height = int(1/3 * self.Wheight)
        self._x=x
        self._y=y
        self.Vdirector=(1,0)
        self.Velocity=10
        self.winpos=[int(self.x-self.width/2),int(self.y-self.height/2)]
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @x.setter
    def x(self,x):
        self._x=x
        self.winpos[0]=int(self.x-self.width/2)
        return
    @y.setter
    def y(self,y):
        self._y=y
        self.winpos[1]=int(self.y-self.height/2)
        return

class Pong():
    def __init__(self):
        self.Wwidth,self.Wheight= GetInfo()
        self.run=True
        self.autowall=Mur(0,int(self.Wheight/2))
        self.autowall.x=int(self.autowall.width/2)
        self.wall=Mur(0,int(self.Wheight/2))
        self.wall.x=int(self.Wwidth-self.wall.width/2)
        self.ball=Balle(200)
        self.window=Window(self.wall,self.autowall,self.ball,self)

    def end(self):
        self.run=False
        print("fin")
        return

    def check(self):
        i=self.ball
        if 0>=i.x-i.width/2:
            self.end()
        if i.x+i.width/2>=self.Wwidth:
            self.end()
        if 0>=i.y-i.height/2:
            i.Vdirector=Collimur((0,-1),i.Vdirector)
            i.y=i.y+-1*(i.y-i.height/2)
        if i.y+i.height/2>=self.Wheight:
            i.Vdirector=Collimur((0,1),i.Vdirector)
            i.y=i.y-(i.y+i.height/2 - self.Wheight)
        
        wall=self.wall
        x,y=i.x,i.y
        Bwidth,Bheight=i.width/2,i.width/2
        Wx,Wy=wall.x,wall.y
        Wwidth,Wheight=wall.width/2,wall.height/2
        if x+Bwidth>=Wx-Wwidth and (Wy-Wheight <= y-Bheight <=Wy+Wheight or Wy-Wheight <= y+Bheight <=Wy+Wheight):
            Vecteur=Collimur((-1,0),i.Vdirector)
            i.Vdirector=Vecteur
            #i.x=i.x-(Wx-Wwidth-x+Bwidth)#-1

        wall=self.autowall
        x,y=i.x,i.y
        Bwidth,Bheight=i.width/2,i.width/2
        Wx,Wy=wall.x,wall.y
        Wwidth,Wheight=wall.width/2,wall.height/2
        if x-Bwidth<=Wx+Wwidth and (Wy-Wheight <= y-Bheight <=Wy+Wheight or Wy-Wheight <= y+Bheight <=Wy+Wheight):
            Vecteur=Collimur((1,0),i.Vdirector)
            i.Vdirector=Vecteur
            #i.x=i.x+(Wx-Wwidth+x+Bwidth)#+1
        return
    
    def go(self):
        self.window.main()
        
        threading.Thread(target=win32gui.PumpMessages, daemon=True).start()
        
        while self.run:
            self.check()
            xy=Vcalc(self.ball.Velocity,self.ball.Vdirector,self.ball.x,self.ball.y)
            self.ball.x,self.ball.y=xy
            self.autowall.y=self.ball.y
        #    self.window.update(W1,self.ball.winpos[0],self.ball.winpos[1],self.ball.width,self.ball.height)
        #    self.window.update(W2,self.autowall.winpos[0],self.autowall.winpos[1],self.autowall.width,self.autowall.height)
        #    self.window.update(W3,self.wall.winpos[0],self.wall.winpos[1],self.wall.width,self.wall.height)
            self.window.update("block",self.ball.winpos[0],self.ball.winpos[1],self.ball.width,self.ball.height)
            self.window.update("Lwall",self.autowall.winpos[0],self.autowall.winpos[1],self.autowall.width,self.autowall.height)
            self.window.update("Rwall",self.wall.winpos[0],self.wall.winpos[1],self.wall.width,self.wall.height)
            time.sleep(1/FPS)
            

try:
    pong=Pong()
    pong.go()
except Exception as e:
    print(e)
    pong.window.run=False



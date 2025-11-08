import win32gui
import win32con
import win32api
import time
import threading

class Window:
    def __init__(self):
        self.dicte={}
        self.wndclass=win32gui.WNDCLASS()
        self.run=True
        self.Name=[]
        self.hinst=None

    def getInfo(self,name):
        rect = win32gui.GetWindowRect(self.dicte[name])
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y
        return (x,y,w,h)

    def wndproc(self,hwnd, msg, wparam, lparam):
        if msg == win32con.WM_DESTROY:
            win32gui.PostQuitMessage(0)
            
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
            200, 200, width, height,       
            0, 0, self.hinst, None)
        self.dicte[name]=hwnd
        return hwnd

    def loop(self,name):
        
        while msg:=win32gui.GetMessage(self.dicte[name],0,0) :
            win32gui.TranslateMessage(msg)
            win32gui.DispatchMessage(msg)

    def main(self):
        #self.createWindowClass()
        for i in self.Name:
            win32gui.ShowWindow(self.dicte[i], win32con.SW_SHOWNORMAL)
            win32gui.UpdateWindow(self.dicte[i])
        

    def updatePlace(self,name,x,y,width,height):
        hwnd=self.dicte[name]
        win32gui.MoveWindow(hwnd,x,y,width,height,0)

    def StartPixelUpdate(self,name):
        hwnd=self.dicte[name]
        hdc=win32gui.GetDC(hwnd)
        return hwnd,hdc

    def updatePixel(self,name,hdc,hwnd,x,y,color):
        r,g,b=color[0],color[1],color[2]
        win32gui.SetPixel(hdc,x,y,win32api.RGB(r,g,b))

    def StopPixelUpdate(self,name,hdc,hwnd):
        win32gui.ReleaseDC(hwnd,hdc)



from PIL import Image, ImageWin

im = Image.open(r"C:/Users/xoxar/Desktop/perso/img/todraw.png") 
newsize = (1920,1080)
new_img = Image.new("RGB", (newsize[0], newsize[1]), (0, 0, 0))
#im.thumbnail(newsize,Image.LANCZOS)
#im=im.resize(newsize,Image.Resampling.LANCZOS) #Resampling.NEAREST, Resampling.BOX, Resampling.BILINEAR, Resampling.HAMMING, Resampling.BICUBIC or Resampling.LANCZOS
new_img.paste(im, (1920//2 - im.size[0]//2, 1080//2 - im.size[1]//2))
#width, height = im1.size 
#left = 6
#top = 400
#right = 500
#bottom = 600
#im1 = im.crop((left, top, right, bottom))
dib = ImageWin.Dib(new_img)



window=Window()
window.createWindowClass()
window.NewWindow("test",1920,1080)
window.main()
hwnd,hdc=window.StartPixelUpdate("test")
#dib.draw(hwnd, (400,400,700,700))
dib.expose(hdc)
#threading.Thread(target=win32gui.PumpMessages, daemon=True).start()
def refresh():
    dib.expose(hdc)
    win32gui.PostMessage(hwnd, win32con.WM_PAINT, 0, 0)
    threading.Timer(1/60, refresh).start()
refresh()
window.loop("test")

#while True:
#    dib.expose(hdc)
#    time.sleep(1/60)

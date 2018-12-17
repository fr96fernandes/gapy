import subprocess
from Tkinter import *
import tkMessageBox
import time
def install(w4):
    proc = subprocess.Popen('apt-get install -y libc6:i386', shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
    proc.wait()
    print('done')
    proc = subprocess.Popen('apt-get install -y libbz2-1.0:i386', shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
    proc.wait()
    print('done')
    proc = subprocess.Popen('apt-get install -y patch make cmake g++ pkg-config libx11-dev libxext-dev libxtst-dev libfreetype6-dev libgl1-mesa-dev libglu1-mesa-dev libpulse-dev libasound2-dev lib32z1', shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
    proc.wait()
    print('done')
    proc = subprocess.Popen('dpkg --add-architecture i386', shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
    proc.wait()
    print('done')
    proc = subprocess.Popen('apt-get update', shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
    proc.wait()
    print('done')
    proc = subprocess.Popen('apt-get install -y ia32-libs', shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
    proc.wait()
    print('all install done')
    w4.configure(text='Dependencies Installed')

def installing(top,btn,w4):
    w4.configure(text='Installing Dependencies')
    btn.configure(state=DISABLED)
    Tk.update(top)
    install(w4)   

def startServer(game):
    print(game.get())
    if game.get()==1:
        proc1 = subprocess.Popen('../games/assaultcube/assaultcube.sh', shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
        while True:
            proc2 = subprocess.Popen('sudo ./ga-server-periodic config/server.desktop.conf', shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
            proc2.wait()
    elif game.get()==2:
        #this one was not working, possibly to install and start a new game
        print('2')
    elif game.get()==3:
        proc1 = subprocess.Popen('../games/sauerbraten/bin_unix/linux_64_client', shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
        while True:
            proc2 = subprocess.Popen('sudo ./ga-server-periodic config/server.desktop.conf', shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
            proc2.wait()
    else:
        print('No Selected')
        tkMessageBox.showinfo(title='Error',message='Game was not selected.')
        

def interface():
    top = Tk()
    w = Label(top, text='Welcome to APT \n You can start your GamingAnywhere Cloud Gaming Server in the buttons bellow.')
    w.pack()
    w4 = Label(top,text='')
    btn = Button(top, text='Install dependencies', command= lambda: installing(top,btn,w4))
    btn.pack(anchor = E)
    w2 = Label (top, text='\n\n\n Please select the game you want to start.')
    w2.pack()
    var = IntVar()
    R1 = Radiobutton(top, text="AssaultCube", variable=var, value=1)
    R1.pack( anchor = W )
    R2 = Radiobutton(top, text="Openttd", variable=var, value=2)
    R2.pack( anchor = W )
    R3 = Radiobutton(top, text="Sauerbraten", variable=var, value=3)
    R3.pack( anchor = W)
    btn2 = Button(top, text='Start Server',command= lambda: startServer(var))
    btn2.pack()
    w3 = Label(top,text='\nStatus:')
    w3.pack(anchor = E)
    w4.pack(anchor = E)
    top.mainloop()

if __name__ == "__main__":
    interface()
    
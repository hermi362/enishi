# tutorial source:  https://realpython.com/python-gui-tkinter/
# Widget classes: Label  Button  Entry  Text  Frame

import tkinter as tk
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk
import os
import os.path
import sys

# global variables
resizeX = 1280
resizeY = 960
resizePath = str()

def log(msg):
    txtLog.insert(tk.END, msg)
    txtLog.see(tk.END)

def visitDir(path):
    # list all files and dirs in path
    for f in os.listdir(path):
        pf = os.path.join(path, f)
        if os.path.isdir(pf):
            log("➡ フォルダー処理中： %s\n" % pf)
            visitDir(pf)
        else:
            if f.lower().endswith('.jpg') or f.lower().endswith('.jpeg'):
                shrinkJPEG(pf)

def shrinkJPEG(f_img):
    log("   解像度変更中： %s ...\n" % f_img)

    window.update_idletasks()

    img = Image.open(fp=f_img, formats=['JPEG'])
    if img.width <= resizeX:
        log("** %d ピクセルより小さい、スキップ。 \n" % (resizeX))
        return

    exif = b''  # init with an empty bytearray
    if 'exif' in img.info:
        exif = img.info['exif']   # get exif_data
    img = img.resize((resizeX,resizeY))

    stat_result = os.stat(f_img)  # get modification time
    mtime = stat_result.st_mtime

    img.save(f_img, exif=exif, optimize=True, quality=85)
    # NOTE: saving EXIF data like this means that the new reduced resolution is NOT in the EXIF data.
    
    img.close()  # close underlying jpg file if not already closed
    
    global boolKeepDate
    if boolKeepDate.get() == "1":
        os.utime(f_img, (mtime, mtime)) # preserve modification time (as time of shot)




window = tk.Tk()
window.title("写真ファイル解像度ダウン")

def open_dir():
    '''Launch Folder Open dialog box'''
    global resizePath
    resizePath = askdirectory(mustexist=True)
    if resizePath:
        txtLog.insert(tk.END,f'写真フォルダ： {resizePath}\n')
        txtLog.insert(tk.END,f'これで良ければ、「スタート」ボタンおクリック。\n\n')
        btnStart["state"] = "normal"
    else:
        btnStart["state"] = "disabled"



def start_compression():
    '''start the recursive file resizing process'''
    global resizeX
    global resizeY
    resizeX = int(entryX.get())
    resizeY = int(entryY.get())

    visitDir(resizePath)
    log("終了\n")
    
frmTitle = tk.Frame(relief=tk.RAISED, borderwidth=2, pady=20)
lblTitle1 = tk.Label(master=frmTitle, text="写真ファイル解像度ダウン")
lblTitle1.pack()
lblTitle2 = tk.Label(master=frmTitle, text="v0.9")
lblTitle2.pack()

# load Enishi logo
tkimgLogo = ImageTk.PhotoImage(Image.open("enishi_logo_gr.png"))
lblLogo = tk.Label(master=frmTitle, image=tkimgLogo)
lblLogo.pack()
frmTitle.grid(row=0, sticky="ew", padx=5, pady=5)

# frame for resolution options
frmSizes1 = tk.Frame()
frmSizes1.grid(row=3, padx=5)
tkimgBear1 = ImageTk.PhotoImage(Image.open("workbear-big.png"))
lblBear1 = tk.Label(master=frmSizes1, image=tkimgBear1)
lblBear1.grid(row=0, column=0)
tkimgArrow = ImageTk.PhotoImage(Image.open("arrow.png"))
lblArrow = tk.Label(master=frmSizes1, image=tkimgArrow)
lblArrow.grid(row=0, column=1)

frmSizes2 = tk.Frame(master=frmSizes1)
frmSizes2.grid(row=0, column=2)
strX = tk.StringVar()
strX.set(str(resizeX))
entryX = tk.Entry(master=frmSizes2, textvariable=strX, width=8)
entryX.pack()
tkimgBear2 = ImageTk.PhotoImage(Image.open("workbear-small.png"))
lblBear2 = tk.Label(master=frmSizes2, image=tkimgBear2)
lblBear2.pack()

boolKeepDate = tk.StringVar(value="1")  # whether or not to perserve the jpg file modification date
chkKeepDate = tk.Checkbutton(master=frmSizes2, text="写真ファイルの作成日付そのまま", 
    variable=boolKeepDate)
chkKeepDate.pack()

strY = tk.StringVar()
strY.set(str(resizeY))
entryY = tk.Entry(master=frmSizes1, textvariable=strY, width=8)
entryY.grid(row=0, column=3)

frmButtons = tk.Frame()
btnFolder = tk.Button(master=frmButtons, text="写真フォルダー選択…", width=25, command=open_dir)
btnFolder.grid(row=0, column=0, sticky="w")
btnStart = tk.Button(master=frmButtons, text="スタート", width=25, command=start_compression)
btnStart.grid(row=0, column=1, sticky="e")
btnStart["state"] = "disabled"
frmButtons.grid(row=4, sticky="", padx=5, pady=10)

frmLog = tk.Frame()
frmLog.grid(row=5, sticky="nsew", padx=5, pady=5)
txtLog = tk.Text(master=frmLog)
txtLog.pack(side="left", expand=True, fill="both")
scrollY = tk.Scrollbar(master=frmLog, orient="vertical", command=txtLog.yview)
scrollY.pack(side="right", expand=False, fill="y")
txtLog.configure(yscrollcommand=scrollY.set)
txtLog.insert(tk.END, "注意：対象写真ファイルは上書きされます。\n")
txtLog.insert(tk.END, "フォルダーを選択してください。\n")

window.columnconfigure(0, weight=1)
window.rowconfigure(5, weight=1)
window.mainloop()

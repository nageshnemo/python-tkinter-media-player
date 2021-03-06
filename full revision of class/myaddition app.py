#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.19
#  in conjunction with Tcl version 8.6
#    Jan 25, 2019 05:43:15 PM IST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import myaddition app_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    myaddition app_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    myaddition app_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 
        font10 = "-family {Segoe UI Black} -size 12 -weight bold "  \
            "-slant italic -underline 0 -overstrike 0"
        font9 = "-family {Yu Gothic UI Semibold} -size 18 -weight bold"  \
            " -slant roman -underline 1 -overstrike 0"

        top.geometry("600x354+378+103")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.017, rely=0.085, height=41, width=434)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''number addition program''')
        self.Label1.configure(width=434)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.067, rely=0.367, height=21, width=154)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''enter first no''')
        self.Label2.configure(width=154)

        self.txtfno = tk.Entry(top)
        self.txtfno.place(relx=0.317, rely=0.367,height=20, relwidth=0.273)
        self.txtfno.configure(background="white")
        self.txtfno.configure(disabledforeground="#a3a3a3")
        self.txtfno.configure(font="TkFixedFont")
        self.txtfno.configure(foreground="#000000")
        self.txtfno.configure(insertbackground="black")

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.1, rely=0.48, height=21, width=124)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font10)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''enter second no''')
        self.Label3.configure(width=124)

        self.txtsno = tk.Entry(top)
        self.txtsno.place(relx=0.333, rely=0.48,height=20, relwidth=0.273)
        self.txtsno.configure(background="white")
        self.txtsno.configure(disabledforeground="#a3a3a3")
        self.txtsno.configure(font="TkFixedFont")
        self.txtsno.configure(foreground="#000000")
        self.txtsno.configure(insertbackground="black")

        self.lblresult = tk.Label(top)
        self.lblresult.place(relx=0.117, rely=0.621, height=31, width=324)
        self.lblresult.configure(background="#d9d9d9")
        self.lblresult.configure(disabledforeground="#a3a3a3")
        self.lblresult.configure(foreground="#000000")
        self.lblresult.configure(width=324)

        self.Btnadd = tk.Button(top)
        self.Btnadd.place(relx=0.017, rely=0.706, height=54, width=137)
        self.Btnadd.configure(activebackground="#ececec")
        self.Btnadd.configure(activeforeground="#000000")
        self.Btnadd.configure(background="#d9d9d9")
        self.Btnadd.configure(disabledforeground="#a3a3a3")
        self.Btnadd.configure(foreground="#000000")
        self.Btnadd.configure(highlightbackground="#d9d9d9")
        self.Btnadd.configure(highlightcolor="black")
        self.Btnadd.configure(pady="0")
        self.Btnadd.configure(text='''add''')
        self.Btnadd.configure(width=137)

        self.Btnclear = tk.Button(top)
        self.Btnclear.place(relx=0.317, rely=0.706, height=54, width=167)
        self.Btnclear.configure(activebackground="#ececec")
        self.Btnclear.configure(activeforeground="#000000")
        self.Btnclear.configure(background="#d9d9d9")
        self.Btnclear.configure(disabledforeground="#a3a3a3")
        self.Btnclear.configure(foreground="#000000")
        self.Btnclear.configure(highlightbackground="#d9d9d9")
        self.Btnclear.configure(highlightcolor="black")
        self.Btnclear.configure(pady="0")
        self.Btnclear.configure(text='''clear''')
        self.Btnclear.configure(width=167)

        self.Btnquit = tk.Button(top)
        self.Btnquit.place(relx=0.633, rely=0.706, height=44, width=147)
        self.Btnquit.configure(activebackground="#ececec")
        self.Btnquit.configure(activeforeground="#000000")
        self.Btnquit.configure(background="#d9d9d9")
        self.Btnquit.configure(disabledforeground="#a3a3a3")
        self.Btnquit.configure(foreground="#000000")
        self.Btnquit.configure(highlightbackground="#d9d9d9")
        self.Btnquit.configure(highlightcolor="black")
        self.Btnquit.configure(pady="0")
        self.Btnquit.configure(text='''Quit''')
        self.Btnquit.configure(width=147)

if __name__ == '__main__':
    vp_start_gui()






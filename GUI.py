#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 15:09:33 2018

@author: saher
"""

import Tkinter as tk
from imageClass import *
class MyFirstGUI:
    def __init__(self, master):
        self.tmp = imageClass()
        self.master = master
        master.minsize(width=666, height=300)
        master.title("A simple GUI")

        #self.label = tk.Label(master, text="This is our first GUI!")
        #self.label.grid(row=0, column=100)

        #self.master.grid_columnconfigure(0, weight=1)

        

        self.searchButton = tk.Button(master, text="browse", command= lambda: self.tmp.openFile())
        self.searchButton.grid(row=3, column=1)
        
        self.saveButton = tk.Button(master, text="Save Image", command= lambda: self.tmp.saveImage())
        self.saveButton.grid(row=4, column=1)
        
        v = tk.IntVar()

        #self.r1 = tk.Radiobutton(master, text="One", variable=v, value=1)#.pack(anchor=W)
        #self.r2 = tk.Radiobutton(master, text="Two", variable=v, value=2)#.pack(anchor=W)
        
        self.r1=tk.Radiobutton(master,text="Salt And Pepper",variable=v,value=1, command= lambda: callFunandShowlist1())
        self.r2=tk.Radiobutton(master,text="Gaussian",variable=v,value=2, command= lambda: callFunandShowlist2())
        self.r3=tk.Radiobutton(master,text="Avg Filter",variable=v,value=3, command= lambda: callFunandShowlist3())
        self.r4=tk.Radiobutton(master,text="Gaussian Filter",variable=v,value=4, command= lambda: callFunandShowlist4())
        
        self.r1.grid(row=2, column=0)
        self.r2.grid(row=3, column=0)
        self.r3.grid(row=4, column=0)
        self.r4.grid(row=5, column=0)
        
        self.mylistbox = tk.Listbox()
        self.mylistbox.insert(tk.END, "original")
        
        
        self.callHistory = tk.Button(master, text="call history", command= lambda: callHistory())
        
        
        
        def callFunandShowlist1():
            showList("Salt And Pepper")
            self.tmp.addSaltAndPepper()
        
        def callFunandShowlist2():
            showList("Gaussian")
            self.tmp.addGaussian()
        
        def callFunandShowlist3():
            showList("Avg Filter")
            self.tmp.avgFilter()
    
        def callFunandShowlist4():
            showList("Gaussian Filter")
            self.tmp.gaussianFilter()
            
            
        def showList(s):
            self.mylistbox.insert(tk.END, s)
            self.mylistbox.grid(row=0, column=1)
            self.callHistory.grid(row=0, column=2)
            
            
        def callHistory():
            index = self.mylistbox.curselection()[0]
            self.tmp.callHistory(index)
            
        

        
        


        


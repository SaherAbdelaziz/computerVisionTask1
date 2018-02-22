#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 15:20:23 2018

@author: saher
"""

import os
import Tkinter as tk
import tkFileDialog
from PIL import Image, ImageTk
import cv2
import numpy as np
from matplotlib import pyplot as plt
import GUI
class imageClass:
    
    def __init__(self):
        self.inputImage = None
        self.OutputImage = None
        self.panelA = None
        self.panelB = None
        
        self.allImages=[]
        self.allOperationsText = []
        self.countOperations = 0
    
    def addSaltAndPepper(self):
        
        if self.inputImage is None:
            return
        
        self.countOperations+=1
        rnd = np.random.rand(self.inputImage.shape[0], self.inputImage.shape[1])

        print rnd.shape
        noisy = self.inputImage.copy()
        ## for prob = 0.3
        ## >> rnd < 0.3 will be set to 0
        ## >> rnd > 0.7 will be set to 1
        ## >> rnd in between will keep its original values
        noisy[rnd < .1] = 0
        noisy[rnd > 1 - .1] = 255
        self.OutputImage = noisy
        self.allOperationsText.append("Salt And Pepper")
        self.showOutput()
        return noisy
    
    def addGaussian(self):
        if self.inputImage is None:
            return
        self.countOperations+=1
        gauss_nois = np.zeros(self.inputImage.shape, dtype=np.uint8)
        m = (500,500,500)
        s = (500,500,500)
        cv2.randn(gauss_nois,m,s)
        noised_img = self.inputImage + gauss_nois
        self.OutputImage = noised_img
        self.allOperationsText.append("Gaussian")
        self.showOutput()
        
        return noised_img
    
    def avgFilter(self):
        if self.inputImage is None:
            return
        self.countOperations+=1
        blur = cv2.blur(self.inputImage, (5, 5))
        self.OutputImage = blur
        self.allOperationsText.append("Avg Filter")
        self.showOutput()
        
        return blur
    
    def gaussianFilter(self):
        if self.inputImage is None:
            return
        self.countOperations+=1
        gblur = cv2.GaussianBlur(self.inputImage,(5,5),0)
        self.OutputImage = gblur
        self.allOperationsText.append("Gaussian Filter")
        self.showOutput()
        
        return gblur
        

    def openFile(self):
        
	path = tkFileDialog.askopenfilename()
	if len(path) > 0:
	    self.inputImage = cv2.imread(path)
        self.OutputImage = cv2.imread(path)
        
        self.inputImage = cv2.cvtColor(self.inputImage, cv2.COLOR_BGR2RGB)
        self.OutputImage = cv2.cvtColor(self.inputImage, cv2.COLOR_BGR2RGB)
 
        self.allImages.append(self.inputImage) 
        panelAImage = Image.fromarray(self.inputImage)
        panelAImage = ImageTk.PhotoImage(panelAImage)
                
        
        if self.panelA is None :
            self.panelA = tk.Label(image=panelAImage)
            self.panelA.image = panelAImage
            self.panelA.grid(row = 0 , column=0)
        else:
			self.panelA.configure(image=panelAImage)
			self.panelA.image = self.panelAImage
			
            
    def showOutput(self):
        
        self.allImages.append(self.OutputImage) 
        
        self.inputImage = self.OutputImage
        panelAImage = Image.fromarray(self.OutputImage)
        panelAImage = ImageTk.PhotoImage(panelAImage)
        
        if self.panelA is None:
            self.panelA = tk.Label(image=panelAImage)
            self.panelA.image = panelAImage
            self.panelA.grid(row = 0 , column=0)
        else:
            self.panelA.configure(image=panelAImage)
            self.panelA.image = panelAImage
    
    def callHistory(self , index):
        print "indexxxxxxxxxxx" , index
        self.inputImage = self.allImages[index]
        panelAImage = Image.fromarray(self.inputImage)
        panelAImage = ImageTk.PhotoImage(panelAImage)
        
        if self.panelA is None:
            self.panelA = tk.Label(image=panelAImage)
            self.panelA.image = panelAImage
            self.panelA.grid(row = 0 , column=0)
        else:
            self.panelA.configure(image=panelAImage)
            self.panelA.image = panelAImage
        
    def saveImage(self):
        self.OutputImage = cv2.cvtColor(self.OutputImage, cv2.COLOR_RGB2BGR)
        f = tkFileDialog.asksaveasfilename()
        if f is None: 
            return
        #text2save = str(text.get(1.0, END)) # starts from `1.0`, not `0.0`
        #f.write(text2save)
        #f.close() # `()` was missing.
        #tkFileDialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        print f
        cv2.imwrite(str(f)+".jpg" , self.OutputImage)    
    

        
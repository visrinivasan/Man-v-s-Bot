#!/usr/bin/env python
tesseract_cmd = 'tesseract'

try:
    import Image
except ImportError:import numpy as np
import os
import cv2
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
from Tkinter import Tk, Label, Frame, Canvas, Button, ALL
import itertools

#set number of rows and columns
ROWS = 15
COLS = 15

class TTT:
    '''
        main class
    '''
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack(fill="both", expand=True)
        self.label = Label(self.frame, text='SCRABBLE Game', height=2, font="Arial 14", bg='black', fg='blue')
        self.label.pack(fill="both", expand=True)
        self.canvas = Canvas(self.frame, width=300, height=300)
        self.canvas.pack(fill="both", expand=True)
        self.status = Label(self.frame, text='Start Game', height=2, font="Arial 14", bg='white', fg='black')
        self.status.pack(fill="both", expand=True)
        self.restart = Button(self.frame, text="Restart", command=self.restart)
        self.restart.pack(fill="both", expand=True)
        self.next = Button(self.frame, text="Next Move", command=self.next)
        self.next.pack(fill="both", expand=True)
        self.__board()
        self.board = [0 for x in range(0,ROWS*COLS)]
        self.winner = None
        self.lastmoves = []
		
        # Read Image
     	#vc = cv2.VideoCapture(0)
 
	    #if vc.isOpened(): # try to get the first frame
	     #rval, self.img = vc.read()
        #else:
	     #rval = False
        self.img = cv2.imread('scrabble3.jpg')
        self.img = cv2.resize(self.img, (300, 300)) 
		
        count = 0
        for j in range(0,300,(300/ROWS)):
            for i in range(0,300,(300/COLS)):
                self.crop_img = self.img[j+1:j+(300/ROWS)-1, i+1:i+(300/COLS)-1]
                cv2.imwrite('image/test.png',self.crop_img)
                img = Image.open('image/test.png')
                str2 = pytesseract.image_to_string(img,config='-psm 10000')
                str1 = ''.join([k for k in str2 if not k.isdigit()])
                str = ''.join(e for e in str1 if e.isalnum())
		if not str:
		   str = ' '
                #print(str)
                self.canvas.create_text(i+10, j+10, font="Purisa",text=str)
                self.board[count] = str
                #cv2.namedWindow('dst_rt', cv2.WINDOW_NORMAL)
                #cv2.resizeWindow('dst_rt', 300, 300)
                #cv2.imshow('dst_rt', self.crop_img)
                #cv2.waitKey(0)		
                count = count+1

	board = np.reshape(self.board, (-1, 15))
	rows = (''.join(row) for row in board)
	columns = (''.join(column) for column in zip(*board))
	words = [word for line in itertools.chain(rows,columns) for word in line.split() if len(word) > 1]
	print(words)

    def restart(self):
        self.canvas.delete(ALL)
        self.__board()
        self.changeStatus('Start Game')
        self.board = [0 for x in range(0,ROWS*COLS)]
        self.winner = None
        self.lastmoves = []
		
		# Read Image
		#vc = cv2.VideoCapture(0)
 
		#if vc.isOpened(): # try to get the first frame
			#rval, self.img = vc.read()
        #else:
			#rval = False
        self.img = cv2.imread('scrabble3.jpg')
        self.img = cv2.resize(self.img, (300, 300)) 
        
        count = 0
        for j in range(0,300,(300/ROWS)):
            for i in range(0,300,(300/COLS)):
                self.crop_img = self.img[j+1:j+(300/ROWS)-1, i+1:i+(300/COLS)-1]
                cv2.imwrite('image/test.png',self.crop_img)
                img = Image.open('image/test.png')
                str2 = pytesseract.image_to_string(img,config='-psm 10000')
                str1 = ''.join([k for k in str2 if not k.isdigit()])
                str = ''.join(e for e in str1 if e.isalnum())
		if not str: 
		   str = ' '
                #print(str)
                self.canvas.create_text(i+10, j+10, font="Purisa",text=str)
                self.board[count] = str
                count = count+1
				
	board = np.reshape(self.board, (-1, 15))
	rows = (''.join(row) for row in board)
	columns = (''.join(column) for column in zip(*board))
	words = [word for line in itertools.chain(rows,columns) for word in line.split() if len(word) > 1]
	print(words)
	self.changeStatus("Robotic Arm's turn")
		
    def next(self):

        # Read Image
        #vc = cv2.VideoCapture(0)

        #if vc.isOpened(): # try to get the first frame
             #rval, self.img = vc.read()
        #else:
             #rval = False
        self.img = cv2.imread('scrabble3.jpg')
        self.img = cv2.resize(self.img, (300, 300)) 
        
        count = 0
        for j in range(0,300,(300/ROWS)):
            for i in range(0,300,(300/COLS)):
                self.crop_img = self.img[j+1:j+(300/ROWS)-1, i+1:i+(300/COLS)-1]
                cv2.imwrite('image/test.png',self.crop_img)
                img = Image.open('image/test.png')
                str2 = pytesseract.image_to_string(img,config='-psm 10000')
                str1 = ''.join([k for k in str2 if not k.isdigit()])
                str = ''.join(e for e in str1 if e.isalnum())
                print(str)
                self.canvas.create_text(i+10, j+10, font="Purisa",text=str)
                self.board[count] = str
                count = count+1
	
	board = np.reshape(self.board, (-1, 15))
        rows = (''.join(row) for row in board)
        columns = (''.join(column) for column in zip(*board))
        words = [word for line in itertools.chain(rows,columns) for word in line.split() if len(word) > 1]
	print(words)
		
    def __board(self):
        for i in range(0,300,2*(300/COLS)):
            self.canvas.create_rectangle(i, 0 , i + (300/COLS), 300, outline="black")
			
        for j in range(0,300,2*(300/ROWS)):
            self.canvas.create_rectangle(0, j , 300, j + (300/ROWS), outline="black")
				
    def changeStatus(self, status):
        self.status['text'] = status
	
			
# Program Starts Here
root = Tk()
app = TTT(root)
root.mainloop()

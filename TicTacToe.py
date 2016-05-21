import numpy as np
import os
import cv2
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
from Tkinter import Tk, Label, Frame, Canvas, Button, ALL

def min_max_move(instance, marker):
    bestmove = None
    bestscore = None
    
    if marker == 2:
        for m in instance.get_free_cells():
            instance.mark(m, 2)
            if instance.is_gameover():
                score = instance.get_score()
            else:
                mov_pos, score = min_max_move(instance, 1)
            instance.revert_last_move()

            if bestscore == None or score > bestscore:
                bestscore = score
                bestmove = m
    else:
        for m in instance.get_free_cells():
            instance.mark(m, 1)
            if instance.is_gameover():
                score = instance.get_score()
            else:
                mov_pos, score = min_max_move(instance, 2)
            instance.revert_last_move()

            if bestscore == None or score < bestscore:
                bestscore = score
                bestmove = m
    return bestmove, bestscore

def scale(image, max_size):
    """
    resize 'image' to 'max_size' keeping the aspect ratio 
    and place it in center of white 'max_size' image 
    """
    back = Image.new("RGB", max_size, (255,255,255,255))   ## luckily, this is already black!
    back.paste(image, ((max_size[0]-image.size[0])/2,
						(max_size[1]-image.size[1])/2))
    return back

class TTT:
    '''
        main class
    '''
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack(fill="both", expand=True)
        self.label = Label(self.frame, text='Tic Tac Toe Game', height=2, font="Arial 14", bg='black', fg='blue')
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
        self.canvas.bind("<ButtonPress-1>", self.handler)
        self.board = [0 for x in range(0, 9)]
        self.winner = None
        self.lastmoves = []
		
	# Read Image
	vc = cv2.VideoCapture(0)
 
	if vc.isOpened(): # try to get the first frame
	     rval, self.img = vc.read()
        else:
	     rval = False
	#self.img = cv2.imread('image/tictac5.png')
        self.img = cv2.resize(self.img, (300, 300)) 
        
        count = 0
        for j in range(0,300,100):
            for i in range(0,300,100):
                self.crop_img = self.img[j+10:j+90, i+10:i+90]
                cv2.imwrite('image/test.png',self.crop_img)
                img = Image.open('image/test.png')
                #img = scale(img, (640,480))
                #img.save("image/test.bmp")
                str = pytesseract.image_to_string(img,config='-psm 10000')
                if str == 'O':
                    print(str)
                    x = count%3
                    y = int(count/3)
                    X = 100 * (x + 1)
                    Y = 100 * (y + 1)
                    self.canvas.create_oval(X - 25, Y - 25, X - 75, Y - 75, width=4, outline="green")
                    self.board[count] = 2
                if str == 'X':
                    print(str)
                    x = count%3
                    y = int(count/3)
                    X = 100 * x
                    Y = 100 * y
                    self.canvas.create_line(X + 25, Y + 25, X + 75, Y + 75, width=4, fill="red")
                    self.canvas.create_line(X + 25, Y + 75, X + 75, Y + 25, width=4, fill="red")
                    self.board[count] = 1
                cv2.namedWindow('dst_rt', cv2.WINDOW_NORMAL)
                cv2.resizeWindow('dst_rt', 300, 300)
                cv2.imshow('dst_rt', self.crop_img)
                cv2.waitKey(0)
                count = count + 1		

    def restart(self):
        self.canvas.delete(ALL)
        self.__board()
        self.changeStatus('Start Game')
        self.canvas.bind("<ButtonPress-1>", self.handler)
        self.board = [0 for x in range(0, 9)]
        self.winner = None
        self.lastmoves = []
		
	# Read Image
        vc = cv2.VideoCapture(0)

        if vc.isOpened(): # try to get the first frame
             rval, self.img = vc.read()
        else:
             rval = False
        #self.img = cv2.imread('image/tictac5.png')
        self.img = cv2.resize(self.img, (300, 300)) 
        
        count = 0
        for j in range(0,300,100):
            for i in range(0,300,100):
                self.crop_img = self.img[j+10:j+90, i+10:i+90]
                cv2.imwrite('image/test.png',self.crop_img)
                img = Image.open('image/test.png')
                #img = scale(img, (640,480))
                #img.save("image/test.bmp")
                str = pytesseract.image_to_string(img,config='-psm 10000')
                if str == 'O':
                    x = count%3
                    y = int(count/3)
                    X = 100 * (x + 1)
                    Y = 100 * (y + 1)
                    self.canvas.create_oval(X - 25, Y - 25, X - 75, Y - 75, width=4, outline="green")
                    self.board[count] = 2
                if str == 'X':
                    x = count%3
                    y = int(count/3)
                    X = 100 * x
                    Y = 100 * y
                    self.canvas.create_line(X + 25, Y + 25, X + 75, Y + 75, width=4, fill="red")
                    self.canvas.create_line(X + 25, Y + 75, X + 75, Y + 25, width=4, fill="red")
                    self.board[count] = 1
                count = count + 1		
	
    def next(self):
        if self.is_gameover():
            if self.winner == 2:
                self.changeStatus("O Won the Game !")
            elif self.winner == 1:
                self.changeStatus("X Won the Game !")
            else:
                self.changeStatus("Game Draw !")
            return

        # Read Image
        vc = cv2.VideoCapture(0)

        if vc.isOpened(): # try to get the first frame
             rval, self.img = vc.read()
        else:
             rval = False
        #self.img = cv2.imread('image/tictac4.png')
        self.img = cv2.resize(self.img, (300, 300)) 
        
        count = 0
        for j in range(0,300,100):
            for i in range(0,300,100):
                self.crop_img = self.img[j+10:j+90, i+10:i+90]
                cv2.imwrite('image/test.png',self.crop_img)
                img = Image.open('image/test.png')
                #img = scale(img, (640,480))
                #img.save("image/test.bmp")
                str = pytesseract.image_to_string(img,config='-psm 10000')
                if str == 'O':
                    x = count%3
                    y = int(count/3)
                    X = 100 * (x + 1)
                    Y = 100 * (y + 1)
                    self.canvas.create_oval(X - 25, Y - 25, X - 75, Y - 75, width=4, outline="green")
                    self.board[count] = 2
                if str == 'X':
                    x = count%3
                    y = int(count/3)
                    X = 100 * x
                    Y = 100 * y
                    self.canvas.create_line(X + 25, Y + 25, X + 75, Y + 75, width=4, fill="red")
                    self.canvas.create_line(X + 25, Y + 75, X + 75, Y + 25, width=4, fill="red")
                    self.board[count] = 1
                count = count + 1
		
		pos, score = min_max_move(self, 1)
        self.markFinal(pos, 1);

        if self.is_gameover():
            if self.winner == 2:
                self.changeStatus("O Won the Game !")
            elif self.winner == 1:
                self.changeStatus("X Won the Game !")
            else:
                self.changeStatus("Game Draw !")
            return
		
    def get_free_cells(self):
        moves = []
        for i,v in enumerate(self.board):
            if v == 0:
                moves.append(i)
        return moves

    def mark(self,pos, marker):
        self.board[pos] = marker
        self.lastmoves.append(pos)

    def revert_last_move(self):
        self.board[self.lastmoves.pop()] = 0
        self.winner = None

    def is_gameover(self):
        win_positions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6),(1,4,7),(2,5,8), (0,4,8), (2,4,6)]
        for i,j,k in win_positions:
            if self.board[i] == self.board[j] and self.board[j] == self.board[k] and self.board[i] != 0:
                self.winner = self.board[i]
                return True
        if 0 not in self.board:
            self.winner = 0
            return True
        return False

    def get_score(self):
        if self.is_gameover():
            if self.winner == 2:
                return 1 # Won
            elif self.winner == 1:
                return -1
        return 0

    def __board(self):
        self.canvas.create_rectangle(0, 0, 300, 300, outline="black")
        self.canvas.create_rectangle(100, 300, 200, 0, outline="black")
        self.canvas.create_rectangle(0, 100, 300, 200, outline="black")
				
    def changeStatus(self, status):
        self.status['text'] = status

    def markFinal(self, pos, marker):
        x = pos%3
        y = int(pos/3)
        if marker == 2:
            X = 100 * (x + 1)
            Y = 100 * (y + 1)
            self.canvas.create_oval(X - 25, Y - 25, X - 75, Y - 75, width=4, outline="green")
            self.changeStatus("X's Move !")
        else:
            X = 100 * x
            Y = 100 * y
            self.canvas.create_line(X + 25, Y + 25, X + 75, Y + 75, width=4, fill="red")
            self.canvas.create_line(X + 25, Y + 75, X + 75, Y + 25, width=4, fill="red")
            self.changeStatus("O's Move !")
        
        self.board[pos] = marker
		
    def handler(self, event):
        '''
        handle mouse click event on the board
        '''
        x = int(event.x / 100)
        y = int(event.y / 100)
        if self.board[y*3+x] == 0:
            self.markFinal(y*3+x, 2)
			
# Program Starts Here
root = Tk()
app = TTT(root)
root.mainloop()

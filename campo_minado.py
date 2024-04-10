import tkinter as tk
import tkinter.messagebox as messagebox

import random

class Color:
    gray_light = '#CDC9C9'
    border = '#2F4F4F',
    red = '#FF0000'

    

class CampoMInado:
    def __init__(self, minefield, rows, cols, n_mines):
        self.mine_field = minefield
        self.rows = rows
        self.n_mines = n_mines
        self.cols = cols
        self.board = [[0] * cols for i in range(rows)]
        self.cells = []
        self.CreateMines()
        self.CreateBoard()
        
    def CreateMines(self):
        for _ in range(self.n_mines):
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            self.board[row][col] = 1
        
    def CreateBoard(self):
        for row in range(self.rows):
            cel_list = []
            for col in range(self.cols):
                cel = tk.Button(
                    self.mine_field,
                    width=2, height=2,
                    command=lambda row=row, col=col: self.reveal(row, col),
                    bg= Color.gray_light,
                    highlightbackground=Color.border )
                cel.grid(row=row, column=col)
                cel_list.append(cel)
            self.cells.append(cel_list)
        
    def reveal(self, row, col):
        if self.board[row][col] == 1:
            self.cells[row][col].config(text='BUM!', bg=Color.red, state='disabled', )
            messagebox.showinfo("Fim de jogo", "Você perdeu! Tente novamente!")
            self.mine_field.quit() 
    
    
minefield = tk.Tk()
minefield.title("Jogo - Campo Minado")

campo = CampoMInado(minefield, 16, 16, 46)
minefield.mainloop()
import tkinter as tk


class Color:
    gray_light = '#CDC9C9'
    border = '#2F4F4F'

class CampoMInado:
    def __init__(self, minefield, rows, cols, n_mines):
        self.mine_field = minefield
        self.rows = rows
        self.n_mines = n_mines
        self.cols = cols
        self.board = [-1 * cols for i in range(rows)]
        self.cells = []
        self.createBoard()
        
    def createBoard(self):
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
        print("reveal")  
    
    
minefield = tk.Tk()
minefield.title("Jogo - Campo Minado")

campo = CampoMInado(minefield, 16, 16, 46)
minefield.mainloop()
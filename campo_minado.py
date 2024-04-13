import tkinter as tk
import tkinter.messagebox as messagebox
from collections import deque

import random

class Color:
    gray_light = '#CDC9C9'
    border = '#2F4F4F',
    red = '#FF0000'

    

class CampoMInado:
    #inicializa as variáveis
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
        #usa ramdom para criar minas em lugares "aleatórios"
        for _ in range(self.n_mines):
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            self.board[row][col] = 1
        
    def CreateBoard(self):
        # Cria o campo minado usando tk
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
            
    def bfs(self, start_row, start_col):
        visited = set() # cria visitados
        queue = deque([(start_row, start_col)]) #fila, insere coluna e linha que foi clicado na fila
        while queue: 
            row, col = queue.popleft() # pega o 1 da fila, inicia com o que o jogador clicou
            visited.add((row, col)) # marca como visitado
            adjacent_mines = 0 #calculo de adjancentes da bomba
            for r in range(max(0, row - 1), min(row + 2, self.rows)):
                for c in range(max(0, col - 1), min(col + 2, self.cols)):
                    if self.board[r][c] == 1:
                        adjacent_mines += 1
                        
            self.cells[row][col].config(text=str(adjacent_mines), state='disabled') # revela as minas adjacentes
            print(adjacent_mines)
            if adjacent_mines == 0: # caso não tenha minas adjacentes onde o jogador clicou, a bfs continua
                for r in range(max(0, row - 1), min(row + 2, self.rows)):
                    for c in range(max(0, col - 1), min(col + 2, self.cols)):
                        if (r, c) not in visited and self.cells[r][c]['state'] != 'disabled':
                            queue.append((r, c)) # adiciona a linha e a coluna a fila
                            print(queue)
                            visited.add((r, c)) # adiciona a linha e coluna como visitado
    def revealAll():
        print("Revelar todas os outros campos, incluindo as bombas")
        
    def reveal(self, row, col):
        if self.board[row][col] == 1:
            self.cells[row][col].config(text='BUM!', bg=Color.red, state='disabled', )
            self.revealAll
            messagebox.showinfo("Fim de jogo", "Você perdeu! Tente novamente!")
            self.mine_field.quit() 
        else:
            self.bfs(row, col)
   

    
    
minefield = tk.Tk()
minefield.title("Jogo - Campo Minado")

campo = CampoMInado(minefield, 16, 16, 46)
minefield.mainloop()
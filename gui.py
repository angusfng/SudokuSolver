import pygame, sys
from sudoku import solve, validNumber

pygame.font.init()

class Cube:
	def __init__(self, value, row, col, width, height):
		self._value = value
		self._row = row
		self._col = col
		self._width = width
		self._height = height
		self._selected = False

	def draw(self, win):
		fnt = pygame.font.SysFont("comicsans", 40)

		gap = self._width / 9
		x = self._col * gap
		y = self._row * gap

		if self._value != 0:
			text = fnt.render(str(self._value), 1, (0, 0, 0))
			win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))

		if self._selected:
			pygame.draw.rect(win, (255,0,0), (x,y, gap ,gap), 3)

	def setValue(self, value):
		self._value = value

class Grid:
	b = [[1,0,1,0,0,0,0,6,5],
	     [0,0,0,6,0,9,0,8,0],
	     [3,0,0,0,4,8,0,0,0],
	     [0,0,0,0,2,0,0,5,8],
	     [0,0,6,0,0,0,1,2,0],
	     [0,0,0,0,9,0,0,0,0],
	     [0,4,0,0,0,0,0,0,0],
	     [0,0,0,3,0,0,5,7,0],
	     [5,2,3,1,0,0,4,0,0]]

	def __init__(self, rows, cols, width, height):
		self._rows = rows
		self._cols = cols
		self._cubes = [[Cube(self.b[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
		self._width = width
		self._height = height
		self._model = None
		self._selected = None

	def draw(self, win):
		# Draw Grid Lines
		gap = self._width / 9
		for i in range(self._rows + 1):
			if i % 3 == 0 and i != 0:
				thick = 4
			else:
				thick = 1
			pygame.draw.line(win, (0,0,0), (0, i*gap), (self._width, i*gap), thick)
			pygame.draw.line(win, (0,0,0), (i*gap, 0), (i*gap, self._height), thick)
			

		for i in range(self._rows):
			for j in range(self._cols):
				self._cubes[i][j].draw(win)

	def click(self, pos):
		if pos[0] < self.width and pos[1] < self.height:
			gap = self.width / 9
			x = pos[0] // gap
			y = pos[1] // gap
			return (int(y), int(x))
		else:
			return None



def redrawWindow(win, board):
	win.fill((255, 255, 255))
	board.draw(win)

def main():
	win = pygame.display.set_mode((540, 600))
	pygame.display.set_caption("Sudoku")
	key = None
	run = True
	board = Grid(9, 9, 540, 540)

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					key = 1

			if event.type = pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				clicked = board.click(pos)

		redrawWindow(win, board)
		pygame.display.update()


main()
pygame.quit()
sys.exit()
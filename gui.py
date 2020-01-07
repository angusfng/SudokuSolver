import pygame, sys
from sudoku import solve, validNumber, printBoard

# initializes fonts
pygame.font.init()

class Square:
	def __init__(self, value, row, col, width, height):
		self._value = value # Value in the square
		self._row = row # What row it is in
		self._col = col # What column it is in
		self._width = width # Width of the square
		self._height = height # Height of the square

	# Gets the value in the square
	def getValue(self):
		return self._value

	# Sets the value in the square
	def setValue(self, value):
		self._value = value

	def getRow(self):
		return self._row

	def getCol(self):
		return self._col

	def getWidth(self):
		return self._width

	def getHeight(self):
		return self._height

	# Puts the numbers into the square
	# Work this out
	def draw(self, win):
		fnt = pygame.font.SysFont("comicsans", 40)

		gap = self.getWidth() / 9
		x = self.getCol() * gap
		y = self.getRow() * gap

		if self.getValue() != 0:
			text = fnt.render(str(self.getValue()), 1, (0, 0, 0))
			win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))
	

class Grid:
	a = [[0,0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0,0]]

	b = [[0,0,3,9,0,0,0,4,2],
		 [0,9,1,0,5,0,3,8,0],
		 [5,0,0,0,0,0,0,6,0],
		 [0,0,8,3,4,9,0,0,0],
		 [3,0,6,7,0,2,4,0,8],
		 [0,0,0,5,6,8,7,0,0],
		 [0,2,0,0,0,0,0,0,9],
		 [0,3,4,0,9,0,1,2,0],
		 [9,6,0,0,0,3,8,0,0]]

	def __init__(self, rows, cols, width, height):
		self._rows = rows
		self._cols = cols
		self._squares = [[Square(self.b[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
		self._width = width
		self._height = height
		self._selected = None
		self._board = self.b

	def getRows(self):
		return self._rows

	def getCols(self):
		return self._cols
	
	def getSquares(self):
		return self._squares

	def getWidth(self):
		return self._width

	def getHeight(self):
		return self._height

	def getSelected(self):
		return self._selected

	def setSelected(self, row, col):
		self._selected = (row, col)

	def getBoard(self):
		return self._board

	def setBoard(self, row, col, value):
		self._board[row][col] = value

	def draw(self, win):
		# Draw Grid Lines
		gap = self.getWidth() / 9
		for i in range(self.getRows() + 1):
			if i % 3 == 0 and i != 0:
				thick = 4
			else:
				thick = 1
			pygame.draw.line(win, (0,0,0), (0, i*gap), (self.getWidth(), i*gap), thick)
			pygame.draw.line(win, (0,0,0), (i*gap, 0), (i*gap, self.getHeight()), thick)
			

		for i in range(self.getRows()):
			for j in range(self.getCols()):
				self.getSquares()[i][j].draw(win)

	# Click position in the grid
	def click(self, pos):
		if pos[0] < self.getWidth() and pos[1] < self.getHeight():
			gap = self.getWidth() / 9
			x = pos[0] // gap
			y = pos[1] // gap
			return (int(y), int(x))
		else:
			return None

	# Places the number into the square
	def place(self, val):
		row, col = self.getSelected()
		if self.getSquares()[row][col].getValue() == 0:
			self.getSquares()[row][col].setValue(val)
			# Also places into the board for solve purpose
			self.setBoard(row, col, val)

	# Clears an individual square of the board
	def clearSquare(self):
		row, col = self.getSelected()
		self.getSquares()[row][col].setValue(0)
		self.setBoard(row, col, 0)

	# Solves the entire board
	def solve(self):
		solved = solve(self.getBoard())
		print(solved)
		if solved:
			for i in range(self.getRows()):
				for j in range(self.getCols()):
					self.getSquares()[i][j].setValue(solved[i][j])
					self.setBoard(i, j, solved[i][j])
		else:
			print("Not solveable")

	# Clears the entire board
	def clearBoard(self):
		for i in range(self.getRows()):
			for j in range(self.getCols()):
				#print("set {} {} to 0".format(i, j))
				self.getSquares()[i][j].setValue(0)
				self.getBoard()[i][j] = 0


def redrawWindow(win, board):
	# Fills surface with white
	win.fill((255, 255, 255))
	board.draw(win)

def main():
	# Returns the surface
	win = pygame.display.set_mode((540, 540))
	# Names the window
	pygame.display.set_caption("Sudoku")
	# What key was pressed
	key = None
	# Loop for the game
	run = True
	# Grid object
	board = Grid(9, 9, 540, 540)

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			# Keys pressed
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					key = 1
				if event.key == pygame.K_2:
					key = 2
				if event.key == pygame.K_3:
					key = 3
				if event.key == pygame.K_4:
					key = 4
				if event.key == pygame.K_5:
					key = 5
				if event.key == pygame.K_6:
					key = 6
				if event.key == pygame.K_7:
					key = 7
				if event.key == pygame.K_8:
					key = 8
				if event.key == pygame.K_9:
					key = 9
				if event.key == pygame.K_DELETE:
					if board.getSelected() != None:
						board.clearSquare()
					key = None
				if event.key == pygame.K_RETURN:
					
					board.solve()
					key = None
				if event.key == pygame.K_c:
					board.clearBoard()
					key = None
			
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				clicked = board.click(pos)
				if clicked:
					board.setSelected(clicked[0], clicked[1])
					key = None

		# Put number into square
		if board.getSelected() and key != None:
			board.place(key)
		# Updates the board constantly
		redrawWindow(win, board)
		pygame.display.update()


main()
pygame.quit()
sys.exit()
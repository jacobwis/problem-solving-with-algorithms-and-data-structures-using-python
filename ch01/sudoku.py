import math

puz1 = [[8,0,0,9,3,0,0,0,2],
		[0,0,9,0,0,0,0,4,0],
		[7,0,2,1,0,0,9,6,0],
		[2,0,0,0,0,0,0,9,0],
		[0,6,0,0,0,0,0,7,0],
		[0,7,0,0,0,6,0,0,5],
		[0,2,7,0,0,8,4,0,6],
		[0,3,0,0,0,0,5,0,0],
		[5,0,0,0,6,2,0,0,8]]


class Sudoku:
	def __init__(self,start):
		self.grid = self.setupGrid(start)
		self.blockSize = int(math.sqrt(len(start)))

	def setupGrid(self,start):
		for i in range(1,self.blockSize):

		squares = []
		currentRow = 1
		for row in start:
			currentCol = 1
			for column in row:
				square = {'row': currentRow, 'col': currentCol}
				if column != 0:
					square['val'] = column
					square['solved'] = True
				else:
					square['val'] = None
					square['candidates'] = list(range(1,len(start)+1))
					square['solved'] = False
				squares.append(square)
				currentCol += 1
			currentRow += 1
		return squares

	def getRow(self,n):
		cells = []
		for cell in self.grid:
			if cell["row"] == n:
				cells.append(cell)
		return cells

	def getCol(self,n):
		cells = []
		for cell in self.grid:
			if cell["col"] == n:
				cells.append(cell)
		return cells

	def getBlock(self,r,c):
		points = [1]
		for i in range(1,self.blockSize):
			point = (i * self.blockSize) + 1
			points.append(point)
		return points

	def printGrid(self):
		currentRow = 1
		blockColCount = 0
		blockRowCount = 1
		print('|', end="")
		for square in self.grid:
			if square['val'] != None:
				val = square['val']
			else:
				val = ' '
			blockColCount += 1
			if square["row"] == currentRow:
				print(val, end="")
				if blockColCount == self.blockSize:
					print('|', end="")
					blockColCount = 0
			else:
				print('')
				if blockRowCount == self.blockSize:
					print("-"*((self.blockSize * self.blockSize)+ (self.blockSize + 1)))
					blockRowCount = 0
				print('|', end="")
				print(val, end="")
				currentRow += 1
				blockRowCount += 1
		print('')

	def getUnsolved(self):
		unsolved = []
		for cell in self.grid:
			if cell["solved"] == False:
				unsolved.append(cell)
		return unsolved

def main():
	puzzle = Sudoku(puz1)
	print(puzzle.getBlock(0,1))

main()	

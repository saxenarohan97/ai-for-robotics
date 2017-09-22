from operator import add

grid = [[0, 0, 1, 0, 0, 0], 
		[0, 0, 1, 0, 0, 0],
		[0, 0, 0, 0, 1, 0],
		[0, 0, 1, 1, 1, 0],
		[0, 0, 0, 0, 1, 0]]

goal = [4, 5]

delta = [[-1, 0],
		[0, -1],
		[1, 0],
		[0, 1]]

delta_name = ['^', '<', 'v', '>']

cost = 1

for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] == 1:
			grid[i][j] = 99
		else:
			grid[i][j] = -1

grid[goal[0]][goal[1]] = 0

ctr = 1
previous_ctr = 0

space = [[' ' , ' ', ' ', ' ', ' ', ' '], 
		[' ' , ' ', ' ', ' ', ' ', ' '],
		[' ' , ' ', ' ', ' ', ' ', ' '],
		[' ' , ' ', ' ', ' ', ' ', ' '],
		[' ' , ' ', ' ', ' ', ' ', ' ']]

while ctr!=0 and previous_ctr != ctr:
	previous_ctr = ctr
	ctr = 0

	for i in range(len(grid)):
		for j in range(len(grid[i])):

			if grid[i][j] != -1 and grid[i][j] != 99:

				for motion in delta:
					cell = map(add, motion, [i, j])
					complement = (delta.index(motion) + 2) % len(delta)

					if cell[0]>=0 and cell[0]<5 and cell[1]>=0 and cell[1]<6:

						if grid[cell[0]][cell[1]] == -1:

							grid[cell[0]][cell[1]] = grid[i][j]+1
							space[cell[0]][cell[1]] = delta_name[complement]

			elif grid[i][j] == -1:

				ctr += 1


for row in grid:
	print row

print ''

space[goal[0]][goal[1]] = '*'

for row in space:
	print row
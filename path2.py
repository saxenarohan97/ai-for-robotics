from operator import add

grid = [[0, 0, 0, 0, 0, 0],
		[0, 1, 1, 1, 1, 0],
		[0, 1, 0, 0, 0, 0],
		[0, 1, 0, 0, 0, 0],
		[0, 1, 0, 0, 0, 0]]

heuristic = [[9, 8, 7, 6, 5, 4],
			 [8, 7, 6, 5, 4, 3],
			 [7, 6, 5, 4, 3, 2],
			 [6, 5, 4, 3, 2, 1],
			 [5, 4, 3, 2, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0],
		[0, -1],
		[1, 0],
		[0, 1]]

delta_name = ['^', '<', 'v', '>']

cost = 1
###############################################################
space = grid
open = [[0, init[0], init[1]]]
path = []

for i in range(len(grid)):
	for j in range(len(grid)):
		if (grid[i][j] == 1):
			space[i][j] = -1

space[init[0]][init[1]] = -2

pos = -1
ctr = 0

while True:
	if open == []:
		break

	low = 0
	for i in range(len(open)):
		if open[i][0] + heuristic[open[i][1]][open[i][2]] < open[low][0] + heuristic[open[low][1]][open[low][2]]:
			low = i

	spread = []

	for motion in delta:
		cell = list(map(add, [cost, motion[0], motion[1]], open[low]))

		if (cell[1]>=0 and cell[1]<5 and cell[2]>=0 and cell[2]<=5 and space[cell[1]][cell[2]]==0):
				spread.append(cell)
				ctr+=1
				space[cell[1]][cell[2]] = ctr

	open.remove(open[low])
	for s in spread:
		open.append(s)

	for o in open:
		if o[1]==goal[0] and o[2]==goal[1]:
			pos = open.index(o)
			break

	if pos != -1:
		break

if pos == -1:
	print("fail \n")

else:
	print(open[pos], "\n")

space[init[0]][init[1]] = 0

for row in space:
	print(row)

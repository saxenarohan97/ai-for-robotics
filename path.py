from operator import add

grid = 	       [[1, 1, 0, 1, 1, 0, 1],
                [1, 0, 0, 1, 1, 0, 1],
                [1, 0, 1, 1, 1, 1, 1],
                [1, 0, 0, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0],
		[0, -1],
		[1, 0],
		[0, 1]]

delta_name = ['^', '<', 'v', '>']

cost = 1
###############################################################
space = grid						#SPACE IS MY EXPAND
open = [[0, init[0], init[1]]]

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

	low = 100000
	for i in range(len(open)):
		if open[i][0] < low:
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

if pos != -1:
	print(open[pos], "\n")

else:
	print("fail \n")

for i in range(len(space)):
	for j in range(len(space[i])):
		if space[i][j] == 0:
			space[i][j] = -1

space[init[0]][init[1]] = 0

for s in space:
	print(s)

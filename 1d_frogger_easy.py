import sys

params = sys.stdin.readline()
params = params.split()

board = sys.stdin.readline()
board = board.split()

loc = int(params[1])-1
magic = int(params[2])
bound = int(params[0])-1

visited = []
i = 0
while True:
	if loc > bound:
		print("right\n" + str(i))
		break
	elif loc < 0:
		print("left\n" + str(i))
		break  
	elif loc in visited:
		print("cycle\n" + str(i))
		break

	tile = int(board[loc])

	if tile == magic:
		print("magic\n" + str(i))
		break

	else:
		visited.append(loc)
		loc = loc + tile
		i = i + 1
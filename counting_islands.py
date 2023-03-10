import queue

def read_input():
	rows, cols = map(int, input().split())

	field = []
	for _ in range(rows):
		row = [int(x) for x in input().split()]
		field.append(row)

	return field

def is_in_field(row, col, max_row, max_col):
	return row >= 0 and row < max_row and col >= 0 and col < max_col

def solve(field):
	if len(field) == 0 or len(field[0]) == 0:
		return 0

	rows, cols = len(field), len(field[0])
	is_cell_visited = [[False for _ in range(cols)] for _ in range(rows)]
	possible_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

	answer = 0
	q = queue.Queue()

	for row in range(rows):
		for col in range(cols):
			if field[row][col] == 0 or is_cell_visited[row][col] == True:
				continue
			else:
				answer += 1

				q.put((row, col))
				is_cell_visited[row][col] = True

				while not q.empty():
					cur_row, cur_col = q.get()
					for row_move, col_move in possible_moves:
						candidate_row = cur_row + row_move
						candidate_col = cur_col + col_move

						if is_in_field(candidate_row, candidate_col, rows, cols) \
							and field[candidate_row][candidate_col] == 1 \
							and not is_cell_visited[candidate_row][candidate_col]:
							is_cell_visited[candidate_row][candidate_col] = True
							q.put((candidate_row, candidate_col))

	return answer

field = read_input()
islands_number = solve(field)
print(islands_number)

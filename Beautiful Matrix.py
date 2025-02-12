matrix = [list(map(int, input().split())) for _ in range(5)]
position_one = [(i, row.index(1)) for i, row in enumerate(matrix) if 1 in row][0]
target_position = (2, 2)
 
moves = abs(position_one[0] - target_position[0]) + abs(position_one[1] - target_position[1])
print(moves)

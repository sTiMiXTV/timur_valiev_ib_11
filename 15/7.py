def find_mountain(heightsMap):
    top_row, top_column, top_height = 0, 0, 0
    for x in range(len(heightsMap)):
        for y in range(len(heightsMap[x])):
            height = heightsMap[x][y]
            if height > top_height:
                top_height = height
                top_row = x
                top_column = y
    return top_row, top_column

a = [[2, 4, 2, 3, 2], [3, 2, 3, 4, 3]]
row, col = find_mountain(a)
print(a[row][col])

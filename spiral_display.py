def spiral_display(arr, row_end, column_end):
	row_start_index = 0
	column_start_index = 0
	while row_start_index < row_end and column_start_index < column_end:
		for i in range(column_start_index, column_end):
			print(arr[row_start_index][i], end=" ")
		row_start_index += 1
		for i in range(row_start_index, row_end):
			print(arr[i][column_end - 1], end=" ")
		column_end -= 1
		
		if row_start_index < row_end:
			for i in range(column_end - 1, column_start_index - 1, -1):
				print(arr[row_end - 1][i], end=" ")
			row_end -= 1
		if column_start_index < column_end:
			for i in range(row_end - 1, row_start_index - 1, -1):
				print(arr[i][column_start_index], end=" ")
			column_start_index += 1


arr = [[1, 2, 3, 4, 5, 6],
	   [7, 8, 9, 10, 11, 12],
	   [13, 14, 15, 16, 17, 18]]

spiral_display(arr, 3, 6)

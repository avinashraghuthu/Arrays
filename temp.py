from os import listdir
from os.path import isfile, join

#Main program

count = 1
display_str = '---'


def recursive_display(current_path, count):
	content_list = listdir(current_path)
	for i in content_list:
		print display_str * count, i
		if not isfile(join(current_path, i)):
			recursive_display(join(current_path, i), count+count)


def prepare_dict(my_path):
	output = {}
	dir_list = [my_path]
	while dir_list:
		current_path = dir_list.pop(0)
		content_list = listdir(current_path)
		for i in content_list:
			if isfile(join(current_path, i)):
				try:
					output[current_path].append(i)
				except KeyError, e:
					output[current_path] = [i]
			else:
				dir_list.append(join(my_path, i))
	return output


def display_contents(my_path):
	output = prepare_dict(my_path)
	sorted_keys = sorted(output)
	count = 1
	display_str = '---'
	prev_len = None
	key = sorted_keys.pop(0)
	file_list = output[key]
	for i in file_list:
		print display_str * count, i
	for key in sorted_keys:
		curr_len = len(key.split('/'))
		print display_str*count, key.split('/')[-1]
		if not prev_len:
			prev_len = curr_len
		if prev_len != curr_len:
			count += count
		file_list = output[key]
		for i in file_list:
			print display_str*(count+1), i
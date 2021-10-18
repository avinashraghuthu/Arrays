#  https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/


def platform_count(arrival, departure):
	arr_len = len(arrival)
	arrival.sort()
	departure.sort()
	current_count = 0
	min_platform_count = 0
	arrival_index = 0
	departure_index = 0
	while arrival_index < arr_len and departure_index < arr_len:
		if arrival[arrival_index] < departure[departure_index]:
			current_count += 1
			arrival_index += 1
			if min_platform_count < current_count:
				min_platform_count = current_count
		else:
			current_count -= 1
			departure_index += 1
	return min_platform_count


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
print("Minimum Number of Platforms Required = ", platform_count(arr, dep))

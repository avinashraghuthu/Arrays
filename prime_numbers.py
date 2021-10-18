def SieveOfEratosthenes(n):
	is_prime = [True] * (n + 1)
	number = 2
	while number * number <= n:
		if is_prime[number]:
			for i in range(number * number, n + 1, number):
				is_prime[i] = False
		number += 1
	return is_prime


is_prime = SieveOfEratosthenes(15)
[print(i) for i in range(2, len(is_prime)) if is_prime[i]]
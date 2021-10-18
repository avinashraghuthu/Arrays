# defining a decorator
# https://realpython.com/primer-on-python-decorators/#decorators-with-arguments

def hello_decorator(func):
	# inner1 is a Wrapper function in
	# which the argument is called
	
	# inner function can access the outer local
	# functions like in this case "func"
	i=0
	print("hi")
	def inner1(*args, **kwargs):
		print("Hello, this is before function execution")
		
		# calling the actual function now
		# inside the wrapper function.
		print("inner args", *args)
		input_str = args[0]
		func("avi "+input_str)
		
		print("This is after function execution")
	
	return inner1


# defining a function, to be called inside wrapper
@hello_decorator
def function_to_be_used(input_str):
	print("This is inside the function !!")
	print(input_str)

# calling the function
function_to_be_used("hi")

# Python program showing
# class decorator with
# return satement

class SquareDecorator:
	
	def __init__(self, type):
		# self.function = function
		self.type = type
	
	def __call__(self, func):
		def inner(*args, **kwargs):
			print("type", self.type)
			# before function
			# print("type", self.type)
			result = func(*args, **kwargs)
			
			# after function
			return result
		
		return inner


# adding class decorator to the function
@SquareDecorator("4_xx")
def get_square(n):
	print("given number is:", n)
	return n * n


print("Square of number is:", get_square(10))

# passing 'function_to_be_used' inside the
# decorator to control its behavior
# function_to_be_used = hello_decorator(function_to_be_used)




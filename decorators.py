from datetime import datetime
# 1 type:


def decorator_v1(func):
	b_time = datetime.now()

	def wrap():
		print("Before function being called at %s" % b_time)
		func_out = func()
		print("Total time taken for output is %s " % (datetime.now() - b_time).microseconds)
		return func_out
	return wrap


@decorator_v1
def square_of_20():
	return [i**2 for i in range(20)]

# print(squareof_20())


# decorator with main function arguments
def decorator_v2(func):
	b_time = datetime.now()

	def wrap(*args, **kwargs):
		print('args are %s' % args)
		print('kwargs are %s' % kwargs)
		print("Before function being called at %s" % b_time)
		func_out = func(*args, **kwargs)
		print("Total time taken for output is %s microseconds" % (datetime.now() - b_time).microseconds)
		return func_out
	return wrap


@decorator_v2
def square_of_n(n):
	return [i**2 for i in range(n)]

# print(square_of_n(20))


# decorator with both function and decorators arguments
def decorator_v3(name, *args, **kwargs):
	print('decorator_v3\'s args %s' % str(args))
	print('decorator_v3\'s kwargs %s' % str(kwargs))
	print('my decorator name is %s' % name)
	def func_decorator(func):
		b_time = datetime.now()

		def wrap(*args, **kwargs):
			print('args are %s' % str(args))
			print('kwargs are %s' % str(kwargs))
			print("Before function being called at %s" % b_time)
			func_out = func(*args, **kwargs)
			print("Total time taken for output is %s microseconds" % (datetime.now() - b_time).microseconds)
			return func_out
		return wrap
	return func_decorator


# @decorator_v3('square of numbers', "Hurrah", message='Hello All!')
# def square_of_n(n):
# 	return [i**2 for i in range(n)]

# print(square_of_n(20))


# class based decorators
class BasicDecorators:

	def __init__(self, function):
		self.function = function


	def __call__(self, *args, **kwargs):
		b_time = datetime.now()
		print("Hi! My First class based decorator!! ")
		func_out = self.function(*args, **kwargs)
		print("Hurrah! It worked too and took total time of %s us. See the output Below" % (datetime.now() - b_time).microseconds)
		return func_out


#  without argument in decorated function
@BasicDecorators
def square_of_20():
	return [i**2 for i in range(20)]

# print(square_of_20())


# Argument in decorated function
@BasicDecorators
def square_of_n(n):
	return [i**2 for i in range(n)]

# print(square_of_n(100))


# class based argumented decorators
class BasicDecorators:

	def __init__(self, function, *args, **kwargs):
		self.function = function
		self.argument = None
		print(args, kwargs)



	def __call__(self, *args, **kwargs):
		b_time = datetime.now()
		print("Hi! My First class based decorator with Arguments ( %s ) works!! " % self.argument)
		func_out = self.function(*args, **kwargs)
		print("Hurrah! It worked too and took total time of %s us. See the output Below" % (datetime.now() - b_time).microseconds)
		return func_out


# Argument in decorated function
@BasicDecorators
def square_of_n(n):
	return [i**2 for i in range(n)]

print(square_of_n(100))



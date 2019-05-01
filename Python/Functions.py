def print_two(*args):
	arg1, arg2 = args
	print(f"arg1 = {arg1} and arg2 = {arg2}")
def print_two_again(arg1,arg2):
	print(f"arg1 = {arg1} and arg2 = {arg2}")
def print_one(arg1):
	print(f"arg1 = {arg1}")
def print_none():
	print("I Got None")
print_two("Varish is number", 1)
print_two_again("Varish is number", 1)
print_one("Varish")
print_none
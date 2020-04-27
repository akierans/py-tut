#This one is like you scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")

#OK, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")

#This just takes one argument
def print_one(arg1):
	print(f"arg1: {arg1}")

#This one takes no arguments
def print_none():
	print("I got nothin'.")

print_two("Ash","Kierans")
print_two_again("Two","Again")
print_one("One")
print_none()
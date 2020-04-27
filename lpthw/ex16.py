from sys import argv

#Pulls params from commanline input
script, filename = argv

#Explains what we're going to do instructing hwow to interrupt
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

#Accepts input
#Not validated for return only!
input("?")

print("Opening the file...")
#sets target as filename
target = open(filename, 'w')

#Truncates File
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three line.")
#Accepts New input 3 lines
line1 = input("line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")
comb = f"""
{line1} \n
{line2} \n
{line3} \n
"""

print("I'm going to write these lines to the file.")

#Writes lines one at a time with a new line escape character between
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
target.write(comb)

print("And finally, we close it.")
#Closes once complete
target.close()
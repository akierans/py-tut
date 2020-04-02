from sys import argv

#Passes file name from python initiation commant
script, filename = argv

#Stores filename as a parameter of the command open insid the variable txt
txt = open(filename)

print(f"Here's your file {filename}:")
#print the output of variable txt.read()
print(txt.read())

#Repeat the process taking the filename from user.
print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt.close()
txt_again.close()
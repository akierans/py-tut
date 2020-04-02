from sys import argv
from os.path import exists

script, from_file, to_file = argv

#Explainer
print(f"Copying from {from_file} to {to_file}")

#We could do these two on one line, how?
#Opens the file from terminal
in_file = open(from_file)
#Reads the data from the file
indata = in_file.read()

#Runs methond 'len' - length on that data, and returns in a string
print(f"The input file is {len(indata)} bytes long.")

#Checks if output already exists
print(f"Does the ouput file exist? {exists(to_file)}.")

print("Ready, hit RETURN to continue, CTROL-C to abort.")
#Do you want to continue
input()

#Open (or create) output file in WRITE mode
out_file = open(to_file, 'w')
#Write the loaded data stored in indata to the file
out_file.write(indata)

print("Alright, all done.")

#Close both files
out_file.close()
in_file.close()
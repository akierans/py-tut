types_of_people = 10;
#String in String
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
#2 Strings inside string
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

#String in string
print(f"I said: {x}")

#String in string
print(f"I also said: '{y}'")

hilarious = False
#String in string
joke_evaluation = "Isn't that joke so funny!? {}"
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
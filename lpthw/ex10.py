#\t Add's a TAB
tabby_cat = "\tI'm tabbed in."
#\n Starts a new Line
persian_cat = "I'm a split\non a line."
#\\ escapes a backslash so it appears in the string

backslash_cat = "I'm \\ a \\ cat."

#\a adds a system bleep
#\N adds a Unicode symbol where name is in the {} following \N{}
fat_cat = """
I'll do a list\N{COLON}
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
\a
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
import mystuff
mystuff.apple()

print(mystuff.tangerine)

class MyStuff(object):

	def __init__(self):
		self.tangerine = "And now a thousand years between"

	def apple(self):
		print("I AM CLASSY APPLES!")


thing = MyStuff()
thing.apple()
print(thing.tangerine)


mystuff1 = {
	'apples':'I AM APPLES - PLURAL' 
}

#Dict style
print('-' * 10)
print(mystuff1['apples'])
print('-' * 10)

#Module style
mystuff.apple()
print(mystuff.tangerine)

#Class Style
thing = MyStuff()
thing.apple()
print(thing.tangerine)
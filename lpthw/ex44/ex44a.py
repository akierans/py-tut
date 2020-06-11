class Parent(object):

	def implicit(self):
		print("PARENT implicit()")

class Child(Parent):
	pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

#this will print...

#PARENT implicit()
#PARENT implicit()

#Even though Child class has no methods it calls the ones defined in Parent class.
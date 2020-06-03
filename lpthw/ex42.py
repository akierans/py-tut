##Animal is-a object (yes, sort of confusing) look at the extra credit.

class Animal(object):
	pass

## class Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		## class Dog has-a name
		self.name = name

## Class Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		## class Cat has-a name
		self.name = name

## Class Person
class Person(object):

	def __init__(self, name):
		## class Person has-a name
		self.name = name
		## class Person has-a Pet
		self.pet = None

## class Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		## class Employee has-a Name, Salary
		super(Employee, self).__init__(name)
		## class Employee has Salary
		self.salary = salary

## class Fish
class Fish(object):
	pass

## class Salmon is-a Fish
class Salmon(Fish):
	pass

## class Halibut is-a Fish
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## Mary has-a pet Satan
mary.pet = satan

## Employee is-a Person, has-a name/salary Frank 120000
frank = Employee("Frank", 120000)

## Frank has-a pet rover, Rover is-a Dog is-a Animal
frank.pet = rover

## Flipper is-a Fish
flipper = Fish()

## Crouse is-a Salmon
crouse = Salmon()

## Harry is-a Halibut
harry = Halibut()
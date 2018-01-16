#My first python file object-oriented

class firstClasse:
	pass

class Employee:

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.email = first_name + last_name + '@domain.com'


	#Create a mathod called full name
	def full_name(self):
		return '{} {}'.format(self.first_name,self.last_name)

print ("-----------------------------------------------")

emp_1 = Employee('Gabrielly', 'Andrade')

print('Name: ',emp_1.first_name)
print('Surname: ',emp_1.last_name)
print('Email: ',emp_1.email)

print ('{} {}'.format(emp_1.first_name, emp_1.last_name))

print ("-----------------------------------------------")
emp_2 = Employee('Lisa', 'Simpson')

#Print object.method
print(emp_2.full_name())
#Print object.attribute
print(emp_2.email)

print ("-----------------------------------------------")
emp_3 = Employee('Bart', 'Simpson')

#Print object.attribute
print(emp_3.full_name())
#Print class.method
print(Employee.full_name(emp_3))
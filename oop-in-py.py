# python object-oriented programming


class Employee:
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '_' + last + '@company.com'

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

emp1 = Employee('Steve', 'Harrington', 500000)

print(emp1.email)
print(emp1.fullname())
# python object-oriented programming
print("imported 'Employee'")

class Employee:
	raise_amount = 1.04
	num_of_emps = 0

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '_' + last + '@company.com'

		Employee.num_of_emps += 1

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount
	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

class Developer(Employee):
	raise_amount = 1.10

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang

dev_1 = Developer('Steve','Harrington', 55000, 'Python')
dev_2 = Developer('Test','Employee', 55000, 'Java')

print(dev_1.prog_lang)
print(dev_2.prog_lang)

# import datetime
# my_date = datetime.date(2019, 5, 17)
# print("Work day? " + str(Employee.is_workday(my_date)))
# emp1 = Employee('Steve', 'Harrington', 55000)
# emp_str_1 = 'steven-harrington-55000'
# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.email)
# print(new_emp_1.pay)
# Employee.set_raise_amt(1.05)
# print(emp1.raise_amount)
# Employee.raise_amount = 1.05
# print(emp1.raise_amount)
# emp1.apply_raise()
# print(Employee.__dict__)
# print(Employee.num_of_emps)



class student:
    def __init__(self, name, rollnumber):
        self.name = name
        self.rollnumber = rollnumber
    def display(self):
        print("name:", self.name)
        print("rollnumber:", self.rollnumber)
s1 = student("abhi", 20)
s1.display()

class student:
	def __init__(self, name, marks):
		self.name = name
		self.__marks = marks

	def get_marks(self):
		return self.__marks

	def set_marks(self, new_marks):
		if 0 <= new_marks <= 100:
			self.__marks = new_marks
		else:
			print("Invalid marks. Please enter a value between 0 and 100.")

s1 = student("alice", 85)
print(s1.name)
print(s1.get_marks())
s1.set_marks(90)
print(s1.get_marks())


#print
class A:
    def method1(self):
        print("Method 1 from class A")
    def method2(self):
        print("Method 2 from class A")
class B(A):
    def method3(self):
        print("Method 3 from class B")
b = B()
b.method1() 

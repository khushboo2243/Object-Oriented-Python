#classes aallows logially grouping of data and functions in a way that's easy to resue
#and also to build upon if need be.
#data and functions asscoaited with a specific class are called attributes and methods
#mathods-> a function associated with class

class Employee: #each employee will have specific attributes (names, email, role)
    #pass       #when you don't want to keep a class empty, write pass
    def __init__(self,first, last, pay):  #this method can be seen as initialize or a constructor. When a method is created
        self.first=first                  #inside a class they ereceive the instance as first argument. By convention, the instance
        self.last=last                #is called self.
        self.pay=pay
        self.email=first + '.'+ last +'@company.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp_1 = Employee('Corey','Schafer','5000')    #each of these employees are instances of class employee. emp_1 is passed as the self argument.
emp_2 = Employee('Test','User','6000')    #both of these employee objects have different locations in memory.

'''print(emp_1)
print(emp_2)

emp_1.first='Corey'                          #the long method of allocating values for each attribute of an instance. defininf these attributes
emp_1.last='Schafer'                          inside the class simplifies the process and lessens the amount of code.
emp_1.email='Corey.Schafer@company.com'
emp_1.pay= 5000

emp_2.first='Test'             
emp_2.last='User'
emp_2.email='Test.User@company.com'
emp_2.pay= 6000'''

print(emp_1.email)
print(emp_2.email)
print (emp_1.fullname())                   #when a method fir full name is defined inside the class.
#print('{} {}'.format(emp_1.first,emp_1.last))  #when a method is not present for full name.

print(Employee.fullname(emp_1))

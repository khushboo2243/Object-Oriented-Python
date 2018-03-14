#Special methods

class Employee: 
    num_of_emps=0
    raise_amount=1.04                   
    def __init__(self,first, last, pay):  #methods surrounded by two underscores (dunder methods) are a set of predefined methods 
        self.first=first                  #can be used to enrich classes. __init__ is one example.
        self.last=last                
        self.pay=pay
        self.email=first + '.'+ last +'@company.com'
        Employee.num_of_emps +=1    #using a class to access this class variable because we don't want this variable to give different values at any time.
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) #class_variables are supposed to be accessed through the class or through instance

    def __repr__(self):
        return "Employee({}, {}, {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} = {}'.format(self.fullname(),self.email)

    def __add__(self,other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

#print(emp_1)

#repr and str special methods resolves printing problems related to Employee instance
# They take off this statement which appears otherwise on the shell: <__main__.Employee object at 0x000001E2FF5E1198>

#print(repr(emp_1)) #this is a direct call to repr and str methods.
#print(str(emp_1))

print(emp_1.__repr__())  #this is the call to repr and str defined under the class
print(emp_1.__str__())

#application of dunder add method.
print(emp_1 +emp_2)

#application of dunder len method
print((len(emp_1)))


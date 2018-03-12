#Class variables are different from instance variable in a manner that they should
#remain same for all the instances. For eg: appraisal rates
class Employee: #each employee will have specific attributes (names, email, role)
    num_of_emps=0
    raise_amount=1.04                     #class variables
    def __init__(self,first, last, pay):  
        self.first=first                  
        self.last=last                
        self.pay=pay
        self.email=first + '.'+ last +'@company.com'
        Employee.num_of_emps +=1    #using a class to access this class variable because we don't want this variable to give different values at any time.
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) #class_variables are supposed to be accessed through the class or through instance

emp_1 = Employee('Corey','Schafer','5000')    
emp_2 = Employee('Test','User','6000')    


#testing class variables
print(emp_1.raise_amount)
print(Employee.raise_amount)        #the value of raise_amount printed here is the class variable  
print(emp_2.raise_amount)

print(Employee.__dict__)

emp_1.raise_amount=1.05              # this will change raise_Amount for only emp_1

print(emp_1.raise_amount)

print(Employee.num_of_emps)

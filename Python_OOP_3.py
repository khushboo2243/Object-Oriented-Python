#class methods take the class as first instance as opposed to regular methods which take
#instance as the first method. In order to turn a regular method to a class method, a decorator
#has to be added at the top of this method, @classmethod.
#class methoda can also be used as alternative constructors (example included in the code)
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

    @classmethod
    def set_raise_amt(cls, amount): #cls specifies class. cannot use "class" because its a 
        cls.raise_amount=amount                            #keyword to create classes.

    @classmethod
    def from_string(cls,emp_str):     #this serves as an alternative constructor which will help split the string based on hyphen as a delimiter
        first, last, pay = emp_str.split('-') 
        return cls(first, last, pay)  #returning a new employee object


emp_1 = Employee('Corey','Schafer','5000')    
emp_2 = Employee('Test','User','6000')    

#testing class method
Employee.set_raise_amt(1.05) #calling the class method which allocates new value of raise amnt
emp_1.set_raise_amt(1.05) #using the class method through instance works the same way but is not recommended.
print(emp_2.raise_amount)

#testing alternative constructor

emp_str_1= 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'

new_emp_1 = Employee.from_string(emp_str_1)  #splits te strings on the basis of hyphens

print(new_emp_1.email)        #it's visible how values are split in the input string





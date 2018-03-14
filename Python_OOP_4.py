#static methods do not pass any instance or class as the first argument.
#They are announced with a decorator @staticmethod

class Employee: 
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

    @staticmethod           #the static method will check if a given weekday is a holiday or not
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6: #the inbuilt weekday method of Python allocates
            return False                                #numbers to each of the days, Monday=0 and so on
        return True

emp_1 = Employee('Corey','Schafer','5000')    
emp_2 = Employee('Test','User','6000')    


#testing the static method

import datetime
my_date = datetime.date(2017,9,10)

print(Employee.is_workday(my_date))



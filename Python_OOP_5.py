#inheritance allows inheriting attributes and methods from the parent class.
#By creating subclasses, all the functionality from the parent class can be used
#or overriden without changing information in the parent class.
#Basically, inheritance allows resuing the code.

class Employee: 
    num_of_emps=0
    raise_amount=1.04                   
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


class Developer(Employee):  
    raise_amount=1.10        #the developer class will have it's own raise amount and the instance
                             #of this class will have the raise amount of 10%
    def __init__(self,first, last, pay, prog_lang):  #developer's own init method to add prog_language
        super().__init__(first, last, pay)            # super.init() supplies first, last and pay to Developer's
        self.prog_lang=prog_lang

class Manager(Employee):
    def __init__(self,first, last, pay, employees=None): # a new argument, list of employees is added, with default value=None
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []    #set the employee list to an empty list if argument is not provided
        else:
            self.employees = employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Corey','Schafer','5000','Python')  
dev_2 = Developer('Test','User','6000','Java')

print(dev_1.email)       
print(dev_2.email)

#tests newly added raise amount specifically for Developers.
print(dev_1.raise_amount)

'''when an instance is created for class Developer, first the program tries tofind init method
inside Developer. Since, there is no init inside Developer, python follows the inheritance chain
upwards. This chain is called method resolution order'''

#test newly added argument, programming language.
print(dev_1.prog_lang)
print(dev_2.prog_lang)

#testing lists of employees

mgr_1 = Manager('Sue','Smith',90000, [])

print(mgr_1.email)
mgr_1.print_emps()

mgr_1.add_emp(dev_2)   #check adding the employee function
mgr_1.add_emp(dev_1)   
mgr_1.print_emps()
mgr_1.remove_emp(dev_2) #check removal function
print("\nnew list after removal of employee")
mgr_1.print_emps()

#testing isinstance() function

print(isinstance(mgr_1,Manager))    #check whether, mgr_1 is an instance of Manager, Developer and Employee 
print(isinstance(mgr_1,Employee))
print(isinstance(mgr_1,Developer))

#testing issubclass() function
print(issubclass(Manager,Employee))
print(issubclass(Developer,Employee)) #check whether, Developer and Manager are an instance Employee
print(issubclass(Manager,Developer))

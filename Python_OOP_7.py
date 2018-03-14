#Property decorator acts as a getter or setter.

class Employee: 
    num_of_emps=0
    raise_amount=1.04                   
    def __init__(self,first, last):  #methods surrounded by two underscores (dunder methods) are a set of predefined methods 
        self.first=first                  #can be used to enrich classes. __init__ is one example.
        self.last=last                
        
    @property                  #after using @property, the fullname cannot be set using a command
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @fullname.setter          #setter helps fullname taking a new value from the user
    def fullname(self,name):
        first, last= name.split(' ')
        self.first = first
        self.last= last

    @fullname.deleter          
    def fullname(self):
        print("Delete name!")
        self.first = None
        self.last= None
    @property
    def email(self):                 # a new email method so that the email gets updated with any changes in the name
        return '{}.{}@email.com'.format(self.first,self.last)



emp_1= Employee('John','Smith')
emp_1.fullname='Corey Schafer'   #this works because of @fullname.setter

#del emp_1.fullname     #uncomment to test deleter function

#print(emp_1.email())

#testing the change of name causing change of email as well

#emp_1.first= 'Jim'
#print(emp_1.email()) #email is being called in form of a function

#testing after adding @property
print(emp_1.email)

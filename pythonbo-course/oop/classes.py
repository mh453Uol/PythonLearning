students = []
countIndex = 0

class Student:
# python classes first letter uppercase 
# python function and variable lowercase

    # This is a class attribute (static) every 
    # class get one of these however not shared 
    # across classes
    school_name = "Elmhurst"

    #constructor (initialization)
    # self like this you dont have to pass
    def __init__(self,name,id = 1):
        # countIndex = countIndex + 1 # this would create a
        # variable in the function scope this is because 
        # python thinks we are assigning a variable 
        # since to assign all you do it write variable name

        if id == 1:
            # To tell python we mean global we do
            global countIndex
            countIndex = countIndex + 1
            self.id = countIndex # This makes a instance attribute
        else:
            self.id = countIndex # This makes a instance attribute
        
        students.append(self)
        self.name = name

    # override toString
    def __str__(self):
        return "Name:{0} and Id:{1}".format(self.name,self.id)

print(Student.school_name) # weird prints Elmhurst  
# class attribute dont care about instance 

#print(Student("Majid"))
#print(Student("John"))




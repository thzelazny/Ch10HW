
class Employee:
    def __init__(self,empname,empid,empdept,emptitle,empsalary):
        self.__empname=empname
        self.__empid=empid
        self.__empdept=empdept
        self.__emptitle=emptitle
        self.__empsalary=empsalary

    def return_empname(self):
        return self.__empname
    #def give_empname(self,empname):
        #self.__empname=empname

    def return_empid(self):
        return self.__empid

    #def give_empid(self,empid):
        #self.__empid=empid
    
    def return_empdept(self):
        return self.__empdept
    
    #def give_empdept(self,empdept):
        self.__empdept=empdept
    
    def return_emptitle(self):
        return self.__emptitle
    
    #def give_emptitle(self,emptitle):
        self.__emptitle=emptitle
    
    def return_empsalary(self):
        return self.__empsalary
    
    #def give_empsalary(self,empsalary):
        self.__empsalary=empsalary
    
#emp=Employee("Thomas Zelazny",892555575,"MIS","Coder",8900)
#print("Employee Name: ",emp.return_empname())
#print("Employee ID: ",emp.return_empid())
#print("Employee Dept: ",emp.return_empdept())
#print("Employee Title: ",emp.return_emptitle())
#print("Employee Salary: $",emp.return_empsalary())
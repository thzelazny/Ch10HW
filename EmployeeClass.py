
class Employee:
    def __init__(self,empname,empid,empdept,emptitle,empsalary):
        self.__empname=empname
        self.__empid=empid
        self.__empdept=empdept
        self.__emptitle=emptitle
        self.__empsalary=empsalary

    def return_empname(self):
        return self.__empname

    def return_empid(self):
        return self.__empid

    
    def return_empdept(self):
        return self.__empdept
    
    
    def return_emptitle(self):
        return self.__emptitle
    
    
    def return_empsalary(self):
        return self.__empsalary
    
    
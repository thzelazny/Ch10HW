class PayrollDeduction:
    def __init__(self,p_description,p_date,p_charge,p_empid):
        self.__p_description=p_description
        self.__p_date=p_date
        self.__p_charge=p_charge
        self.__p_empid=p_empid

    def return_description(self):
        return self.__p_description
    
    def return_p_date(self):
        return self.__p_date
    
    def return_p_charge(self):
        return self.__p_charge
    
    def return_p_empid(self):
        return self.__p_empid
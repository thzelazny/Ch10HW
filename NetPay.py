
import EmployeeClass as e
import PayrollDeductionClass as p
emp= e.Employee("Jimmy Smith",58475,"Information Systems","Developer",6800)

ded_1=p.PayrollDeduction("food court","8/14/2022",22.50,39119)
ded_2=p.PayrollDeduction("gift contribution","8/12/2022",25.00,58475)
ded_3=p.PayrollDeduction("food court","8/17/2022",15.25,21547)
ded_4=p.PayrollDeduction("vending machine","8/22/2022",3.00,58475)
ded_5=p.PayrollDeduction("vending machine","8/5/2022",2.75,58475)

print("**Employee Pay**")
print("Name:",emp.return_empname())
print("ID Number:",emp.return_empid())
print("Department:",emp.return_empdept())
print("Gross Pay: $",float(emp.return_empsalary()),sep='')
print("Net Pay: $",emp.return_empsalary()-ded_2.return_p_charge()-ded_4.return_p_charge()-ded_5.return_p_charge(),sep='')


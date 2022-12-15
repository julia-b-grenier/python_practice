class Employee:
    annual_salary = 12000
    
    def __init__(self, id1, name):
        self.id1 = id1
        self.name = name
        
    @classmethod
    def salary(cls):
        return round(cls.annual_salary/12,2)
    
    
class HourlyEmployee(Employee):
    def __init__(self, id1, name, hours_worked_in_month, hourly_rate):
        super().__init__(id1, name)
        self.hours_month = hours_worked_in_month
        self.hourly_rate = hourly_rate
        
    def salary(self):
        return round(self.hours_month*self.hourly_rate,2)
    
    
class PayrollSystem():
    @staticmethod
    def calc_payroll(l_employees):
        for e in l_employees:
            s =[str(e.id1),e.name,str(e.salary())]
            print(" ".join(s))

employee = Employee(1, 'John Smith')
hourly_employee = HourlyEmployee(2, 'Jane Doe', 40, 20)
payroll_system = PayrollSystem()
payroll_system.calc_payroll([employee, hourly_employee])
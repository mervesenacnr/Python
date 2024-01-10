class Employee:
    def __init__(self, name, last, age, pay):
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay

emp_1 = Employee("James", "Hughes", "32", 5000)
emp_2 = Employee("Charlie", "Brown", "22", 3000)

print(emp_1.__dict__,"\n",emp_2.__dict__)

"""
Instance Variable: Class'tan yaratılan objelerin kendilerine özgün değişkenleridir.
Class Variable: Class'tan yaratılan tüm objelerde paylaşılan değişkenlerdir.
* Instance variable her obje için farklı olabilir ama class variable hepsi için aynı olmak zorundadır.
"""

class Employee2:
    raise_percent = 1.05

    def __init__(self, name, last, age, pay):
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay

    def apply_raise(self):
        self.pay = self.pay * self.raise_percent

emp_3 = Employee2("Merve", "Çınar", "22", 1000)
print(emp_3.__dict__)
emp_3.apply_raise()
print(emp_3.__dict__)


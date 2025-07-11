#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

class EmployeeManager:
    def __init__(self, data_file='employee_data.txt'):
        self.data_file = data_file
        self.employees = []
        self.load_employees()

    def load_employees(self):
        if not os.path.exists(self.data_file):
            return
        with open(self.data_file, 'r') as f:
            for line in f:
                if line.strip():
                    self.employees.append(Employee.from_line(line))

    def save_employees(self):
        with open(self.data_file, 'w') as f:
            for emp in self.employees:
                f.write(emp.to_line())

    def add_employee(self):
        try:
            name = input("Enter Name: ").strip()
            dept = input("Enter Department: ").strip()
            salary = float(input("Enter Salary: "))
            year = int(input("Enter Joining Year: "))
            new_emp = Employee(name, dept, salary, year)
            self.employees.append(new_emp)
            print("✅ Employee added successfully.\n")
        except ValueError:
            print("❌ Invalid input. Please enter correct data types.\n")

    def list_employees(self):
        if not self.employees:
            print("No employees found.")
            return
        for emp in self.employees:
            emp.display()

    def search_employee(self, term):
        term = term.lower()
        results = list(filter(lambda emp: term in emp.name.lower() or term in emp.department.lower(), self.employees))
        if not results:
            print("No matching employees found.")
        for emp in results:
            emp.display()

    def sort_by_salary(self, desc=False):
        self.employees.sort(key=lambda emp: emp.salary, reverse=desc)
        print("Sorted by salary " + ("(descending):" if desc else "(ascending):"))
        self.list_employees()

    def generate_report(self, report_file='employee_report.txt'):
        total = len(self.employees)
        avg_salary = sum(emp.salary for emp in self.employees) / total if total else 0
        with open(report_file, 'w') as f:
            f.write(f"Employee Summary Report\n")
            f.write(f"-----------------------\n")
            f.write(f"Total Employees: {total}\n")
            f.write(f"Average Salary: Rs.{avg_salary:.2f}\n\n")
            f.write("List of Employees:\n")
            for emp in self.employees:
                f.write(f"{emp.name} ({emp.department}) - Rs.{emp.salary:.2f} - Joined: {emp.joining_year}\n")
        print("📄 Report generated as 'employee_report.txt'\n")


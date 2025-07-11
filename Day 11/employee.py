#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Employee:
    def __init__(self, name, department, salary, joining_year):
        self.name = name
        self.department = department
        self.salary = float(salary)
        self.joining_year = int(joining_year)

    def display(self):
        print(f"Name: {self.name}, Department: {self.department}, "
              f"Salary: Rs.{self.salary:.2f}, Joining Year: {self.joining_year}")

    def to_line(self):
        return f"{self.name},{self.department},{self.salary},{self.joining_year}\n"

    def from_line(line):
        name, dept, sal, year = line.strip().split(',')
        return Employee(name, dept, float(sal), int(year))


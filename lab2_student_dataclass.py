'''
Create a Student dataclass

It should include a name(float), college id(int), 
and GPA(float)

create a main function to test

use comments to compare data class vs regular class
'''


import dataclasses

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    college_id: int
    gpa: float 

def Main():
    sam = Student('Sam', 1135669, 24.5)
    

    print(sam)

Main()

#Traditional

# class Student:
#     def __init__(self, name, college_id, gpa):
#         self.name = name
#         self.college_id = college_id
#         self.gpa = gpa
#     def __str__(self):
#         return f'Name: {self.name}, ID: {self.college_id}, GPA: {self.gpa}'
# def main():
#     sam = Student('Sam', 1135669, 25.6)
#     print(sam)

# main()




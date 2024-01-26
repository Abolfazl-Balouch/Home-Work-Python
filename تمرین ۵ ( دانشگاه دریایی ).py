# -*- coding: utf-8 -*-
"""Untitled47.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FIpAWdfaSoBpwcWhepzOzEZcKvfqIXYY
"""

import re

class University:
    current_menu = 'log in/sign up menu'

    def __init__(self):
        pass

    def sign_up(self, user_type, user_id, user_name, user_password):
        if user_type == 'S':
            student = Student(user_type, user_id, user_name, user_password)
        elif user_type == 'P':
            professor = Professor(user_type, user_id, user_name, user_password)
        else:
            output.append('invalid type')

    def log_in(self, user_id, user_password):
        try:
            if Person.people[int(user_id)].password == user_password:
                output.append("logged in successfully!")
                if Person.people[int(user_id)].type == 'P':
                    output.append('entered professor menu')
                    University.current_menu = 'professor menu'
                else:
                    output.append('entered student menu')
                    University.current_menu = 'student menu'
                Person.people[int(user_id)].logged_in = True
            else:
                output.append('incorrect password')
        except:
            output.append('incorrect id')

    def course_list(self):
        output.append('course list:')
        for course in Course.courses.values():
            output.append(f'{course.id} {course.name} {course.current_num}/{course.capacity}')


output = list()


class Person:
    people = dict()

    def __init__(self, user_id, user_name, user_password):
        a = 0
        try:
            self.id = int(user_id)
        except:
            output.append('invalid id')
            a = 1
        if len(re.findall('[ ]+', user_name)) == 0:
            self.name = user_name
        elif a == 0:
            output.append('invalid name')
            a = 1
        if (
            len(user_password) >= 4
            and len(re.findall('[ ]+', user_password)) == 0
            and len(re.findall('[*.!@$%^&()]+', user_password)) != 0
        ):
            self.password = user_password
        elif a == 0:
            output.append('invalid password')
            a = 1
        if a == 0:
            try:
                b = Person.people[self.id]
                output.append('id already exists')
            except:
                output.append('signed up successfully!')
                self.logged_in = False
                Person.people[self.id] = self


class Course:
    courses = dict()

    def __init__(self, course_id, course_name, course_capacity):
        a = 0
        if len(re.findall('[ ]+', course_name)) == 0:
            self.name = course_name
        else:
            output.append('invalid course name')
            a = 1
        if a == 0:
            try:
                self.id = int(course_id)
            except:
                output.append("invalid course id")
                a = 1
        if a == 0:
            try:
                self.capacity = int(course_capacity)
            except:
                output.append("invalid course capacity")
                a = 1
        if a == 0:
            try:
                b = Course.courses[self.id]
                output.append("course id already exists")
                a = 1
            except:
                pass
        if a == 0:
            output.append('course added successfully!')
            self.current_num = 0
            Course.courses[self.id] = self


class Student(Person):
    def __init__(self, user_type, user_id, user_name, user_password):
        super().__init__(user_id, user_name, user_password)
        self.type = user_type
        self.courses = list()

    def get_course(self, course_id):
        try:
            if Course.courses[int(course_id)] not in self.courses:
                if Course.courses[int(course_id)].current_num != Course.courses[
                    int(course_id)
                ].capacity:
                    self.courses.append(Course.courses[int(course_id)])
                    Course.courses[int(course_id)].current_num += 1
                    output.append('course added successfully!')
                else:
                    output.append("course is full")
            else:
                output.append("you already have this course")
        except:
            output.append('incorrect course id')


class Professor(Person):
    def __init__(self, user_type, user_id, user_name, user_password):
        super().__init__(user_id, user_name, user_password)
        self.type = user_type

    def add_course(self, course_id, course_name, course_capacity):
        course = Course(course_id, course_name, course_capacity)
        self.course = course


university = University()

while True:
    user_input = input().strip()

    if user_input.split()[0] != 'edu' or user_input.split()[-1] != 'edu':
        output.append('invalid command')
    elif re.search(r'\s{2,}', user_input):
        output.append('invalid command')
    else:
        if user_input.split()[1] == 'exit':
            break
        elif user_input.split()[1] == 'log' and user_input.split()[2] == 'in':
            pattern = r'-i\s+((?:[^-]+))\s+-p\s+((?:[^-]+))'
            match = re.search(pattern, user_input)
            if match:
                user_id = match.group(1).strip()
                user_password = match.group(2)[0:-4].strip()
                university.log_in(user_id=user_id, user_password=user_password)
            else:
                output.append('invalid command')
        elif user_input.split()[1] == 'sign':
            pattern = r'(-.\s)+-i\s+((?:[^-]+))\s+-n\s+((?:[^-]+))\s+-p\s+((?:[^-]+(?:\s+[^-]+)*))'
            match = re.search(pattern, user_input)
            if match:
                user_type = match.group(1)[1]
                user_id = match.group(2).strip()
                user_name = match.group(3).strip()
                user_password = match.group(4)[0:-4].strip()
                university.sign_up(
                    user_type=user_type,
                    user_id=user_id,
                    user_name=user_name,
                    user_password=user_password,
                )
            else:
                output.append('invalid command')
        elif user_input.split()[1] == 'add':
            if University.current_menu == 'professor menu':
                pattern = r'-c\s+((?:[^-]+))\s+-i\s+((?:[^-]+))\s+-n\s+((?:[^-]+(?:\s+[^-]+)*))'
                match = re.search(pattern, user_input)
                if match:
                    course_name = match.group(1).strip()
                    course_id = match.group(2).strip()
                    course_capacity = match.group(3)[0:-4].strip()
                    course = Course(course_id=course_id, course_name=course_name, course_capacity=course_capacity)
                else:
                    output.append('invalid command')
            else:
                output.append('invalid command')
        elif user_input.split()[1] == 'log':
            if University.current_menu != 'log in/sign up menu':
                for person in Person.people.values():
                    if person.logged_in:
                        person.logged_in = False
                        break
                output.append("logged out successfully!")
                output.append('entered log in/sign up menu')
                University.current_menu = 'log in/sign up menu'
            else:
                output.append('invalid command')
        elif (
            user_input.split()[1] == 'show'
            and user_input.split()[2] == 'course'
            and (University.current_menu == 'student menu' or University.current_menu == 'professor menu')
        ):
            university.course_list()
        elif user_input.split()[1] == 'get':
            if user_input.split()[3] == '-i':
                if University.current_menu == 'student menu':
                    for person in Person.people.values():
                        if person.logged_in:
                            person.get_course(user_input.split()[4])
                else:
                    output.append('invalid command')
            else:
                output.append('invalid command')
        elif user_input.split()[1] == 'current':
            output.append(University.current_menu)
        else:
            output.append('invalid command')

for i in output:
    print(i)
# -*- coding: utf-8 -*-
"""Untitled36.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hi86SE7l_rCuD58ukCESlFihwa5lEoPM
"""

class Patient:
    patients = list()
    output = list()
    full_times = list()
    visit_list = list()

    def __init__(self, id, name, family_name, age, height, weight):
        try:
            if age < 0:
                Patient.output.append('error: invalid age')
                raise NameError
            if height < 0:
                Patient.output.append('error: invalid height')
                raise NameError
            if weight < 0:
                Patient.output.append('error: invalid weight')
                raise NameError
            for patient in Patient.patients:
                if id == patient.id:
                    Patient.output.append("error: this ID already exists")
                    raise NameError
            self.id = id
            self.name = name
            self.family_name = family_name
            self.age = age
            self.height = height
            self.weight = weight
            Patient.patients.append(self)
            Patient.output.append("patient added successfully")
        except NameError:
            pass

    @staticmethod
    def display_id(id):
        flag = False
        for patient in Patient.patients:
            if id == patient.id:
                Patient.output.append(f'patient name: {patient.name}')
                Patient.output.append(f"patient family name: {patient.family_name}")
                Patient.output.append(f"patient age: {patient.age}")
                Patient.output.append(f"patient height: {patient.height}")
                Patient.output.append(f"patient weight: {patient.weight}")
                flag = True
                break
        if not flag:
            Patient.output.append('error: invalid ID')

    @staticmethod
    def delete_patient(id):
        flag = False
        for patient in Patient.patients:
            if id == patient.id:
                Patient.patients.remove(patient)
                Patient.output.append("patient deleted successfully!")
                vv = Patient.visit_list.copy()
                for tple in vv:
                    if tple[0].id == id:
                        Patient.visit_list.remove(tple)
                flag = True
                break
        if not flag:
            Patient.output.append('error: invalid id')

    @staticmethod
    def add_visit(id, beginning_time):
        flag = False
        for patient in Patient.patients:
            if id == patient.id:
                flag = True
                if beginning_time not in Patient.full_times:
                    if 9 <= beginning_time <= 18:
                        Patient.full_times.append(beginning_time)
                        Patient.output.append("visit added successfully!")
                        Patient.visit_list.append((patient, beginning_time))
                        break
                    else:
                        Patient.output.append("error: invalid time")
                else:
                    Patient.output.append("error: busy time")
                    break
        if not flag:
            Patient.output.append('error: invalid id')

    @staticmethod
    def display_visit_list():
        Patient.output.append("SCHEDULE:")
        for tple in Patient.visit_list:
            patient = tple[0]
            Patient.output.append(f"{tple[1]}:00 {patient.name} {patient.family_name}")


while True:
    x = input().split()
    if len(x) > 0:
        if x[0] == 'add' and x[1] == 'patient':
            p = Patient(int(x[2]), x[3], x[4], int(x[5]), int(x[6]), int(x[7]))
        elif x[0] == 'display' and x[1] == 'patient':
            Patient.display_id(int(x[2]))
        elif x[0] == 'exit':
            break
        elif x[0] == 'add' and x[1] == 'visit':
            Patient.add_visit(int(x[2]), beginning_time=int(x[3]))
        elif x[0] == 'display' and x[1] == 'visit':
            Patient.display_visit_list()
        elif x[0] == 'delete':
            Patient.delete_patient(int(x[2]))
        else:
            Patient.output.append('invalid command')
    else:
        Patient.output.append('invalid command')

for i in Patient.output:
    print(i)
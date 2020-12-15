# Team KOCY -- William Yin, Liam Kronman, Jason Chan, Stella Oh
# SoftDev
# K16 -- No Trouble
# 2020-12-14

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


courses_csv = open("courses.csv")
students_csv = open("students.csv")

courses_reader = csv.DictReader(courses_csv)
students_reader = csv.DictReader(students_csv)

# Tried to avoid hardcoding the column names but it became too complicated.
# created = False
# for row in courses_reader:
#     columns = list(row.keys())
#     if not created:
#         column_string = ", ".join(columns)
#         command = "create table courses (" + column_string + ");"
#         c.execute(command)
#         created = True
#
#     insertion_string = ""
#     for column in columns:

courses_create_command = "create table courses (code text, mark integer, id integer);"          # test SQL stmt in sqlite3 shell, save as string
c.execute(courses_create_command)    # run SQL statement

for row in courses_reader:
    insert_command = "insert into courses (code, mark, id) values ('" + row['code'] + "', " + row['mark'] + ", " + row['id'] + ");"
    c.execute(insert_command)

students_create_command = "create table students (name text, age integer, id integer);"          # test SQL stmt in sqlite3 shell, save as string
c.execute(students_create_command)    # run SQL statement

for row in students_reader:
    insert_command = "insert into students (name, age, id) values ('" + row['name'] + "', " + row['age'] + ", " + row['id'] + ");"
    c.execute(insert_command)

courses_csv.close()
students_csv.close()

#==========================================================

db.commit() #save changes
db.close()  #close database

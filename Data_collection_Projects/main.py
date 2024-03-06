# Establishing the connection to database using sql
import mysql.connector as  conn
# Entering the hsot , user and passwd to connect
my_data_base = conn.connect(host="localhost",user='root',passwd='root')

my_data_base # name of the variable of connector of data base 
'''
when ever we need the data base we need to connect to call it

'''
print("Data Base Connection is SuccessFull")
my_cursor = my_data_base.cursor() # establishing cursor as my_cursor

my_cursor.execute("show databases")
print("Now it is showing my all Data-Bases present on my local Host")
print(my_cursor.fetchall())
# my_cursor.execute("Create database student-data")
# my_cursor.execute("Show databases")
# print("Again")
# print(my_cursor.fetchall())

# the above is commented beacuse the database has been created


# Name , email and Age as input to 
name = input("Enter your name : ")
email = input("Enter your Email id : ")
age =  int(input("Enter Your Age : "))
my_cursor.execute('use student_data')

print("We are using the databse : ","student_data")

# creating table in the same database

# my_cursor.execute('create table student_data.table1(Name varchar(30),Email-id varchar(56),age int(3))') it is showing error 

#Create a Database
import sqlite3

#Create a connnection or create a new database if one does not exist
conn = sqlite3.connect('employee.db')

#create a cursor object
cur = conn.cursor()

#Create a Table
create_table = """
            CREATE TABLE employees(
            emp_id integer PRIMARY,
            f_name text,
            l_name test,
            job_title test,
            )

"""

#excute create table statement
cur.execute(create_table)

print('Table has been created')

#commit changes to the database
conn.commit()

#close connection
conn.close()
import sqlite3
import sys

def create_table_employees():
    c.execute("""CREATE TABLE IF NOT EXISTS employees (
                  first TEXT,
                  last TEXT,
                  pay INTEGER
                  )""")

def interface():
    print('''Choose option:
         1 - Input employee data
         2 - Select data from employees
         3 - Quit
         ''')
    user_input = int(input())
    if user_input == 1:
        print('Enter employee\'s first name: ')
        f_name = input()
        print('Enter employee\'s last name: ')
        l_name = input()
        print('Enter employee\'s salary: ')
        salary = int(input())
        input_query(f_name, l_name, salary)
        
    elif user_input == 2:
        cols = {
            'first_name': 'first',
            'last_name': 'last',
            'salary': 'pay',
            'all': '*'
            }
        column_name = ''
        while column_name not in cols.keys():
            print('Enter name of column("first_name", "last_name", "salary" or "all"): ')
            column_name = input()
            if column_name not in cols.keys():
                print('There is no such column. Try again.')
        print('Enter condition(e.g.: "last_name IS \"Smith\" or "salary < 100000"): ')
        user_condition = input()
        lst = user_condition.split()
        i = 0
        while i < len(lst):
            if lst[i] in cols.keys():
                lst[i] = cols[lst[i]]    
            i += 1
        user_condition = ' '.join(lst)       
        response = select_query(cols[column_name], user_condition)
        print_data(response)
    elif user_input == 3:
        print('Bye-bye!')
        conn.close()
        sys.exit()
    else:
        print('Not a valid choice!')

def input_query(first, last, pay):
    command = f'INSERT INTO employees VALUES (\'{first}\', \'{last}\', {pay})'
    c.execute(command)
    conn.commit()
    print('Employee data succesfully inserted.')

def select_query(column,condition):
    command = f'SELECT {column} FROM employees WHERE {condition}'
    c.execute(command)
    print('Employee data succesfully selected.')
    data = c.fetchall()
    return data

def print_data(data):
    if data != None:
        if type(data) == tuple :
            print(data)
        elif type(data) == list :
            for item in data:
                print(item)
    else:
        print('Data not found!')
    print('-' * 30)
    print()
    
    

conn = sqlite3.connect('employee.db')   
c = conn.cursor()   

create_table_employees()




while True:
    interface()


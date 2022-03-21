# Sindri Snaer Gunnarsson
# 12-03-22
# Collates data from employee and company files and displays it
# Some code and ideas borrowed from open-office session on Friday 2022-03-11
import csv

STAFF_LEVELS = '1'
EMPLOYEES = '2'
QUIT = 'Q'
SELECTION_TEXT = f"""Select option:
{STAFF_LEVELS}: Show staff levels
{EMPLOYEES}: Show employees
{QUIT}: Quit
Selection: """
DAYS_TEXT = '|1234567'
BARRIER = '--------'


def get_info(company):
    """Takes company info and splits it into name and planning days,
    checks if company name is valid"""
    try:
        company_info = open(company + '_info.txt', 'r')
        comp_name = company_info.readline().strip()
        planning_days = int(company_info.readline().split(':')[-1])
        company_info.close()
    except FileNotFoundError:
        print('Invalid filename')
        raise SystemExit
    return comp_name, planning_days


def employee_info(company, planning_days):
    """Takes the employee file and collates it into a dictionary"""
    normal_file = open(company + '_employees.csv', 'r')
    employee_csv = csv.DictReader(normal_file, delimiter=';')
    employees_dict = {}
    for item in employee_csv:
        employees_dict[item['ID']] = {
            'Name': item['Name'],
            'Address': item['Address'],
            'Schedule': [0 for _ in range(planning_days)]
            }
    normal_file.close()
    return employees_dict


def company_schedule(company, planning_days):
    """Fills in the schedule for each employee and counts how
    many people are working each day, returns updated employee
    dictionary and list with schedule info"""
    emp_dict = employee_info(company, planning_days)
    normal_file = open(company + '_schedule.csv', 'r')
    schedule_csv = csv.DictReader(normal_file, delimiter=';')
    staff = [0 for _ in range(planning_days)]
    for item in schedule_csv:
        if int(item['Duty']) == 1:
            emp_dict[item['EmpID']]['Schedule'][int(item['Day'])] = 1
            staff[int(item['Day'])] += 1
    normal_file.close()
    return emp_dict, staff


def print_barrier_and_days(planning_days):
    """Prints barrier marked with '-' and the weekdays from 1 to 7
    separated by |"""
    for _ in range(int(planning_days / 7)):
        print(BARRIER, end='')
    print()
    for _ in range(int(planning_days / 7)):
        print(DAYS_TEXT, end='')
    print()


def print_whole_schedule(planning_days, comp_name, staff_schedule):
    """Prints out the company staff schedule for the timeframe
    where X marks an employee at work that day"""
    print(f'\n{comp_name}')
    for row in range(max(staff_schedule), 0, -1):
        for i in range(planning_days):
            if i % 7 == 0:
                print('|', end='')
            if staff_schedule[i] >= row:
                print('X', end='')
            else:
                print(' ', end='')
        print()
    print_barrier_and_days(planning_days)


def print_employee_schedule(planning_days, staff_id, emp_dict):
    """Prints out the employee's schedule for the timeframe"""
    print(f'{emp_dict[staff_id]["Name"]} ({emp_dict[staff_id]["Address"]})')
    for i in range(planning_days):
        if i % 7 == 0:
            print('|', end='')
        if emp_dict[staff_id]['Schedule'][i] == 0:
            print(' ', end='')
        else:
            print('X', end='')
    print()
    print_barrier_and_days(planning_days)


def print_employee_list(emp_dict):
    """Prints list of employees sorted by ID's in the format
    'ID: Name - Address'"""
    print('\nEmployees:')
    for emp_id, emp in sorted(emp_dict.items()):
        print(f'{emp_id}: {emp["Name"]} - {emp["Address"]}')


# --------- Main -----------

company_name = input('Filename: \n')
name, days = get_info(company_name)
employees, staffing = company_schedule(company_name, days)

selection = input(SELECTION_TEXT)
while selection != QUIT:
    if selection == STAFF_LEVELS:
        print_whole_schedule(days, name, staffing)
    elif selection == EMPLOYEES:
        print_employee_list(employees)
        employee_id = input('Employee Id: \n')
        if employee_id in employees:
            print_employee_schedule(days, employee_id, employees)
        else:
            print('Employee not found')
    selection = input(SELECTION_TEXT)

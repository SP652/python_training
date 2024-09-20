import sqlite3

class Employee:
    def __init__(self, employee_id, employee_name, employee_salary, designation, department):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.employee_salary = employee_salary
        self.designation = designation
        self.department = department

    def save_to_db(self):
        conn = sqlite3.connect('airline_management.db')
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO employees (employee_id, employee_name, employee_salary, designation, department) VALUES (?, ?, ?, ?, ?)",
                       (self.employee_id, self.employee_name, self.employee_salary, self.designation, self.department))
        conn.commit()
        conn.close()

    @staticmethod
    def display_employees():
        conn = sqlite3.connect('airline_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()
        conn.close()

        print("\n--- Employee Details ---")
        for emp in employees:
            print(f"ID: {emp[0]}, Name: {emp[1]}, Salary: {emp[2]}, Designation: {emp[3]}, Department: {emp[4]}")
        print("------------------------")

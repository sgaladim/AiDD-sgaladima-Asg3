import csv
from employee import Employee

def load_employees(filename="employee_data.csv"):
    employees = []
    with open(filename, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            emp = Employee(
                int(row["id"]),
                row["fname"],
                row["lname"],
                row["department"],
                row["phNumber"]
            )
            employees.append(emp)
    return employees

def save_employees(employees, filename="employee_data.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["id", "fname", "lname", "department", "phNumber"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for emp in employees:
            writer.writerow({
                "id": emp.id,
                "fname": emp.fname,
                "lname": emp.lname,
                "department": emp.department,
                "phNumber": emp._Employee__phNumber  # Save raw phone number
            })

def add_employee(employees, new_employee, filename="employee_data.csv"):
    """Add a new Employee to the list and save to CSV."""
    if not isinstance(new_employee, Employee):
        raise TypeError("new_employee must be an Employee object")
    employees.append(new_employee)
    save_employees(employees, filename)


def edit_employee(employees, index, fname=None, lname=None, department=None, phNumber=None, filename="employee_data.csv"):
    """Edit an existing Employee (ID cannot be changed)."""
    try:
        emp = employees[index]
    except IndexError:
        raise IndexError("Employee index out of range")
    if fname is not None:
        emp.fname = fname
    if lname is not None:
        emp.lname = lname
    if department is not None:
        emp.department = department
    if phNumber is not None:
        emp.phNumber = phNumber
    save_employees(employees, filename)


def delete_employee(employees, index, filename="employee_data.csv"):
    """Delete an Employee by index."""
    try:
        del employees[index]
    except IndexError:
        raise IndexError("Employee index out of range")
    save_employees(employees, filename)

def print_employees(employees):
    """Prints a list of employees in the format: 1. ID - Last, First - Department - Phone"""
    for idx, emp in enumerate(employees, 1):
        print(f"{idx}. {emp.id} - {emp.lname}, {emp.fname} - {emp.department} - {emp.phNumber}")

def main():
    employees = load_employees()
    while True:
        print("\nEmployee Manager Menu:")
        print("1. List Employees")
        print("2. Add Employee")
        print("3. Edit Employee")
        print("4. Delete Employee")
        print("5. Quit")
        choice = input("Select an option (1-5): ").strip()
        if choice == "1":
            print_employees(employees)
        elif choice == "2":
            try:
                id = int(input("Enter ID: "))
                fname = input("Enter first name: ")
                lname = input("Enter last name: ")
                department = input("Enter department (3 uppercase letters): ")
                phNumber = input("Enter phone number (10 digits): ")
                new_emp = Employee(id, fname, lname, department, phNumber)
                add_employee(employees, new_emp)
                print("Employee added.")
            except Exception as e:
                print(f"Error adding employee: {e}")
        elif choice == "3":
            try:
                idx = int(input("Enter employee number to edit: ")) - 1
                fname = input("New first name (leave blank to keep): ") or None
                lname = input("New last name (leave blank to keep): ") or None
                department = input("New department (leave blank to keep): ") or None
                phNumber = input("New phone number (leave blank to keep): ") or None
                edit_employee(employees, idx, fname, lname, department, phNumber)
                print("Employee updated.")
            except Exception as e:
                print(f"Error editing employee: {e}")
        elif choice == "4":
            try:
                idx = int(input("Enter employee number to delete: ")) - 1
                delete_employee(employees, idx)
                print("Employee deleted.")
            except Exception as e:
                print(f"Error deleting employee: {e}")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()

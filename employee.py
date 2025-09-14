#Write a Python class called Employee with attributes: id, fname, lname, 
# department, and phNumber. Use private variables and getters/setters. 
# Add validation:  - First/last names cannot be empty or contain digits 
# - Department must be exactly 3 uppercase letters 
# - Phone number must be 10 digits 
# Include docstrings.
class Employee:
    """
    A class to represent an employee.

    Attributes:
        id (int): The employee's ID.
        fname (str): The employee's first name.
        lname (str): The employee's last name.
        department (str): The employee's department (3 uppercase letters).
        phNumber (str): The employee's phone number (10 digits).
    """

    def __init__(self, id, fname, lname, department, phNumber):
        self.__id = id
        self.fname = fname
        self.lname = lname
        self.department = department
        self.phNumber = phNumber

    @property
    def id(self):
        """Get the employee's ID."""
        return self.__id

    @property
    def fname(self):
        """Get the employee's first name."""
        return self.__fname

    @fname.setter
    def fname(self, value):
        """Set the employee's first name with validation."""
        if not value or any(char.isdigit() for char in value):
            raise ValueError("First name cannot be empty or contain digits.")
        self.__fname = value

    @property
    def lname(self):
        """Get the employee's last name."""
        return self.__lname

    @lname.setter
    def lname(self, value):
        """Set the employee's last name with validation."""
        if not value or any(char.isdigit() for char in value):
            raise ValueError("Last name cannot be empty or contain digits.")
        self.__lname = value

    @property
    def department(self):
        """Get the employee's department."""
        return self.__department

    @department.setter
    def department(self, value):
        """Set the employee's department with validation."""
        if len(value) != 3 or not value.isupper():
            raise ValueError("Department must be exactly 3 uppercase letters.")
        self.__department = value

    @property
    def phNumber(self):
        """Get the employee's phone number."""
        # Format as (XXX)XXX-XXXX when accessed
        num = self.__phNumber
        return f"({num[:3]}){num[3:6]}-{num[6:]}"

    @phNumber.setter
    def phNumber(self, value):
        """Set the employee's phone number with validation."""
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must be exactly 10 digits.")
        self.__phNumber = value

if __name__ == "__main__":
    import logging
    logging.basicConfig(filename="employee_test.log", level=logging.ERROR)
    test_cases = [
        # Valid
        {"id": 1, "fname": "John", "lname": "Doe", "department": "HRD", "phNumber": "1234567890"},
        # Invalid first name
        {"id": 2, "fname": "J0hn", "lname": "Smith", "department": "ENG", "phNumber": "1234567890"},
        # Invalid last name
        {"id": 3, "fname": "Jane", "lname": "Sm1th", "department": "ENG", "phNumber": "1234567890"},
        # Invalid department
        {"id": 4, "fname": "Alice", "lname": "Brown", "department": "eng", "phNumber": "1234567890"},
        # Invalid phone number
        {"id": 5, "fname": "Bob", "lname": "White", "department": "FIN", "phNumber": "12345"},
    ]
    for case in test_cases:
        try:
            emp = Employee(case["id"], case["fname"], case["lname"], case["department"], case["phNumber"])
            print(f"Created Employee: {emp.id}, {emp.fname}, {emp.lname}, {emp.department}, {emp.phNumber}")
        except Exception as e:
            logging.error(f"Failed to create Employee with data {case}: {e}")
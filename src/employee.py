def add_employee(emp_id, name, department):

    employee = {
        "Employee_ID": emp_id,
        "Name": name,
        "Department": department
    }

    return employee


def display_employee(*employees):

    print("Employee Details")

    for employee in employees:
        print("_______________")
        for key,value in employee.items():
            print(key,"=",value)


emp=add_employee(101,"Lavanya","IT")
emp1=add_employee(105,"Mani","Lead engineer")

display_employee(emp,emp1)
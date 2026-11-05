def apply_leave(emp_id, emp_name, days):

    if days <= 0:
        return "Invalid leave days"

    leave = {
        "Employee_ID": emp_id,
        "Employee_Name": emp_name,
        "Leave_Days": days,
        "Status": "Pending"
    }

    return leave


# Collect all applications in a list
all_leaves = []

all_leaves.append(apply_leave(101, "Lavanya", 2))
all_leaves.append(apply_leave(102, "Ravi", 3))

# Print them all
for leave in all_leaves:
    print(leave)
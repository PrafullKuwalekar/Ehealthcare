# Program 1
def dictionary_basics():
    student_info = {"name": "Alice", "age": 24, "major": "Data Science"}
    print("Dictionary:", student_info)
    
    print("Name:", student_info["name"])
    print("Major:", student_info["major"])

dictionary_basics()

# Program 2
def add_update_dictonary():
    grade = {"Math": 85, "Science": 90, "English": 78}

    grade["History"] = 88 
    grade["Science"] = 95

    print("Updateed Dictonary:", grade)

add_update_dictonary()

# Program 3
def remove_dictonary_entry():
    grade = {"Math": 85, "Science": 95, "English": 78, "History": 88}

    grade.pop("English")
    print("Dictonary after removel:", grade)

remove_dictonary_entry()

# Program 4
def dictonary_method():
    employee = {"Name": "Bob", "Position": "Data analysis", "Salary": 7000}

    print("Keys:", employee.keys())
    print("Value:", employee.values())
    print("Item:", employee.items())

dictonary_method()

# Program 5
def nested_dictonary():
    course = {
        "Data science": {"Credits":4, "Instructor": "Dr.Smith"},
        "Machine learning": {"Credits": 3, "Instructor": "Dr. Johnson"}
    }

    print("Machine Learning Instructor:", course["Machine learning"]["Instructor"])

nested_dictonary()

# Program 6
def aggregate_dictonary_data():
    sale = {"Product A": 150, "Product B": 200, "Product C": 100}

    total_item_sold = sum(sale.values())
    print("Total Item Sold:", total_item_sold)

aggregate_dictonary_data()

# Program 7
def merge_dictionaries():
    dict_A = {"key1": "value1", "key2": "value2"}
    dict_B = {"key2": "updated_value", "key3": "value3"}

    merged_dict = dict_A | dict_B
    print("Merged Dictonary:", merged_dict)

merge_dictionaries()

# Program 8
def filter_dictonary():
    score = {"Alice": 85, "Bob": 65, "Charlie": 90, "Devid": 72}

    passed = {name: score for name, score in score.items() if score>= 70}
    print("Passed student:", passed)

filter_dictonary()

# Program 9
def pratical_dictonary_operation():
    student = [("Alice", 85), ("Bob", 72), ("Charlie", 90)]

    student_dict = {name: grade for name, grade in student}
    print("Student Dictonary:", student_dict)

pratical_dictonary_operation()

# Program 10
def pratical_dictonary_operations():
    employee = [
        {"Name": "Alice", "Position": "Engineer", "Salary": 70000},
        {"Name": "Bob", "Position": "Manager", "Salary": 80000},
        {"Name": "Charlie", "Position": "Analysis", "Salary": 75000}
    ]

    total_salary = sum(emp["Salary"] for emp in employee)
    avg_salary = total_salary / len(employee)
    print("Average Salary:", avg_salary)

    high_earn = [emp["Name"] for emp in employee if emp["Salary"] > 75000]
    print("High earn:", high_earn)

pratical_dictonary_operations()
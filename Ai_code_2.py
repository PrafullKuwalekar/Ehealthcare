# Program 1
def tuple_creation_operation():
    student_info = ("Alice", 24, "Data Science")
    print("Tuple:", student_info)

    print("First Element:", student_info[0])
    print("Last Element:", student_info[-1])

tuple_creation_operation()

# Program 2
def tuple_unpacking():
    coordinate = (10, 20)

    x, y = coordinate
    print("x:", x, "y:", y)

tuple_unpacking()

# Program 3
def tuple_indexing_slicing():
    fruit = ("Apple", "Banana", "Cherry", "Date", "ELderberry")

    print("Second fruit:", fruit[1])
    print("Forth fruit:", fruit[3])

    some_fruits = fruit[:3]
    print("Some fruits:", some_fruits)

tuple_indexing_slicing()

# Program 4
def convert_tuple_list():
    grade = [85, 90, 78, 92]

    grade_tuple = tuple(grade)
    print("Tuple:", grade_tuple)
    print("Type:", type(grade_tuple))

convert_tuple_list()

# Program 5
def nested_tuple():
    course_data = (("Data science", 40, "Online"), ("Machine learning", 45, "On-campus"))

    for course in course_data:
        print(f"Course Name: {course[0]}, Duration: {course[1]} hours, Mode: {course[2]}")

nested_tuple()

# Program 6
def tuple_method():
    number = (1, 2, 3, 4, 5, 2)

    count_2 = number.count(2)
    print("Count of 2:", count_2)

    index_3 = number.index(3)
    print("Index of 3:", index_3)

tuple_method()

# Program 7
def tuple_immutability():
    immutable_data = (1, 2, 3)

    try:
        immutable_data[1] = 5
    except TypeError as e:
        print("Error:", e)
        print("Explantation: Tuple are immutable, meaning their element cannot be changed once created.")
    
tuple_immutability()

# Program 8
def aggregate_tuple_data():
    sale = (150, 200, 250, 300, 350)

    total_sale = sum(sale)
    print("Total_sale:", total_sale)

aggregate_tuple_data()

# Program 9
def filter_tuple_data():
    age = (15, 22, 19, 27, 30, 14, 25)

    adult = tuple(_ for _ in age if _ >= 18)
    print("Adult Tuple:", adult)

filter_tuple_data()

# Program 10
def pratical_tuple_operation():
    employee = [("Alice", 70000), ("Bob", 80000), ("Charlie", 75000)]

    total_salary = sum(salary for _, salary in employee)
    avg_salary = total_salary / len(employee)
    print("Average salary:", avg_salary)

    high_earn = tuple(name for name, salary in employee if salary > 75000)
    print("High Earn:", high_earn)

pratical_tuple_operation()
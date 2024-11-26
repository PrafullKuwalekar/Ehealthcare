# Program 1
def basic_for_loop():
    number = [1, 2, 3, 4, 5]
    print("Numbers in the list:")
    for _ in number:
        print(_)

basic_for_loop()

# Program 2
def calculate_sum_with_loop():
    value = [10, 20, 30, 40, 50]
    total_sum = 0

    for _ in value:
        total_sum += _
    print("Total Sum:", total_sum)

calculate_sum_with_loop()

# Program 3
def create_square_with_loop():
    number = list(range(1, 11))
    square = []
    for _ in number:
        square.append(_**2)
    print("Square list:", square)

create_square_with_loop()

# Program 4
def filter_adult_with_loop():
    ages = [15, 22, 19, 27, 30, 14, 25]
    adult = []
    for _ in ages:
        if _ >= 18:
            adult.append(_)
    print("Adult List:", adult)

filter_adult_with_loop()

# Program 5
def nested_loop_example():
    student = ["Alice", "Bob", "Charlie"]
    subject = ["Maths", "Science", "History"]

    for _ in student:
        for __ in subject:
            print(f"{_} studies {__}")
        
nested_loop_example()

# Program 6
def iterate_dictonary():
    grades = {"Alice": 85, "Bob": 90, "Charlie": 78}

    print("Student Grade")
    for name, grade in grades.items():
        print(f"{name}: {grade}")

iterate_dictonary()

# Program 7
def range_function_example():
    print("First 10 even No")
    for even in range(0, 20, 2):
        print(even)
    print("First 10 odd No")
    for odd in range(1, 20, 2):
        print(odd)

range_function_example()

# Program 8
def reverse_loop():
    fruits = ["Apple", "Banana", "Cherry", "Date"]
    print("Fruits inn reverse order: ")
    for fruit in reversed(fruits):
        print(fruit)

reverse_loop()

# Program 9
def sum_even_number():
    number = [5, 15, 8, 22, 10, 30]
    even_sum = 0
    for _ in number:
        even_sum += _
    print("Sum of even numbers:", even_sum)

sum_even_number()

# Program 10
def manipulated_dataset_with_loop():
    product = [
        {"name": "Laptop", "price": 800},
        {"name": "Phone", "price": 600},
        {"name": "Tablet", "price": 300},
        {"name": "Monitor", "price": 150}
    ]

    total_cost = 0
    for _ in product:
        total_cost += _["price"]
    print("Total cost:", total_cost)

    expensive_product = []
    for __ in product:
        if __["price"] > 400:
            expensive_product.append(_["name"])
    print("Expensive product:", expensive_product)

manipulated_dataset_with_loop()
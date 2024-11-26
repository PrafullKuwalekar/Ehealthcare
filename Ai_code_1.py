# Program 1
def basic_list_operation():
    score = [85, 90, 78, 92, 88]
    print("Original List:", score)

    print("First Element:", score[0])
    print("Last Element:", score[-1])

    score.append(95)
    print("After adding 95:", score)

    score.remove(78)
    print("After removing 78:", score)

basic_list_operation()

# Program 2 
def basic_statistics():
    import statistics

    temperture_reading = [20.5, 22.3, 19.8, 21.0, 23.5]

    avg_temp = statistics.mean(temperture_reading)
    print("Average Temperture:", avg_temp)

    max_temp = max(temperture_reading)
    min_temp = min(temperture_reading)
    print("Maximum Temperture:", max_temp)
    print("Minimum Temperture:", min_temp)

    temp_range = max_temp - min_temp
    print("Tempurture Range:", temp_range)

basic_statistics()

# Program 3
def list_comprehension():
    integer = list(range(1, 11))

    square = [x**2 for x in integer]
    print("Square list:", square)

list_comprehension()

# Program 4
def filter_list():
    ages = [15, 22, 19, 27, 30, 14, 25]

    adult = [age for age in ages if age >= 18]
    print("Adult list:", adult)

filter_list()

# Program 5
def nested_list():
    student_grade = [['Alice', 85, 90], ['Bob', 78, 82], ['Charlie', 92, 88]]

    for student in student_grade:
        name = student[0]
        avg_grade = sum(student[1:]) / len (student[1:])
        print(f"{name}: Average Grade = {avg_grade}")

nested_list()

# Program 6 
def agregate_data():
    sale = [150, 200, 250, 300, 350]

    Total_sale = sum(sale)
    print("Total sale:", Total_sale)

    percentage = [(_ / Total_sale) * 100 for _ in sale]
    print("Percentage Contribution:", percentage)

agregate_data()

# Program 7
def sort_list():
    product = ["Apple", "Banana", "Grape", "Orange", "Kiwi"]
    product.sort()
    print("Sorted product:", product)

    price = [1.2, 0.5, 2.0, 1.0, 1.5]
    price.sort(reverse=True)
    print("Sorted price:", price)

sort_list()

# Program 8
def combine_list():
    name = ["Alice", "Bob", "Charlie"]
    score = [85, 92, 88]

    student_info = list(zip(name, score))
    print("student Info:", student_info)

combine_list()

# Program 9
def modify_list():
    numbers = [10, 20, 30, 40, 50]

    numbers[1] = 25
    numbers[-1] = 45

    numbers.reverse()
    print("Modified list:", numbers)

modify_list()

# Program 10
def practical_dataset():
    import statistics  # For calculating the median
    
    # Create list
    grades = [55, 60, 75, 80, 90, 65, 85, 95]
    
    # Remove grades below 70
    grades = [grade for grade in grades if grade >= 70]
    print("Filtered Grades:", grades)
    
    # Calculate median
    median_grade = statistics.median(grades)
    print("Median Grade:", median_grade)
    
    # Categorize grades
    grade_categories = ["A" if grade >= 90 else 
                        "B" if grade >= 80 else 
                        "C" if grade >= 70 else 
                        "F" for grade in grades]
    print("Grade Categories:", grade_categories)

practical_dataset()

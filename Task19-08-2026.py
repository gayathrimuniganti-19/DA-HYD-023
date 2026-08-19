'''
#Task1: Student Grade Calculator
def calculate_grade(mark):
    """Convert a numeric mark into a letter grade"""
    if mark >= 80:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 40:
        return "C"
    else:
        return "Fail"
for i in range(3):
    mark = float(input(f'Enter mark for student {i + 1}:'))
    grade = calculate_grade(mark)
    print(f'Student {i + 1}: Mark = {mark} -> Grade = {grade}')
--------
#Task2:Shopping Bill Calculator
def calculate_bill(price, quantity = 1, discount = 0):
    """"Calculate final bill using price, quantity and discount percentage"""
    total = price * quantity
    final_amount = total - (total * discount / 100)
    return final_amount
#call with only price
bill1 = calculate_bill(100)
print(f'Only price=100 -> Bill = {bill1}')
#call with price and quantity
bill2 = calculate_bill(100,3)
print(f'price=100, quantity=3 -> Bill = {bill2}')
#call with all values as keyword arguments
bill3 = calculate_bill(price=100, quantity=3, discount=10)
print(f'price=100, quantity=3, discount=10 -> Bill == {bill3}')
----------
#Task3:BMI Calculator
def calculate_bmi(weight, height):
    """Calculate BMI = weight(kg)/ height(m) squared"""
    return weight / (height ** 2)
def bmi_status(bmi):
    """Classify BMI value into a category"""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"
for i in range(3):
    name = input(f'Enter name of person {i + 1}:')
    weight = float(input('Enter weight(kg):'))
    height = float(input('Enter height(m):'))
    bmi = calculate_bmi(weight, height)
    status = bmi_status(bmi)
    print(f'{name}: BMI = {round(round(bmi, 2))} -> {status}')
----------
#Task4:Marks Summary Using *args
def mark_summary(*args):
    """Return total and average of any number of marks"""
    if len(args)==0:
        return 0, 0
    total = 0
    for i in args:
        total += i
    average = total / len(args)
    return total, average
total, avg = mark_summary(80)
print(f'One mark (80)-> Total = {total}, Average = {avg}')
total, avg = mark_summary(70,85,90,60)
print(f'Several marks -> Total = {total}, Average = {avg}')
total, avg = mark_summary()
print(f'No marks -> Total = {total}, Averge = {avg}')
--------
'''
#Task5:Employee Details Using **kwargs
def display_employee(**kwargs):
    """Display all supplied employee fields; flag missing salary/department"""
    print('Employee Details:')
    for key, value in kwargs.items():
        print(f'{key}:{value}')
    if 'salary' not in kwargs:
        print('Note: Salary information is missing')
    if 'department' not in kwargs:
        print('Note: Department infomation is missing')
display_employee(name='John', ages=30, department='Sales', salary=50000)
print()
display_employee(name='Priya', age=27)
















    

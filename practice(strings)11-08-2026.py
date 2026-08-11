'''
#Task-1 Text Case converter
text = input("Enter the sentence:")
methods = [text.upper(),text.lower(), text.title(), text.capitalize(),text.swapcase()]
for x in methods:
    print(x)
if text.isupper():
    print("Uppercase")
elif text.islower():
    print("Lowercase")
elif text.istitle():
    print("Titlecase")
elif text.capitalize():
    print("Capitalize")
elif text.swapcase():
    print("Swapcase")
elif text.casefold():
    print("Casefold")
else:
    print("mixedcase")
------------------------
#Task-2 Username Validator
while True:
    username = input("Enter a username: ")

    if username == "quit":
        print("Program stopped.")
        break
    if username.isalnum():
        print("Contains only letters and numbers")
    else:
        print("Does not contain only letters and numbers")
    if username and username[0].isalpha():
        print("Begins with a letter")
    else:
        print("Does not begin with a letter")
    if username.isidentifier():
        print("Valid Python identifier")
    else:
        print("Not a valid Python identifier")
    if username.isascii():
        print("Contains only ASCII characters")
    else:
        print("Contains non-ASCII characters")
------------------------
#Task-3 Formatted Student Report
print("STUDENT REPORT")

for i in range(3):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))

    if marks >= 80:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade = "Fail"

    print(name.ljust(10), str(marks).rjust(5), grade.rjust(5))
print()
------------------------
'''
#Task-4 Character and Text Analyser
text = input("Enter a line of text: ")
letters = 0
digits = 0
spaces = 0
printable = 0
non_printable = 0
for ch in text:
    if ch.isalpha():
        letters += 1

    if ch.isdigit():
        digits += 1

    if ch.isspace():
        spaces += 1

    if ch.isprintable():
        printable += 1
    else:
        non_printable += 1
print("\n----- Text Analysis -----")
print(f"Letters       : {letters}")
print(f"Digits        : {digits}")
print(f"Spaces        : {spaces}")
print(f"Printable     : {printable}")
print(f"Non-printable : {non_printable}")
print(f"Lowercase     : {text.islower()}")
print(f"Uppercase     : {text.isupper()}")
print(f"Title case    : {text.istitle()}")








































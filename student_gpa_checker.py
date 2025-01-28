
"""
Author: Carson Doubiago
File Name: student_gpa_checker.py
Description: This app accepts student names and GPAs, checks whether they qualify for the Dean's List or Honor Roll, and prints appropriate messages.
The program will quit when the last name 'ZZZ' is entered.
"""

def main():
    while True:
        # Ask for student's last name
        last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
        if last_name.upper() == 'ZZZ':
            print("Exiting the program. Goodbye!")
            break

        # Ask for student's first name
        first_name = input("Enter the student's first name: ")

        # Ask for student's GPA
        try:
            gpa = float(input("Enter the student's GPA: "))
        except ValueError:
            print("Invalid input. Please enter a valid GPA as a number.")
            continue

        # Check qualifications
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"{first_name} {last_name} does not qualify for the Dean's List or Honor Roll.")

if __name__ == "__main__":
    main()

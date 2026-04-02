# ============================================================
# Assignment - Part 1: Python Basics & Control Flow
# Theme: Student Grade Tracker
# ============================================================
# Task 1 - Data Parsing & Profile Cleaning     (5 marks)
# Task 2 - Marks Analysis Using Loops          (8 marks)
# Task 3 - Class Performance Summary           (7 marks)
# Task 4 - String Manipulation Utility         (5 marks)
# ============================================================


# ============================================================
# TASK 1 — Data Parsing & Profile Cleaning (5 marks)
# ============================================================

print("=" * 60)
print("TASK 1 — Data Parsing & Profile Cleaning")
print("=" * 60)

# Raw student data given in the question
# Names have messy spacing/casing, roll is a string, marks is a string
raw_students = [
    {"name": " ayesha SHARMA ",  "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",      "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",   "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",      "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",   "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

# We will store the cleaned students in this list
cleaned_students = []

for student in raw_students:
    # Step 1: Clean the name — remove extra spaces and convert to Title Case
    clean_name = student["name"].strip().title()

    # Step 2: Convert roll number from string to integer
    clean_roll = int(student["roll"])

    # Step 3: Split marks string by ", " and convert each mark to integer
    clean_marks = [int(m) for m in student["marks_str"].split(", ")]

    # Step 4: Validate name — every word must contain only alphabetic characters
    words = clean_name.split()
    is_valid = all(word.isalpha() for word in words)
    validity = "✓ Valid name" if is_valid else "✗ Invalid name"

    # Store the cleaned student as a dictionary
    cleaned_students.append({
        "name": clean_name,
        "roll": clean_roll,
        "marks": clean_marks,
        "valid": validity
    })

    # Step 5: Print a formatted profile card using f-strings
    print("=" * 32)
    print(f"Student : {clean_name}  {validity}")
    print(f"Roll No : {clean_roll}")
    print(f"Marks   : {clean_marks}")
    print("=" * 32)

# Step 6: Find student with roll number 103 and print name in ALL CAPS and lowercase
for s in cleaned_students:
    if s["roll"] == 103:
        print(f"\nStudent with Roll 103 in ALL CAPS : {s['name'].upper()}")
        print(f"Student with Roll 103 in lowercase : {s['name'].lower()}")


# ============================================================
# TASK 2 — Marks Analysis Using Loops & Conditionals (8 marks)
# ============================================================

print("\n" + "=" * 60)
print("TASK 2 — Marks Analysis Using Loops & Conditionals")
print("=" * 60)

# Given data for this task
student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

# Step 1: Print each subject with marks and grade label using a for loop
print(f"\nGrade Report for {student_name}:")
print("-" * 40)

for subject, mark in zip(subjects, marks):
    # Assign grade based on marks range
    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "F"

    print(f"{subject:<12} : {mark}  →  Grade: {grade}")

# Step 2: Calculate total, average, highest and lowest
total   = sum(marks)
average = round(total / len(marks), 2)

# Find highest scoring subject
highest_mark    = max(marks)
highest_subject = subjects[marks.index(highest_mark)]

# Find lowest scoring subject
lowest_mark    = min(marks)
lowest_subject = subjects[marks.index(lowest_mark)]

print(f"\nTotal Marks        : {total}")
print(f"Average Marks      : {average}")
print(f"Highest Subject    : {highest_subject} ({highest_mark})")
print(f"Lowest Subject     : {lowest_subject} ({lowest_mark})")

# Step 3: While loop — simulate a marks entry system for new subjects
print("\n--- Add New Subjects (type 'done' to stop) ---")

new_subjects_count = 0   # count how many valid subjects were added

while True:
    subject_input = input("Enter subject name (or 'done' to stop): ")

    # Stop the loop when user types 'done'
    if subject_input.lower() == "done":
        break

    # Ask for marks for that subject
    marks_input = input(f"Enter marks for {subject_input} (0-100): ")

    # Validate marks — must be a number between 0 and 100
    try:
        new_mark = int(marks_input)
        if new_mark < 0 or new_mark > 100:
            print("Warning: Marks must be between 0 and 100. Not added.")
            continue
    except ValueError:
        # Triggered if user types something that is not a number
        print("Warning: Invalid marks. Please enter a number. Not added.")
        continue

    # If valid, add to our lists
    subjects.append(subject_input)
    marks.append(new_mark)
    new_subjects_count += 1
    print(f"'{subject_input}' with marks {new_mark} added successfully!")

# After loop ends, print summary
updated_average = round(sum(marks) / len(marks), 2)
print(f"\nNew subjects added  : {new_subjects_count}")
print(f"Updated average     : {updated_average}")


# ============================================================
# TASK 3 — Class Performance Summary (7 marks)
# ============================================================

print("\n" + "=" * 60)
print("TASK 3 — Class Performance Summary")
print("=" * 60)

# Given class data
class_data = [
    ("Ayesha Sharma", [88, 72, 95, 60, 78]),
    ("Rohit Verma",   [55, 68, 49, 72, 61]),
    ("Priya Nair",    [91, 85, 88, 94, 79]),
    ("Karan Mehta",   [40, 55, 38, 62, 50]),
    ("Sneha Pillai",  [75, 80, 70, 68, 85]),
]

passed = 0   # count students who passed
failed = 0   # count students who failed

# Store averages to find class topper and class average later
student_averages = []

# Print formatted table header
print(f"\n{'Name':<20} | {'Average':^7} | {'Status'}")
print("-" * 42)

for name, student_marks in class_data:
    # Calculate average rounded to 2 decimal places
    avg = round(sum(student_marks) / len(student_marks), 2)

    # Pass if average >= 60, else Fail
    status = "Pass" if avg >= 60 else "Fail"

    # Count pass/fail
    if status == "Pass":
        passed += 1
    else:
        failed += 1

    # Store for later use
    student_averages.append((name, avg))

    # Print formatted row
    print(f"{name:<20} | {avg:^7} | {status}")

# After the table, print summary
print(f"\nStudents Passed     : {passed}")
print(f"Students Failed     : {failed}")

# Find class topper (student with highest average)
topper_name, topper_avg = max(student_averages, key=lambda x: x[1])
print(f"Class Topper        : {topper_name} ({topper_avg})")

# Class average = average of all students' averages
class_avg = round(sum(avg for _, avg in student_averages) / len(student_averages), 2)
print(f"Class Average       : {class_avg}")


# ============================================================
# TASK 4 — String Manipulation Utility (5 marks)
# ============================================================

print("\n" + "=" * 60)
print("TASK 4 — String Manipulation Utility")
print("=" * 60)

# Given essay with messy leading/trailing whitespace
essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# Step 1: Strip leading and trailing whitespace
clean_essay = essay.strip()
print(f"\nStep 1 - Stripped Essay:\n{clean_essay}")

# Step 2: Convert to Title Case and print
title_essay = clean_essay.title()
print(f"\nStep 2 - Title Case:\n{title_essay}")

# Step 3: Count how many times "python" appears (case-insensitive)
# clean_essay is already lowercase after strip, so we count directly
python_count = clean_essay.count("python")
print(f"\nStep 3 - Count of 'python': {python_count}")

# Step 4: Replace every "python" with "Python 🐍" and print
replaced_essay = clean_essay.replace("python", "Python 🐍")
print(f"\nStep 4 - Replaced Essay:\n{replaced_essay}")

# Step 5: Split clean_essay into individual sentences by splitting on ". "
sentences = clean_essay.split(". ")
print(f"\nStep 5 - Sentences List:\n{sentences}")

# Step 6: Print each sentence numbered, adding "." if it doesn't already end with one
print("\nStep 6 - Numbered Sentences:")
for i, sentence in enumerate(sentences, start=1):
    sentence = sentence.strip()   # remove any extra spaces
    if not sentence.endswith("."):
        sentence += "."           # add period if missing
    print(f"{i}. {sentence}")

print("\n" + "=" * 60)
print("All Part 1 Tasks Complete!")
print("=" * 60)

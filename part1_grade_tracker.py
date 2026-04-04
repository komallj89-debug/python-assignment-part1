# Part 1 - Grade Tracker
# basically cleaning messy student data, doing some mark analysis and string stuff

print("=" * 50)
print("TASK 1 - Data Parsing")
print("=" * 50)

# raw data with messy names and marks as strings
raw_students = [
    {"name": " ayesha SHARMA ",  "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",      "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",   "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",      "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",   "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

for student in raw_students:
    name = student["name"].strip().title()
    roll = int(student["roll"])
    marks = [int(m) for m in student["marks_str"].split(", ")]

    words = name.split()
    valid = all(w.isalpha() for w in words)  # just checking no numbers/symbols in name
    validity = "Valid" if valid else "Invalid"

    cleaned_students.append({
        "name": name,
        "roll": roll,
        "marks": marks,
        "valid": validity
    })

    print(f"Name: {name} ({validity}), Roll: {roll}, Marks: {marks}")

# printing roll 103's name in both cases
for s in cleaned_students:
    if s["roll"] == 103:
        print(f"\nRoll 103 uppercase: {s['name'].upper()}")
        print(f"Roll 103 lowercase: {s['name'].lower()}")


print("\n" + "=" * 50)
print("TASK 2 - Marks Analysis")
print("=" * 50)

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print(f"\nReport for {student_name}:")

for subject, mark in zip(subjects, marks):
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
    print(f"  {subject}: {mark} -> {grade}")

total = sum(marks)
avg = round(total / len(marks), 2)
high = max(marks)
low = min(marks)

print(f"\nTotal: {total}")
print(f"Average: {avg}")
print(f"Highest: {subjects[marks.index(high)]} ({high})")
print(f"Lowest: {subjects[marks.index(low)]} ({low})")

print("\nAdd new subjects (type done to stop):")
added = 0

while True:
    sub = input("Subject name: ")
    if sub.lower() == "done":
        break

    m = input(f"Marks for {sub}: ")
    try:
        m = int(m)
        if m < 0 or m > 100:
            print("marks should be between 0 and 100, skipping this one")
            continue
    except ValueError:
        print("that doesn't look like a number, try again")
        continue

    subjects.append(sub)
    marks.append(m)
    added += 1
    print(f"added {sub} with marks {m}")

new_avg = round(sum(marks) / len(marks), 2)
print(f"\nSubjects added: {added}")
print(f"New average after additions: {new_avg}")


print("\n" + "=" * 50)
print("TASK 3 - Class Summary")
print("=" * 50)

class_data = [
    ("Ayesha Sharma", [88, 72, 95, 60, 78]),
    ("Rohit Verma",   [55, 68, 49, 72, 61]),
    ("Priya Nair",    [91, 85, 88, 94, 79]),
    ("Karan Mehta",   [40, 55, 38, 62, 50]),
    ("Sneha Pillai",  [75, 80, 70, 68, 85]),
]

passed = 0
failed = 0
averages = []

print(f"\n{'Name':<20} {'Avg':^7} Status")
print("-" * 38)

for name, mlist in class_data:
    avg = round(sum(mlist) / len(mlist), 2)
    status = "Pass" if avg >= 60 else "Fail"

    if status == "Pass":
        passed += 1
    else:
        failed += 1

    averages.append((name, avg))
    print(f"{name:<20} {avg:^7} {status}")

print(f"\nPassed: {passed}, Failed: {failed}")

# finding the topper using max with a lambda
topper = max(averages, key=lambda x: x[1])
print(f"Topper: {topper[0]} with avg {topper[1]}")

class_avg = round(sum(a for _, a in averages) / len(averages), 2)
print(f"Class avg: {class_avg}")


print("\n" + "=" * 50)
print("TASK 4 - String Manipulation")
print("=" * 50)

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

essay = essay.strip()
print(f"\nStripped:\n{essay}")

print(f"\nTitle case:\n{essay.title()}")

count = essay.count("python")
print(f"\n'python' appears {count} times")

print(f"\nReplaced:\n{essay.replace('python', 'Python 🐍')}")

sentences = essay.split(". ")
print(f"\nSentences: {sentences}")

# numbering each sentence and making sure it ends with a dot
print("\nNumbered:")
for i, s in enumerate(sentences, 1):
    s = s.strip()
    if not s.endswith("."):
        s += "."
    print(f"{i}. {s}")

Python 3.13.17 (tags/v3.13.17:64e080d, Oct 21 2026, 14:08:53) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
applicants = [
    {"name": "Anu", "marks": [90, 85, 88], "attendance": 92, "income": 180000},
...     {"name": "Bala", "marks": [86, 82, 89], "attendance": 95, "income": 150000},
...     {"name": "Charan", "marks": [70, 75, 72], "attendance": 88, "income": 100000},
... ]
... 
... MIN_AGGREGATE = 80
... MIN_SUBJECT = 60
... MIN_ATTENDANCE = 75
... MAX_INCOME = 250000
... 
... eligible = []
... 
... for student in applicants:
...     average = sum(student["marks"]) / len(student["marks"])
...     if (average >= MIN_AGGREGATE
...             and min(student["marks"]) >= MIN_SUBJECT
...             and student["attendance"] >= MIN_ATTENDANCE
...             and student["income"] <= MAX_INCOME):
...         eligible.append((student, average))
... 
... eligible.sort(key=lambda item: (
...     -item[1], -item[0]["attendance"], item[0]["income"], item[0]["name"]
... ))
... 
... print("Scholarship ranking")
... for rank, (student, average) in enumerate(eligible, start=1):

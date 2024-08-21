#wAp that converts students scores to grades

students_marks = {
  "Jenny":92,
  "Henry":78,
  "Dimpy":56,
  "Rahul":41,
  "Aniket":99,
  "Prem":34,
}
print(students_marks)
student_grades = {
  "grade1" :"A+",
  "grade2":"A",
  "grade3": "B+",
  "grade4":"B",
  "grade5":"C",
  "grade6": "D",
  "grade7": "E",
  "grade8":"f",
}
#print(student_grades)

for i in students_marks:
  if students_marks[i] >= 91:
    students_marks[i] = student_grades["grade1"]
  elif students_marks[i] >= 81:
    students_marks[i] = student_grades["grade2"]
  elif students_marks[i] >= 71:
    students_marks[i] = student_grades["grade3"]
  elif students_marks[i] >= 61:
    students_marks[i] = student_grades["grade4"]
  elif students_marks[i] >= 51:
    students_marks[i] = student_grades["grade5"]
  elif students_marks[i] >= 41:
    students_marks[i] = student_grades["grade6"]
  else:
    students_marks[i] = student_grades["grade7"]
print(students_marks)
#WAP to add a dict into alist

student_data = [
  {
    "Name":"Ram",
    "roll_no":10,
    "age":20,
    "course":"python"
  },
  {
    "name": "Mohan",
    "roll_no": 20,
    "age": 22,
    "course": "java",
  }
]
#print(student_data)
def add_dict(name,roll_no,age,course):
  new_dict = {}
  new_dict["name"] = name
  new_dict["roll_no"] = roll_no
  new_dict["age"] = age
  new_dict["course"] = course
  #student_data[1] = new_dict #this is when u want to reassign
  student_data.append(new_dict)
  print(student_data)
  
add_dict("zika",30,25, "eng");  
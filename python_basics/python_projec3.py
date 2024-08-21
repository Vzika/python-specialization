#Writa quiz game program

question_dict = {
  "ques1" : "The ability of a class to acquire the attribtes and methods of another class is called ------ ",
  "ques2" : "Which of the following is a type of inheritance?",
  "ques3": "What type of inheritance has multiple subclases to a single subclass?",
  "ques4" : "What is the depth of multilevel inheritance in python?",
  "ques5": "What does MRO stand for?",
}

opt_dict = [ 
  ["A. Inheretance",  "B. Abstraction ", " C. Polymophism ", " D. Object" ],
  ["A. single ", "B. Double",  "C. Multiple",  "D. Both A and C"],
  ["A. Multiple inheritance", "B. Multilevel inheritance",  "C. Heirachical",  "D. None of the above"],
  ["A. Two leve",  "B. Three level", "C. Any level", "D. None of these"],
  ["A. Method recursive Object",  "B. Method Resolution Order",  "C. Main Resolution Order" "D. Method Resolution Object"]
]
#print(opt_dict[0]);

def quiz():
  for index, val in enumerate(question_dict):
    #print(index)# 0
    #print("*****")
    #print(val)# "ques1"
    print(question_dict[val])
    for j in opt_dict[index]:
      print(j)
     # print(i[ques])    
quiz();
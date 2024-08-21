class QuizGame:
  def __init__(self):
    self.total_score = 5 
    self.answer_count = 0
    self.totalperc = 0
    
  def welcome(self):
    print("welcome to the quize game competition!!\n\n*************************************")
  def quiz1(self):
    quest1 = input("The ability of a class to acquire the attribtes and methods of another class is called ------ \n A. Inheretance \n B. Abstraction \n C. Polymophism \n D. Object \n Enter A/B/C/D: ")
    
    print(quest1)
    if quest1.upper() == "A":
      print("correct answer")
      self.answer_count += 1
      self.total_score = self.total_score - 4
      self.totalperc = 20
      #print("your current score is" + self.answer_count + "/"  self.total_score)
      print(f"Your current score is {self.answer_count}/{self.total_score}")

    else:
      print("Incorrect answer")
      self.total_score = self.total_score - 4
      print(f"your current score is {self.answer_count}/{self.total_score}")
  
  def quiz2(self):
    quest2 = input("Which of the following is a type of inheritance? \n A. single \n B. Double \n C. Multiple\n D. Both A and C \n Enter A/B/C/D: ")
    
    print(quest2)
    if quest2.upper() == "D":
      print("correct answer")
      self.answer_count += 1
      self.total_score = self.total_score + 1
      self.totalperc += 20
      print(f"Your current score is {self.answer_count}/{self.total_score}")

    else:
      print("Incorrect answer")
      self.total_score = self.total_score + 1
      print(f"your current score is {self.answer_count}/{self.total_score}")
  
  def quiz3(self):
    quest3 = input("What type of inheritance has multiple subclases to a single subclass? \n A. Multiple inheritance \n B. Multilevel inheritance \n C. Heirachical\n D. None of the above\n Enter A/B/C/D: ")
    
    print(quest3)
    if quest3.upper() == "C":
      print("correct answer")
      self.answer_count += 1
      self.total_score = self.total_score + 1
      self.totalperc += 20
      print(f"Your current score is {self.answer_count}/{self.total_score}")

    else:
      print("Incorrect answer")
      self.total_score = self.total_score + 1
      print(f"your current score is {self.answer_count}/{self.total_score}")
      
  def quiz4(self):
    quest4 = input("What is the depth of multilevel inheritance in python? \n A. Two leve \n B. Three level  \n C. Any level\n D. None of these\n Enter A/B/C/D: ")
    
    print(quest4)
    if quest4.upper() == "C":
      print("correct answer")
      self.answer_count += 1
      self.total_score = self.total_score + 1
      self.totalperc += 20
      print(f"Your current score is {self.answer_count}/{self.total_score}")

    else:
      print("Incorrect answer")
      self.total_score = self.total_score + 1
      print(f"your current score is {self.answer_count}/{self.total_score}")
      
  def quiz5(self):
    quest5 = input("What does MRO stand for? \n A. Method recursive Object\n B. Method Resolution Order \n C. Main Resolution Order\n D. Method Resolution Object \n Enter A/B/C/D: ")
    
    print(quest5)
    if quest5.upper() == "B":
      print("correct answer")
      self.answer_count += 1
      self.total_score = self.total_score + 1
      self.totalperc += 20
      print(f"Your current score is {self.answer_count}/{self.total_score}")

    else:
      print("Incorrect answer")
      self.total_score = self.total_score + 1
      print(f"your current score is {self.answer_count}/{self.total_score}")
    print(f"your total score is {self.totalperc}%") 
     
wel = QuizGame()
wel.welcome();
wel.quiz1();
wel.quiz2()
wel.quiz3();
wel.quiz4();
wel.quiz5();

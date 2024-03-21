class Student:
    def __init__(self, name, age, curs, mark, mark2, amark, amark2):
        self.name = name
        self.age = age
        self.curs = curs
        self.mark = mark
        self.mark2 = mark2
        self.amark = amark
        self.amark2 = amark2
        # self.mark = 89
        # self.mark2 = 79
    
    def increase_year(self):
        self.age += 1
        self.curs += 1

    def update_grade(self):
          self.mark = 79
          l = [self.mark,89]
          sum = 0
          for num in l:
               sum += num       
          self.amark = sum / len(l)
          self.mark2 = 65
          ll = [self.mark2,88]
          sum2 = 0
          for num in ll:
               sum2 += num       
          self.amark2 = sum2 / len(ll)
              
    def get_info():
            s = Student("Nikita", 18, 1, 0, 0, 0, 0)
            s2 = Student("Vova", 19, 2, 0, 0, 0, 0)
            s.update_grade()
            s2.update_grade()
            s.increase_year()
            s2.increase_year()
            print(s.name,s.age,s.curs,s.mark,s.amark, s2.name, s2.age, s2.curs,s2.mark2, s2.amark2)
s = Student
s3 = Student
s3.get_info()
"""Exercise 2 (Folder 9 ex_2.py)
1. Write a class called Student with the attributes name (str) and
studyProgram (str)
2. Create three instances. One for yourself, one for your left neighbour and one
for our right neighbour.
3. Add a method printInfo that prints the name and studyProgram of a
Student. Test your method on the objects!
4. Modify the code and add age and gender to the attributes. Modify your
printing methods respectively too."""


class Student:
    def __init__(self, name: str, studyprogram:str):
        self.name : str = name
        self.studyprogram : str = studyprogram
        self.age = None
        self.gender = None

    def __str__(self) ->str:
        if self.age and self.gender:
            return f"il nome dello studente è {self.name},gender {self.gender},ha {self.age} e segue il programma di {self.studyprogram},"
        else:
            if self.age:
                return f"il nome dello studente è {self.name},ha {self.age} e segue il programma di {self.studyprogram},"
            elif self.gender:
                return f"il nome dello studente è {self.name},gender {self.gender} e segue il programma di {self.studyprogram},"
            else:
                return f"il nome dello studente è {self.name} e segue il programma di {self.studyprogram},"
                
    def gender_age(self, gender : str, age : int):
        self.gender = gender
        self.age  = age

marco = Student("Marco D.", "Cloud")
print(marco)
filippo = Student("Filippo G.", "Cloud")
print(filippo)
gaia = Student("Gaia F.", "FullStack")
print(gaia)
marco.gender_age("M",23)
filippo.gender_age("M",21)
gaia.gender_age("F",23)
print(marco)



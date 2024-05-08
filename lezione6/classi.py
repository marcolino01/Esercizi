class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    

    def __str__(self) -> str:
        return f"Person(name={self.name},age={self.age},height={self.height},weight={self.weight})"
    


alice = Person("Alice W.", 45, 156, 48)
bob = Person("Bob M.", 36, 180, 86)

if alice.age > bob.age:
    print(alice)
else:
    print(bob)

person_list : list = []
marco = Person("Marco D.", 23, 173, 71)
lorenzo = Person("Lorenzo P.", 22, 176, 76)
stefano = Person("Stefano R.", 54, 176, 78)
person_list.append(alice)
person_list.append(marco)
person_list.append(bob)
person_list.append(lorenzo)
person_list.append(stefano)

min_age : int = float('inf')
index_min_age : int = 0
for i in range(len(person_list)):
    if person_list[i].age < min_age:
        min_age = person_list[i].age
        index_min_age = i
persone = person_list[index_min_age]
print(f"il nome della persona più giovane è {persone}")




class Person:
    #yapıcı metodlar(constructor)
    def __init__(self,name,surname,year):
        #object attributes
        self.name=name
        self.surname=surname
        self.year=year
    #instance methods
    def intro(self):
        return f"benim adım {self.name} ve soyadım {self.surname}"
    def calculate_age(self):
        return f"{2022-self.year}"
p1=Person("Uğur","Kara",1983)
p2=Person("Dilan","Yaşar",1999)
print(p1.intro())
print(p2.intro())
print(p1.calculate_age())
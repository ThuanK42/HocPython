''' Ke thua lop,phuong thuc giong extend ben java '''

''' lop cha'''


class Father:
    def name(self):
        print('dmmmmm')


'''extend lop nao thi dua lop do vao ngoac tron'''


class Son(Father):
    def age(self):
        print('mother fucker')


t = Son()
t.name()
t.age()

"Ke thua nang cao: ke thua luon thuoc tinh cua thang cha trong lop con"


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("chao may, t ten la: ", self.name, ', tuoi t la: ', self.age)


class Student(Person):
    def __init__(self, name, age, grade):
        Person.__init__(self, name, age)
        self.grade = grade

    def info_grade(self):
        print('lop cua t la: ', self.grade)

hsa = Student('Phong hao dau la','90','Su Lai Khac')
hsa.info()
hsa.info_grade()
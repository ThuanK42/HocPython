''' Tao than chuong trinh '''

""" __init__ tu khoa bat buoc khi khoi tao constructor, ko duoc dung return
    self: bat buoc (no tro den doi tuong minh new ra)
    __str__ in doi tuong ra, thuc ra meo biet no dung de lam gi
    __del__ xoa doi tuong
"""


class Tuong:
    def __init__(self, ten, thong, vo, tri):
        print('Ten: ', ten, 'Thong: ', thong, 'Vo: ', vo, 'Tri: ', tri)

    def __str__(self):
        return '-' * 50

    def __del__(self):
        print('May da xoa data roi do =...=')


class SatPhaLang:
    def __init__(self, name, age):
        self.age = age
        self.name = name
    def info2(self):
        print(self.name,self.age)


tu_hoang = Tuong('Tu Hoang', 123, 98, 87)
print(tu_hoang)

tu_hoang2 = Tuong('Tu Hoang', 123, 98, 88)
del tu_hoang2

spl = SatPhaLang('sat pha lang',22)
spl.info2()

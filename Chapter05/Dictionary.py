'''Tim hieu ve Dictionary'''

a = {"Skill": "Phần Thiên Quyết", "Skill_2": "Bát Cực Băng", "Skill_3": 'Hoàng Tuyền Thiên Nộ',
     "Skill_4": "Thiên Băng Địa Liệt Trảm", "Skill_5": "Qủy Phủ Thần Công"}

# type(a): Xac dinh kieu du lieu
print('Kieu du lieu cua a la: ', type(a))

# id(a): Xac dinh id cua a
print('id cua a la: ', id(a))

# len(a): Tong so phan tu cua dict
print('Do dai cua a: ', len(a))

# dict['key']: Lay gia tri cua key
print('gia tri cua key Skill_2: ', a['Skill_2'])

# del dict[index]: Xoa phan tu o vi tri index
del a['Skill_5']
print(a)

# dict.keys(): Lay ra khoa cua dictonary
print('Cac khoa trong dictionary da cho la: ', a.keys())

# dict.values(): Lay ra gia tri cua dictionary
print('Cac value trong dictionary da cho la: ', a.values())

# dict.items(): Hien thi day du key va value cua dictionary
print('Cac item trong dictionary da cho la: ', a.items())

t = a.items()
for item2 in t:
    print(item2[0])

'''
- Chu y:
+ Khong the them phan tu theo kieu dict = dict + dict trong dictionary
+ No se loc cac phan tu trung key
+ Chuyen tu dict -> list no se bo phan value
'''

diem = dict(A=11, B=12, C=99)
print(diem)
print(list(diem))

result = {i: i ** 2 for i in range(10)}
print(result)

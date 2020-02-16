'''Kien thuc ve Tuple co ban'''

a = (1,9,8,3,6,5,7)

#type(a): Xac dinh kieu du lieu cua a
t = type(a)
print(t)

#id(a): Xac dinh id cua a
t=id(a)
print(t)

#tuple[index]: lay gia tri phan tu tai vi tri index
t = a[2]
print(t)

# lap lai nhieu 1 tuple = cach: tuple +tuple=... hoac tuple = tuple * n => Cong don
a=a*4
print(a)

# lay 1 doan trong mang tuple da cho: tuple[from:To] -> from <=x<To
'''hieu de hon cai from dem tu 0 con cai to dem tu 1'''
'''from dem tu 0 ta dc 8, To dem tu 1 ta dc 6 : cach hieu 1'''
''' cach hieu 2: 2<=x<5. cai nay 2 dau deu tinh tu 0'''
print(a[2:5])
print(a[3:])
print(a[:10])

#Gop tuple con va list con
'''vd: 2 tuple'''
t0 = (1,2,3)
t1=(4,5,6)
t = (t0,t1)
print(t)

'''vd: 1 tuple + 1 list'''
t2 = ('quang','hieu','son')
t3 = ['quynh','ha','huyen']
t =(t2,t3)
print(t)

#Chu y: trong tuple khong duoc phep thay doi gia tri vd: tuple[index]=x
'''Co the thay gia tri bang cach nhu sau chu y doi voi lisst thoi'''

l1 =[1,3,5]
t = (7,9,11)
t5 = (0,2,4,l1,t)
print(t5)
'''gio t duoc 1 tuple (0,2,4,[1,3,5],(7,9,11)). Chu y thang nay co 5 phan tu la 0,2,4 va [1,3,5] va (7,9,11)'''
'''gio ta thay doi 5 = 99 nhu sau, thang nay list nen moi doi duoc'''
t5[3][2]=99
'''tai sao la t5[3][2]. vi 3 la vi tri list trong tuple, so 2 la vi tri cua 5 trong list'''
print(t5)

'''Tim hieu ve doi tuong sets'''

a = {11, 33, 55, 77, 88, 99}

# type(a): xac dinh kieu du lieu
print(type(a))

# id(a): xac dinh id cua du lieu
print(id(a))

# len(a): xac dinh do dai mang
print(len(a))

'''Chu y: Sets khong duoc phep dung index vi du nhu set[index]'''

'''Neu muon lay index cua 1 gia tri trong sets thi minh phai gan index cho phan tu do trong set'''
'''Quen noi sets no se sap xep day so theo trat tu ngau nhien nhu o day'''
'''a sau khi sap xep se la: 33,99,11,77,55,88'''
'''b1: gan index cho tung phan tu trong sets'''
b, c, d, e, f, g = a
'''b=33,c=99,...'''
print(b)

"""=> Sets co dac diem la lay diem chung, bo phan thua, sap sep gia tri tang dan (a->z,0->9)"""
# set('abbcccddddeeeee') -> ('a','b','c','d','e')
s1 = set('aaalllppppoqqqqq')
print(s1)

'''linh tinh: kiem tra 1 ky tu co trong list da cho hay ko'''
print('a' in s1)

# A,B : {{},{}}
A = {1, 2, 3, 4}
B = {5, 6, 7, 8}
T = A, B
print('A,B: ', T)
print(type(T))

# A-B: Loai bo nhung phan tu trong SetA ma SetB co
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8}
T = A - B
print('A - B: ', T)
print(type(T))

# A|B: Gop 2 set lai voi nhau va loai bo phan tu set A da co
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8}
T = A | B
print('A | B: ', T)
print(type(T))

# A&B: lay diem chung
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8}
T = A & B
print('A & B: ', T)
print(type(T))

# A^B: gop lai roi bo phtu trung nhau
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8}
T = A ^ B
print('A ^ B: ', T)
print(type(T))

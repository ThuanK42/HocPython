''' Danh sach method cua list'''

'''Khai bao list'''

l = [1, 2, 3, 4, 5]

print(type(l))
l + [10]
print(l)

# list.append(value): Them phan tu vao cuoi list
l.append(32)
print(l)
# list.insert(index,value): Them phan tu vao tri index + 1 (mang dem tu 1)
l.insert(3, 34)
print(l)

# list.pop(index): Xoa phan tu o vi tri index
l.pop(3)
print(l)

# list.count(value): Dem so lan xuat hien cua phan tu
t = l.count(3)

print('So lan xuat hien cua so 3 trong ds la: ', t)
# list.sort(): Sap xep theo thu tu tang dan
l2 = [9, 7, 5, 3, 1, 2]
l2.sort()
print(l2)

l3 = ['Bảo','Đao','Đồ','Long']
l3.sort()
print(l3)

# list.reverse(): Dao nguoc vi tri phan tu
l.reverse()
print(l)

# del list[from:to]: Xoa phan tu tu vi tri from -> to (fron <=x<to)
del l[0:2]
print(l)

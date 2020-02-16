''' Toi uu code trong python '''

l = []

for item in range(10):
    l.append(item ** 2)

print(l)

''' cach them phan tu khac vao mang thay the ham append la ghi truoc for'''
'''vd 1:'''
l = [item2 ** 2 for item2 in range(10)]
print(l)

'''vd 2:'''
l2 = [item3 for item3 in l if item3 % 2 == 0]
print(l2)

'''vd linh tinh ve mang'''
la=[1,2,3]
lb=[4,5,6]
lc=[]
for x in la:
    for y in lb:
        lc.append((x,y))
print(lc)

'''-> ghi ngan gon lai cai tren'''
la=[1,2,3]
lb=[4,5,6]
lc2=[(x,y) for x in la for y in lb]
print(lc2)


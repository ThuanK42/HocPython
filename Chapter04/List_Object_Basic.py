'''Kien thuc co ban ve doi tuong List'''

""" List -> []"""
l=[1,2,3,4,5,6,7,8,9]

#type(a): Xac dinh kieu du lieu

#id(a): Xac dinh id cua du lieu

#len(list): Chieu dai cua list
print("Độ dài list đã cho là: ",len(l))

#list[n]: lay ra gia tri cua phan tu thu n trong list, phai qua trai tinh tu -1, trai qua phai tinh tu 0
print("Gía trị của phần tử thứ 2 trong list là:",l[2])

'''Python có thể mảng cộng, nhân,.. mảng được'''
print(l+l)

#list[index]= value: Cap nhat gia tri moi cho list
'''cap nhat vi tri thu 2 trong list thanh 2 (3->2)'''
l[2]=2
print(l)

#list[from:to]: lay ra day so tu from<=x<to
'''2<=x<5'''
print(l[1:4])

'''1 vai vi du khac'''
'''cap nhat phan tu va cong luon vao mang'''
l = [1,2,3,4]
l = l+[l[3]+1]
print(l)

l = l + [6]
print(l)

t = range(5,19,3)
print(list(t))

#string[:to]: Lay chu tu 0 den vi tri to



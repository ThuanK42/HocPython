''' Ham Range tao ra 1 day so'''

# Range(n), n la so phan tu cua day so tu nhien bat dau tu 0
x = range(15)
'''x la mang chua gia tri tu 0->14'''
print(type(x))
''' in x ra co nhieu cach: cach1: gan no cho list'''
print(list(x))
'''cach 2 dung vong lap for'''
for item in x:
    print(item)

# range(a,b) -> in ra gia tri x : a<=x<b
y = range(6, 9)
print(list(y))

#range(a,b,c) -> in ra gia tri a<=x<b, moi phan tu cach nhau c gia tri
print(list(range(1,10,2)))


# Trong python bao gom cac phep so sanh sau; >,<,>=,<=,==,!=
# Kiem tra doi tuong nay co phai la doi tuong kia: is
# Kiem tra doi tuong nay co nam trong day ky tu: in
xx = 15.0
x = 15
print(xx == x)
a = type(xx)
b=id(xx)
c = type(x)
d=id(x)
print(a,b,c,d)

# kiem tra dua nay co phai la dua kia khong
m=10
n=10
print(type(m),id(m),type(n),id(n))
print(m is n)

# kiem tra dua nay co nam trong dua kia khong

A = [1,8,3,5,10]
a = 8
print(a in A)
B = "Le Van Thuan"
b = "Thuan"
print(b in B)
print("thuan" in B)

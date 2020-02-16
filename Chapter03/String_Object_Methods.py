'''Bai nay se noi ve nhung method co ban voi string cua Python'''

chuoi = 'lê văn thuận'

# tenchuoi.capitalize(): In hoa các chữ đâu tiên của chuỗi
print(chuoi.capitalize())

# tenchuoi.upper(): In hoa toàn bộ chuỗi
print(chuoi.upper())

# tenchuoi.lower(): In thường toàn bộ chuỗi
print(chuoi.lower())

# tenchuoi.swapcase(): Chuyển đổi thường <-> hoa
print(chuoi.swapcase())

'''a = tong so ky tu trong chuoi sau khi them ky tu b vao chuoi ban dau'''
# tenchuoi.ljust(a,b): thêm vào sau mỗi chuỗi ký tự với tổng số phần tử bao gồm luôn chuỗi gốc.
string = 'chuoi'
print(string.ljust(9, 'a'))

# tenchuoi.rjust(a,b): thêm vào trước mỗi chuỗi ký tự với tổng số phần tử bao gồm luôn chuỗi gốc
string = 'chuoi'
print(string.rjust(9, 'a'))

# tenchuoi.center(a,b): thêm vào trước và sau mỗi chuỗi ký tự với tổng số phần tử bao gồm luôn chuỗi gốc
string = 'chuoi'
print(string.center(10, 'a'))

# tenchuoi.lstrip() or tenchuoi.lstrip('*'): huy bo khoang trang hoac ky tu ben trai
string2 = '                                         bảo đao đồ long'
print(string2.lstrip())
string21 = '********bảo đao đồ long fake'
print(string21.lstrip('*'))

# tenchuoi.rstrip() or tenchuoi.rstrip('*'): huy bo khoang trang hoac ky tu ben phai
string3 = 'hiệu lệnh thiên hạ       '
print(string3.rstrip())
string31 = 'diệt sát quần hùng*******'
print(string31.rstrip('*'))

# tenchuoi.strip() or tenchuoi.strip('*'): huy bo khoang trang hoac ky tu,.... xung quang chuoi
string4 = '  ỷ thiên kiếm diệt quần hùng        '
print(string4.strip())

# tenchuoi.find('chuoi can tim trong ten chuoi',start,end): Tim kiem tu trong 1 chuoi -> tra ve vi tri tu do trong chuoi
chuoi10 = 'I am super hero'
print(chuoi10.find("super"))
print(chuoi10.find("er", 9))
print(chuoi10.find("am", 1, len(chuoi10)))

# 'chuoi' in s: Kiem tra tu co trong 1 chuoi hay khong
print('hero' in chuoi10)

# chuoi.index('string'): Lay ra vi tri cua 1 tu dang tim
print(chuoi10.index('hero'))

# chuoi.replace(find,replace,index): Tim va thay the tu
chuoi11 ='Vạn đại quân sư Gia Cát Lượng'
print(chuoi11.replace("Gia Cát Lượng","Khổng Minh"))

# chuoi.isalnum(): Tra ve true neu chuoi co it nhat 1 ky tu(a->Z,0->9),false khi co ky tu dac biet, khoan trang
s = "Teo"
print(s.isalnum())
s1="Teo 123"
print(s1.isalnum())
s2=""
print(s2.isalnum())

# chuoi.isalpha(): Tra ve true neu chuoi khong co khoan trang va ky tu dac biet, so=>chuoi la chu auto true
s99 = 'Teo'
print(s99.isalpha())
s98='Teo123'
print(s98.isalpha())
s97='Teo$'
print(s97.isalpha())

# chuoi.isdigit(): Tra ve true neu chuoi la so
s96 = '123'
print(s96.isdigit())
s95='123qqq'
print(s95.isdigit())

# chuoi.isspace(): Tra ve true neu chuoi la khoan trang
s94 = " "
print(s94.isspace())

print("123 erwer ".isspace())
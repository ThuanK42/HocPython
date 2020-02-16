'''Tham khao trang https://pyformat.info'''

name = 'Lê Văn Thuận'
age='22'
status='Tôi tên là: '+name+". Tôi năm nay: "+age+" tuổi"
print(status)

#format(a,b,c,...): Thay thế các dấu {} trong chuỗi bằng các biến trong hàm format
status_chage='Tôi tên là: {} .Tôi năm nay: {} tuổi'.format("Lê Văn Thuận","22")
print(status_chage)

''' {n}: n la so thu tu cua cac bien trong format'''
status_chage_2='Hoc sinh 1: {2}, hoc sinh 2: {1}, hoc sinh 3: {0}'.format("Thuận","Quang","Hiếu")
print(status_chage_2)

'''dung format cho list thi phai bat buoc co dau * phia truoc de noi no la mang'''
ds = ["Thuận","Quang","Hiếu","Sơn","Hậu"]
status_chage_3 = 'Danh sách sinh viên khoa CNTT là: {3},{1},{0},{2}'.format(*ds)
print(status_chage_3)

#Noi chuoi trong format
'''Chu y: : la mac dinh,sau 2 cham la ky tu can them, ><^ trai,phai,giua, 20 la tong so ky tu sau khi them vao chuoi'''
'''vd: them 5 dau gach ben phai chuoi abcdef'''
print('{:-<11}'.format("abcdef"))
'''vd: them 5 dau gach ben trai chuoi abcdef'''
print('{:->11}'.format("abcdef"))
'''vd: them 5 dau gach vao 2 ben chuoi abcdef'''
print('{:-^11}'.format("abcdef"))

# Truyen so vao chuoi trong format nho dung :d (d la digit)
status_chage_4 = "Mã số sinh viên của tôi là: {0:d}".format(16130606)
print(status_chage_4)

# dung de ngan cach cac con so chang han
status_chage_5=2000000000000
print("{:,}".format(status_chage_5))
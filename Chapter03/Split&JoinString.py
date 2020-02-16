''' Thao tac noi va cat chuoi'''

chuoi = 'Bảo đao đồ long hiệu lệnh thiên hạ, Ỷ thiên kiếm diệt sát quần hùng'

# chuoi.split(): Cat chuoi dua vao khoan trang => result: mảng các chuỗi đã loại bỏ khoản trắng
print(chuoi.split())

# chuoi.split('a'): Cat chuoi dua vao ky tu a
print(chuoi.split('a'))

# chuoi.split('',number): cat chuoi dua vao ky tu va so lan cat
'''cat chuoi theo khoan trang 3 lan'''
print(chuoi.split(' ', 3))

# chuoi.join(list): Gop list thanh chuoi -> them vao sau moi phan tu trong chuoi 1 tu gi do, nhu o duoi la khoan trang
ll = chuoi.split();
k = ' '
print(k.join(ll))

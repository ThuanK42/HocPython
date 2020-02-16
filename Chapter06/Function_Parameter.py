''' hoc tao function ban'''

"""
- Chu y
+ Dat bien trong funtcion neu muon truyen tham so cho funtcion lun thi phai dat tu phai sang trai
+ input muon truyen nhieu bien thi them * vao truoc bien input, tam hieu no bien thanh mang
+ * la 1 gia tri, ** la 2 gia tri (vi du (a): la 1 gia tri nhung (a=2) thi no la 1 key:value tuc la 2 gia tri)
"""


def tong_3_so(a, b, c):
    return print('Tong cua ', a, b, c, 'la: ', a + b + c)


tong_3_so(1, 4, 7)


def tong(n1, n2, n3=100):
    return print('sum = ', n1 + n2 + n3)


tong(4, 21)


def tong_n_so(*data):
    t = 0
    for item in data:
        t += item
    return t


print('tong n so: ', tong_n_so(10, 20, 900000))

'''vd: neu tham so truyen vao la nhieu list nho thi sao'''


def tong_list(*mang_lon):
    ''' dau qua nhieu mang nho thi dau ra cung phai la mang'''
    ketqua = []
    for mang_nho in mang_lon:
        tong = 0
        for item in mang_nho:
            tong += item
        ketqua.append(tong)
    return ketqua


t = tong_list([1, 2, 3], [4, 5], [7, 8, 9])
print(t)

''' ham nay hay su dung'''


def in_ra_tong_tien_sp(**data):
    tien = 0
    for name, price in data.items():
        ''' co 2 cai {} la vi co 2 gia tri trong format'''
        row = "{:20}{:10}".format(name, price)
        print(row)
        tien += price
    print("-" * 30)
    return print("{:20}{:10}".format("Tong tien: ", tien))


in_ra_tong_tien_sp(nokia=21000, samsung=2019119, bphone=2020202)


def tong_di_dang(n1, n2, n3, *mang, **dict):
    t1 = n1 + n2 + n3
    t2=0
    t3=0
    for item in mang:
        t2 = t2 + item
    for k, v in dict.items():
        t3 = t3 + v
    tong=[t1,t2,t3]
    return tong


print(tong_di_dang(100,200,300,1,23,4,4,3,43,434,v1=11,v2=222,v3=3333))

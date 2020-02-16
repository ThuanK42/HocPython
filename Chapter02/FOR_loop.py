'''duyet phan tu don gian trong for'''
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 1111)
for n in a:
    print(n, end=' ')

b = (1, 8, 7, 6, 5)
i = 0
for n in b:
    print(i)
    i += 1

'''duyet array dang dictionaries'''
dit = {'Thuan': 20, 'Quang': 21, 'Son': 33, 'Thuy': 21}
''' moi phan tu trong dict co 2 gia tri la key:value'''
for key in dit:
    print(key)
'''truy cap gia tri value cua tung key trong tung phan tu'''
for key in dit:
    print(dit[key])

'''duyet tung phan tu trong 1 chuoi'''

name = 'Lee Van Thuan'
for tung_phan_tu in name:
    if tung_phan_tu != ' ':
        print(tung_phan_tu * 10)

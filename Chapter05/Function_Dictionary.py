''' Function trong Dictionary '''

dict={
    'name':'Le Van Thuan',
    'age':22,
    'live':'Nha Trang, Khanh Hoa',
    'phone':'0983172229'
}

#type(a): Kieu du lieu
print(type(dict))

#id(a): ID cua du lieu
print(id(dict))

#len(a): do dai hay tong so phan tu cua dict
print(len(dict))

#dict['key']: gia tri cua key
print(dict['live'])

#dict['key'] = b: Gan gia tri key = b
dict['age']=23
print(dict['age'])

#del dict['key']: xoa phan tu co khoa la key
del dict['age']
print(dict)

'''in va not in trong dictionary'''

print('live' in dict)
print('age' not in dict)

#dict.clear(): xoa sach dict
dict.clear()
print(dict)

#dict.pop('key'): xoa phan tu
dict={
    'name':'Le Van Thuan',
    'age':22,
    'live':'Nha Trang, Khanh Hoa',
    'phone':'0983172229'
}
print(dict.pop('name'))

#dict.popitem(): xoa ngau nhien phan tu
dict={
    'name':'Le Van Thuan',
    'age':22,
    'live':'Nha Trang, Khanh Hoa',
    'phone':'0983172229'
}
print(dict.popitem())
print(dict)



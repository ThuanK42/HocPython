"""" Bai hoc co ban ve String trong Python"""

say='I love you,Trinh Trinh!'

#type(a) : xac dinh kieu du lieu
print(type(say))

#id(a): xac dinh id cua gia tri a
print(id(say))

#len(a): lay do dai chuoi a
print(len(say))

#tenchuoi[index]: lay chu o vi tri thu index trong ten chuoi
'''chu y: Python no cung coi 1 chuoi la la 1 mang string'''
'''Chu y: Lay phai qua trai thi la so am, con lay tu trai qua phai la so duong'''
'''vd: nhu chuoi say tren minh se lay chu T vi tri 11 nhu sau'''
print(say[11])

'''=> Khong the thay the ky tu trong chuoi o bai hien tai. vd say[0]=BBB la khong the duoc'''

#tenchuoi[from:to]: lay chu tu vi tri from den vi tri to
print(say[11:16])

#tenchuoi[from:]: lay chu tu vi tri from den het
print(say[11:])

#tenchuoi[:to]: lay chu tu 0 den vi tri TO
print(say[:10])



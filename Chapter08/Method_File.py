f = open("data/1.txt", "r")

#file.tell() cho biet doc toi vi tri nao trong file
fpos = f.tell()
print("doc toi vi tri thu", fpos)

line = f.readline()
print(line, end="")
fpos = f.tell()
print("Doc toi vi tri", fpos)

'''
line = f.readline()
print(line, end="")
fpos = f.tell()
print("Doc toi vi tri", fpos)
'''

#f.seek() dua con tro chuot toi vi tri minh can, bat dau doc tu vi tri ay

f.seek(239)
print("-"*39)
data = f.read()
print(len(data))
print(data)





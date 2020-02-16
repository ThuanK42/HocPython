''' dem ky tu trung lap, ket qua dua vao dict ('ky tu':so lan trung lap)'''


def countChar(*data):
    dic = {}
    for item in data:
        for i in item:
            i = i.upper()
            if i in dic:
                dic[i] = dic[i] + 1
            else:
                dic[i] = 1
    return dic


print(countChar("Toi", "hoc", "Python"))

'''viet lai ham range truyen tu 1-> 3 tham so tuy y nhung van dung'''


def rangeCustomize(*data):
    start = length = step = 0
    if (len(data) == 3):
        start = data[0]
        length = data[1]
        step = data[2]
    elif (len(data) == 2):
        start = data[0]
        length = data[1]
        step = 1
    else:
        start = 0
        length = data[0]
        step = 1
    i = start

    while i < length:
        print(i)
        ''' yield giong return, no tao ra 1 ham (generator) rieng de luu tru gia tri
            , va the la khi return thi no tra ve mang, vi vay ket qua cua ham nay thanh list
             Tom lai, return tra ve 1 lan roi dung, con yield thi no tra xong no chay lai lien tuc'''
        yield i
        i = i + step


a = rangeCustomize(0, 5, 2)
b = rangeCustomize(0, 5)
c = rangeCustomize(5)

print(list(a))
print(list(b))
print(list(c))


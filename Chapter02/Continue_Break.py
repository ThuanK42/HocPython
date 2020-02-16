for letter in 'Python':
    if letter != 'h':
        print(letter)

''' gap continue no se nhay toi vong lap ke tiep va khong chay cac lenh phia sau no trong luot do'''

for letter2 in 'Le Van Thuan':
    if letter2 == 'a':
        ''' neu ky tu = a thi no se toi vong lap ke tiep, ko thuc thi cau lenh phia duoi no nua'''
        continue
    print(letter2)

''' break dung luon vong lap '''

for letter2 in 'Python':
    if letter2 == 'h':
        break
    print(letter2)
    
''' Function trong Python'''

""" Funtcion: cong thuc chung def tenfunction(): lam gi do"""


def helloWord():
    print('Hello_2_3')


''' muon goi ham chi viec go ten ham'''
helloWord()


def sayGoogbye():
    print('Googbye.See you later !')
    return 'Ahiihi'


print(sayGoogbye())


def sayGoogbye2():
    return ('Googbye.See you later !')


print(sayGoogbye2())

bye = sayGoogbye2()
print(bye)


def ahihi(n):
    i = 0
    while i < n:
        print('ocshossss')
        i += 1


ahihi(12)
""""
- Chu y:
+ Chi dung return khi muon lay gia tri ham do de dung cho nhung cong viec khac 
"""

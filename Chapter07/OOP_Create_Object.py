''' Dac diem co ban cua doi tuong trong Py thon'''

"""
- Dac diem:
+ Doi tuong la thuc the cua class
+ Thuoc tinh (variable): dac diem cua doi tuong
+ Hanh dong (function): hanh dong cua doi tuong
vd: chim co dac diem la co long vu, dau, canh, mat, mo, hanh dong: bay, nhay , an ngu,...
"""


class Warrior:
    name = ''
    thong = 0
    vo = 0
    tri = 0
    ''' self no chi den doi tuong hien tai, hay object luc minh neu ra'''

    def info_tuong(self):
        print('Tuong: ' + tuong.name
              , 'Thong: ', tuong.thong
              , 'Vo: ', tuong.vo
              , 'Tri: ', tuong.tri)

    def hieu_ung_skill(self, ten_skill, dac_diem_skill):
        print('Ky nang', ten_skill, dac_diem_skill)


tuong = Warrior()
tuong.name = 'Tu Hoang'
tuong.thong = 100
tuong.vo = 90
tuong.tri = 87
ky_nang = 'Liet dia'
dac_diem_ky_nang = ': Chem manh vao dat, gay sat thuong vat ly bang 120% diem thong hien tai cua tuong'

tuong.info_tuong()
tuong.hieu_ung_skill(ky_nang, dac_diem_ky_nang)

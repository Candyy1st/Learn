"""
A = 80-100
B = 70-79
C = 60-69
D = 40-59
E = 0-39
"""

jawab = 'y'
while jawab == 'y':
    nAngka = int(input('Masukkan Nilai : '))
    if nAngka >= 80 and nAngka <= 100:
        nHuruf = 'A'
    elif nAngka >= 70 and nAngka <= 79:
        nHuruf = 'B'
    elif nAngka >= 60 and nAngka <= 69:
        nHuruf = 'C'
    elif nAngka >= 40 and nAngka <= 59:
        nHuruf = 'D'
    elif nAngka >= 0 and nAngka <= 39:
        nHuruf = 'E'
    else:
        nHuruf = 'Angka yang dimasukkan tidak Valid'
    print(f'Nilai {nAngka} = {nHuruf}')
    print('Ulangi lagi (y/n) ? ')
    jawab = input()


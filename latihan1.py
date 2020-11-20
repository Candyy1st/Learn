"""
Golongan    Gaji Pokok  Potongan
A          10.000.000   2.5%
B           8.500.000   2.0%
C           7.000.000   1.5%
D           5.000.000   1.0%
"""

kKar = int(input('Masukkan Kode Karyawan    : '))
nKar = str(input('Masukkan Nama Karyawan    : '))
nGol = str(input('Masukkan Golongan         : '))

status = 1
if status == 1:
    if nGol == 'A':
        gPok = '10000000'
        per = 2.5
        pot = 0.025
        pPot = int(pot * int(gPok))
        gTot = int(int(gPok) - pPot)
    elif nGol == 'B':
        gPok = ' 8500000'
        per = 2.0
        pot = 0.02
        pPot = int(pot * int(gPok))
        gTot = int(int(gPok) - pPot)
    elif nGol == 'C':
        gPok = ' 7000000'
        per = 1.5
        pot = 0.015
        pPot = int(pot * int(gPok))
        gTot = int(int(gPok) - pPot)
    elif nGol == 'D':
        gPok = ' 5000000'
        per = 1.0
        pot = 0.01
        pPot = int(pot * int(gPok))
        gTot = int(int(gPok) - pPot)
    else:
        gPok = 'Kode Golongan Tidak Valid'


print('=' * 80)
print('Struk Rincian Gaji Karyawan')
print('-' * 80)
print(f'Nama Karyawan                   : {nKar}                 (Kode : {kKar})')
print(f'Golongan                        : {nGol}')
print(f'Status (1:Menikah, 2:Lajang)    : {status}')
print('-' * 80)
print(f'Gaji Pokok                      : Rp. {gPok}')
print(f'Potongan ({per} %)                : Rp. {pPot}')
print('-' * 80)
print(f'Gaji Bersih                     : Rp. {gTot}')
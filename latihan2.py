a = int(input('Masukkan kode karyawan      : '))
b = str(input('Masukkan nama karyawan      : '))
c = int(input('Status (1:Menikah 2:Belum) : '))

if c == 1:
    c = 'Menikah'
    d = int(input('Jumlah Anak                 : '))
    gol = input('Masukkan golongan           : ')
    tun = int(0.1)
    tuna = int(0.05)
else:
    c = 'Lajang'
    d = 0
    gol = input('Masukkan golongan           : ')
    tun = 0
    tuna = 0

if gol == 'A':
    pota = '(25%)'
    gp = 10000000
    tun = (tun * gp)
    tuna = ((tuna * gp) * d)
    gk = gp + tun + tuna
    pot = 0.025 * gk
    gb = int(gk - pot)
elif gol == 'B':
    pota = '(2%)'
    gp = 8500000
    tun = (tun * gp)
    tuna = ((tuna * gp) * d)
    gk = gp + tun + tuna
    pot = 0.02 * gk
    gb = int(gk - pot)
elif gol == 'C':
    pota = '(15%)'
    gp = 7000000
    tun = (tun * gp)
    tuna = ((tuna * gp) * d)
    gk = gp + tun + tuna
    pot = 0.015 * gk
    gb = int(gk - pot)
elif gol == 'D':
    pota = '(1%)'
    gp = 5000000
    tun = (tun * gp)
    tuna = ((tuna * gp) * d)
    gk = gp + tun + tuna
    pot = 0.01 * gk
    gb = int(gk - pot)
else:
    pota = '(- %)'
    gp = '-'
    tun = '-'
    tuna = '-'
    gk = '-'
    pot = '-'
    gb = '-'
    print()
    print('Golongan yang anda masukkan tidak sesuai input')
    
    
print()
print('======================================================================')
print('                     Struk Rincian Gaji Karyawan')
print('----------------------------------------------------------------------')
print('Nama Karyawan      :', b, '          Kode : ', a)
print('Golongan           :', gol)
print('Status             :', c)
print('Jumlah Anak        :', d)
print('----------------------------------------------------------------------')
print('Gaji Pokok         : Rp.', gp)
print('Tunjangan Pasangan : Rp.', tun)
print('Tunjangan Anak     : Rp.', tuna)
print('----------------------------------------------------------------------')
print('Gaji Kotor         : Rp.', gk)
print('Potongan           : Rp.', pot, pota)
print('----------------------------------------------------------------------')
print('Gaji Bersih        : Rp.', gb)
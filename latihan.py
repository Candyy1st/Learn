a = int(input('Masukkan Nilai Bahasa Indonesia : '))
b = int(input('Masukkan Nilai IPA : '))
c = int(input('Masukkan Nilai Matematika : '))

if (a>=0 and a<=100) and (b>=0 and b<=100) and (c>=0 and c<=100):
    if a>= 60 and b>=60 and c>70:
        print('Lulus')
    else:
        print('Tidak Lulus')
        if 'Tidak Lulus':
            print('Sebab :')
            if a<60:
                print(f'Nilai B.Indo : {a}')
            if b<60:
                print(f'Nilai IPA : {b}')
            if c<70:
                print(f'Nilai Matematika : {c}')
else:
    print('Ada nilai yang tidak sesuai')
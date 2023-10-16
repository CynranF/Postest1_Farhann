def login():
    while True:
        print("*****HALAMAN LOGIN*****")
        Nama = str(input("Silahkan Masukkan Nama anda: "))
        NIM = int(input("Silahkan Masukkan NIM anda: "))        
        PIN = int(input("Silahkan Masukkan PIN anda: "))
        if Nama == "Farhan" and NIM == 2309116028 and PIN == 2005:
            print("Login Berhasil")
            return True
        else:
            print("Data yang anda masukkan salah")

berhasil_login = login()
if berhasil_login:
    print('Selamat Datang di program menghitung volume bangun ruang')
    print('Silahkan Memilih Bangun ruang')
    print('1. Bola')
    print('2. Tabung')
    print('3. limas segita')
    
    Operasi = str(input('pilihlah salah satu operasi (1,2,3) -->'))
    if Operasi == '1':
        JariJari = float(input('Masukan Jari-Jari: '))
        if JariJari %7 == 0:
            phi = 22/7
        elif JariJari %7 != 0:
            phi = 3.14
        Hasil = 4/3 * phi * JariJari**3
        print(f'Volume dari Bolanya adalah {Hasil}')
    if Operasi == '2':
        JariJari = float(input('Masukan Jari-Jari: '))
        if JariJari %7 == 0:
            phi = 22/7
        elif JariJari %7 != 0:
            phi = 3.14
        Tinggi = float(input('Masukkan Tinggi: '))
        Hasil = phi * JariJari**2 * Tinggi
        print(f'Volume dari tabungnya adalah {Hasil}')
    if Operasi == '3':
        Alas = float(input('Masukkan luas alas: '))
        Tinggi = float(input('Masukkan tinggi limas: '))
        Hasil = 1/3 * Alas * Tinggi
        print(f'Volume dari Limas Segitanya adalah {Hasil} ')
        

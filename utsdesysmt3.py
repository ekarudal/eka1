class Student:

    Jumlah_Umur = 0
    Jumlah_Berat_Badan = 0

    def __init__(self, Nama, Umur, Tinggi, Berat, Jenis_Kelamin):
        self.Nama = Nama
        self.Umur = Umur
        self.Tinggi = Tinggi
        self.Berat = Berat
        self.Jenis_Kelamin = Jenis_Kelamin

        Student.Jumlah_Umur += self.Umur
        Student.Jumlah_Berat_Badan += self.Berat

    def Belajar(self, Pelajaran):
        print(self.Nama, "sedang belajar ", Pelajaran)

    def Membaca(self, Buku):
        print(self.Nama, 'sedang membaca ', Buku)

    def Berdiri(self, kursi):
        print(self.Nama, 'sedang berdiri di', kursi)

    def Berjalan(self, Tujuan, Teman):
        print(self.Nama, 'sedang berjalan ke', Tujuan, 'bersama', Teman.Nama)


Desy = Student('Desy', 19, 157, 49, "Perempuan")
Dedi = Student('Dedi', 24, 160, 59, "laki-Laki")
Erick = Student('Erick', 26, 168, 57, "Perempuan")

Desy.Belajar('Pemrograman Dasar')
Desy.Membaca('Buku Cerita')
Desy.Berdiri('Kursi')
Desy.Berjalan('Laboratorium', Dedi)
print("")
Dedi.Belajar('Pemrograman Dasar')
Dedi.Membaca('Buku Cerita')
Dedi.Berdiri('Kursi')
Dedi.Berjalan('Laboratorium', Erick)
print("")
Erick.Belajar('Pemrograman Dasar')
Erick.Membaca('Buku Cerita')
Erick.Berdiri('Kursi')
Erick.Berjalan('Laboratorium', Dedi)

print('\n')

print ("::::::: JUMLAH BERAT BADAN DAN UMUR :::::::")
print('berat badan: ', Student.Jumlah_Berat_Badan, "Kg")
print('umur: ', Student.Jumlah_Umur, "tahun")
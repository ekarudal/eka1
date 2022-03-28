class Student:
    def __init__ (self, nama, umur, tinggi, berat_badan, jenis_kelamin, buku):
        self.nama = nama
        self.umur = umur
        self.tinggi = tinggi
        self.berat_badan = berat_badan
        self.jenis_kelamin = jenis_kelamin
        self.buku = buku
      

    def belajar(self, matkul):
        print("Saat di kelas "+ self.nama+ " sedang asik belajar "+ matkul.buku+ " dengan teliti")

    def membaca(self, bacaan):
        print(self.nama+ " pada pagi ini sedang membaca buku "+ bacaan.buku+ " bersama bunda")
    
    def berdiri(self):
        print("Saat upacara bendera "+ self.nama+ " harus selalu berdiri dengan tegap")

    def berjalan(self):
        print(self.nama+ " dan pacarnya berjalan kaki menuju masjid itu")

student1 = Student("eka", 19, 171, 66, "laki-laki", "perkalian")
student2 = Student("Dedi", 24, 160, 59,"laki-laki", "sejarah kemerdekaan" )
student3 = Student("Erick", 26, 168, 57, "perempuan", "keagamaan")

print("----------------------- Student 1 ---------------------")
student1.belajar(student1)
student1.membaca(student1)
student1.berdiri()
student1.berjalan()

print("")
print("----------------------- Student 2 ---------------------")
student2.belajar(student2)
student2.membaca(student2)
student2.berdiri()
student2.berjalan()

print("")
print("----------------------- Student 3 ---------------------")
student3.belajar(student3)
student3.membaca(student3)
student3.berdiri()
student3.berjalan()

print("")
print("Jumlah berat badan total ketiganya :", student1.berat_badan + student2.berat_badan + student3.berat_badan, 'kg')
print("Jumlah umur total ketiganya        :", student1.umur + student2.umur +student3.umur, 'tahun')








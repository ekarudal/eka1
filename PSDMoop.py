class Departemen:
    jumlah_departemen = 0

    def __init__(self, departemen, jumlah_staf_magang, orang):
        self.departemen = departemen
        self.jumlah_staf_magang = jumlah_staf_magang
        self.orang = orang
        Departemen.jumlah_departemen += 1

    def tampilkan_info(self):
        print("Departemen :", self.departemen)
        print("Jumlah staf magang :", self.jumlah_staf_magang, self.orang)
        print()

PSDM = Departemen("PSDM", 11, "orang")
DAGRI = Departemen("DAGRI", 11, "orang")
HUBLU = Departemen("HUBLU", 11, "orang")
SOSMAS = Departemen("SOSMAS", 11, "orang")
MEDFO = Departemen("MEDFO", 11, "orang")
KEPROF = Departemen("KEPROF", 11, "orang")
KWU = Departemen("KWU", 10, "orang")
DPM = Departemen("DPM", 6, "orang")

print("Departemen HMSI 2021")

PSDM.tampilkan_info()
DAGRI.tampilkan_info()
HUBLU.tampilkan_info()
SOSMAS.tampilkan_info()
MEDFO.tampilkan_info()
KEPROF.tampilkan_info()
KWU.tampilkan_info()
DPM.tampilkan_info()

print("Total Departemen :", Departemen.jumlah_departemen, "Departemen")
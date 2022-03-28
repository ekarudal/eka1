class Distro :
    total_harga = 0
    total_produk = 0
    hasil_semua = 0

    def __init__(self, produk, merk, ukuran, harga, jumlah):
        self.produk = produk
        self.merk = merk
        self.ukuran = ukuran
        self.harga = harga
        self.jumlah = jumlah
        self.total_harga += harga*jumlah
        hargatotal.hasil_semua +=1

    def tampil(self):
        print("Barang yang dibeli" ,self.produk , "bermerk", self.merk, "ukurannya" , self.ukuran, "seharga Rp." , self.harga, "jumlah pembelian", self.jumlah, "pcs" )
         
    def hargatotal(self):
        print("Harga total   : Rp.", self.total_harga)
        print("")

        

produk1 = Distro('Kaos', 'Peter Says Denim', 'S', 100000, 2) 
produk2 = Distro('Kaos', 'Peter Says Denim', 'M', 150000, 2)
# produk3 = Distro('Kaos' ,'Peter Says Denim','L', 200000)
# produk4 = Distro('Kaos' ,'Peter Says Denim','XL', 250000)
# produk5 = Distro('Celana', 'Peter Says Denim', 'S' , 70000,)
# produk6 = Distro('Celana' ,'Peter Says Denim', 'M' , 80000)
# produk7 = Distro('Celana' ,'Peter Says Denim', 'L' , 90000)
# produk8 = Distro('Celana' ,'Peter Says Denim', 'XL' , 100000)
# produk9 = Distro('Kaos' ,'erigo', 'S' , 120000)
# produk10 = Distro('Kaos', 'erigo', 'M' , 140000)
# produk11 = Distro('Kaos', 'erigo', 'L' , 160000)
# produk12 = Distro('Kaos', 'erigo', 'XL' , 180000)
# produk13 = Distro('Celana', 'erigo', 'S' , 65000)
# produk14 = Distro('Celana', 'erigo', 'M' , 750000)
# produk15 = Distro('Celana' ,'erigo', 'L' , 85000)
# produk16 = Distro('Celana' ,'erigo', 'XL' , 95000)
# produk17 = Distro('Kaos' ,'Greenlight', 'S' , 212000)
# produk18 = Distro('Kaos', 'Greenlight', 'M' , 312000)
# produk19 = Distro('Kaos', 'Greenlight', 'L' , 412000)
# produk20 = Distro('Kaos', 'Greenlight', 'XL' , 512000)
# produk21 = Distro('Celana', 'Greenlight', 'S' , 121000)
# produk22 = Distro('Celana', 'Greenlight', 'M' , 1410000)
# produk23 = Distro('Celana' ,'Greenlight', 'L' , 161000)
# produk24 = Distro('Celana' ,'Greenlight', 'XL' , 181000)
# produk25 = Distro('Kaos' ,'3Second', 'S' , 82000)
# produk26 = Distro('Kaos', '3Second', 'M' , 92000)
# produk27 = Distro('Kaos', '3Second', 'L' , 102000)
# produk28 = Distro('Kaos', '3Second', 'XL' , 112000)
# produk29 = Distro('Celana', '3Second', 'S' , 66000)
# produk30 = Distro('Celana', '3Second', 'M' , 760000)
# produk31 = Distro('Celana' ,'3Second', 'L' , 86000)
# produk32 = Distro('Celana' ,'3Second', 'XL' , 96000)

produk1.tampil()
print("Jumlah Produk :", Distro.total_produk, "pcs")
produk1.hargatotal()
produk2.tampil()
print("Jumlah Produk :", Distro.total_produk, "pcs")
produk2.hargatotal()
print(hargatotal.hasil_semua)



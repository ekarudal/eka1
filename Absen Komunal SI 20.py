from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "test1"

)

app = QApplication([])
app.setWindowIcon(QIcon('logo1.png'))

window = QMainWindow()
window.setWindowTitle("Absen Komunal SI ")
window.setStyleSheet('background-color: #FF00FF')
window.setGeometry(510, 220, 450, 330)
window.setFixedSize(450, 330)

lbl_judul = QLabel("Sistem Informasi 20", window)
lbl_judul.adjustSize()
lbl_judul.setStyleSheet("font: 19pt Times New Roman")
lbl_judul.setFixedWidth(300)
lbl_judul.setFixedHeight(50)
lbl_judul.move(110, 0)

nama = QLabel(window)
nama.setText("Nama\t\t        =")
nama.setStyleSheet('font : 10pt Times New Roman')
nama.setFixedWidth(200)
nama.move(10, 70)
nama1 = QLineEdit(window)
nama1.setText('')
nama1.setStyleSheet('background-color:white')
nama1.setFixedSize(200,20)
nama1.move(145, 77)

nim = QLabel(window)
nim.setText("NIM\t\t        =")
nim.setStyleSheet('font : 10pt Times New Roman')
nim.setFixedWidth(200)
nim.move(10, 110)
nim2 = QLineEdit(window)
nim2.setText('')
nim2.setStyleSheet('background-color:white')
nim2.setFixedSize(200,20)
nim2.move(145, 117)


keterangan = QLabel(window)
keterangan.setText("Keterangan\t        =")
keterangan.setStyleSheet('font : 10pt Times New Roman')
keterangan.setFixedWidth(200)
keterangan.move(10, 150)
keterangan_hadir = QRadioButton("Hadir", window)
keterangan_hadir.setStyleSheet('font : 9.5pt Times New Roman')
keterangan_hadir.move(145, 151)
keterangan_tidak_hadir = QRadioButton("Tidak Hadir", window)
keterangan_tidak_hadir.setStyleSheet('font : 9.5pt Times New Roman')
keterangan_tidak_hadir.move(225, 151)

radio_group_keterangan = QButtonGroup(window)
radio_group_keterangan.addButton(keterangan_hadir)
radio_group_keterangan.addButton(keterangan_tidak_hadir)

alasan = QLabel(window)
alasan.setText("Alasan tidak hadir      ")
alasan.setStyleSheet('font : 10pt Times New Roman')
alasan.setFixedWidth(200)
alasan.move(10, 190)
alasan4 = QLineEdit(window)
alasan4.setText('')
alasan4.setStyleSheet('background-color:white')
alasan4.setFixedSize(200,20)
alasan4.move(145, 197)


def Insert():
    namaa = nama1.text()
    nimm = nim2.text()
    ket = radio_group_keterangan.checkedButton().text()
    alasann = alasan4.text()
    mycursor = db.cursor()

    sql = "INSERT INTO tubes_pbo (NAMA, NIM, Keterangan, Alasan_Tidak_Hadir) VALUES (%s, %s, %s, %s)"
    data = (namaa, nimm, ket, alasann)
    mycursor.execute(sql, data)
    db.commit()


btn_insert = QPushButton("Simpan", window)
btn_insert.setStyleSheet('background-color:white')
btn_insert.move(185, 270)
btn_insert.clicked.connect(Insert)

window.show()
app.exec_()
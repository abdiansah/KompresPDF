# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kompresgui_qt.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import math
import os
import sys
from pathlib import Path

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_FMain(object):
    def setupUi(self, FMain):
        FMain.setObjectName("FMain")
        FMain.resize(719, 481)
        FMain.setFixedSize(FMain.width(), FMain.height()) # MATIKAN MAX/MIN BUTTON
        FMain.setWindowIcon(QtGui.QIcon('icon-pdf.png'))
        self.centralwidget = QtWidgets.QWidget(FMain)
        self.centralwidget.setObjectName("centralwidget")
        self.GLokasiFileFolder = QtWidgets.QGroupBox(self.centralwidget)
        self.GLokasiFileFolder.setGeometry(QtCore.QRect(3, 6, 391, 111))
        self.GLokasiFileFolder.setObjectName("GLokasiFileFolder")
        self.RBFile = QtWidgets.QRadioButton(self.GLokasiFileFolder)
        self.RBFile.setGeometry(QtCore.QRect(21, 40, 50, 20))
        self.RBFile.setChecked(True)
        self.RBFile.setObjectName("RBFile")
        self.RBFolder = QtWidgets.QRadioButton(self.GLokasiFileFolder)
        self.RBFolder.setGeometry(QtCore.QRect(110, 40, 70, 20))
        self.RBFolder.setObjectName("RBFolder")
        self.BBuka = QtWidgets.QPushButton(self.GLokasiFileFolder)
        self.BBuka.setGeometry(QtCore.QRect(303, 72, 71, 30))
        self.BBuka.setObjectName("BBuka")
        self.EPath = QtWidgets.QLineEdit(self.GLokasiFileFolder)
        self.EPath.setGeometry(QtCore.QRect(21, 74, 271, 28))
        self.EPath.setText("")
        self.EPath.setReadOnly(False)
        self.EPath.setObjectName("EPath")
        self.EPath.setDragEnabled(True)
        self.GInformasiHasilKompresi = QtWidgets.QGroupBox(self.centralwidget)
        self.GInformasiHasilKompresi.setGeometry(QtCore.QRect(3, 125, 711, 311))
        self.GInformasiHasilKompresi.setObjectName("GInformasiHasilKompresi")
        self.TInformasiKompresi = QtWidgets.QTextEdit(self.GInformasiHasilKompresi)
        self.TInformasiKompresi.setGeometry(QtCore.QRect(10, 25, 691, 271))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.TInformasiKompresi.setFont(font)
        self.TInformasiKompresi.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.TInformasiKompresi.setReadOnly(True)
        self.TInformasiKompresi.setObjectName("TInformasiKompresi")
        self.GJenisKompresi = QtWidgets.QGroupBox(self.centralwidget)
        self.GJenisKompresi.setGeometry(QtCore.QRect(403, 6, 311, 111))
        self.GJenisKompresi.setObjectName("GJenisKompresi")
        self.RBEbook = QtWidgets.QRadioButton(self.GJenisKompresi)
        self.RBEbook.setGeometry(QtCore.QRect(21, 80, 121, 20))
        self.RBEbook.setChecked(True)
        self.RBEbook.setObjectName("RBEbook")
        self.RBPrinter = QtWidgets.QRadioButton(self.GJenisKompresi)
        self.RBPrinter.setGeometry(QtCore.QRect(157, 80, 128, 20))
        self.RBPrinter.setObjectName("RBPrinter")
        self.RBScreen = QtWidgets.QRadioButton(self.GJenisKompresi)
        self.RBScreen.setGeometry(QtCore.QRect(21, 40, 113, 20))
        self.RBScreen.setObjectName("RBScreen")
        self.RBPrepress = QtWidgets.QRadioButton(self.GJenisKompresi)
        self.RBPrepress.setGeometry(QtCore.QRect(157, 40, 133, 20))
        self.RBPrepress.setObjectName("RBPrepress")
        self.BKeluar = QtWidgets.QPushButton(self.centralwidget)
        self.BKeluar.setGeometry(QtCore.QRect(630, 443, 84, 30))
        self.BKeluar.setObjectName("BKeluar")
        self.BInfo = QtWidgets.QPushButton(self.centralwidget)
        self.BInfo.setGeometry(QtCore.QRect(540, 443, 84, 30))
        self.BInfo.setObjectName("BInfo")
        self.BKompresPDF = QtWidgets.QPushButton(self.centralwidget)
        self.BKompresPDF.setGeometry(QtCore.QRect(5, 444, 95, 30))
        self.BKompresPDF.setObjectName("BKompresPDF")
        self.BBukaLokasi = QtWidgets.QPushButton(self.centralwidget)
        self.BBukaLokasi.setGeometry(QtCore.QRect(106, 444, 153, 30))
        self.BBukaLokasi.setObjectName("BBukaLokasi")
        self.BManual = QtWidgets.QPushButton(self.centralwidget)
        self.BManual.setGeometry(QtCore.QRect(450, 443, 84, 30))
        self.BManual.setObjectName("BManual")
        self.GUtilitas = QtWidgets.QGroupBox(self.centralwidget)
        self.GUtilitas.setGeometry(QtCore.QRect(3, 482, 711, 151))
        self.GUtilitas.setObjectName("GUtilitas")
        self.CBMenu = QtWidgets.QComboBox(self.GUtilitas)
        self.CBMenu.setGeometry(QtCore.QRect(10, 50, 211, 28))
        self.CBMenu.setObjectName("CBMenu")
        self.CBMenu.addItem("")
        self.CBMenu.addItem("")
        # self.CBMenu.addItem("")
        self.BProses = QtWidgets.QPushButton(self.GUtilitas)
        self.BProses.setGeometry(QtCore.QRect(10, 110, 84, 30))
        self.BProses.setObjectName("BProses")
        self.LMenu = QtWidgets.QLabel(self.GUtilitas)
        self.LMenu.setGeometry(QtCore.QRect(11, 31, 32, 16))
        self.LMenu.setObjectName("LMenu")
        self.LInformasi = QtWidgets.QLabel(self.GUtilitas)
        self.LInformasi.setGeometry(QtCore.QRect(240, 30, 56, 16))
        self.LInformasi.setObjectName("LInformasi")
        self.TInformasiUtilitas = QtWidgets.QTextEdit(self.GUtilitas)
        self.TInformasiUtilitas.setGeometry(QtCore.QRect(238, 51, 461, 87))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.TInformasiUtilitas.setFont(font)
        self.TInformasiUtilitas.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.TInformasiUtilitas.setReadOnly(True)
        self.TInformasiUtilitas.setObjectName("TInformasiUtilitas")
        self.BReset = QtWidgets.QPushButton(self.centralwidget)
        self.BReset.setGeometry(QtCore.QRect(360, 443, 84, 30))
        self.BReset.setObjectName("BReset")
        FMain.setCentralWidget(self.centralwidget)
        self.actionKeluar = QtWidgets.QAction(FMain)
        self.actionKeluar.setObjectName("actionKeluar")

        self.retranslateUi(FMain)
        QtCore.QMetaObject.connectSlotsByName(FMain)
        FMain.setTabOrder(self.RBFile, self.RBFolder)
        FMain.setTabOrder(self.RBFolder, self.EPath)
        FMain.setTabOrder(self.EPath, self.BBuka)
        FMain.setTabOrder(self.BBuka, self.RBScreen)
        FMain.setTabOrder(self.RBScreen, self.RBEbook)
        FMain.setTabOrder(self.RBEbook, self.RBPrepress)
        FMain.setTabOrder(self.RBPrepress, self.RBPrinter)
        FMain.setTabOrder(self.RBPrinter, self.TInformasiKompresi)
        FMain.setTabOrder(self.TInformasiKompresi, self.BKompresPDF)
        FMain.setTabOrder(self.BKompresPDF, self.BBukaLokasi)
        FMain.setTabOrder(self.BBukaLokasi, self.BReset)
        FMain.setTabOrder(self.BReset, self.BManual)
        FMain.setTabOrder(self.BManual, self.BInfo)
        FMain.setTabOrder(self.BInfo, self.BKeluar)
        FMain.setTabOrder(self.BKeluar, self.CBMenu)
        FMain.setTabOrder(self.CBMenu, self.BProses)
        FMain.setTabOrder(self.BProses, self.TInformasiUtilitas)

        ### DEKLARASI FUNGSI EVENT ####################################################################

        self.RBFile.clicked.connect(self.file_folder_klik)
        self.RBFolder.clicked.connect(self.file_folder_klik)
        self.BBuka.clicked.connect(self.buka_klik)
        self.BKompresPDF.clicked.connect(self.kompres_pdf_klik)
        self.BBukaLokasi.clicked.connect(self.buka_lokasi_klik)
        self.BReset.clicked.connect(self.reset_klik)
        self.BManual.clicked.connect(self.manual_klik)
        self.BInfo.clicked.connect(self.info_klik)
        self.BKeluar.clicked.connect(self.keluar_klik)
        self.BProses.clicked.connect(self.proses_klik)

    def retranslateUi(self, FMain):
        _translate = QtCore.QCoreApplication.translate
        FMain.setWindowTitle(_translate("FMain", "Kompresi PDF"))
        self.GLokasiFileFolder.setTitle(_translate("FMain", "Lokasi File/Folder"))
        self.RBFile.setText(_translate("FMain", "File"))
        self.RBFolder.setText(_translate("FMain", "Folder"))
        self.BBuka.setText(_translate("FMain", "Buka"))
        self.GInformasiHasilKompresi.setTitle(_translate("FMain", "Informasi Hasil Kompresi"))
        self.GJenisKompresi.setTitle(_translate("FMain", "Jenis Kompresi"))
        self.RBEbook.setText(_translate("FMain", "E-Book (150 dpi)"))
        self.RBPrinter.setText(_translate("FMain", "Printer (300+ dpi)"))
        self.RBScreen.setText(_translate("FMain", "Screen (72 dpi)"))
        self.RBPrepress.setText(_translate("FMain", "Prepress (300 dpi)"))
        self.BKeluar.setText(_translate("FMain", "Keluar"))
        self.BInfo.setText(_translate("FMain", "Info"))
        self.BKompresPDF.setText(_translate("FMain", "Kompres PDF"))
        self.BBukaLokasi.setText(_translate("FMain", "Buka Lokasi File/Folder"))
        self.BManual.setText(_translate("FMain", "Manual"))
        self.GUtilitas.setTitle(_translate("FMain", "Utilitas"))
        self.CBMenu.setItemText(0, _translate("FMain", "Hapus Semua Kata \"KOMPRES\""))
        self.CBMenu.setItemText(1, _translate("FMain", "Hapus Semua File Kompresi"))
        # self.CBMenu.setItemText(2, _translate("FMain", "Ubah Seluruh Nama File"))
        self.BProses.setText(_translate("FMain", "Proses"))
        self.LMenu.setText(_translate("FMain", "Menu"))
        self.LInformasi.setText(_translate("FMain", "Informasi"))
        self.BReset.setText(_translate("FMain", "Reset"))
        self.actionKeluar.setText(_translate("FMain", "Keluar"))

### DEFINISI FUNGSI EVENT ####################################################################

    def file_folder_klik(self):
        self.EPath.clear()
        self.TInformasiKompresi.clear()

    def buka_klik(self):
        if self.RBFile.isChecked():
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Ambil File PDF", "",
                                                                "File PDF (*.pdf)", options=options)
            self.EPath.setText(fileName)
            LOK = "LOKASI FILE\t: "
        else:
            # folderName = self.FD_dialog.getExistingDirectory(None, "Select Directory")
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            folderName = str(QtWidgets.QFileDialog.getExistingDirectory(None, "Pilih Folder PDF", options=options))
            self.EPath.setText(folderName)
            LOK = "LOKASI FOLDER\t: "

        self.TInformasiKompresi.clear()
        self.TInformasiUtilitas.clear()
        if self.EPath.text()!="":
            self.TInformasiKompresi.append(LOK+self.EPath.text())

    def kompres_pdf_klik(self):
        lokasi_path = self.EPath.text()
        if self.TInformasiKompresi.toPlainText()!="":
            self.TInformasiKompresi.clear()
        else:
            if self.EPath.text().startswith("file://"):  # drag drop linux
                lokasi_path = lokasi_path[7:]
                self.EPath.setText(lokasi_path)

        if os.path.exists(lokasi_path):
            # MODE1 = '-dPDFSETTINGS=/default'
            MODE1 = '-dPDFSETTINGS=/screen'
            MODE2 = '-dPDFSETTINGS=/ebook'
            MODE3 = '-dPDFSETTINGS=/prepress'
            MODE4 = '-dPDFSETTINGS=/printer'
            jenis = self.GJenisKompresi.children()
            for item in jenis:
                if item.isChecked():
                    mode = item.text()

            if self.RBFile.isChecked():
                self.TInformasiKompresi.append("LOKASI FILE\t: " + lokasi_path)
                file_size = self.convert_size(os.path.getsize(lokasi_path))
                self.TInformasiKompresi.append("UKURAN FILE\t: " + file_size)
            elif self.RBFolder.isChecked():
                self.TInformasiKompresi.append("LOKASI FOLDER\t: " + lokasi_path)
                total_ukuran_file = 0
                filenames = os.listdir(lokasi_path)
                file_pdf = 0
                files = []
                for f in filenames:
                    if f.endswith(".pdf"):
                        files.append(f)
                        total_ukuran_file = total_ukuran_file + os.path.getsize('{}/{}'.format(lokasi_path, f))
                        file_pdf += 1
                self.TInformasiKompresi.append("JUMLAH FILE\t: " + str(len(filenames)))
                self.TInformasiKompresi.append("JUMLAH FILE PDF\t: " + str(file_pdf))

            MODE = ""
            if mode == "Screen (72 dpi)":       MODE = MODE1
            elif mode == "E-Book (150 dpi)":    MODE = MODE2
            elif mode == "Prepress (300 dpi)":  MODE = MODE3
            elif mode == "Printer (300+ dpi)":  MODE = MODE4
            self.TInformasiKompresi.append("")
            self.TInformasiKompresi.append("MODE KOMPRESI")
            self.TInformasiKompresi.append("  - " + mode)

            self.TInformasiKompresi.append("")
            self.TInformasiKompresi.append("INFORMASI HASIL KOMPRESI")

            if self.RBFile.isChecked():
                des_file, file_size = self.kompres_file(lokasi_path, MODE)
                self.TInformasiKompresi.append("  - Nama File\t: " + des_file)
                # file_size = self.convert_size(os.path.getsize(des_file))
                file_size = self.convert_size(file_size)
                self.TInformasiKompresi.append("  - Ukuran File\t: " + file_size)
            elif self.RBFolder.isChecked():
                if file_pdf != 0:
                    file_pdf, total_ukuran_kompres = self.kompres_folder(lokasi_path, files, MODE)
                    self.TInformasiKompresi.append("  - Nama Folder\t: " + self.EPath.text())
                    self.TInformasiKompresi.append("  - Sebelum Kompres\t: "+ self.convert_size(total_ukuran_file))
                    self.TInformasiKompresi.append("  - Setelah Kompres\t: "+ total_ukuran_kompres)
                else:
                    QMessageBox.warning(self, "Kesalahan", "Lokasi file atau folder tidak ditemukan!", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "Kesalahan", "Lokasi file atau folder tidak ditemukan!", QMessageBox.Ok)

    def buka_lokasi_klik(self):
        if (self.EPath.text() != ''):
            if self.RBFile.isChecked():
                basedir = os.path.dirname(self.EPath.text())
                os.system("xdg-open '{}'".format(basedir))
            elif self.RBFolder.isChecked():
                os.system("xdg-open '{}'".format(self.EPath.text()))
        else:
            QMessageBox.warning(self, "Kesalahan", "Lokasi file atau folder tidak ditemukan!", QMessageBox.Ok)

    def reset_klik(self):
        self.RBFile.setChecked(True)
        self.EPath.clear()
        self.RBEbook.setChecked(True)
        self.TInformasiKompresi.clear()
        self.TInformasiUtilitas.clear()

    def manual_klik(self):
        path_app = os.path.realpath(__file__)
        p = Path(path_app)
        path_dir = str(p.parent)
        path_info = path_dir + '/manual.pdf'
        os.system("xdg-open "+path_info)

    def info_klik(self):
        path_app = os.path.realpath(__file__)
        p = Path(path_app)
        path_dir = str(p.parent)
        path_info = path_dir + '/info.txt'
        info = open(path_info).read()
        self.TInformasiKompresi.setText(info)

    def keluar_klik(self):
        sys.exit()

    def proses_klik(self):
        if self.RBFolder.isChecked():
            if os.path.exists(self.EPath.text()):
                menu = self.CBMenu.currentIndex()
                print(menu)
                filenames = os.listdir(self.EPath.text())
                c = 0
                files = []
                for f in filenames:
                    if f.endswith(".pdf"):
                        files.append(f)
                        c += 1
                if c != 0:
                    if menu == 0:   # hapus semua kata "KOMPRES"
                        reply = QMessageBox.question(self, 'PERHATIAN', "Apakah file PDF ASLI sudah dipindahkan? Jika belum pilih NO!",
                                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                        if reply == QMessageBox.Yes:
                            self.TInformasiUtilitas.setText("Proses penghapus kata \"KOMPRES\"")
                            self.TInformasiUtilitas.setText("PERINGATAN:")
                            self.TInformasiUtilitas.setText(" - Jika terdapat file PDF ASLI segera pindahkan ke lokasi lain!")
                            self.TInformasiUtilitas.setText(" - Jika tidak dipindahkan file PDF ASLI akan ditimpa file kompresi")
                            self.TInformasiUtilitas.append("\nLokasi folder\t\t: {}".format(self.EPath.text()))
                            self.TInformasiUtilitas.append("Daftar nama file yang diubah\t:")
                            i = 0
                            for f in files:
                                src = "{}/{}".format(self.EPath.text(), f)
                                if (src.endswith("--KOMPRES.pdf")):
                                    file_baru = Path(src).name
                                    n = len(file_baru)-13
                                    file_baru = file_baru[:n]
                                    des = "{}/{}.pdf".format(self.EPath.text(), file_baru)
                                    self.TInformasiUtilitas.append("  - {} => {}".format(src, des))
                                    os.rename(src, des)
                                    i += 1
                            if i != 0:
                                self.TInformasiUtilitas.append("\nPerubahan nama file PDF selesai")
                            else:
                                self.TInformasiUtilitas.append("\nTidak ada nama file PDF yang diubah!")
                            self.TInformasiUtilitas.append("Untuk melihat hasilnya, tekan tombol [Folder]")
                    elif menu == 1: # hapus semua file kompresi (kata "KOMPRES" jangan hilang)
                        self.TInformasiUtilitas.setText("menu 0")
                    elif menu == 2: # mengubah seluruh nama file PDF sesuai dengan LABEL
                        label, ok = QtWidgets.QInputDialog.getText(self, "Input Label", "Nama Label:")
                        if ok == True:
                            self.TInformasiUtilitas.setText("Proses perubahan nama file pdf")
                            self.TInformasiUtilitas.append("\nLokasi folder\t\t: {}".format(self.EPath.text()))
                            self.TInformasiUtilitas.append("Daftar nama file yang diubah\t:")
                            i = 1
                            for f in files:
                                src = "{}/{}".format(self.EPath.text(), f)
                                des = "{}/{}-{}.pdf".format(self.EPath.text(), label, i)
                                self.TInformasiUtilitas.append("  - {} => {}-{}.pdf".format(f, label, i))
                                os.rename(src, des)
                                i += 1
                            self.TInformasiUtilitas.append("\nPerubahan nama file pdf selesai")
                            self.TInformasiUtilitas.append("Untuk melihat hasilnya, tekan tombol [Folder]")
                else:
                    QMessageBox.warning(self, "Kesalahan", "File PDF tidak tersedia di lokasi ini!", QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "Kesalahan", "Lokasi folder tidak ditemukan!", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "Kesalahan", "Lokasi folder belum dipilih!", QMessageBox.Ok)

### DEFINISI FUNGSI UTAMA ####################################################################

    def kompres_file(self, src_file, mode):
        basedir = os.path.dirname(__file__)
        path_exe = os.path.join(basedir, 'ps2pdf')

        basedir = os.path.dirname(src_file)     # ekstraks dir
        basefile = os.path.basename(src_file)   # ekstraks file ekstensi (pdf)

        nama_file = basefile[:len(basefile)-4]  # nama file tanpa ekstensi
        nama_file = '{}--KOMPRES.pdf'.format(nama_file)
        des_file = os.path.join(basedir, nama_file)

        os.system('{} {} \'{}\' \'{}\''.format(path_exe, mode, src_file, des_file))
        ukuran_file = os.path.getsize(des_file)
        return des_file, ukuran_file

    def kompres_folder(self, src_dir, files, mode):
        # d = "KOMPRES"
        # if os.path.exists('{}/{}'.format(src_dir,d)):
        #     print("hapus dir")
        #     os.rmdir('{}/{}'.format(src_dir,d))
        #     os.mkdir('{}/{}'.format(src_dir,d))
        # else:
        #     os.mkdir('{}/{}'.format(src_dir,d))
        total_ukuran = 0
        for f in files:
            _,ukuran_file = self.kompres_file('{}/{}'.format(src_dir, f), mode)
            total_ukuran = total_ukuran + ukuran_file
        return len(files), self.convert_size(total_ukuran)

    def convert_size(self, size_bytes):
        if size_bytes == 0:
               return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])
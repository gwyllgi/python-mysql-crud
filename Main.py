import mysql.connector
import os

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="bmroot",
    database="crudpython"
)

#if db.is_connected():
#    print("Berhasil terhubung ke Database!")

def tambah_data(db):
    owner = input("Nama Owner: ")
    series = input("Seri: ")
    type = input("Tipe: ")
    manufacturer = input("Manufacturer: ")
    val = (owner,series,type,manufacturer)
    cursor = db.cursor()
    sql = "INSERT INTO cars (owner, series, type, manufacturer) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil disimpan!".format(cursor.rowcount))

def tampil_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM cars"
    cursor.execute(sql)
    result = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Data kosong!")
    else:
        for data in result:
            print(data)

def update_data(db):
    cursor = db.cursor()
    tampil_data(db)
    id_cars = input("Pilih ID Cars -> ")
    owner = input("Nama Owner baru: ")
    series = input("Series: ")
    type = input("Tipe: ")
    manufacturer = input("Manufacturer: ")

    sql = "UPDATE cars SET owner=%s, series=%s, type=%s, manufacturer=%s WHERE id_cars=%s"
    val = (owner, series, type, manufacturer, id_cars)
    cursor.execute(sql, val)
    db.commit()
    print("{} data telah diubah!".format(cursor.rowcount))

def hapus_data(db):
    cursor = db.cursor()
    tampil_data(db)
    id_cars = input("Pilih ID Cars -> ")
    sql = "DELETE FROM cars WHERE id_cars=%s"
    val = (id_cars,)
    cursor.execute(sql, val)
    db.commit()
    print("{} data telah dihapus!".format(cursor.rowcount))

def cari_data(db):
    cursor = db.cursor()
    keyword = input("Kata kunci: ")
    sql = "SELECT * FROM cars WHERE owner LIKE %s OR series LIKE %s"
    val = ("%{}%".format(keyword), "%{}%".format(keyword))
    cursor.execute(sql, val)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Data tidak ada")
    else:
        for data in results:
            print(data)

def tampil_menu(db):
    print(" *** CARS OWNER DATABASE ***")
    print("1. Tambah Data")
    print("2. Tampilkan Semua Data")
    print("3. Perbarui Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("0. Keluar")
    print("----------------------------")
    menu = input("Pilih menu -> ")

    os.system("clear")

    if menu == "1":
        tambah_data(db)
    elif menu == "2":
        tampil_data(db)
    elif menu == "3":
        update_data(db)
    elif menu == "4":
        hapus_data(db)
    elif menu == "5":
        cari_data(db)
    elif menu == "0":
        exit()
    else:
        print("Menu tidak tersedia!")


if __name__ == "__main__":
    while(True):
        tampil_menu(db)

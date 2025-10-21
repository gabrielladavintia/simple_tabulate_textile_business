from tabulate import tabulate
# Program Penjualan Online Toko Kain Samudra 

listKain = [
    {
        'nama': 'Trilobel',
        'stock': 120,
        'harga': 1000000
    },
    {
        'nama': 'Lotto Tipis',
        'stock': 150,
        'harga': 1200000
    },
    {
        'nama': 'Lotto Tebal',
        'stock': 190,
        'harga': 1500000
    },
    {
        'nama': 'Scuba',
        'stock': 250,
        'harga': 2000000
    },
    {
        'nama': 'Diadora',
        'stock': 220,
        'harga': 1500000
    },
    {
        'nama': 'Fleece',
        'stock': 350,
        'harga': 1400000
    },
    {
        'nama': 'Dry Fit',
        'stock': 220,
        'harga': 1300000
    },
    {
        'nama': 'Cotton Cardet',
        'stock': 400,
        'harga': 1200000
    },
    {
        'nama': 'Cotton Combed',
        'stock': 300,
        'harga': 1200000
    },
    {
        'nama': 'Spandex Balon',
        'stock': 350,
        'harga': 1200000
    },
    {
        'nama': 'Spandex Rayon',
        'stock': 420,
        'harga': 1200000
    },
    {
        'nama': 'Kulit Jeruk',
        'stock': 220,
        'harga': 1200000
    },
    {
        'nama': 'PE Double',
        'stock': 320,
        'harga': 1200000
    },
    {
        'nama': 'Double Face',
        'stock': 250,
        'harga': 1200000
    },
    {
        'nama': 'Haiget st45',
        'stock': 200,
        'harga': 1200000
    }
]

listWarna = [
    {
        'nama supplier': 'Supplier 1',
        'jenis kain': ['fleece', 'paragon', 'diadora', 'lotto sandwich', 'dry fit', 'scuba'],
        'warna': ['zumba putih', 'hitam tebal']
    },
    {
        'nama supplier' : 'Supplier 2',
        'jenis kain' : ['abutai', 'lotto tipis'],
        'warna' : ['hijau TNI', 'Abu sedang', 'coklat kopi 56']
    },
    {
        'nama supplier' : 'Supplier 3',
        'jenis kain' : ['abutai', 'lotto tebal', 'cotton cardet', 'cotton combed', 'spandex balon', 'spandex rayon'],
        'warna' : ['serena putih']
    },
    {
        'nama supplier' : 'Supplier 4',
        'jenis kain' : ['abutai', 'lotto tipis'],
        'warna' : ['abutai kuning kenari tua', 'abutai biru disko/turkis sedang', 'abutai merah cabe tua', 'abutai hijau tua', 'abutai coklat sample ganjil', 'abutai hj botol ganjil 63', 'abutai putih, abutai hitam', 'lotto tipis st45']
    },
    {
        'nama supplier' : 'Pabrik',
        'jenis kain' : ['kulit jeruk', 'abutai, double face', 'lotto, PE double', 'haiget st45'],
        'warna' : ['putih', 'broken white', 'cream36']
    },
    {
        'nama supplier' : 'Supplier 5',
        'jenis kain' : ['scuba', 'paragon', 'diadora', 'spandex balon']
    }
]

cart = []

def menampilkanDaftarKain() :
    table = [["Trilobel","1000000"],["Scuba", "2000000"],["Lotto Tebal", "1500000"],["Lotto Tipis", "1200000"],["Fleece", "1400000"],["Kulit Jeruk", "1250000"],["Spandex Rayon", "1450000"],["Spandex Balon", "1500000"],["Haiget st45", "1150000"],["Cotton Combed", "1500000"],["Cotton Cardet", "1100000"],["Double Face", "2000000"],["PE Double", "1900000"],["Diadora", "1000000"]]
    headers = ["Jenis Kain", "Rp"]
    print(tabulate(table, headers, tablefmt="plain"))
    
def menambahKain() :
    namaKain = input('Masukkan Nama Jenis Kain : ')
    stockKain = int(input('Masukkan Stock Kain : '))
    hargaKain = int(input('Masukkan Harga Kain : '))
    listKain.append({
        'nama': namaKain,
        'stock': stockKain,
        'harga': hargaKain
    })
    menampilkanDaftarKain()

def menghapusKain() :
    menampilkanDaftarKain()
    indexKain = int(input('Masukkan index kain yang ingin dihapus : '))
    del listKain[indexKain]
    menampilkanDaftarKain()

def membeliKain() :
    menampilkanDaftarKain()
    while True :
        indexKain = int(input('Masukkan index kain yang ingin dibeli : '))
        listWarna = input('Warna apa yang ingin dibeli :  ')
        qtyKain = int(input('Masukkan jumlah yang ingin dibeli : '))
        if(qtyKain > listKain[indexKain]['stock']) :
            print('Stock tidak cukup, stock {} tinggal {}'.format(listKain[indexKain]['nama'],listKain[indexKain]['stock']))
        else :
            cart.append({
                'nama': listKain[indexKain]['nama'], 
                'qty': qtyKain, 
                'harga': listKain[indexKain]['harga'], 
                'index': indexKain
            })
        print('Isi Cart :')
        print('Nama\t| Qty\t| Harga')
        for item in cart :
            print('{}\t| {}\t| {}'.format(item['nama'], item['qty'], item['harga']))
        checker = input('Mau beli yang lain? (ya/tidak) = ')
        if(checker == 'tidak') :
            break

while True :
    pilihanMenu = input('''
        Selamat Datang di Toko Kain Samudra

        List Menu :
        1. Jenis Kain Yang Kami Jual
        2. Input Stock Kain Masuk
        3. Menghapus Stock Kain
        4. Membeli Kain
        5. Cetak Resi

        Masukkan angka Menu yang ingin dijalankan : ''')

    if(pilihanMenu == '1') :
        menampilkanDaftarKain()
    elif(pilihanMenu == '2') :
        menambahKain()
    elif(pilihanMenu == '3') :
        menghapusKain()
    elif(pilihanMenu == '4') :
        membeliKain()
    elif(pilihanMenu == '5') :
        break

# Selamat Datang untuk admin
print('Selamat Datang ke Toko Kain Samudra')

# Untuk nama pembeli dan apa yang dia mau beli
nama = input("Masukan nama pembeli ")
item = input("Jenis kain apa yang dibeli? ")
warna = input("Warna apa yang dibeli? ")
harga = float(input("Harga : Rp "))
kuantitas = int(input("kuantitas : "))

# Hitung belanjaan
total_harga = harga*kuantitas

# Bukti transaksi
print()
print("=" * 50)
print("Bukti transaksi:")
print("Nama: " + nama.title())
print("Barang yang dibeli: " + item.lower() + " " + warna.capitalize())
print("Harga: Rp" + str(harga))
print("Kuantitas: "+str(kuantitas))
print("Total Harga: Rp" + str(total_harga))
print("=" * 50)
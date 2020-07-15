# django-stock-chain
--------------------
Kita membangun Django Stock Chain application untuk mempermudah pekerjaan sehari-hari di gudang. Dibuat menggunakan Django dan beberapa library jQuery

## Table of Contents
* [Technologies](#technologies)
* [Setup](#setup)
* [Daftar Fitur](#daftar-fitur)
* [Tata Cara Penggunaan](#tata-cara-penggunaan)
* [Contact Me](#contact-me)

## Technologies

* Python v3.6
* Django v3.0.4
* jQuery v3.2.1
* Bootstrap v4
* Selebihnya bisa dilihat di requirements.txt

## Setup

Sebelum menggunakan aplikasi ini, pastikan sudah terinstall python3 dan pip3 di komputer anda. Untuk mengecek apakah python sudah terinstal, buka terminal dan ketik

```
python3 --version && pip3 --version
```

Jika nomor version belum muncul, lakukan langkah berikut
```
# pastikan repo sudah terupdate
sudo apt update && sudo apt upgrade

# install dependency yang dibutuhkan
sudo apt install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-venv python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info

# clone repo ini
git clone https://github.com/dovjay/django-stock-chain

# install venv untuk menjalankan virtual env python
python3 -m venv ./venv

# aktifkan venv
source venv/bin/activate

# install requirement dari python
cd django-stock-chain
pip install -r requirements.txt

# jalankan server
python manage.py runserver
```

## Daftar Fitur
* Dasbor - menampilkan total produk, total aset, dan total profit. Top 10 Produk yang paling banyak terjual dan search bar untuk mencari produk.
* Kontak - menyimpan kontak yang terkategori sebagai supplier dan/atau customer
* Inventori - bagian inventori dibagi menjadi:
  1. Produk - nama, kode, gambar, kategori dari produk ditampilkan disini. bisa export daftar produk ke file CSV untuk dibuka di Excel
  2. Varian Produk - ukuran, tipe produk, harga jual dan beli, serta stok dari suatu produk.
  3. Kategori - untuk mempermudah membedakan jenis produk
* Invoice - pembuatan invoice untuk penjualan. Secara otomatis menyesuaikan stok yang tersedia di gudang. export daftar invoice ke file CSV untuk dibuka di Excel
* Gudang - salah satu bagian penting dalam aplikasi ini. sebelum memulai menggunakan, sebaiknya tambahkan gudang untuk keperluan pencatatan.
* Akun dan permission - buat akun tambahan untuk mengurus suatu gudang dengan menambahkan permission ke akun tersebut.

## Tata Cara Penggunaan

Klik link dibawah untuk lompat ke bagian yang ingin dibaca.
* [Gudang](#gudang)
* [Kontak](#kontak)
* [Produk](#produk)
* [Varian Produk](#varian-produk)
* [Kategori](#kategori)
* [Invoice](#invoice)
* [Akun dan Permissionn](#akun-dan-permission)

### Gudang
Gudang adalah elemen terpenting dalam sistem disini. Maka dari itu kami menaruh gudang sebagai tata cara pertama dalam menggunakan aplikasi ini. Untuk membuat gudang, langkah-langkah yang harus dilakukan adalah:

* Pergi ke **Pengaturan**
* Klik **Tambah Gudang/Toko**
* Masukkan info gudang yang tertera di form. (Simbol * menandakan harus diisi)
* Klik **Simpan**

Gudang telah tersimpan dan akan terlihat di daftar gudang di halaman **Pengaturan**.

Untuk mengupdate atau hapus gudang juga tersedia tombol di daftar gudang.

Perlu diinggat, jika anda menghapus sebuah gudang, maka anda akan menghapus Invoice, Produk dan variannya, dan Permission yang ada didalamnya.

### Kontak
Kontak bersifat opsional. tapi akan sangat membantu jika anda ingin menambah produk atau membuat invoice. Langkah-langkah membuat kontak adalah:

* Pergi ke **Kontak**
* Klik **Tambah Kontak**
* Masukkan info kontak yang tertera di form. (Simbol * menandakan harus diisi)
* Klik **Simpan**

Kontak sudah tersimpan dan akan terlihat di daftar kontak.

Untuk mengedit kontak, arahkan pointer ke salah satu item (untuk versi mobile, klik salah satu item) dan akan terlihat ikon edit (warna hijau) dan delete (warna merah).

Tersedia juga fitur pencarian berdasarkan nama, telp, atau email untuk mencari kontak

### Produk

#### Prasyarat
1. Sudah membuat minimal 1 gudang

Produk termasuk dalam tab Inventori. Informasi suatu produk akan dipakai dalam pembuatan varian produk, dan invoice. Langkah-langkah membuat produk adalah:

* Klik **Inventori**
* Pergi ke **Produk**
* Klik **Tambah Produk**
* Masukkan info produk yang tertera di form. (Simbol * menandakan harus diisi)
* Klik **Simpan**

Setelah anda meng-klik simpan, maka anda akan langsung diarahkan ke halaman varian produk untuk melihat/menambah varian produk yang sudah diinput ke sistem.

Didalam halaman daftar produk, ada opsi untuk melihat varian produk, update, dan hapus.

Tombol **Export** yang ada di samping tombol **Tambah Produk** berguna untuk mengexport daftar produk dari suatu gudang menjadi file CSV yang bisa dilihat menggunakan Excel.

Tersedia juga fitur pencarian berdasarkan Nama atau kode produk berdasarkan gudang.

Note:
1. Menghapus **Produk** akan menghapus semua **Varian Produk** dan item yang ada di **Invoice**

### Varian Produk

#### Prasyarat
1. Sudah membuat minimal 1 gudang
2. Sudah membuat minimal 1 produk

Varian produk akan kosong jika anda belum menambahkan atau memilih produk apapun. Untuk memilih produk, silahkan Input kode produk terlebih dahulu kemudian akan muncul informasi produk dan variannya. Setelah informasi produk muncul, baru anda bisa menambah, edit, hapus varian dari produk tersebut. Langkah-langkah untuk menambah varian adalah:

* Klik **Tambah Varian**
* Masukkan info varian produk yang tertera di form. (Simbol * menandakan harus diisi)
* Klik **Simpan**

Akan terlihat varian produk baru dibawah produk info serta opsi untuk update atau hapus.

Note:
1. **Kode Produk** yang bisa di input di halaman **Varian Produk** hanya produk-produk yang ada di **Gudang** yang sudah dipilih di halaman **Produk**

### Kategori

Kategori berguna untuk mengelompokkan jenis barang supaya mempermudah proses filter atau pencarian. Langkah-langkah untuk membuat kategori adalah:

* Klik **Inventori**
* Pergi ke **Kategori**
* Klik **Tambah Kategori**
* Masukkan info kategori yang tertera di form. (Simbol * menandakan harus diisi)
* Klik **Simpan**

Kategori yang sudah tersimpan akan tampil di daftar kategori. Disitu anda juga bisa mengupdate dan menghapus kategori yang kurang pas.

Tersedia juga fitur pencarian berdasarkan nama kategori.

### Invoice

#### Prasyarat
1. Sudah membuat minimal 1 gudang
2. Sudah membuat minimal 1 produk
3. Sudah membuat minimal 1 varian produk dengan stok miminal 1

Kami juga mempunyai fitur invoice untuk mencatat semua aktivitas jual beli ke customer yang secara otomatis akan menyesuaikan jumlah stok yang masih tersedia di gudang. Untuk langkah-langkah membuat invoice adalah:

* Pergi ke **Invoice**
* Klik **Tambah Invoice**
* Akan tampil sejumlah form seperti:
  - Status: Ubah status menjadi 'Hutang' atau 'Lunas' ketika invoice akan dicetak
  - Customer
  - Jatuh Tempo: tanggal terakhir penagihan invoice
  - Tanggal Bayar: tanggal terhitung customer sudah membayar lunas invoice
  - Item Table: Item yang akan dimasukkan ke dalam invoice
  - Diskon: jumlah diskon dari semua total barang yang ada dalam invoice dalam bentuk persen
  - Notes: Catatan tambahan
* Untuk menambah item, klik **Tambah Item** dan akan muncul form barang yang akan ditambahkan ke invoice
* Masukkan **Kode Barang** yang ingin di cari
* Pilih **Ukuran** yang tersedia
* Masukkan jumlah **Quantity** (Tidak bisa melebihi jumlah stok yang tersisa di gudang)
* Masukkan harga (secara otomatis akan terisi jika **Harga Jual** sudah ditetapkan di bagian **Varian Produk**)
* Klik **Tambah** untuk menambah item
* (Opsional) Masukkan jumlah diskon (dalam persen)
* (Opsional) Masukkan notes
* Klik **Simpan**

Setelah tersimpan akan muncul di daftar Invoice beserta status yang ada disitu. invoice juga bisa di print ketika tidak berstatus 'Draft'. Juga bisa di update atau di hapus jika masih ada yang kurang pas.

Tombol **Export** berfungsi untuk mengexport daftar invoice selain status 'Draft' ke file CSV untuk dibuka di Excel.

Tersedia juga fitur pencarian berdasarkan no invoice dan nama customer

### Akun dan Permission

Terkadang kita membutuhkan tambahan tenaga untuk mengurus banyak gudang. Oleh karena itu, kami membuat sistem dimana anda bisa menambah user untuk mengakses suatu gudang dan membantu menambahkan informasi apa saja yang dibutuhkan. Untuk membuat User langkah-langkahnya adalah:

* Pergi ke **Pengaturan**
* Klik **Tambah Akun**
* Masukkan info Akun yang tertera di form. (Simbol * menandakan harus diisi)
* (Opsional) Centang Is superuser jika anda yakin ingin memberi akses lebih ke User
* Klik **Simpan**

Setelah itu akan menuju ke halaman pengaturan lagi. Kemudian lanjut ke penambahan permission supaya user punya akses ke suatu gudang. Cara nya adalah:

* Klik **Tambah Permission**
* Masukkan info Permission yang tertera di form. (Simbol * menandakan harus diisi)
* Klik **Simpan**

Sekarang user sudah bisa login dan mengakses sistem berdasarkan permission gudang yang diberikan.

Note:
1. Superuser tidak akan terlihat di daftar akun
2. Akun yang bukan superuser hanya bisa mengakses tab pengaturan dan akses lain menjadi terbatas
3. Satu user hanya bisa memiliki satu permission gudang

## Contact Me

Created by [@dovjay](https://github.com/dovjay). If you have any more question, feel free to contact me via: [Email](mailto:dovansanjaya24@gmail.com) or [Instagram](https://instagram.com/dovan_sanjaya)

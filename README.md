## Daftar Isi
* [Algoritma TSP](#algoritma-tsp)
* [Teknologi](#teknologi)
* [Cara Menjalankan Program](#cara-menjalankan-program)
* [Author](#author)


# Algoritma TSP
Algoritma TSP yang digunakan adalah algoritma Divide-and-Conquer. Alasannya adalah karena algoritma Divide-and-Conquer cocok untuk penyelesaian TSP. Algoritma Divide-and-Conquer juga pasti dapat menghasilkan hasil optimal tidak seperti algoritma lain seperti Greedy. Algoritma Divide-and-Conquer juga jauh lebih cepat dari algoritma seperti Brute Force dalam menyelesaikan TSP. Algoritma Dynamic Programming tidak dipakai karena dalam penyelesaian rekursif TSP, tidak begitu banyak dilakukan perhitungan ulang dari sub-problem yang sudah pernah diselesaikan dan algoritmanya hanya terdiri dari perbandingan-perbandingan saja. Oleh karena itu, pembuat menilai penggunaan dynamic programming tidak begitu berpengaruh ke kecepatan algoritma dan akan menambah beban dari menyimpan hasil-hasil perhitungan.
# Teknologi
## Backend
Flask


Backend menggunakan Flask karena memudahkan penggunaan library Plotly untuk menggambar graf. Framework Flask juga sederhana untuk dipakai sehingga tidak menyulitkan dalam pembuatan backend. Bahasa Python juga cukup fleksibel dalam manipulasi data sehingga memudahkan dalam memroses input dari frontend. Untuk database digunakan MySQL.
## Frontend
ReactJS


Frontend menggunakan ReactJS karena ReactJS memudahkan desain UI dan membuat UI merespon ke input dengan cepat karena web dapat langsung di-update melalui ReactJS. Penerimaan dan pengelolaan input juga cukup mudah melalui ReactJS dan bagian-bagian dari web dapat dengan mudah dipisahkan melalui struktur ReactJS.

# Library
## Python
1. Plotly
2. Numpy
3. Datetime
4. MySQL Connector
## ReactJS
1. Axios

# Cara Menjalankan Program
## Setup Backend
1. cd ke folder `backend`
2. Jalankan perintah `python app.py`

## Setup Frontend
1. cd ke folder `frontend`
2. Jalankan perintah `npm install`
3. Jalankan perintah `npm start`
4. Aplikasi web akan terbuka di url `http://localhost:3000`

## Menggunakan Program
1. Web terbagi menjadi dua bagian yaitu untuk bagian TSP Solver dan pencarian hasil dari database. Dua bagian ini dapat dilihat dari dua kotak yang ada.
2. Untuk bagian penyelesaian TSP dari input, ada di kotak bagian kiri
3. Input untuk TSP Solver dapat berupa file atau input langsung
### Input File
1. Tekan tombol input file lalu masukkan file-file yang diinginkan. File harus dalam bentuk .txt dan sesuai format. Format dapat dilihat di bawah ini atau di file template.txt di folder test
2. Tekan tombol `Cari Jalur Terpendek` yang ada di bawah input file untuk melihat jawaban dari file-file yang dimasukkan
3. Jawaban dapat dilihat di bagian bawah kotak bagian kiri

#### Format File
##### Format:

  Nama Lokasi: Perusahaan, lokasiA, string
  \
  Koordinat: (0,0) | (floatx,floaty) | (x,y)    
  Identitas Kurir: string
  \
  Waktu Pengiriman: HH:MM:SS    
  Kecepatan Rata-rata Kurir: float


##### Contoh:

  Nama Lokasi: Perusahaan, Indomaret, Neraka, ITB, Rumah    
  Koordinat: (-3,-3) | (3,4) | (12,3) | (-5,-7) | (6,-3)    
  Identitas Kurir: Kevin    
  Waktu Pengiriman: 07:12:00    
  Kecepatan Rata-rata Kurir: 20   

### Input Langsung
1. Untuk kolom titik awal pengiriman, identitas kurir, waktu pengiriman, dan kecepatan rata-rata kurir, isi kolom yang ada dengan input yang sesuai
2. Tekan tombol di bawah tiap kolom tersebut untuk menyimpan nilai input
3. Untuk menghapus nilai input, tekan tombol 'X' yang ada di samping nilai input yang tersimpan atau masukkan input lagi
4. Untuk bagian nama lokasi dan koordinat, untuk tiap lokasi serta koordinatnya, isi kolom untuk nama lokasi dan koordinat(x,y) lalu tekan tombol `Tambah Lokasi Pengiriman` untuk menyimpan suatu lokasi dan koordinatnya.
5. Ulangi langkah 4 untuk setiap pasangan lokasi dan koordinat yang ingin diinput
6. Untuk menghapus semua input di bagian ini, tekan tombol `clear`
7. Ketika semua input sudah disimpan, tekan tombol `Cari Jalur Terpendek` yang ada di paling bawah kotak bagian kiri untuk melihat jawaban
8. Jawaban dapat dilihat di bagian bawah kotak bagian kiri

### Pencarian dari Database
1. Masukkan nilai untuk kolom identitas dan tanggal
2. Tekan tombol `Tentukan Identitas Kurir` dan `Tentukan Tanggal Pengiriman` untuk menyimpan input masing-masing
3. Tekan tombol `clear` untuk menghapus semua input di bagian ini
5. Ketika semua input sudah tersimpan, tekan tombol `Cari` untuk melihat data dari semua pengiriman yang memiliki identitas kurir dan tanggal pengiriman yang sama dengan input

# Author
- Girvin Junod 13519096

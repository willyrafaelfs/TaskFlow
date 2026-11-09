# TaskFlow

Aplikasi daftar tugas sederhana berbasis web. Nama **TaskFlow** direkomendasikan sebagai nama proyek karena singkat, mudah diingat, dan menggambarkan alur pengelolaan tugas. Nama yang digunakan di antarmuka saat ini masih “My Todo List”.

## Fitur

- Menambahkan tugas.
- Menandai tugas sebagai selesai atau aktif.
- Memfilter daftar berdasarkan semua, aktif, atau selesai.
- Menghapus tugas satu per satu atau menghapus semua tugas yang selesai.
- Menyimpan daftar tugas di `localStorage` browser, sehingga data tetap ada setelah halaman dimuat ulang pada browser yang sama.
- Menyediakan versi alternatif berbasis terminal melalui Python.

## Menjalankan aplikasi web

Tidak diperlukan instalasi dependensi. Dari folder proyek, jalankan server web lokal:

```powershell
python -m http.server 8000
```

Buka <http://localhost:8000> di browser. Untuk menghentikan server, tekan `Ctrl+C` di terminal.

Ikon pada halaman menggunakan Font Awesome dari CDN, sehingga ikon memerlukan koneksi internet.

## Menjalankan versi terminal

Jika Python tersedia, jalankan:

```powershell
python index.py
```

Ikuti menu di terminal untuk menambah, melihat, menyelesaikan, dan menghapus tugas.

## Berkas proyek

- `index.html` — struktur halaman aplikasi web.
- `styles.css` — tampilan dan gaya aplikasi.
- `script.js` — interaksi aplikasi web dan penyimpanan browser.
- `index.py` — versi aplikasi daftar tugas berbasis terminal.

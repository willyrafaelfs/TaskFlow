# TaskFlow

Aplikasi daftar tugas sederhana yang berjalan langsung di browser. Tambahkan tugas, tandai sebagai selesai, dan saring daftar sesuai statusnya. Aplikasi web tidak memerlukan proses build atau instalasi dependensi.

## Fitur

- Menambahkan dan menghapus tugas.
- Menandai tugas sebagai selesai atau belum selesai.
- Menyaring daftar untuk melihat semua, tugas aktif, atau tugas selesai.
- Menghapus semua tugas yang sudah selesai.
- Menyimpan tugas di `localStorage` browser.

## Menjalankan secara lokal

### Aplikasi web

Persyaratan: Python 3 untuk menjalankan server web lokal. Tidak ada dependensi proyek yang perlu dipasang.

Klon repositori dari GitHub atau GitLab, lalu masuk ke folder proyek:

```bash
git clone https://github.com/willyrafaelfs/TaskFlow.git
cd TaskFlow
```

Atau gunakan GitLab:

```bash
git clone https://gitlab.com/willyrafaelfs/TaskFlow.git
cd TaskFlow
```

Jalankan server lokal:

```bash
python -m http.server 8000
```

Buka <http://localhost:8000> di browser. Hentikan server dengan `Ctrl+C` di terminal.

> Ikon menggunakan Font Awesome dari CDN, sehingga memerlukan koneksi internet.

### Aplikasi terminal Python

Repositori ini juga menyertakan versi daftar tugas berbasis terminal:

```bash
python index.py
```

Versi terminal berjalan terpisah dari aplikasi web dan tidak menggunakan daftar tugas yang sama.

## Penyimpanan data

Daftar tugas disimpan di `localStorage`. Data hanya tersedia pada browser dan perangkat tempat tugas dibuat; data tidak tersinkron ke perangkat lain. Menghapus data situs dari browser juga dapat menghapus daftar tugas.

## Struktur berkas

| Berkas | Keterangan |
| --- | --- |
| `index.html` | Struktur halaman aplikasi web |
| `styles.css` | Gaya dan tata letak |
| `script.js` | Interaksi aplikasi dan penyimpanan tugas di browser |
| `index.py` | Versi aplikasi daftar tugas berbasis terminal |

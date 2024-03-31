# Aplikasi Web Profil dan Buku Tamu

Aplikasi web ini dibangun menggunakan Django dan Python, dirancang untuk menampilkan informasi diri termasuk foto dan berita terkini, serta menyediakan form buku tamu bagi pengunjung untuk meninggalkan pesan.

# Fitur

- **Halaman Profil**: Menampilkan informasi diri termasuk nama, deskripsi singkat, dan foto diri. Informasi dan foto bisa diubah sesuai dengan pengguna aplikasi.
- **Halaman Berita**: Menampilkan berita-berita terkini yang diambil dari sumber online atau ditulis secara manual. Halaman ini memberikan update terbaru kepada pengunjung.
- **Form Buku Tamu**: Memungkinkan pengunjung untuk meninggalkan pesan atau komentar. Data yang diminta meliputi nama, email, dan pesan dari pengunjung.

## Teknologi

- **Backend**: Aplikasi ini menggunakan Django sebagai kerangka kerja web dan Python sebagai bahasa pemrogramannya.
- **Frontend**: HTML, CSS, dan JavaScript digunakan untuk desain antarmuka pengguna.

## Instalasi

1. Klon repositori ini atau unduh sebagai ZIP dan ekstrak. \s
   `git clone https://github.com/adammmmd/mycv.git`
2. install library yang digunakan dan jalankan aplikasi \s
   `pip install pillow django_import_export` \s
   `python manage.py runserver`

untuk mengakses data dengan django-admins
`python manage.py createsuperuser`

# Cubers Paradise

**Tugas 2 PBP**

Nama: Ricky Setiawan

Kelas: PBP E

NPM: 2206083161

Tautan aplikasi adaptable: [cubersparadise](https://cubersparadise3.adaptable.app/).

## Membuat sebuah proyek Django baru
1. Membuat sebuah direktori lokal baru sesuai yang diinginkan seperti cubersparadise dan buka command prompt atau terminal ke direktori tersebut.
2. Buat *virtual environment* agar *package* serta *dependencies* dari aplikasi kita terisolasi sehingga tidak akan bertabrakan dengan versi lain yang mungkin ada didalam komputer. Dapat dilakukan dengan menulis `python -m venv env` pada command prompt.
3. Jalankan *virtual environment* dengan `env\Scripts\activate.bat` untuk windows dan `source env/bin/activate` untuk mac/linux.
4. Untuk keluar dari *virtual environment* kita hanya butuh menuliskan `deactivate` pada command prompt untuk melakukannya (tetapi jalankan setelah semua sudah selesai).
5. Buat sebuah berkas `requirements.txt` yang berisi
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
pillow
```
5. Lalu install dengan command `pip install -r requirements.txt` yang akan menginstall semua yang ada di `requirements.txt`.
6. Buat proyek Django baru dengan command berikut `django-admin startproject cubersparadise .` dan direktori proyek Django baru dengan nama cubersparadise (tidak harus bernama cubersparadise bisa disesuaikan dengan keinginan) akan muncul di direktori yang sudah kita buat diawal.
7. Buka file bernama `settings.py` di dalam direktori proyek lalu cari `ALLOWED_HOSTS` dan ubah menjadi ```["*"] ``` didalamnya untuk mengizinkan akses dari semua host.
8. Jalankan server dengan perintah `python manage.py runserver` lalu akses `http://localhost:8000` jika terdapat gambar rocket maka Django sudah terinstall.
9. Untuk menghentikan server cukup menggunakan `ctrl+c` untuk menghentikannya.

## Membuat aplikasi dengan nama main pada proyek tersebut.
1. Jalankan *virtual environment* dan jalankan perintah `python manage.py startapp main` untuk membuat direktori aplikasi bernama main didalam proyek.
2. Jangan lupa menambahkan ``` 'main', ``` pada bagian `INSTALLED_APPS` didalam `settings.py`.





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
pillow #untuk gambar-gambar
```
5. Lalu install dengan command `pip install -r requirements.txt` yang akan menginstall semua yang ada di `requirements.txt`.
6. Buat proyek Django baru dengan command berikut `django-admin startproject cubersparadise .` dan direktori proyek Django baru dengan nama cubersparadise (tidak harus bernama cubersparadise bisa disesuaikan dengan keinginan) akan muncul di direktori yang sudah kita buat diawal.
7. Buka file bernama `settings.py` di dalam direktori proyek lalu cari `ALLOWED_HOSTS` dan ubah menjadi ```["*"] ``` didalamnya untuk mengizinkan akses dari semua host. Tambahkan juga
```
# Media settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
untuk mengatur gambar-gambar yang ditambahkan.
8. Jalankan server dengan perintah `python manage.py runserver` lalu akses `http://localhost:8000` jika terdapat gambar rocket maka Django sudah terinstall.
9. Untuk menghentikan server cukup menggunakan `ctrl+c` untuk menghentikannya.
10. Buat sebuah berkas yang dinamai `.gitignore` yang akan memberi tahu git berkas dan direktori mana saja yang harus diabaikan. Berikut isi yang harus dimasukkan didalam .gitignore.
```
# Django
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
media

# Backup files
*.bak 

# If you are using PyCharm
# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf

# AWS User-specific
.idea/**/aws.xml

# Generated files
.idea/**/contentModel.xml

# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml

# Gradle
.idea/**/gradle.xml
.idea/**/libraries

# File-based project format
*.iws

# IntelliJ
out/

# JIRA plugin
atlassian-ide-plugin.xml

# Python
*.py[cod] 
*$py.class 

# Distribution / packaging 
.Python build/ 
develop-eggs/ 
dist/ 
downloads/ 
eggs/ 
.eggs/ 
lib/ 
lib64/ 
parts/ 
sdist/ 
var/ 
wheels/ 
*.egg-info/ 
.installed.cfg 
*.egg 
*.manifest 
*.spec 

# Installer logs 
pip-log.txt 
pip-delete-this-directory.txt 

# Unit test / coverage reports 
htmlcov/ 
.tox/ 
.coverage 
.coverage.* 
.cache 
.pytest_cache/ 
nosetests.xml 
coverage.xml 
*.cover 
.hypothesis/ 

# Jupyter Notebook 
.ipynb_checkpoints 

# pyenv 
.python-version 

# celery 
celerybeat-schedule.* 

# SageMath parsed files 
*.sage.py 

# Environments 
.env 
.venv 
env/ 
venv/ 
ENV/ 
env.bak/ 
venv.bak/ 

# mkdocs documentation 
/site 

# mypy 
.mypy_cache/ 

# Sublime Text
*.tmlanguage.cache 
*.tmPreferences.cache 
*.stTheme.cache 
*.sublime-workspace 
*.sublime-project 

# sftp configuration file 
sftp-config.json 

# Package control specific files Package 
Control.last-run 
Control.ca-list 
Control.ca-bundle 
Control.system-ca-bundle 
GitHub.sublime-settings 

# Visual Studio Code
.vscode/* 
!.vscode/settings.json 
!.vscode/tasks.json 
!.vscode/launch.json 
!.vscode/extensions.json
.history
```

## Membuat aplikasi dengan nama main pada proyek tersebut.
1. Jalankan *virtual environment* dan jalankan perintah `python manage.py startapp main` untuk membuat direktori aplikasi bernama main didalam proyek.
2. Jangan lupa menambahkan ``` 'main', ``` pada bagian `INSTALLED_APPS` didalam `settings.py`.
```
INSTALLED_APPS = [
    ...,
    'main',
    ...
]
```
## Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
1. Masuk ke berkas urls.py pada direktori proyek (cubersparadise) dan isi sebagai berikut.
```
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
kode ini akan menambahkan path aplikasi kita dan juga menambahkan url gambar.

## Membuat model pada aplikasi main dengan nama Item.
1. Masuk ke models.py yang berada di main dan tambahkan kode berikut
```
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='items/')  

    def __str__(self):
        return self.name

```
untuk menambahkan model item dengan atribut-atributnya.
2. Lalu lakukan migrasi dengan menjalankan perintah `python manage.py makemigrations` untuk membuat migrasinya dan jalankan `python manage.py migrate` untuk melakukan migrasi.

## Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
1. 
## Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
1. Buat berkas baru `urls.py` didalam aplikasi `main`

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Request (URL)
   |
   v
URL Mapping (urls.py)
   |
   v
Data Query (models.py)
   |
   v
Data Retrieval and Processing (views.py)
   |
   v
Response Creation (views.py)
   |
   v
Template Rendering (HTML Template)
   |
   v
HTTP Response (views.py)
   |
   v
   Browser Pengguna


1. Request (URL)
Klien (pengguna) memasukkan URL ke browser mereka untuk mengakses aplikasi Django.

2. URL Mapping (urls.py)
File urls.py di proyek Django mengatur rute URL. Ini mengarahkan permintaan ke fungsi yang sesuai di views.py berdasarkan URL yang dimasukkan oleh klien.

3. Data Query (models.py)
Di dalam models.py, permintaan data (query) ke database dapat dilakukan menggunakan model "Item". Ini melibatkan pengambilan data dari database sesuai dengan permintaan yang diberikan.

4. Data Retrieval and Processing (views.py)
Fungsi di views.py digunakan untuk mengambil data yang diperlukan dari model, melakukan pemrosesan logika bisnis jika diperlukan, dan menyiapkan data untuk ditampilkan di dalam template HTML.

5. Response Creation (views.py)
Setelah data diproses, fungsi di views.py akan membuat objek respons HTTP yang akan dikirimkan kembali ke klien. Ini bisa berupa objek HttpResponse yang berisi HTML atau data JSON, tergantung pada permintaan.

6. Template Rendering (HTML Template)
Template HTML digunakan untuk merender data yang telah disiapkan di dalam views. HTML template ini mengatur tampilan halaman yang akan ditampilkan kepada pengguna, dan data dari views dimasukkan ke dalam template.

7. HTTP Response (views.py)
Objek respons HTTP yang telah dibuat di views dikirimkan kembali ke klien, dan hasilnya akan ditampilkan di browser pengguna.

Dengan cara ini, aplikasi web berbasis Django memproses permintaan dari klien dengan memisahkan peran masing-masing komponen (urls.py, views.py, models.py, dan HTML template) untuk menghasilkan respon yang akhirnya ditampilkan kepada pengguna.

## Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Kita menggunakan virtual environment untuk mengisolasi dependensi dan paket Python yang digunakan dalam proyek Django. Ini memungkinkan kita untuk menghindari konflik antara versi berbeda dari paket dan memastikan bahwa proyek kita dapat berjalan dengan benar. Tanpa menggunakan virtual environment, kita mungkin akan mengalami masalah dengan dependensi yang saling bertentangan antara proyek-proyek yang berbeda.

Kita masih dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapi ini tidak disarankan karena dapat menyebabkan masalah dependensi yang rumit.

## Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
MVC (Model-View-Controller)
MVC adalah pola desain arsitektur perangkat lunak yang memisahkan aplikasi menjadi tiga bagian utama:

1. Model: Bagian ini menangani pengelolaan data dan logika bisnis dalam aplikasi.
2. View: Bertugas menampilkan informasi kepada pengguna, sehingga pengguna dapat melihat dan berinteraksi dengan aplikasi.
3. Controller: Bagian ini menerima input dari pengguna dan mengatur interaksi antara Model dan View.

MVT (Model-View-Template)
MVT adalah varian dari pola MVC yang digunakan dalam kerangka kerja Django:

1. Model: Mirip dengan bagian Model dalam MVC, ini mengelola data dan logika bisnis aplikasi.
2. View: Bertanggung jawab untuk mengatur logika presentasi dan mengirim data ke template.
3. Template: Bagian ini menampilkan data yang diterima dari View dalam bentuk yang sesuai untuk ditampilkan kepada pengguna.

MVVM (Model-View-ViewModel)
MVVM adalah pola desain arsitektur yang umumnya digunakan dalam pengembangan aplikasi berbasis data:

1. Model: Bertanggung jawab untuk mengelola data dan logika bisnis, mirip dengan Model dalam MVC dan MVT.
2. View: Berperan dalam menampilkan informasi kepada pengguna seperti pada pola sebelumnya.
3. ViewModel: Bagian ini menghubungkan Model dan View. ViewModel mengubah data Model ke dalam format yang dapat ditampilkan oleh View, memungkinkan tampilan yang lebih dinamis dan reaktif kepada perubahan data.

Dalam semua tiga pola desain ini, tujuannya adalah memisahkan peran masing-masing komponen dalam aplikasi agar lebih mudah dikelola dan dimodifikasi. Hal ini membantu dalam pengembangan aplikasi yang bersih, terstruktur, dan mudah dipelihara.




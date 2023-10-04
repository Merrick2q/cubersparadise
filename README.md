# Cubers Paradise

# Tugas 2 PBP

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
1. Buat direktori baru bernama `templates` yang akan menampung semua berkas html.
2. Buka views.py pada direktori aplikasi main.
3. Tambahkan berkas berikut.
```
from django.shortcuts import render

def product_list(request):
    sample_items = [
        {
            'name': 'Mscube MS3X',
            'quantity': 5,
            'description': 'Puzzle rubik flagship oleh Mscube. Pendiri Mscube adalah mantan designer dari perusahaan pembuat rubik paling terkenal di dunia yaitu Gancube.',
            'image': 'https://www.thecubicle.com/cdn/shop/products/DianSheng-MS3X-3x3-black-internal_1200x1200.jpg?v=1670870380',  
        },
        {
            'name': 'Dayan Tengyun V3 M',
            'quantity': 3,
            'description': 'Rubik Tengyun generasi ketiga dari Dayan yang terkenal dengan putarannya yang sunyi.',
            'image': 'https://www.thecubicle.com/cdn/shop/products/dayan-tengyun-v3-m_1200x1200.jpg?v=1670433801',  
        },
        {
            'name': 'Huameng YS3M',
            'quantity': 7,
            'description': 'Rubik dari perusahaan baru bernama Huameng yang merupakan anak perusahaan perusahaan pembuat rubik terkenal MoYu.',
            'image': 'https://www.thecubicle.com/cdn/shop/products/moyu-huameng-ys3m-standard_grande.jpg?v=1687294228', 
        },
    ]

    return render(request, 'product_list.html', {'items': sample_items})
```
3. `from django.shortcuts import render` akan menjalankan render yang memunculkan berkas html didalam direktori template saat menjalankan aplikasi nantinya.
4. Disini karena saya membuat tabel dengan banyak produk saya membuat inputnya berupa *list*.
5. Lalu ubah isi dari berkas html dengan sintaks Django `{{ }}` agar data dari view dapat masuk ke berkas html tersebut.

## Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
1. Buat berkas baru `urls.py` didalam aplikasi `main`. Isi dengan kode dibawah
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
]
```
Kode ini akan mengkonfigurasi routing URL aplikasi main.

## Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
1. Masuk ke akun adaptable pada web adaptable.
2. Masuk ke *app dashbaord* dan tekan `New App`.
3. Pilih `Connect an Existing Repository` dan pilih repositori proyek yang sudah kita push ke github.
4. Pilih Python App Template sebagai template deployment dan PostgreSQL sebagai tipe basis data yang akan digunakan.
5. Sesuaikan dengan versi python yang terinstall di komputer kita dan tambahkan `python manage.py migrate && gunicorn <nama proyek>.wsgi` pada start command.
6. Lalu tentukan nama aplikasi yang kita inginkan muncul sebagai domain.
7. Tekan pada bagian `HTTP Listener on PORT` dan tekan deploy app.
8. Tunggu sejenak hingga aplikasi kita berhasil di jalankan oleh adaptable (Kadang bermasalah).

## Membuat sebuah README.md yang berisi tautan menuju aplikasi Adaptable
1. Cara mudahnya adalah langsung menambahkan README.md melalui github.

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
```
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
```

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

# Tugas 3 PBP
## Apa perbedaan antara form POST dan form GET dalam Django?
1. form POST: adalah form yang digunakan untuk mengirimkan data form yang memiliki potensi besar atau sensitif ke server tanpa terlihat oleh pengguna (seperti pengiriman data pengguna, dan lain-lainnya).
2. form GET: adalah form yang digunakan untuk mengambil data dari server dengan parameter tertentu (seperti pencarian dan atau filter data).

## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
1. XML (eXtensible Markup Language): XML adalah bahasa markup yang digunakan untuk mendefinisikan struktur data. Ini adalah format teks yang dapat disesuaikan dengan tag-tag yang digunakan untuk mengelompokkan dan mengatur data.
- Penggunaan Umum: XML sering digunakan untuk pertukaran data antara sistem yang berbeda. Ini sering digunakan dalam layanan web, berkas konfigurasi, dan sebagai format penyimpanan data.
- Keunggulan: XML memiliki kemampuan untuk menggambarkan struktur data yang sangat kompleks dan mendukung validasi terhadap struktur tersebut. Ini juga mendukung atribut yang memungkinkan penggunaan metadata tambahan.
- Kelemahan: XML memiliki sintaks yang lebih berat dibandingkan dengan JSON dan HTML, sehingga bisa lebih sulit dibaca oleh manusia. Ukuran file XML biasanya lebih besar dibandingkan JSON dan HTML.

2. JSON (JavaScript Object Notation): JSON adalah format pertukaran data yang ringan dan mudah dibaca oleh manusia. Ini menggunakan sintaks objek dan array dari JavaScript untuk merepresentasikan data.
- Penggunaan Umum: JSON sering digunakan dalam pertukaran data antara aplikasi web dan server, penyimpanan konfigurasi, serta sebagai format data untuk API REST.
- Keunggulan: JSON memiliki sintaks yang mudah dibaca, ringkas, dan ringan. Ini merupakan format yang sangat populer dalam pengembangan web modern.
- Kelemahan: JSON tidak mendukung atribut seperti XML dan memiliki dukungan yang lebih terbatas untuk tipe data yang kompleks.

3. HTML (Hypertext Markup Language): HTML adalah bahasa markup yang digunakan untuk membuat halaman web. Ini digunakan untuk mendefinisikan struktur dan tampilan konten pada halaman web.
- Penggunaan Umum: HTML adalah bahasa dasar untuk membuat halaman web. Ini digunakan untuk menampilkan teks, gambar, tautan, formulir, dan elemen-elemen lain di dalam browser web.
- Keunggulan: HTML dioptimalkan untuk mengatur tampilan dan interaksi antarmuka pengguna. Ini memiliki dukungan yang kuat untuk tautan dan formulir web.
- Kelemahan: HTML tidak dirancang untuk pertukaran data struktural, seperti XML dan JSON. Ini lebih fokus pada presentasi dan interaksi pengguna.
Dalam konteks pengiriman data, XML dan JSON umumnya digunakan untuk pertukaran data antara aplikasi atau sistem, sementara HTML digunakan untuk membuat halaman web yang dapat diakses oleh pengguna melalui browser web. Pemilihan format tergantung pada kebutuhan dan tujuan pengiriman data.

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON saat ini sering digunakan dalam pertukaran data bukan lain adalah karena keunggulannya. Berikut ini keunggulan dari penggunaan JSON.
- Ringan dan mudah dibaca
- Ringan dalam penggunaan sumber daya
- Dukungan untuk tipe data yang umum
- Kompatibilitas dengan JavaScript
- Dukungan untuk RESTful API
- Banyak library yang tersedia
- Dukungan untuk pengembangan terdistribusi

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
## Membuat input form untuk menambahkan objek model pada app sebelumnya.
1. Pertama-tama kita buat berkas baru bernama `forms.py` yang memiliki tujuan untuk membuat struktur form yang kita inginkan. Disini saya mengisi berkas `forms.py` saya sebagai berikut.
```
from django import forms
from main.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "quantity", "description", "image"]

```
disini saya membuat form untuk nama, banyak barang, deskripsi, dan juga gambar dari produknya (saat ini saya ubah image pada models.py menjadi URLfield).
2. Lalu pindah ke `views.py` dan menambahkan beberapa import yaitu 
```
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from main.forms import Product
from django.urls import reverse
```
untuk dapat mengakses data pada `forms.py` dan `models.py` dan juga untuk dapat melakukan redirect setelah data dari form disimpan.
3. Menambahkan fungsi baru pada `viewss.py`
```
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:product_list'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```
yang akan menyimpan form yang kita atau pengguna kirimkan dan menampilkan pada template html.
4. Buat sebuah berkas html baru untuk menampilkan halaman form kita sesuai keinginan dan juga menambahkan button pada berkas html utama kita.

## Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
1. Pergi ke `views.py` dan saya tambahkan fungsi-fungsi berikut.
```
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:product_list'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
fungsi ini akan memungkinkan kita untuk dapat melihat produk yang telah kita tambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.

## Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
1. Pada `urls.py` di main kita akan mengimport semua yang baru saja kita tambahkan yaitu
```
from main.views import product_list, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
```
2. Lalu kita sesuaikan path url-nya.
```
urlpatterns = [
    path('', product_list, name='product_list'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]
```
sekarang kita dapat melihat semua semua produk yang telah kita tambahkan dalam berbagai format. Untul xml dan juga json kita dapat melihat barang kita dengan menambahkan `xml/`, `xml/<int:id>/`, `json/`, atau `json/<int:id>/` dengan `<int:id>` berarti barang urutan keberapa yang ingin kita liat.

## Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
1. HTML
![urls py - cubersparadise - Visual Studio Code 9_19_2023 11_23_04 PM](https://github.com/Merrick2q/cubersparadise/assets/120576374/f15c4889-0439-43a5-84e5-03eecc40012e)
2. XML
![http___localhost_8000_xml - My Workspace 9_19_2023 11_21_38 PM](https://github.com/Merrick2q/cubersparadise/assets/120576374/3f423e6e-2578-40be-8b5f-125eb656ca1d)
3. JSON
![http___localhost_8000_xml - My Workspace 9_19_2023 11_21_26 PM](https://github.com/Merrick2q/cubersparadise/assets/120576374/b257db4e-bd38-454e-a2a1-0440e2f43528)
4. XML *by* ID
![http___localhost_8000_xml - My Workspace 9_19_2023 11_22_01 PM](https://github.com/Merrick2q/cubersparadise/assets/120576374/89b94dfc-d1e4-421a-900f-047ac2f3b3e4)
5. JSON *by* ID
![http___localhost_8000_xml - My Workspace 9_19_2023 11_22_10 PM](https://github.com/Merrick2q/cubersparadise/assets/120576374/e2dbf022-4327-423a-9aca-f6fd302f90e7)

## Bonus
Saya menambahkan class ini pada html saya yang akan menghitung banyaknya barang yang ada dengan menggunakan `length` yang akan menghitung banyaknya data pada list produk yang ada.
```
<div class="count_item">
    <p>Anda telah memasukkan {{ items|length }} produk pada aplikasi ini</p>
</div>
```
Dan lalu saya style sesuai kemauan saya.

# Tugas 4 PBP
## Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Django UserCreationForm adalah sebuah form atau formulir bawaan django yang berfungsi untuk pendaftaran pengguna. Hal ini memungkinkan pengguna untuk dapat mendaftar ke aplikasi kita dengan mengisi informasi-informasi yang sudah ditentukan (username, password, nama, dll).
Kelebihan: 
- Sederhana dan mudah digunakan
- Integrasi dengan sistem autentikasi Django
- Validasi otomatis (tidak perlu menambahkan validasi)
Kekurangan:
- UserCreationForm dibuat untuk keperluan pendaftaran standar, sehingga jika kita memerlukan fitur yang tidak ada maka kita harus melakukan penyesuaian (menambahkan kode baru)
- Tidak Mendukung Opsi OAuth (autentikasi dengan pihak ketiga)
- Mungkin akan memerlukan validasi tambahan

## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
- Autentikasi
Adalah proses yang dijalani untuk memverifikasi pengguna. Hal ini untuk memeriksa apakah benar orang tersebut adalah orang yang mereka klaim adalah dirinya. Dalam django autentikasi berfokus pada proses verfiikasi apakah pengguna sudah memasukkan informasi-informasi yang valid.
- Otorisasi
Adalah proses setelah autentikasi yang mengatur apasaja yang di izinkan dan tidak dari pengguna tersebut. Dalam django otorisasi berkaitan dengan pengendalian hak akses pengguna terhadap fitur ataupun sumber daya yang dimiliki aplikasi.

Keduanya penting karena keduanya bekerja bersama untuk menciptakan lapisan keamanan yang kokoh dalam aplikasi. Autentikasi memastikan hanya pengguna sah yang dapat masuk ke aplikasi dan otorisasi memastikan pengguna tersebut tidak melakukan hal yang berbeda dengan hak izinnya.

## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies dalam konteks aplikasi web adalah mekanisme penyimpanan data kecil yang digunakan untuk menyimpan informasi sementara dari browser pengguna. Informasi ini kemudian dapat digunakan untuk pengelolaan sesi pengguna, pelacakan, personalisasi, dll.
Django menggunakan cookies untuk mengelola data sesi pengguna dengan memanfaatkan salah satu komponennya yang disebut "Django's Session Framework". Berikut ini adalah cara django mengelola data sesi pengguna.
- Inisiasi session cookies: Saat pengguna memasuki web django, server akan membuat sesi cookie baru yang dikirim ke browser pengguna. Cookie yang dibuat ini mengandung sebuah ID sesi yang unik, yang nantinya akan digunakan untuk mengidentifikasi sesi pengguna.
- Penyimpanan data berdasarkan ID sesi: Informasi dari pengguna dimasukkan kedalam server.
- Pengelolaan data berdasarkan ID sesi: Ketika pengguna memberikan permintaan, Django akan menggunakan ID sesi untuk mengakses data sesi yang tersimpan dalam server sehingga dapat memberikan data yang sesuai.
- Memperbarui data sesuai dengan permintaan: Data yang disimpan juga dapat di ubah ataupun ditambahkan. 
- Penghapusan sesi berdasarkan permintaan: Apabila sesi dari pengguna telah habis (logout atau sesi melebihi limit waktu) data sesi dan cookie akan dihapus.

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan cookies jika dilakukan dengan benar relatif aman. Namun, terdapat beberapa risiko potensial yang dapat terjadi, yaitu
- Pencurian Cookies: Cookies dapat menjadi target pencurian jika tidak dienkripsi dengan baik. Pencuri yang berhasil mendapatkan cookies sesi dapat mengakses sesi pengguna tanpa izin.
- Cross-Site Scripting (XSS): Serangan XSS dapat memungkinkan penyerang untuk mencuri cookies pengguna atau menjalankan kode berbahaya di dalam peramban pengguna. Penggunaan HttpOnly pada cookies dapat membantu mengurangi risiko ini.
- Man-in-the-Middle (MitM) Attacks: Penyerang dalam serangan MitM dapat mencoba menggagalkan atau mencuri cookies saat berinteraksi dengan server dan peramban pengguna.
- Cookie Theft dari Browser: Jika perangkat pengguna rentan terhadap pencurian, cookies dapat dicuri jika peramban pengguna atau perangkat ditinggalkan tanpa pengamanan yang memadai.
- Pelacakan dan Privasi: Cookies sering digunakan untuk melacak perilaku pengguna. Ini dapat menimbulkan masalah privasi jika tidak dikelola dengan benar.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
## Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
1. Pertaman-tama masuk ke virtual environment terlebih dahulu.
2. Lalu disini saya menambahkan beberapa fungsi baru pada `views.py` yang digunakan untuk melakukan registrasi, login, dan logout.
```
def registrasi(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'registrasi.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:product_list")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
3. Tidak lupa juga untuk memasukkan import yang diperlukan.
```
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
```
4. Untuk dapat menampilkan fungsi registrasi dan login kita harus membuat berkas html baru pada `main/template` yang bersesuaian.
- registrasi.html (untuk menampilkan halaman registrasi jika tombol registrasi ditekan)
```
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```
- login.html (untuk menampilkan halaman login sebelum ke halaman main (product_list.html))
```
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:registrasi' %}">Register Now</a>

</div>

{% endblock content %}
```
5. Untuk logout kita hanya perlu menambahkan tombol logout pada `product_list.html`.
```
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
```
6. Lalu kita tambahkan semuanya ke `main/urls,py`.
- Importnya akan menjadi seperti ini
```
from main.views import product_list, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, registrasi, login_user, logout_user
```
- Tambahkan pathnya
```
path('registrasi/', registrasi, name='registrasi'),
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),
```

7. Untuk merestriksi akses halaman `product_list` kita dapat menaruh `@login_required(login_url='/login')` diatas fungsi `product_list`. Dan menambahkan import ini `from django.contrib.auth.decorators import login_required` sehingga agar dapat masuk ke halaman utama pengguna harus melakukan login terlebih dahulu.

## Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
![Cubers Paradise - Google Chrome 9_27_2023 6_51_32 AM](https://github.com/Merrick2q/cubersparadise/assets/120576374/d238012d-c24e-4677-9006-88292c1bfc12)
![Cubers Paradise - Google Chrome 9_27_2023 6_55_51 AM](https://github.com/Merrick2q/cubersparadise/assets/120576374/11b268de-710d-4605-9973-2b070d0f0df6)

## Menghubungkan model Item dengan User.
1. Pada `models.py` kita tambahkan import berikut.
```
from django.contrib.auth.models import User
```
2. Lalu kita tambahkan model `user = models.ForeignKey(User, on_delete=models.CASCADE)` pada class Product
3. Setelah kita kita ke `views.py` untuk mengubah change_product menjadi berikut.
```
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:product_list'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```
4. Lalu pada fungsi product_list kita ubah products menjadi `products = Product.objects.filter(user=request.user)` dan menambahkan nama user pada context dengan `'nama': request.user.username,`. Sehingga fungsi product_list akan menjadi seperti berikut.
```
@login_required(login_url='/login')
def product_list(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'nama': request.user.username,
        'items': products,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, 'product_list.html', context)
```
5. sehabis itu kita melakukan migrasi. Saat menjalankan makemigrations akan muncul error. Kita akan pilih 1 untuk menetapkan default value untuk field user pada semua row yang telah dibuat pada basis data. Ketik 1 lagi agar user (yang sudah kita buat sebelumnya) dapat ditetapkan dengan ID 1 pada model yang sudah ada. Lalu baru kita dapat menjalankan migrate.

## Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
1. Pada `views.py` kita tambahkan import berikut.
```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
2. Ubah `login_user` menjadi sedemikian.
```
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:product_list")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```
3. Lalu kita tambahkan nama dari username dan juga last_login untuk memunculkan infomasi mereka pada fungsi `product_list` dibagian context sehingga menjadi seperti dibawah.
```
@login_required(login_url='/login')
def product_list(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'nama': request.user.username,
        'items': products,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, 'product_list.html', context)
```
4. Lalu pastikan fungsi `logout_user` sudah sesuai dengan dibawah.
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
5. Lalu kita cukup menambahkan pada html utama kita (product_list.html) dengan informasi yang baru kita tambahkan pada context.
```
<h5> Halo {{ nama }} </h5>
<h5> Sesi terakhir login: {{ last_login }} </h5>
```
Sesuaikan penempatannya dengan kode kita.

# Tugas 5
## Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
1. Element selector
    Merupakan selector yang memilih elemen HTML langsung berdasarkan tag elemen tersebut. Bermanfaat jika kita ingin mengubah style semua elemen pada suatu tag.
2. Class selector
    Merupakan selector yang hanya memilih elemen dengan atribut class yang diinginkan. Bermanfaat jika kita ingin mengubah style elemen-elemen yang berkarakteristik sama.
3. ID selector
    Merupakan selector yang memilih elemen berdasarkan ID yang sudah didefinisikan. Bermanfaat jika kita ingin mengubah style elemen secara spesifik (tidak mempengaruhi elemen dengan tag yang sama).
4. Attribute selector
    Merupakan selector yang memilih elemen berdasarkan atributnya. Bermanfaat jika kita ingin mengubah style elemen dengan atribut tertentu.
5. Universal selctor
    Merupakan selector yang akan mempengaruhi semua elemen dalam HTML. Bermanfaat untuk style yang ingin kita aplikasikan ke seluruh elemen.
## Jelaskan HTML5 Tag yang kamu ketahui.
- `<br>`, breakline untuk membuat sebuah break (simpelnya enter).
- `<body>`, mendefinisikan body (isi dari file)dari HTML.
- `<head>`, mendefinisikan head (informasi file seperti judul) dari HTML.
- `<div>`, menentukan sebuah divisi.
- `<header>`, merepresentasikan header atau pendahulu dari file.
- `<h1> hingga <h6>`, mendefinisikan heading.
- `<p>`, mendefinisikan paragraf.
- `<img>`, merepresentasikan gambar.
- `<html>`, mendefinisikan root dari file HTML.
- `<li>`, mendefinisikan item list.
- `<nav>`, mendefinisikan navbar (biasanya untuk link).
- `<style>`, memasukkan internal css ke head dari file.
- `<table>`, mendefinisikan sebuah tabel.
- `<thead>`, membuat sebuah baris yang berisi informasi tabel.
- `<tbody>`, mendefiniskan isi dari tabel.
- `<th>`, mendefinisikan header tabel.
- `<tr>`, mendefinisikan baris pada tabel.
- `<td>`, mendefinisikan sebuah sel tabel.
- `<title>`, mendefinisikan judul dari file.
- `<ul>`, mendefinisikan unordered list.
- `<button>`, mendefinisikan sebuah tombol.
## Jelaskan perbedaan antara margin dan padding.
Margin mengatur kekosongan area yang berada disekitar border sedangkan padding mengatur kekosongan area disekitar content atau isinya langsung. Jadi urutannya dari terdalam hingga terluar adalah content, padding, border, margin.
## Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
Tailwind memiliki tingat kustomisasi yang lebih tinggi dibanding dengan Bootstrap, tetapi Bootstrap memiliki komponen siap pakai yang lebih banyak. Tailwind cenderung memiliki ukuran file yang lebih besar daripada Bootstrap dikarenakan oleh tingkat kostumisasinya.

Kita menggunakan Tailwind saat kita benar-benar ingin mengkostumisasi web kita. Dan kita menggunakan Bootstrap saat kita ingin membangu web dalam waktu yang singkat.
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
## Kustomisasi desain pada templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut.
Saya disini menggunakan internal style untuk css saya.
### Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin.
1. Saya menambahkan css untuk body sehingga mengubah font dan warna dari background dari `login.html`, `registrasi.html`, dan `create_product.html`. Saya juga menambahkan padding dan margin sehingga tampilannya tidak terlalu di pojok.
```
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f0f0f0;
        margin: 10px;
        padding: 10px;
    }
</style>
``` 
### Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card.
1. Saya menambahkan navbar pada bagian `product_list.html`.
```
<header>
    <h1 class="title">Cubers Paradise</h1>
    <nav>
        <ul class="nav">
            <p>Ricky Setiawan</p>
            <p>2206083161</p>
            <p>PBP E</p>
            <h3> Hallo {{ nama }} </h3>
        </ul>
    </nav>
    <a href="{% url 'main:logout' %}">
        <button>
            Logout
        </button>
    </a>  
</header>
```
2. Lalu saya kustomisasi sesuai dengan keinginan saya. Berikut ini style saya pada `product_list.html`
```
<style>
    /* CSS untuk pusatkan teks */
    body {
        text-align: center;
        font-family: Arial, sans-serif;
        background-color: #f0f0f0;
        margin: 0;
        padding: 0;
    }
    header {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        padding: 30px 10px;
        background-color: #333;
        color: #edf0f1;
        height: 35px;
    }
    header a {
        margin-left: 25px;
    }
    .title {
        cursor: pointer;
        margin-right: auto;
    }
    .nav {
        list-style: none;
    }
    .nav p {
        display: inline-block;
        padding: 0px 20px;
    }
    .nav h3 {
        display: inline-block;
        padding: 0px 20px;
    }
    /* CSS untuk gambar dalam tabel */
    img {
        max-width: 200px;
        max-height: 200px;
    }
    /* CSS untuk tabel */
    table {
        margin: 0 auto;
        border: 1px #333;
        border-collapse: collapse;
        border-spacing: 0;
        width: 80%;
        background-color: #fff;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    th, td {
        padding: 10px;
        text-align: center;
    }
    th {
        background-color: #333;
        color: #fff;
    }
    tr:nth-child(even) {
        background-color: #f2f2f2;
    }
    tr:hover {
        background-color: #ddd;
    }
    tr:last-child {
        background-color: #D3D3D3;
    }
    .count_item {
        text-align: center;
        background-color: #333;
        color: #fff;
        font-weight: bold;
        border: 2px solid;
        border-radius: 10px;
        padding: 5px;
        margin: 20px auto;
        max-width: 500px;
    }
    button {
        font-size: small;
        color: #edf0f1;
        padding: 9px 25px;
        background-color: rgba(0,136,169,1);
        border: none;
        border-radius: 50px;
        cursor: pointer;
        transition: all 0.3s ease 0s;
    }
    button:hover {
        background-color: rgba(0,136,169,0.8);
    }
</style>
```
3. Saya juga memiliki `manage_product.html` yang berfungsi untuk menambah, mengurang, atau menghapus jumlah item. Berikut style dari `manage_product.html`.
```
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f0f0f0;
        margin: 0;
        padding: 0;
        text-align: center;
    }
    h2 {
        padding: 25px;
    }
    table {
        border-collapse: collapse;
        width: 80%;
        margin: 20px auto;
    }
    th, td {
        padding: 10px;
        text-align: center;
        border: 1px solid #ddd;
    }
    th {
        background-color: #333;
        color: #fff;
    }
    tr:nth-child(even) {
        background-color: #f2f2f2;
    }
    tr:hover {
        background-color: #ddd;
    }
    .action-buttons { ##untuk tombol tambah, kurang, dan hapus
        display: flex;
        justify-content: space-around;
    }
    .back-button { ##untuk tombol kembali ke halaman utama
        display: block;
        margin-top: 20px;
        text-align: center;
    }
    button {
        font-size: small;
        color: #edf0f1;
        padding: 9px 25px;
        background-color: rgba(0,136,169,1);
        border: none;
        border-radius: 50px;
        cursor: pointer;
        transition: all 0.3s ease 0s;
    }
    button:hover {
        background-color: rgba(0,136,169,0.8);
    }
</style>
```



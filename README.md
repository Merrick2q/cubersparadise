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
![]()

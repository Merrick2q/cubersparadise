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
7. Buka file bernama `settings.py` di dalam direktori proyek lalu cari `ALLOWED_HOSTS` dan ubah menjadi ```["*"] ``` didalamnya untuk mengizinkan akses dari semua host.
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
1. 

## Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
1. Buat berkas baru `urls.py` didalam aplikasi `main`





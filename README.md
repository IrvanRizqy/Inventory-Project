Nama: Irvan
NPM: 2206083514
Kelas: PBP A

Link : [Adaptable Link](https://dwarves-weapon-inventory.adaptable.app/main/)

---------------------------------------------------------------------------------------------------------------------------------------------

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Pertama, membuat proyek Django Baru. Diawali dengan pembuatan direktori, yang saya namakan ``inventory_project``
- Setelah terbuatnya direktori, membuat virtual environment dengan perintah ``python -m venv env`` di command prompt dimana sebelum menjalankan perintah memasuki direktori ``inventory_project`` terlebih dahulu. Perintah ini berguna untuk membuat lingkungan virtual Python menggunakan modul ``venv``, serta untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputer kita.
- Selanjutnya mengkonfigurasi git agar dapat mengubungkan direktori lokal ke git project yang akan dibuat nanti, dengan perintah ``git init``.
- Sebelum dapat memverifikasi konfigurasi git dengan masukan nama dan email github yang digunakan kedalam cmd dengan perintah ``git config user.name "<NAME>"`` dan ``git config user.email "<EMAIL>"``.
- Setelah melakukan koneksi dengan GitHub saya menambahkan berkas dependencies ``requirements.txt``, dan  ``.gitignore``. Isi dari kedua berkas ini sama dengan isi yang diarahkan sebelumnya pada tutorial0 dengan 0 tambahan. Guna dari kedua berkas ini adalah menambahkan dependencies yang dibutuhkan kedalam direktori.
- setelah menambahkan berkas ``requirements.txt`` dalam command prompt saya menjalankan perintah ``pip install -r requirements.txt``. Command ini berguna untak menginstall dependencies kedalam direktori lokal
- Dilanjutkan dengan membuat proyek Django dengan menjalankan perintah ``django-admin startproject <nama_app> .``. Projectnya saya beri nama yang sama dengan direktori lokal ``inventory_project``
- Selanjutnnya saya mempersiapkan repositori baru di github agar dapat dihubungkan dengan direktori lokal yang telah dibuat sebelumnya, repositori ini saya namakan ``Inventory-Project``.
- Selanjutnya sayaa membuka file ``settings.py`` yang ada di dalam folder proyek, cari variabel ``ALLOWED_HOSTS`` dan mengubah nilainya menjadi ``["*"]`` untuk mengizinkan akses dari semua host.
- Sebelum dapat menghubungkan ke github saya membuat branch utama baru dengan perintah ``git branch -M main``, branch ini saya beri nama ``main``.
- Selanjutnya saya hubungkan direktori dengan repositori dengan perintah ``git remote add origin <URL_REPO>``.
- Untuk mengecek apakah projek django saya berjalan benar, saya menjalankan perintah ``env\Scripts\activate.bat`` dan ``python manage.py runserver`` di dalam direktori proyek untuk menjalankan server. Jika melihat animasi roket pada tautan ``http://localhost:8000``, maka proyek Django sudah berhasil. Untuk menghentikan server, saya memasukan input ``Ctrl+C`` di command prompt.
- Setelah terhubung dan mengecek projek django saya melakukan perintah ``git add .``, ``git commit -m <komentar>``, dan ``git push -u origin main``. untuk menyimpan isi direktori lokal ke GitHUb
- Setelah mengecek keberadaan file-file dan direktori dalam repositori github saya lanjutkan dengan membuat aplikasi bernama ``main`` dengan menjalankan perintah ``python manage.py startapp main``.
- Untuk mendaftarkan aplikasi `main` ke dalam proyek, saya mengedit file `settings.py` dan menambahkan `main` ke dalam daftar variabel ``INSTALLED_APPS``.
- Selanjutnya mengedit file `settings.py` yang terletak dalam direktori proyek. Dan menambahkan `main` ke dalam daftar variabel INSTALLED_APPS.
- Selanjutnya melakukan routing pada proyek dengan membuat berkas `urls.py` di dalam direktori main, dan mengisinya dengan kode yang terdapat pada tutorial1
- Selanjutnya membuat model pada aplikasi `main` dengan membuka file `models.py` dan mengisi file tersebut dengan nama Item, atribut-atribut dan tipe data yang ingin digunakan. (Kode yang digunakan tercantum pada tutorial1).
- Untuk memigrasi skema model ke database django lokal saya menggunakan perintah `python manage.py makemigrations` untuk mempersiapkan migrasi dan `python manage.py migrate` untuk menerapkan skema model.
- Selanjutnya membuat sebuah fungsi pada `views.py`. Dalam berkas `views.py` ditambahkan fungsi show_main (Kode yang digunakan tercantum pada tutorial1) dengan context baru seperti name, amount, description, category, dan stats.
- Setelah itu dalam berkas `main.html` yang ada di dalam direktori templates pada direktori `main` sebagai base untuk menampilkan data. Template html yang digunakan tercantum pada tutorial1 dengan tambahan baru seperti table dan list.
- Selanjutnya membuat file `urls.py` pada direktori `main` untuk memetakan fungsi yang telah dibuat pada views.py. (Kode yang digunakan tercantum pada tutorial1)
- Terakhir mengonfigurasi Routing URL Proyek di dalam berkas urls.py yang terletak di dalam direktori proyek (Kode yang digunakan tercantum pada tutorial1).
- Sebelum melakukan deployment ke Adaptable saya mengecek apakah aplikasi yang saya buat berjalan dengan benar dengan menjalankan perintah `python manage.py runserver` dan membuka tautan `http://localhost:8000/main/`.
- Setelah itu jalankan perintah ``git add .``, ``git commit -m <komentar>``, dan ``git push -u origin main``. untuk menyimpan isi direktori lokal ke GitHUb
- Tahap terkahir adalah melakukan deployment ke adaptable. Dimulai dengan login, meilih "New App" dan mengklik tombol "Connect an Existing Repository".
- Repositori yang saya pilih adalah ``Inventory-Project`` untuk dijadikan web baru dalam adaptable.
- Selanjutnya pilih template deployment "Python App Template" dan pilih PostgreSQL sebagai tipe basis data.
- Sesudah itu mesuaikan versi Python dengan versi python perangkat dan mengisi Start Command dengan python manage.py migrate && gunicorn (nama direktori utama).wsgi.
- Masukan nama aplikasi yang mau digunakan dan akhiri dengan mencentang "HTTP Listener on PORT" dan klik "Deploy App" untuk memulai proses deployment aplikasi.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. 

Pertama user akan meminta request kepada Django, lalu Django akan menggunakan `urls.py`. Setelah itu, `views.py` akan mengatur berbagai macam bentuk interaksi agar di dalam `models.py` dapat mengelola dan menyajikan data agar data yang telah diolah oleh `models.py` dapat ditampilkan pada templates dalam berkas `html`. Pada berkas `html`, berisi berbagai macam kode html seperti kode untuk membuat tabel, list, menentukan ukuran font dan lain lain, serta pada berkas `html` juga mengandung tag template Django agar dapat memasukan data dari dalam `views.py` ke dalam berkas `html`. Setelah selesai diolah, output tersebut akan dikirimkan sebagai respon kepada user.

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

![My Img](/main/templates/How%20Django%20Framework%20Works.png) 

Virtual Environment sangat berguna dalam menjaga proyek perangkat lunak Anda tetap rapi dan teratur. Selain menjaga kebersihan Virtual Environment juga berguna dalam mengisolasi proyek, menghindari kontaminasi global, menjaga Versi paket yang konsisten, menjaga kebersihan dan portabilitas, melakukan uji coba dan eksperimen, menjaga keamanan, mengelola versi python, melakukan pengembangan bersama

Mungkin saja membuat aplikasi web Django tanpa virtual environment. Namun, membuat web Django dengan cara ini sangat tidak dianjurkan karena akan lebih sulit untuk membuat proyek yang bagus dan kemungkinan mengalami masalah konflik dependensi di masa depan. Karena tidak menggunakan virtual environment, dependensi proyek yang digunakan akan diinstal secara global, ini akan menyebabkan penglolaan proyek menjadi lebih rumit, tidak bersih, dan kurang fleksibel

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah pola desain arsitektur yang digunakan dalam pengembangan perangkat lunak.
- MVC -> Model: Bagian yang bertugas untuk menyiapkan, mengatur, memanipulasi, dan mengorganisasikan data yang ada di database.
      -> View: Bagian yang bertugas untuk menampilkan informasi dalam bentuk Graphical User Interface (GUI).
      -> Controller: Bagian yang bertugas untuk menghubungkan serta mengatur model dan view agar dapat saling terhubung.
      <->Perbedaan : MVC lebih tua dibanding Pola desain lainnya, dan cenderung digunakan dalam pengembangan berbasis server tradisional. Ini memiliki Controller yang mengatur alur aplikasi. 
- MVT -> Model: Bagian yang bertugas untuk menyiapkan, mengatur, memanipulasi, dan mengorganisasikan data yang ada di database.
      -> View: Bagian yang bertugas untuk menampilkan informasi dalam bentuk Graphical User Interface (GUI).
      -> Template: Bagian yang bertugas untuk menghasilkan tampilan dinamis berdasarkan data yang dikirim oleh Model.
      <->Perbedaan : MVT sering digunakan dalam kerangka kerja web berbasis Python seperti Django. Perbedaannya dengan MVC terletak pada penggunaan Template sebagai komponen tambahan yang digunakan untuk menghasilkan tampilan dinamis.
- MVVM -> Model: Bagian yang bertugas untuk menyiapkan, mengatur, memanipulasi, dan mengorganisasikan data yang ada di database.
       -> View: Bagian yang bertugas untuk menampilkan informasi dalam bentuk Graphical User Interface (GUI).
       -> ViewModel: Bagian yang bertugas untuk mengonversi data dari Model menjadi bentuk yang lebih sesuai untuk ditampilkan oleh View. Ini memungkinkan tampilan untuk berinteraksi dengan data tanpa perlu tahu banyak tentang Model.
       <->Perbedaan : MVVM sering digunakan dalam pengembangan aplikasi berbasis pengguna seperti aplikasi mobile dan desktop.ViewModel digunakan sebagai komponen tambahan yang memungkinkan pemisahan lebih jelas antara tampilan dan logika bisnis.
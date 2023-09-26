Nama: Irvan
NPM: 2206083514
Kelas: PBP A

Link : [Adaptable Link](https://dwarves-weapon-inventory.adaptable.app/main/)

---------------------------------------------------------------------------------------------------------------------------------------------
(Tugas 2)

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

![My Img](/main/templates/How%20Django%20Framework%20Works.png)

Pertama user akan meminta request kepada Django, lalu Django akan menggunakan `urls.py`. Setelah itu, `views.py` akan mengatur berbagai macam bentuk interaksi agar di dalam `models.py` dapat mengelola dan menyajikan data agar data yang telah diolah oleh `models.py` dapat ditampilkan pada templates dalam berkas `html`. Pada berkas `html`, berisi berbagai macam kode html seperti kode untuk membuat tabel, list, menentukan ukuran font dan lain lain, serta pada berkas `html` juga mengandung tag template Django agar dapat memasukan data dari dalam `views.py` ke dalam berkas `html`. Setelah selesai diolah, output tersebut akan dikirimkan sebagai respon kepada user.

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

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

---------------------------------------------------------------------------------------------------------------------------------------------
(Tugas 3)

1. Apa perbedaan antara form POST dan form GET dalam Django?

Method POST akan mengirimkan data atau nilai langsung ke action untuk ditampung, tanpa menampilkan pada URL. Sedangkan method GET akan menampilkan data/nilai pada URL, kemudian akan ditampung oleh action.

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

JSON adalah format pertukaran data terbuka yang dapat dibaca baik oleh manusia maupun mesin. JSON bersifat independen dari setiap bahasa pemrograman dan merupakan output API umum dalam berbagai aplikasi. XML adalah bahasa markah yang menyediakan aturan untuk menentukan data apa pun. XML menggunakan tanda untuk membedakan antara atribut data dan data aktual. Meskipun kedua format tersebut digunakan dalam pertukaran data, JSON adalah opsi yang lebih baru, lebih fleksibel, dan lebih populer.

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

JSON (JavaScript Object Notation) sering digunakan dalam pertukaran data antara aplikasi web modern karena memiliki beberapa keunggulan yang membuatnya sangat cocok untuk tugas ini:

- Ringan dan Mudah Dibaca: JSON memiliki format yang sederhana dan mudah dibaca oleh manusia.
- Dukungan oleh Banyak Bahasa Pemrograman: JSON dapat dengan mudah diproses oleh hampir semua bahasa pemrograman modern. 
- Format Data yang Seragam: JSON menyediakan format yang seragam untuk data terstruktur.
- Ringan dalam Penggunaan Bandwidth: JSON memiliki overhead yang relatif kecil, yang membuatnya efisien dalam penggunaan bandwidth.
- Dukungan untuk Tipe Data yang Umum: JSON mendukung tipe data umum seperti string, angka, boolean, objek, dan array.
- Interoperabilitas: JSON digunakan secara luas dalam pertukaran data antara server dan klien di web.
- Keamanan: JSON memiliki mekanisme untuk menghindari serangan Cross-Site Scripting (XSS) jika diimplementasikan dengan benar. 
- Dukungan untuk Callback: JSON juga dapat digunakan dalam teknik seperti JSONP (JSON with Padding), yang memungkinkan permintaan lintas domain dengan cara yang aman.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Pertama mengatur routing dari `main/` ke `/`. Saya menyalakan virtual environment dengan `env\Scripts\activate.bat`.
- Dilanjutkan dengan memodifikasi path `'main'` menjadi `''` dalam `urls.py` pada folder `inventory_project`.
- Lanjut ke tahap selanjutnya yaitu Mengimplementasi Skeleton sebagai kerangka views. Dengan membuat folder baru bernama tamplate pada root folder dan membuat berkas didalamnya bernama `base.html` (Kode yang digunakan untuk mengisi berkas terdapat pada tutorial2).
- Memodifiksi berkas `settings.py` pada subdirektori `inventory_project` dan menmbahkan `'DIRS': [BASE_DIR / 'templates']` didalam baris `TEMPLATES`.
- Memodifikasi berkas `main.html` pada subdirektori templates yang ada pada direktori main, dan menambahkan `{% extends 'base.html' %}` untuk menggunakan base.html sebagai template utama.
- Selanjutnya membuat FORM Input Data. Pertama membuat berkas baru pada direktori main dengan nama `forms.py` (Kode yang digunakan untuk mengisi berkas terdapat pada tutorial2).
- Dalam berkas `views.py` pada folder main tambahkan from `django.http import HttpResponseRedirect`, `from main.forms import ProductForm`, `from django.urls import reverse` di line pertama.
- Dalam berkas `views.py` yang sama buat fungsi baru bernama `create_product` (Kode yang digunakan untuk mengisi berkas terdapat pada tutorial2).
- Modifikasi fungsi show main dalam berkas `views.py` dengan menambahkan `products = Product.objects.all()` pada line dibawah fungsi show_min. Dan menambahkan `'products': products` kedalam context.
- Import fungsi create product kedalam urls.py dengan `from main.views import show_main, create_product`.
- Tambahkan `path('create-product', create_product, name='create_product')`, ke dalam urlpatterns pada `urls.py` di main untuk mengakses fungsi yang sudah di-import pada poin sebelumnya.
- Buat berkas HTML baru dengan nama `create_product.html` pada direktori main/templates (Kode yang digunakan untuk mengisi berkas terdapat pada tutorial2).
- Dalam `main.html` tambahkan (Kode yang digunakan untuk mengisi berkas terdapat pada tutorial2) di dalam `{% block content %}` untuk menampilkan data produk dalam bentuk table serta tombol "Add New Product".
- Mengembalikan data dalam bentuk XML. Pertama tambahkan import HttpResponse & Serilier dalam berkas `views.py` pada folder main
- Dalam berkas `views.py` pada folder main buat fungsi penerima parmeter request yang dinamakan show_xml. Fungsi ini berguna untuk menyimpan hasil query dari seluruh data yang ada pada product dan mentranslasi objek model menjdi XML (Kode yang digunakan untuk mengisi berkas terdapat pada tutorial2).
- Dalam berkas urls.py pd folder main tambahkan import fungsi `from main.views import show_main, create_product, show_xml`.
- Terakhir tambahkan path url ke dalam urlpatterns `path('xml/', show_xml, name='show_xml')`.
- Mengemblikan data dalam bentuk JSON. Dalam berkas `views.py` pada folder main buat fungsi penerima parmeter request yang dinamakan show_json. Fungsi ini berguna untuk menyimpn hasil query dari seluruh data yang ada pada product dan mentarnslasi objek model menjdi JSON (Kode yang digunakan untuk mengisi berkas terdapat pada tutorial2).
- Dalam berkas urls.py pada folder main tambahkan import fungsi `from main.views import show_main, create_product, show_xml, show_json`.
- Terakhir tambahkan path url ke dalam urlpatterns `path('json/', show_json, name='show_json')`.
- Mengmbalikan data berdsarkan ID dalam bentuk XML dan JSON. Dalam berkas `views.py` pada folder main buat fungsi penerima parmeter request yang dinamakan show_xml_by_id & show_json_by_id . Fungsi ini berguna untuk menyimpan hasil query dari seluruh data yang ada pada product dan mentranslasi objek model menjdi XML dan JSON (Kode yang digunakan untuk mengisi berkas terdapat pada tutorial2).
- Dalam berkas urls.py pd folder main tambahkan import fungsi `from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id`.
- Terakhir tambahkan path url ke dalam urlpatterns `path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id')`, `path('json/<int:id>/', show_json_by_id, name='show_json_by_id')`. 

Screenshot Postman

html :
![My Img](/main/templates/html.png)

xml :
![My Img](/main/templates/xml.png)

json :
![My Img](/main/templates/json.png)

xml id :
![My Img](/main/templates/xml%20id.png)

json id :
![My Img](/main/templates/json%20id.png)

---------------------------------------------------------------------------------------------------------------------------------------------
(Tugas 4)

1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

Django merupakan kerangka kerja full stack yang berfungsi untuk membuat aplikasi web menggunakan bahasa python. Sama halnya dengan flask, developer bisa membangun website secara backend maupun frontend hanya menggunakan framework ini.

Kelebihan Django:
- Ditulis dengan Bahasa Python
- Aman Digunakan
- Fitur Menyederhanakan Proses Development
- Konsep Kerja KISS dan DRY
- Mengimplementasikan ORM
- Dokumentasi Lengkap dan Jelas
- Fleksibel
- Cross Platform
- Template Engine
- Framework Serbaguna

2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

(1)Autentikasi (Authentication):

Autentikasi adalah proses verifikasi identitas pengguna. Ini adalah langkah pertama dalam mengamankan aplikasi web Anda.
Tujuan autentikasi adalah untuk memastikan bahwa pengguna yang mencoba mengakses aplikasi Anda adalah mereka yang mengklaim diri mereka menjadi (misalnya, pengguna dengan nama pengguna dan kata sandi yang benar).
Django menyediakan berbagai metode autentikasi bawaan, termasuk autentikasi berbasis kata sandi, autentikasi berbasis token, dan lainnya.
Autentikasi biasanya terjadi pada tahap login, saat pengguna memasukkan kredensial mereka (seperti nama pengguna dan kata sandi).

(2)Otorisasi (Authorization):

Otorisasi adalah proses yang terjadi setelah autentikasi, yang menentukan apa yang diizinkan atau tidak diizinkan oleh pengguna yang sudah diautentikasi.
Tujuan otorisasi adalah untuk mengontrol akses pengguna ke berbagai bagian dari aplikasi dan sumber daya, seperti halaman web, data, atau tindakan tertentu.
Django menggunakan konsep "permissions" untuk mengatur otorisasi. Anda dapat mendefinisikan aturan yang menentukan siapa yang memiliki akses ke objek atau tindakan tertentu dalam aplikasi Anda.
Contohnya, Anda dapat mengizinkan pengguna tertentu untuk mengedit profil mereka sendiri, tetapi tidak mengizinkan mereka untuk mengedit profil pengguna lain.

-> Mengapa keduanya penting?

- Autentikasi penting karena memastikan bahwa hanya pengguna yang diautentikasi yang memiliki akses ke aplikasi Anda. Tanpa autentikasi yang kuat, aplikasi Anda dapat terbuka untuk akses tidak sah, potensial membahayakan data dan fungsionalitas.
- Otorisasi penting karena memastikan bahwa pengguna yang diautentikasi hanya memiliki akses ke sumber daya yang mereka seharusnya miliki. Ini membantu menjaga privasi data pengguna dan mengontrol tingkat akses dalam aplikasi, mencegah pengguna yang diautentikasi untuk melakukan tindakan yang tidak sah atau mengakses informasi yang tidak mereka miliki.

3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

Cookie HTTP adalah sepotong kecil data yang dikirim dari situs web dan disimpan di komputer pengguna oleh browser web pengguna saat pengguna berselancar. Teknologi ini dirancang untuk menjadi mekanisme andal bagi situs web untuk mengingat informasi stateful atau untuk merekam aktivitas penelusuran pengguna. Mereka juga dapat digunakan untuk mengingat potongan informasi dan data yang sebelumnya dimasukkan pengguna ke dalam bidang formulir seperti nama, alamat, kata sandi, dan nomor kartu kredit.

Django menggunakan cookies untuk mengelola data sesi pengguna dengan bantuan modul built-in yang disebut django.contrib.sessions. Cara kerjanya adalah sebagai berikut:

(1) Memulai Sesi Pengguna: Ketika pengguna pertama kali mengakses situs web Django, server akan membuat sebuah cookie sesi baru yang unik untuk pengguna tersebut. Cookie ini mengandung sebuah identifikasi unik (biasanya berupa token atau ID sesi) yang digunakan oleh server untuk mengenali pengguna di masa mendatang.
(2) Menyimpan Data Sesi: Saat Anda ingin menyimpan data sesi pengguna, seperti informasi login, preferensi, keranjang belanja, atau data lainnya, Django akan mengambil data tersebut dan menyimpannya di dalam sesi yang terkait dengan cookie tersebut. Data ini dienkripsi secara otomatis untuk menjaga keamanannya.
(3) Mengambil Data Sesi: Setiap kali pengguna mengunjungi situs web lagi, cookie sesi akan dikirimkan ke server. Django akan menggunakan informasi dalam cookie tersebut untuk mengidentifikasi sesi pengguna yang sesuai. Kemudian, server akan mengambil data sesi yang terkait dan membuatnya tersedia untuk digunakan dalam tampilan dan kontroler.
(4) Mengakhiri Sesi: Ketika pengguna keluar atau sesi berakhir (misalnya, setelah inaktivitas), Django akan membersihkan data sesi dan menghapus cookie sesi yang terkait.

4. Apakah penggunaan cookies aman secara default dalam 
pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Penggunaan cookies dalam pengembangan web adalah praktik yang umum dan berguna, tetapi ada beberapa risiko potensial yang harus diwaspadai dan dikelola dengan hati-hati. Berikut adalah beberapa risiko potensial yang terkait dengan penggunaan cookies:

- Keamanan Data: Cookies yang berisi data sensitif seperti token otentikasi atau informasi pribadi pengguna harus dienkripsi dengan baik. Jika data ini tidak aman, cookie tersebut dapat diretas oleh pihak yang tidak berwenang.
- Cookie Theft: Pencurian cookie adalah risiko potensial ketika cookie yang menyimpan informasi otentikasi pengguna dicuri oleh penyerang. Penyerang dapat menggunakan cookie tersebut untuk mengambil alih sesi pengguna. Ini adalah risiko khusus ketika tidak menggunakan HTTPS, karena cookie bisa disadap dalam transmisi data.
- Cookies Cross-Site Scripting (XSS): Serangan XSS dapat memungkinkan penyerang menyisipkan skrip berbahaya ke dalam halaman web yang kemudian dapat mengakses dan mencuri cookie pengguna.
- Cookies Persistent: Cookies yang bersifat persisten (berlangsung lama) dapat memiliki risiko lebih tinggi karena mereka tetap ada di sisi klien dalam jangka waktu yang lebih lama, meningkatkan kemungkinan pencurian atau penyalahgunaan.
- Privacy Concerns: Cookies juga memiliki masalah privasi potensial. Mereka dapat digunakan untuk melacak perilaku pengguna di seluruh berbagai situs web, yang dapat memicu kekhawatiran privasi.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Pertama membuat fungsi dan form registrasi. Dimulai dengan menjalankan virtual environment.
- Lanjut dengan menambahkan import `redirect`, `UserCreationForm`, dan `messages` pada views.py dalam direktori main.
- Dalam file yg sama buat fungsi bernama `register` untuk menghasilkan formulir registrasi yang menghasilkan akun pengguna ketika data di-submit dari form.
- Lalu buat berkas file HTML dengan nama `register.html` (Kode yang digunakan untuk mengisi berkas terdapat pada tutorial3) pada folder template dalam direktori main.
- Dan untuk menyelesaikan pembuatan form registrasi masukan impor `from main.views import register` dan url path `path('register/', register, name='register'),`.
- Kedua membuat fungsi login. Pada views.py dalam direktori main tambahkan import `authenticate` dan `login` pada bagian paling atas.
- Dalam file yg sama tambahkan kode (Kode yang digunakan untuk mengisi berkas terdapat pada tutorial3) kedalam fungsi `login`.
- Lalu buat berkas file HTML dengan nama `login.html` (Kode yang digunakan untuk mengisi berkas terdapat pada tutorial3) pada folder template dalam direktori main.
- Dan untuk menyelesaikan pembuatan fungsi login masukan impor `from main.views import login_user` dan url path `path('login/', login_user, name='login'),`.
- Ketiga membuat fungsi logout. Pada views.py dalam direktori main tambahkan import `logout` pada bagian paling atas.
- Dalam file yg sama buat fungsi bernama `logout` dan tambahkan kode (Kode yang digunakan untuk mengisi berkas terdapat pada tutorial3).
- Dalam berkas main.html tambahkan kode (Kode yang digunakan untuk mengisi berkas terdapat pada tutorial3) untuk membuat tombol logout.
- Dan untuk menyelesaikan pembuatan fungsi logout masukan impor `from main.views import logout_user` dan url path `path('logout/', logout_user, name='logout'),`.
- Keempat merestriksi akses ke halaman main. Pada views.py dalam direktori main tambahkan import `login_required` pada bagian paling atas.
- Dan akhiri dengan menambahkan `@login_required(login_url='/login')` di atas fungsi `show_main`.
- Kelima mengimplementasi data dalam cookies dan memunculkannya dalam halaman main. Pastikan logout terlebih dahulu apabila aplikasi Django sedang dijalankan.
- Pada views.py dalam direktori main tambahkan import `HttpResponseRedirect`, `reverse`, dan `datetime` pada bagian paling atas.
- Untuk melihat kapan terakhir kali pengguna melakukan login kita akan menambahkan fungsi `last_login` pada fungsi `login_user` dengan mengganti kode yang ada pada blok `if user is not None` menjadi (Kode yang digunakan untuk mengisi berkas terdapat pada tutorial3).
- Lanjut dengan menambahkan potongan kode `'last_login': request.COOKIES['last_login']` ke dalam variabel `context` pada fungsi `show_main`.
- Tambahkan potongan kode (Kode yang digunakan untuk mengisi berkas terdapat pada tutorial3) dalam fungsi `logout_user`.
- Dan akhiri dengan menambahkan `<h5>Sesi terakhir login: {{ last_login }}</h5>` pada berkas `main.html`. Sebelum lanjut ke tahap terakhir pastikan untuk membuat satu akun pada halaman web kamu terlebih dulu.
- Keenam menghubungkan model product dengan user. Dalam file `models.py` yang ada pada subdirektori main tambahkan kode `from django.contrib.auth.models import User`.
- Pada model Product tambahkan kode `user = models.ForeignKey(User, on_delete=models.CASCADE)` dibawah `class Product(models.Model):`
- Modifikasi fungsi `create_product` dalam berkas `views.py` pada subdirektori `main` dengan menambahkan kode (Kode yang digunakan untuk mengisi berkas terdapat pada tutorial3).
- Dan akhiri dengan mengubah fungsi `show_main` dengan menambahkan `products = Product.objects.filter(user=request.user)` dibawah fungsi `show_main` dan mengubah context name menjadi `request.user.username,`.
- Sebelum melakukan migrasi pastikan semua perubahan telah disimpan, jika sudah lakukan migrasi model dengan `python manage.py makemigrations`.
- Seharusnya, akan muncul error saat melakukan migrasi model. Pilih `1` untuk menetapkan default value untuk field user pada semua row yang telah dibuat pada basis data.
- Ketik angka 1 lagi untuk menetapkan user dengan ID 1 (yang sudah kita buat sebelumnya) pada model yang sudah ada.
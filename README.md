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

---------------------------------------------------------------------------------------------------------------------------------------------
(Tugas 5)

1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

Element selector adalah bagian dari bahasa pemrograman CSS (Cascading Style Sheets) yang digunakan untuk memilih elemen HTML tertentu dan menerapkan gaya atau styling ke elemen tersebut. Setiap jenis elemen selector memiliki manfaatnya sendiri dan digunakan pada situasi yang berbeda-beda. Berikut adalah beberapa jenis elemen selector beserta manfaat dan waktu yang tepat untuk menggunakannya:

- Universal Selector (*):
Manfaat: Universal selector berfungsi untuk memilih semua elemen di dalam dokumen HTML.
Waktu yang tepat: Penggunaan universal selector sebaiknya dibatasi karena dapat memengaruhi semua elemen di halaman web. Biasanya digunakan untuk mereset atau mengatur nilai default CSS.
- Element Selector (Tag Selector):
Manfaat: Selector elemen berfungsi untuk memilih semua elemen dengan tag yang sama, misalnya, `<p>`, `<h1>`, atau `<div>`.
Waktu yang tepat: Ini cocok digunakan ketika Anda ingin menerapkan gaya yang sama pada semua elemen dengan tag tertentu di seluruh halaman web.
- Class Selector (.classname):
Manfaat: Class selector berfungsi untuk memilih elemen berdasarkan nama kelas yang diberikan. Kelas dapat digunakan untuk mengelompokkan elemen dengan gaya yang sama.
Waktu yang tepat: Class selector digunakan ketika ingin menerapkan gaya yang sama pada beberapa elemen yang berbeda dengan kelas yang sama.
- ID Selector (#idname):
Manfaat: ID selector berfungsi untuk memilih elemen berdasarkan ID unik yang diberikan. ID harus unik di dalam halaman.
Waktu yang tepat: ID selector digunakan ketika ingin menerapkan gaya atau perilaku khusus pada satu elemen tertentu dalam halaman.
- Attribute Selector ([attribute=value]):
Manfaat: Attribute selector berfungsi untuk memilih elemen berdasarkan atribut dan nilainya, seperti `<a href="...">`. 
Waktu yang tepat: Ini berguna saat ingin memilih elemen berdasarkan atribut tertentu, seperti mengubah gaya tautan dengan atribut href.
- Pseudo-class Selector (:pseudo-class):
Manfaat: Pseudo-class selector berfungsi untuk memilih elemen berdasarkan keadaan atau interaksi pengguna, seperti :hover untuk mengganti tampilan saat kursor berada di atas elemen.
Waktu yang tepat: Digunakan untuk mengatur perilaku atau tampilan elemen berdasarkan tindakan pengguna, seperti tautan yang berubah warna saat dihover.
- Pseudo-element Selector (::pseudo-element):
Manfaat: Pseudo-element selector berfungsi untuk memilih dan menggaya bagian-bagian khusus dari elemen, seperti ::before untuk menambahkan konten sebelum elemen.
Waktu yang tepat: Digunakan untuk menambahkan konten atau gaya khusus ke bagian-bagian tertentu dari elemen, seperti menambahkan ikon sebelum teks.

2. Jelaskan HTML5 Tag yang kamu ketahui.

- `<header>`: Digunakan untuk mendefinisikan bagian atas atau kepala halaman web. Biasanya berisi elemen-elemen seperti judul, logo, dan navigasi utama.
- `<nav>`: Menunjukkan bagian navigasi dalam halaman web, seperti menu utama atau menu pilihan.
- `<article>`: Digunakan untuk mengelompokkan konten independen yang dapat berdiri sendiri, seperti artikel berita atau posting blog.
- `<section>`: Merepresentasikan bagian dalam halaman web yang memiliki tema atau konten yang terkait secara tematis.
- `<aside>`: Menunjukkan konten yang berkaitan dengan konten di sekitarnya, tetapi tidak penting untuk pemahaman utama halaman.
- `<main>`: Mendefinisikan konten utama dalam halaman web. Hanya boleh ada satu elemen `<main>` dalam satu halaman.
- `<figure>` dan `<figcaption>`: `<figure>` digunakan untuk mengelompokkan elemen media seperti gambar atau video dengan deskripsi atau keterangan yang diwakili oleh elemen `<figcaption>`.
- `<footer>`: Menunjukkan bagian bawah atau kaki halaman web. Biasanya berisi informasi kontak, tautan legal, atau hak cipta.
- `<time>`: Digunakan untuk menandai waktu atau tanggal dalam konten. Ini memungkinkan mesin pencari dan perangkat lainnya untuk lebih memahami konten yang berhubungan dengan waktu.
- `<mark>`: Digunakan untuk menyorot atau menandai teks yang relevan atau penting dalam konten.

3. Jelaskan perbedaan antara margin dan padding.

Margin dan padding adalah dua konsep penting dalam CSS (Cascading Style Sheets) yang digunakan untuk mengatur tata letak dan tampilan elemen dalam halaman web. Meskipun keduanya memengaruhi jarak antara elemen, mereka memiliki perbedaan yang signifikan:

1. Margin:
- Margin adalah ruang di luar batas luar elemen. Ini adalah jarak antara elemen tersebut dengan elemen-elemen lain di sekitarnya.
- Margin tidak memiliki latar belakang atau warna, dan konten tidak dapat ditempatkan dalam margin. Margin hanyalah area kosong yang memisahkan elemen dari elemen-elemen lainnya di sekitarnya.
- Margin digunakan untuk mengontrol jarak antara elemen-elemen satu sama lain di halaman web. Ini dapat digunakan untuk memberikan jarak vertikal atau horizontal antara elemen-elemen.
Padding:

2. Padding:
- Padding adalah ruang di dalam batas elemen. Ini adalah jarak antara batas elemen dan kontennya sendiri.
- Padding dapat memiliki latar belakang atau warna dan dapat berisi konten. Ini berarti Anda dapat mengisi padding dengan warna atau gambar latar belakang, dan konten (teks, gambar, dll.) dalam elemen akan muncul di dalam padding.
- Padding digunakan untuk mengontrol ruang di sekitar konten dalam elemen. Ini sering digunakan untuk mengatur tampilan elemen, seperti memberikan ruang di antara teks dan batas elemen atau mengisi bidang input dalam formulir.

Dalam ringkasannya, margin adalah ruang di luar elemen yang tidak memiliki latar belakang atau konten, sementara padding adalah ruang di dalam elemen yang dapat memiliki latar belakang dan mengandung konten.

4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

Bootstrap dan Tailwind CSS adalah dua framework CSS yang populer digunakan untuk membangun antarmuka pengguna (UI) dalam pengembangan web. Mereka memiliki pendekatan dan karakteristik yang berbeda, sehingga ada situasi di mana salah satu framework lebih cocok daripada yang lain. Berikut perbandingan antara Bootstrap dan Tailwind CSS serta kapan sebaiknya Anda menggunakan salah satu dari keduanya:

Bootstrap:
- Pendekatan: Bootstrap adalah framework CSS yang mendefinisikan komponen UI yang siap pakai (seperti tombol, navigasi, kartu, dll.) dengan gaya bawaan. Bootstrap menggunakan kelas yang sudah ada untuk mengatur tampilan elemen.
- Desain: Bootstrap memiliki desain bawaan yang terlihat profesional dan cukup umum. Desainnya terstruktur dan mudah diimplementasikan tanpa perlu banyak penyesuaian.
- Kesempatan Belajar: Lebih cepat untuk memulai karena Anda tidak perlu menulis banyak kode CSS kustom. Sangat cocok untuk pemula.
- Kemampuan Kustomisasi: Bootstrap dapat disesuaikan dengan menggunakan variabel Sass atau Less, tetapi ada batasan dalam hal sejauh mana Anda dapat mengubah tampilan tanpa menimpa banyak aturan bawaan.

Tailwind CSS:
- Pendekatan: Tailwind CSS adalah framework CSS yang memberikan utilitas CSS ke setiap elemen HTML. Anda membangun UI dengan menggabungkan kelas-kelas utilitas dalam HTML.
- Desain: Tailwind memberikan fleksibilitas yang besar dalam merancang tampilan sesuai kebutuhan Anda. Anda dapat membuat desain yang unik dan khusus.
- Kesempatan Belajar: Memerlukan waktu lebih lama untuk memahami dan memanfaatkan Tailwind sepenuhnya karena Anda perlu memahami berbagai kelas utilitas yang tersedia.
- Kemampuan Kustomisasi: Tailwind sangat kustomisabel, dan Anda dapat membuat tampilan yang sangat khusus. Anda bahkan dapat menyesuaikan setiap aspek dari desain dengan mudah.

Gunakan Bootstrap jika:
- Anda membutuhkan prototipe cepat atau membangun situs web dengan desain standar yang terlihat profesional.
- Anda adalah pemula dalam pengembangan web dan ingin memulai dengan cepat tanpa harus menggali terlalu dalam ke dalam CSS kustom.
- Anda membangun proyek yang lebih kecil dengan anggaran waktu yang terbatas.

Gunakan Tailwind CSS jika:
- Anda ingin kontrol yang lebih besar atas desain dan tampilan UI Anda, dan Anda ingin menciptakan desain yang unik.
- Anda siap untuk belajar dan berinvestasi waktu dalam memahami cara menggunakan dan menyesuaikan Tailwind CSS.
- Anda membangun proyek yang lebih besar dan kompleks yang memerlukan fleksibilitas tinggi dalam desain.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Pertama tambahkan bootstrap ke aplikasi.
- Untuk menambahkannya masuk kedalam file `base.html` didalam folder project django dan tambahkan tag `<meta name="viewport">`.
- Lalu tambahkan Bootstrap CSS dan juga JS (Kode yang digunakan untuk mengisi berkas terdapat pada tutorial4).
- Untuk mengkostumisasi halaman inventory saya menggunakan fitur edit & hapus produk.
- Dalam berkas `views.py` pada folder main saya buat fungsi baru dengan nama `edit_product` & `delete_product`.
- Agar bisa mengedi produk semau kita, saya menambahkan berkas HTML baru dengan nama `edit_product.html` (Kode yang digunakan untuk mengisi berkas terdapat pada tutorial4).
- Dan mengimpornya kedalam berkas yang sama menggunakan `from main.views import edit_product` & `from main.views import delete_product`.
- Lalu menambahkan path url ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor.
- Terakhir tambahkan tombol agar bisa mengakses dengan satu klik.
- Untuk mengkostumisasi halaman login & register saya mengubah warna halaman menjadi sama dengan halaman utama.
- Caranya dengan menggunakan fungsi `Background-color` yang dimasukkan kedalam element `<style></Style>`.
- Dan terakhir saya menggunakan element `<center></center>` untuk memfokuskan pandangan pengguna pada forum input.

---------------------------------------------------------------------------------------------------------------------------------------------
(Tugas 6)

1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Asynchronous programming dan synchronous programming adalah dua paradigma pemrograman yang berbeda dalam cara mereka mengelola eksekusi kode dan menangani tugas-tugas yang memerlukan waktu, seperti I/O (input/output) atau jaringan. Berikut adalah perbedaan utama antara keduanya:

- Synchronous Programming (Program Sinkron):

Eksekusi berurutan: Dalam pemrograman sinkron, kode dieksekusi secara berurutan dari atas ke bawah. Setiap operasi harus menunggu operasi sebelumnya selesai sebelum dapat dijalankan.
Blocking: Jika ada operasi yang memerlukan waktu seperti membaca data dari disk atau mengambil data melalui jaringan, program akan terblokir (blocking) sementara menunggu operasi tersebut selesai. Selama periode ini, aplikasi tidak dapat melakukan tugas lain.
Lebih mudah dipahami: Pemrograman sinkron biasanya lebih mudah dipahami karena alur eksekusi kode lebih terstruktur.

- Asynchronous Programming (Program Asinkron):

Eksekusi non-berurutan: Dalam pemrograman asinkron, kode dapat menjalankan operasi tanpa harus menunggu operasi sebelumnya selesai. Ini memungkinkan program untuk menjalankan tugas-tugas lain selama operasi yang memerlukan waktu masih berjalan.
Non-blocking: Dalam pemrograman asinkron, operasi-operasi yang memerlukan waktu biasanya non-blocking, yang berarti program dapat melanjutkan bekerja dengan operasi lain tanpa harus menunggu yang sedang berjalan.
Kompleksitas tambahan: Pemrograman asinkron biasanya lebih kompleks dibandingkan pemrograman sinkron karena memerlukan pemahaman tentang callback, promise, async/await, atau konsep serupa.

2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Paradigma event-driven programming adalah paradigma pemrograman di mana eksekusi kode program terutama ditentukan oleh kejadian (events) yang terjadi dalam sistem atau aplikasi. Dalam konteks JavaScript dan AJAX (Asynchronous JavaScript and XML), paradigma ini sangat relevan karena JavaScript sering digunakan untuk menangani interaksi pengguna dan permintaan asinkron ke server. Berikut beberapa poin penting tentang paradigma event-driven programming:

- Kejadian (events): Kejadian adalah tindakan atau peristiwa yang terjadi dalam aplikasi atau lingkungan eksternal. Contoh kejadian dalam aplikasi web termasuk klik tombol, pengisian formulir, atau penerimaan respons dari server.

- Penanganan kejadian (event handling): Dalam paradigma ini, Anda menentukan bagaimana program akan merespons setiap jenis kejadian. Anda menentukan fungsi atau kode yang akan dieksekusi ketika suatu kejadian terjadi.

Contoh penerapan paradigma event-driven programming dalam JavaScript dan AJAX pada tugas ini adalah mengambil dan menampilkan data dari server saat pengguna berinteraksi dengan elemen pada halaman web. Misalnya, jika Anda memiliki tombol "Muat Data" dalam halaman web, Anda dapat mengaitkan fungsi JavaScript dengan peristiwa klik tombol ini. Ketika pengguna mengklik tombol tersebut, fungsi tersebut akan dijalankan, dan permintaan AJAX akan dikirim ke server untuk mengambil data. Setelah data diterima, Anda dapat menampilkan data tersebut pada halaman web tanpa perlu mereload seluruh halaman.

Berikut contoh sederhana menggunakan JavaScript dan AJAX untuk menggambarkan penerapan paradigma event-driven programming:

// Mengaitkan fungsi dengan kejadian klik tombol
document.getElementById('load-data-button').addEventListener('click', function() {
  // Membuat permintaan AJAX
  var xhr = new XMLHttpRequest();
  xhr.open('GET', 'data.json', true);

  // Mengatur penanganan respons dari server
  xhr.onload = function() {
    if (xhr.status === 200) {
      // Menampilkan data pada halaman web
      var data = JSON.parse(xhr.responseText);
      document.getElementById('data-container').innerHTML = data.message;
    } else {
      console.error('Gagal mengambil data: ' + xhr.statusText);
    }
  };

  // Mengirim permintaan ke server
  xhr.send();
});

Dalam contoh ini, event-driven programming digunakan untuk menentukan bahwa ketika tombol dengan ID 'load-data-button' diklik, maka permintaan AJAX akan dikirim ke server, dan respons dari server akan ditampilkan pada elemen dengan ID 'data-container'. Ini adalah contoh yang sederhana, namun mengilustrasikan cara paradigma ini digunakan dalam interaksi pengguna dengan aplikasi web yang berbasis JavaScript dan AJAX.

3. Jelaskan penerapan asynchronous programming pada AJAX.

Penerapan asynchronous programming pada AJAX adalah salah satu dari prinsip dasar dalam penggunaan teknologi AJAX (Asynchronous JavaScript and XML). Pemrograman asinkron dalam konteks AJAX memungkinkan Anda untuk mengirim permintaan ke server dan menerima respons tanpa menghentikan atau memblokir eksekusi kode JavaScript lainnya. Ini adalah prinsip yang sangat penting karena tugas-tugas seperti mengambil data dari server atau mengirim data ke server biasanya memerlukan waktu yang signifikan, dan aplikasi web harus tetap responsif selama proses ini berlangsung.

Berikut adalah langkah-langkah penerapan asynchronous programming pada AJAX:

Membuat objek XMLHttpRequest atau menggunakan Fetch API: Anda dapat menggunakan objek XMLHttpRequest atau Fetch API untuk membuat permintaan HTTP ke server. Kedua teknologi ini mendukung pemrograman asinkron dan memungkinkan Anda untuk mengirim permintaan tanpa harus menunggu respons.

Contoh dengan XMLHttpRequest:

var xhr = new XMLHttpRequest();

Contoh dengan Fetch API:

fetch('https://example.com/api/data')
  .then(response => response.json())
  .then(data => {
    // Lakukan sesuatu dengan data yang diterima
  })
  .catch(error => {
    // Tangani kesalahan jika terjadi
  });

Mengatur callback atau promise: Setelah Anda membuat objek permintaan, Anda perlu mengatur apa yang harus dilakukan ketika respons dari server sudah tersedia. Dalam JavaScript modern, ini sering dilakukan menggunakan callback atau promise.

Contoh dengan XMLHttpRequest (callback):

xhr.onreadystatechange = function() {
  if (xhr.readyState === 4 && xhr.status === 200) {
    var response = JSON.parse(xhr.responseText);
    // Lakukan sesuatu dengan respons yang diterima
  }
};

Contoh dengan Fetch API (promise):

fetch('https://example.com/api/data')
  .then(response => response.json())
  .then(data => {
    // Lakukan sesuatu dengan data yang diterima
  })
  .catch(error => {
    // Tangani kesalahan jika terjadi
  });
Mengirim permintaan ke server: Setelah objek permintaan diatur, Anda dapat mengirim permintaan ke server.

Contoh dengan XMLHttpRequest:

xhr.open('GET', 'https://example.com/api/data', true);
xhr.send();

Contoh dengan Fetch API:

fetch('https://example.com/api/data')
  .then(response => response.json())
  .then(data => {
    // Lakukan sesuatu dengan data yang diterima
  })
  .catch(error => {
    // Tangani kesalahan jika terjadi
  });

4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.

Pemilihan antara menggunakan Fetch API atau library jQuery untuk menerapkan AJAX tergantung pada kebutuhan proyek Anda dan preferensi Anda. Berikut adalah perbandingan antara kedua teknologi ini:

Fetch API:

Built-in di Browsers Modern: Fetch API adalah bagian dari spesifikasi JavaScript modern dan sudah tersedia di hampir semua browser terbaru tanpa perlu mengunduh atau menginstal apa pun tambahan.
Promise-based: Fetch API menggunakan promise untuk mengelola permintaan asinkron, yang membuatnya lebih mudah untuk menangani tugas-tugas asinkron dan menghindari callback hell.
Ringan: Fetch API memiliki footprints yang lebih kecil dibandingkan dengan library jQuery karena fokus utamanya adalah mengelola permintaan HTTP saja.
jQuery:

Cross-browser Compatibility: Salah satu keunggulan utama jQuery adalah kompatibilitas lintas browser yang kuat. Ini dapat mengatasi perbedaan perilaku browser dengan konsistensi yang lebih baik.
API yang Lebih Tinggi: jQuery menyediakan antarmuka yang lebih tinggi dan abstraksi yang membuatnya lebih mudah digunakan, terutama untuk pemula. Anda dapat menulis kode dengan jumlah kode yang lebih sedikit untuk melakukan tugas-tugas umum.
Plugins: jQuery memiliki ekosistem plugin yang luas yang dapat membantu Anda menambahkan fitur-fitur kompleks dengan cepat tanpa harus menulis kode dari awal.
Pendapat Pribadi:
Pemilihan antara Fetch API dan jQuery sangat bergantung pada konteks proyek. Jika Anda mengembangkan aplikasi web modern yang ditargetkan untuk browser terbaru atau memiliki kontrol atas versi browser yang digunakan pengguna Anda, maka Fetch API adalah pilihan yang baik. Ini adalah cara yang lebih modern, lebih ringan, dan menggunakan promise, yang dapat membuat kode Anda lebih terstruktur.

Namun, jika Anda perlu mendukung browser yang lebih tua atau ingin menghemat waktu dalam pengembangan aplikasi sederhana dengan tugas-tugas umum seperti manipulasi DOM atau animasi, jQuery dapat menjadi pilihan yang masuk akal. Tetapi perlu diingat bahwa jQuery menjadi kurang populer dalam beberapa tahun terakhir karena perkembangan JavaScript modern, jadi pertimbangkan apakah investasi dalam pembelajaran Fetch API dan JavaScript modern adalah langkah yang lebih baik dalam jangka panjang.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Pertama buat Fungsi dengan nama `get_product_json` yang menerima parameter request untuk Mengembalikan Data JSON.
- Lanjut dengan membuat Fungsi untuk Menambahkan Produk dengan AJAX. Caranya dengan membuat fungsi baru pada `views.py` dengan nama `add_product_ajax` yang menerima parameter `request`.
- Lalu Impor `from django.views.decorators.csrf import csrf_exempt` pada berkas `views.py`.
- Dan tambahkan dekorator `@csrf_exempt` di atas fungsi `add_product_ajax` (Kode yang digunakan untuk mengisi fungsi terdapat pada tutorial5).
- Masuk ke tahap selanjutnya menambahkan Routing Untuk Fungsi `get_product_json` dan `add_product_ajax` pada berkas `urls.py` (Kode yang digunakan untuk mengisi berkas terdapat pada tutorial5).
- Untuk menampilkan data product dengan Fetch() API hapus bagian kode table dengan kode `<table id="product_table"></table>`.
- Lalu buat block `<Script>` di bagian bawah berkas `main.html` dan buat fungsi baru pada block `<Script>` dengan nama `getProducts()`.
- Dan pada block `<Script>` tambah fungsi baru dengan nama `refreshProducts()` untuk me-refresh data produk secara asynchronous.
- Lajut ke tahap selanjutnya membuat modal dan buttonnya untuk menambahkan produk (Kode yang digunakan untuk mengisi berkas terdapat pada tutorial5).
- Terakhir menambahkan data product dengan AJAX. pada block `<Script>` tambahkan fungsi baru dengan nama `addProduct()` dan menambahkan fungsi `onclick` pada button "Add Product" (Kode yang digunakan untuk mengisi fungsi terdapat pada tutorial5).
- Lanjut dengan melakukan perintah collectstatic. Pertama mengonfigurasi File settings.py dengan `STATIC_URL = '/static/'` & `STATIC_ROOT = os.path.join(BASE_DIR, 'static')`
- Kemudian import Modul `os` dan menjalankan perintah `python manage.py collectstatic` untuk mengumpulkan File Static

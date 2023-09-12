Link : https://dwarves-weapon-inventory.adaptable.app/main/

Question
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

Answer
1. 
2. 
3. Mungkin saja membuat aplikasi web Django tanpa virtual environment. Namun, membuat web Django dengan cara ini sangat tidak dianjurkan karena akan lebih sulit untuk membuat proyek yang bagus dan kemungkinan mengalami masalah konflik dependensi di masa depan. Karena tidak menggunakan virtual environment, dependensi proyek yang digunakan akan diinstal secara global, ini akan menyebabkan penglolaan proyek menjadi lebih rumit, tidak bersih, dan kurang fleksibel
4. MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah pola desain arsitektur yang digunakan dalam pengembangan perangkat lunak.
    - MVC -> Model: Bagian yang bertugas untuk menyiapkan, mengatur, memanipulasi, dan mengorganisasikan data yang ada di database.
          -> View: Bagian yang bertugas untuk menampilkan informasi dalam bentuk Graphical User Interface (GUI).
          -> Controller: Bagian yang bertugas untuk menghubungkan serta mengatur model dan view agar dapat saling terhubung.
    <->Perbedaan : MVC adalah pola yang lebih tua dan cenderung digunakan dalam pengembangan berbasis server tradisional. Ini memiliki Controller yang mengatur alur aplikasi.
    
    - MVT -> Model: Bagian yang bertugas untuk menyiapkan, mengatur, memanipulasi, dan mengorganisasikan data yang ada di database.
          -> View: Bagian yang bertugas untuk menampilkan informasi dalam bentuk Graphical User Interface (GUI).
          -> Template: Bagian yang bertugas untuk menghasilkan tampilan dinamis berdasarkan data yang dikirim oleh Model.
    <->Perbedaan : MVT adalah pola yang sering digunakan dalam kerangka kerja web berbasis Python seperti Django. Perbedaannya dengan MVC terletak pada penggunaan Template sebagai komponen tambahan yang digunakan untuk menghasilkan tampilan dinamis.

    - MVVM -> Model: Bagian yang bertugas untuk menyiapkan, mengatur, memanipulasi, dan mengorganisasikan data yang ada di database.
           -> View: Bagian yang bertugas untuk menampilkan informasi dalam bentuk Graphical User Interface (GUI).
           -> ViewModel: Bagian yang bertugas untuk mengonversi data dari Model menjadi bentuk yang lebih sesuai untuk ditampilkan oleh View. Ini memungkinkan tampilan untuk berinteraksi dengan data tanpa perlu tahu banyak tentang Model.
    <->Perbedaan : MVVM adalah pola yang sering digunakan dalam pengembangan aplikasi berbasis pengguna (user interface) seperti aplikasi mobile dan desktop. Ini memiliki ViewModel sebagai komponen tambahan yang memungkinkan pemisahan yang lebih jelas antara tampilan dan logika bisnis.
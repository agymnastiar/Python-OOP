# Python OOP
Prinsip OOP yang akan digunakan:
- Basic OOP
- Inheritance
- Polymorphism

data : bit.ly/MarketingDataETL
## Task 1
Class MarketingDataETL dibuat untuk melakukan proses ETL (Extract, Transform, Load) pada data marketing. Tugas dari class ini adalah untuk mengambil data dari file CSV tersebut, melakukan pembersihan dan transformasi sederhana pada data yang diambil, dan menyimpan data yang telah ditransformasi ke dalam struktur data DataFrame.
1. Metode Extract(): langkah pertama dalam proses ETL. Pada tahap ini, class MarketingDataETL akan membaca data dari file CSV yang disebut "marketing_data.csv". 
2. Metode Transform(): Setelah data berhasil diekstraksi, langkah berikutnya adalah membersihkan dan mentransformasi data. Dalam tahap transformasi, metode transform() akan melakukan serangkaian operasi untuk memperbaiki atau mengubah struktur data agar sesuai dengan kebutuhan analisis selanjutnya.
3. Metode Store(): Langkah terakhir dalam proses ETL adalah menyimpan data yang telah ditransformasi ke dalam struktur data yang sesuai. Dalam konteks ini, metode store() akan menyimpan data yang telah dimodifikasi ke dalam struktur data yang disebut DataFrame. 

## Task 2
Class TargetedMarketingETL merupakan turunan dari MarketingDataETL. Pada bagian ini, ditambahkan metode yang disebut segment_customers(), metode segment_customers() digunakan untuk mengelompokkan pelanggan berdasarkan kriteria tertentu. Selain itu, bagian ini juga mendemonstrasikan konsep polymorphism dengan meng-override metode transform() dalam TargetedMarketingETL. Hal ini memungkinkan penambahan logika segmentasi pelanggan ke dalam proses transformasi data yang dilakukan oleh class TargetedMarketingETL, tanpa mengubah metode transform() di class parent-nya. Dengan demikian, penggunaan inheritance dan polymorphism memungkinkan untuk memperluas dan memodifikasi fungsionalitas class yang sudah ada sesuai dengan kebutuhan spesifik.


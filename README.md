# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan tinggi yang telah berdiri sejak tahun 2000. Hingga saat ini mereka telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus. Jaya Jaya Institut memerlukan sebuah dashboard sebagai alat monitoring agar mudah dalam memahami data dan mengawasi performa belajar para siswanya.

### Permasalahan Bisnis

Berdasarkan kebutuhan bisnis yang sedang dihadapi, maka fokus utama pada proyek ini adalah membuat dashboard sebagai platform monitoring metrik-metrik penting untuk kebutuhan analisis screening siswa yang memerlukan bimbingan khusus sehingga dapat menurunkan peluang mereka terjerumus ke jalan dropout. Institusi juga perlu menyusun strategi yang tepat untuk dapat menjaga kualitas belajar para siswa. 

Berikut pertanyaan bisnis yang diharapkan dapat terjawab melalui proyek ini.
* Apa saja faktor-faktor yang berpengaruh signifikan terhadap tingginya probabilitas mahasiswa dapat mengalami dropout?
* Bagaimana pengaruh Capaian Akademik Mahasiswa terhadap kecenderungan Dropout?
* Bagaimana pengaruh faktor Non-Akademik mahasiswa terhadap kecenderungan Dropout? 
* Bagaimana strategi yang harus dijalankan oleh kampus untuk menekan angka dropout mahasiswa?

### Cakupan Proyek

1) Pengumpulan dan Persiapan Data
2) Pengolahan dan Analisis Data
3) Visualisasi dan Interpretasi Data
4) Pembuatan Dashboard
5) Model Development
6) Model Deployment
7) Rekomendasi

### Persiapan

Sumber data: [Jaya Jaya Institut Dataset](https://raw.githubusercontent.com/Sulbae/Student-s-Performances-Dashboard/refs/heads/main/students_data.csv)

Setup environment:

1. Buat lingkungan virtual
    ```
    conda create --name penerapan-data-science python=3.10 -y
    ```
2. Aktifkan lingkungan virtual
    ```
    conda activate penerapan-data-science
    ```
3. Install dependensi
    ```
    conda install -r requirements.txt
    ```

Pengolahan dan Persiapan Data
``` 
Data Exploration
|---Karakteristik Data
|---Kelengkapan Data
|---Distribusi Data
|---Hubungan antar Data
Data Cleaning
|---Missing Value Handling
Data Preprocessing
|---Data Filtering
|---Feature Engineering
|---Data Encoding
```
Eksplorasi dan Analisis Data
```
Analisis Korelasi Antar Variabel Data 
|---Observasi pengaruh Aspek Capaian Akademik terhadap kejadian Dropout
|---Observasi pengaruh Aspek non-Akademik terhadap kejadian Dropout
```

## Business Dashboard

[Lihat Dashboard]()

Dashboard berisi informasi mengenai ringkasan metrik-metrik penting dan visualisasi data yang diperlukan dalam kegiatan monitoring terhadap berbagai aspek yang berkaitan dengan kondisi pengelolaan sumber daya manusia (talent) perusahaan seperti berikut:
1) Total Karyawan
    - Deskripsi: Jumlah seluruh karyawan yang terdata.
    - Kegunaan: Memberikan informasi mengenai besaran jumlah karyawan yang sedang/telah dikelola perusahaan.
2) Total Attrition
    - Deskripsi: Jumlah karyawan yang telah berhenti/diberhentikan dan tercatat pada database.
    - Kegunaan: Menjadi indikator tinggi-rendahnya tingkat pergantian karyawan (Attrition Rate).
3) Rata-rata Usia (Avg. Age)
    - Deskripsi: Usia rata-rata karyawan secara keseluruhan.
    - Kegunaan: Usia rata-rata dapat menjadi indikator dalam analisis demografi personel tim khususnya dalam monitoring komposisi tim hingga perencanaan promosi dan/atau suksesi.
4) Enviro Satisfaction Rate
    - Deskripsi: Tingkat kepuasan rata-rata karyawan terhadap kondisi lingkungan/budaya kerja perusahaan (Environment Satisfaction).
    - Kegunaan: Menjadi indikator awal dalam mengetahui tingkat kenyamanan perusahaan secara umum bagi seluruh karyawan.
5) Job Satisfaction Rate
    - Deskripsi: Tingkat kepuasan rata-rata karyawan terhadap pekerjaan yang diemban oleh mereka. 
    - Kegunaan: Menjadi indikator awal dalam mengetahui tingkat kesesuaian ekspektasi kerja karyawan dengan beban kerja nyata di kantor/lapangan. Informasi ini akan berguna sebagai early-warning dalam mendeteksi gejala burnout karyawan maupun pengelolaan organisasi yang tidak efisien.
6) Perfomance Rate
    - Deskripsi: Tingkat performa/kinerja rata-rata karyawan secara keseluruhan.
    - Kegunaan: Mengukur kinerja rata-rata karyawan dan sebagai tolak ukur awal yang menggambarkan tingkat produktivitas dari tenaga kerja perusahaan.
7) Rata-rata Pelatihan Yang Diikuti (Avg. Training (Last Year))
    - Deskripsi: Jumlah pelatihan rata-rata yang telah diikuti karyawan selama satu tahun terakhir.
    - Kegunaan: Menjadi indikator pembanding bagi metrik Performance Rate dalam mengukur tingkat produktivitas perusahaan. Jumlah pelatihan dapat menjadi nilai representatif dari besaran investasi yang telah perusahaan lakukan untuk memelihara kualitas talentanya, yakni melalui pemberian fasilitas kegiatan pelatihan bagi para karyawan.
8) Monthly Rate Chart
    - Deskripsi: Menampilkan jumlah Attrition berdasarkan Monthly Rate yang telah dikelompokkan ke dalam level tertentu.
    - Kegunaan: Memberikan informasi mengenai distribusi Attrition karyawan yang tersebar dalam berbagai level gaji bulanan. Data ini digunakan untuk memahami pengaruh besaran gaji yang diterima terhadap tingkat Attrition karyawan.  
9) Percent Salary Hike Chart
    - Deskripsi: Menampilkan jumlah Attrition berdasarkan besaran Percent Salary Hike dalam satu tahun terakhir.
    - Kegunaan: Memberikan informasi besaran persentase kenaikan gaji bulanan dibandingkan dengan gaji sebelumnya. Data ini digunakan untuk memahami pengaruh besaran persentase kenaikan gaji terhadap tingkat Attrition karyawan.
10) Monthly Income Chart
    - Deskripsi: Menampilkan jumlah Attrition berdasarkan Monthly Income yang telah dikelompokkan ke dalam level tertentu.
    - Kegunaan: Memberikan informasi mengenai distribusi Attrition karyawan yang tersebar dalam berbagai level pendapatan total (gaji + pendapatan lain-lain) bulanan. Data ini digunakan untuk memahami pengaruh besaran pendapatan total bulanan yang mampu diperoleh terhadap tingkat Attrition karyawan.

## Conclusion

Berdasarkan hasil analisis dalam proyek ini, maka dapat disimpulkan bahwa:
1. Faktor-faktor yang berpengaruh signifikan terhadap kejadian Dropout
    * Berdasarkan hubungan pengaruh antar variabel yang telah dikalkulasi menggunakan metode perhitungan korelasi matrix, maka dapat diketahui bahwa kejadian Dropout yang dialami mahasiswa selama ini banyak disebabkan akibat lebih dari satu aspek antara lain:
        - Aspek Capaian Akademik
        - Aspek Finansial
        - Aspek Sosial & Psikologis

2. Aspek Capaian Akademik sebagai faktor utama 
    * Mahasiswa dengan capaian akademik yang buruk memiliki tingkat risiko Dropout yang lebih tinggi bila dibandingkan dengan mahasiswa yang memiliki capaian akademik bagus. Capaian yang buruk tersebut dapat dipengaruhi oleh beberapa hal seperti kurangnya motivasi belajar maupun kondisi personal mahasiswa yang kurang memadai. Meskipun begitu, dalam beberapa kasus diketahui bahwa ada juga mahasiswa yang capaian akademiknya sudah bagus, tetapi masih mengalami Dropout. Hal ini menandakan ada faktor lain juga yang memengaruhi kecenderungan Dropout.
3. Aspek non-Akademik sebagai faktor tambahan
    * Selain aspek capaian akademik, kejadian Dropout juga dapat disebabkan oleh aspek non-Akademik seperti:
        - Keterbatasan Finansial Mahasiswa: Terdapat sampel yang menunjukkan bahwa mayoritas mahasiswa yang mengalami Dropout berasal dari kelompok mahasiswa yang memiliki masalah finansial yang ditandai dengan pengambilan pinjaman/utang maupun pembayaran yang tidak tepat waktu. Kelompok seperti ini juga memiliki tingkat risiko Dropout yang cukup tinggi. Hal ini diperkuat dengan data yang menunjukkan bahwa tingkat risiko Dropout pada para penerima beasiswa sangatlah kecil. 
        - Kondisi Makro Ekonomi: Meskipun pengaruhnya terhadap Dropout tidak sekuat masalah finansial secara personal (tidak berpengaruh secara langsung terhadap kejadian Dropout), kondisi makro ekonomi seperti besaran GDP, tingkat inflasi, dan tingkat pengangguran mampu mendorong psikologi mahasiswa dalam memperjuangkan studinya. Ketika indikator-indikator ekonomi tersebut terlihat sedang tidak baik, sebagian mahasiswa justru termotivasi untuk bisa secepatnya menyelesaikan studi sehingga mereka dapat segera fokus mencari pekerjaan dan memiliki penghasilan yang stabil sehingga bisa memenuhi kebutuhan finansial mereka yang semakin tertekan akibat kondisi ekonomi makro yang buruk.


### Rekomendasi Action Items

Berdasarkan temuan-temuan tersebut, berikut adalah rekomendasi strategis yang potensial untuk diterapkan:

1. Penerapan Early Support System
    - Kampus harus lebih jeli dalam mengamati dan menganalisis hasil studi atau capaian akademik mahasiswa mulai dari periode awal (saat masuk maupun semester awal). Ketika menemukan mahasiswa dengan nilai yang minimum, maka dapat segera ambil tindakan untuk melakukan bimbingan khusus kepada mereka sebagai langkah mitigasi dalam menekan angka Dropout mahasiswa.
        
2. Program Bantuan Finansial
    - Apabila mahasiswa terindikasi sebagai Debtor dan/atau tercatat pernah telat melakukan pembayaran, segera lakukan intervensi dini seperti menyediakan layanan konseling untuk membantu mengelola risiko Dropout akibat masalah finansial yang dihadapi.
    - Pemberian keringanan khusus seperti skema pembayaran cicilan dengan syarat juga diharapkan mampu memberikan sedikit kelonggaran terhadap mahasiswa dalam memenuhi biaya pendidikan mereka disaat kondisi finansial mereka sedang tidak baik.
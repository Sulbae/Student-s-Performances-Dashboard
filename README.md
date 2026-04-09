# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan tinggi yang telah berdiri sejak tahun 2000. Hingga saat ini mereka telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus. Jaya Jaya Institut memerlukan sebuah dashboard sebagai alat monitoring agar mudah dalam memahami data dan mengawasi performa belajar para siswanya.

### Permasalahan Bisnis

Angka dropout yang tidak terkontrol tentunya dapat menyebabkan permasalahan yang cukup serius bagi institusi pendidikan tinggi seperti Jaya-Jaya Institut ini. Reputasi yang sudah baik akan tergerus apabila akreditasi kampus turun kasta akibat jumlah dropout mahasiswa yang terus meningkat. Oleh karena itu, diperlukan langkah antisipasi sejak dini untuk dapat memperkecil risiko dropout.

Berdasarkan kebutuhan bisnis yang sedang dihadapi, maka proyek ini dilaksanakan untuk mengembangkan sebuah tool (alat bantu) yang mampu membantu proses screening awal para mahasiswa siswa yang memiliki risiko dropout berdasarkan kriteria yang telah ditentukan. Kriteria tersebut ditentukan berdasarkan hasil analisis variabel-variabel yang paling berpengaruh terhadap dropout mahasiswa di masa lalu (yang telah terjadi).

Sebagai panduan dalam tahapan analisis, berikut beberapa pertanyaan yang dapat dijadikan acuan:
* Apa saja faktor-faktor yang berpengaruh signifikan terhadap tingginya probabilitas mahasiswa dapat mengalami dropout?
* Bagaimana pengaruh Capaian Akademik Mahasiswa terhadap kecenderungan Dropout?
* Bagaimana pengaruh faktor Non-Akademik mahasiswa terhadap kecenderungan Dropout? 

### Cakupan Proyek

Terdapat 2 outcome utama yang akan dikembangkan pada proyek ini yaitu:
* Dashboard Monitoring
    - Dashboard berfungsi untuk membantu para stakeholder dalam monitoring data-data mahasiswa secara keseluruhan

* Aplikasi Dropout Risk Assessment
    - Aplikasi dengan UI sederhana berbasis streamlit yang dapat membantu memprediksi tingkat risiko dropout mahasiswa.  

Secara umum tahapan dalam proyek ini terbagi menjadi beberapa langkah sebagai berikut:
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
|---Data Split
|---Data Encoding
```
Eksplorasi dan Analisis Data
```
Analisis Korelasi Antar Variabel Data 
|---Observasi pengaruh Aspek Capaian Akademik terhadap kejadian Dropout
|---Observasi pengaruh Aspek non-Akademik terhadap kejadian Dropout
```
Model Development & Deployment
```
Model Training & Evaluation
|---RandomForestClassifier
|---Confusion Matrix
Model Inference
|---Streamlit
```

## Business Dashboard

![Dashboard-Preview](https://github.com/user-attachments/assets/afe388a1-1669-468e-9624-3fc7087c8231)

[Lihat Dashboard](https://lookerstudio.google.com/reporting/be1b741c-4a07-4e2f-a0d9-677d8a283da6)

Dashboard berisi informasi mengenai ringkasan metrik-metrik penting dan visualisasi data yang diperlukan dalam kegiatan monitoring data mahasiswa seperti berikut:

A. Overview
1) Total Mahasiswa
    - Memberikan informasi mengenai besaran jumlah mahasiswa baik yang masih aktif maupun yang sudah lulus/dropout.
2) Dropout
    - Memberikan informasi jumlah total mahasiswa yang dropout sesuai dengan filter yang digunakan.  
3) Active
    - Memberikan informasi jumlah total mahasiswa yang masih aktif (enrolled) sesuai dengan filter yang digunakan.   
4) Graduate
    - Memberikan informasi jumlah total mahasiswa yang sudah lulus berdasarkan filter yang digunakan.

B. Macro Economy
1) GDP
    - Memberikan informasi mengenai rata-rata GDP. Data ini digunakan untuk memahami pengaruh aspek Ekonomi Makro terhadap aspek Finansial mahasiswa yang akhirnya berdampak pada kecenderungan Dropout. 
2) Unemployment Rate
    - Memberikan informasi mengenai rata-rata tingkat pengangguran. Data ini digunakan untuk memahami pengaruh aspek Ekonomi Makro terhadap aspek Finansial mahasiswa yang akhirnya berdampak pada kecenderungan Dropout. 
3) Inflation Rate
    - Memberikan informasi mengenai rata-rata tingkat inflasi. Data ini digunakan untuk memahami pengaruh aspek Ekonomi Makro terhadap aspek Finansial mahasiswa yang akhirnya berdampak pada kecenderungan Dropout. 

C. Curricular Unit 1st Sem
1) Credited
    - Memberikan informasi mengenai jumlah SKS mata kuliah yang dikreditkan atau dikonversi/ditransfer pada semester 1. Data ini digunakan untuk memahami seberapa besar pengaruh aspek Capaian Akademik di semester 1 terhadap kecenderungan Dropout.  
2) Enrolled
    - Memberikan informasi mengenai jumlah SKS mata kuliah yang didaftarkan atau diambil pada semester 1. Data ini digunakan untuk memahami seberapa besar pengaruh aspek Capaian Akademik di semester 1 terhadap kecenderungan Dropout.
3) Evaluations
    - Memberikan informasi mengenai jumlah SKS mata kuliah yang diuji atau dinilai pada semester 1. Data ini digunakan untuk memahami seberapa besar pengaruh aspek Capaian Akademik di semester 1 terhadap kecenderungan Dropout.
4) Approved
    - Memberikan informasi mengenai jumlah SKS mata kuliah yang lulus atau berhasil dinilai pada semester 1. Data ini digunakan untuk memahami seberapa besar pengaruh aspek Capaian Akademik di semester 1 terhadap kecenderungan Dropout.
5) Grade
    - Memberikan informasi mengenai nilai akhir atau IPK pada semester 1. Data ini digunakan untuk memahami seberapa besar pengaruh aspek Capaian Akademik di semester 1 terhadap kecenderungan Dropout. 
6) Without Evaluations
    - Memberikan informasi mengenai jumlah SKS mata kuliah yang belum diuji atau dinilai pada semester 1. Data ini digunakan untuk memahami seberapa besar pengaruh aspek Capaian Akademik di semester 1 terhadap kecenderungan Dropout. 

D. Curricular Unit 2nd Sem
1) Credited
    - Memberikan informasi mengenai jumlah SKS mata kuliah yang dikreditkan atau dikonversi/ditransfer pada semester 2. Data ini digunakan untuk memahami seberapa besar pengaruh aspek Capaian Akademik di semester 2 terhadap kecenderungan Dropout.    
2) Enrolled
    - Memberikan informasi mengenai jumlah SKS mata kuliah yang didaftarkan atau diambil pada semester 2. Data ini digunakan untuk memahami seberapa besar pengaruh aspek Capaian Akademik di semester 2 terhadap kecenderungan Dropout. 
3) Evaluations
    - Memberikan informasi mengenai jumlah SKS mata kuliah yang diuji atau dinilai pada semester 2. Data ini digunakan untuk memahami seberapa besar pengaruh aspek Capaian Akademik di semester 2 terhadap kecenderungan Dropout.
4) Approved
    - Memberikan informasi mengenai jumlah SKS mata kuliah yang lulus atau berhasil dinilai pada semester 2. Data ini digunakan untuk memahami seberapa besar pengaruh aspek Capaian Akademik di semester 2 terhadap kecenderungan Dropout. 
5) Grade
    - Memberikan informasi mengenai nilai akhir atau IPK pada semester 2. Data ini digunakan untuk memahami pengaruh aspek Capaian Akademik di semester 2 terhadap kecenderungan Dropout. Data ini digunakan untuk memahami seberapa besar pengaruh aspek Capaian Akademik di semester 2 terhadap kecenderungan Dropout.
6) Without Evaluations
    - Memberikan informasi mengenai jumlah SKS mata kuliah yang belum diuji atau dinilai pada semester 2. Data ini digunakan untuk memahami seberapa besar pengaruh aspek Capaian Akademik di semester 2 terhadap kecenderungan Dropout.

E. Finansial Information
1) Debtor Chart
    - Memberikan informasi mengenai distribusi jumlah mahasiswa yang mengambil pinjaman sesuai kelompok statusnya baik yang dropout, sudah lulus, maupun masih aktif. Data ini digunakan untuk memahami pengaruh aspek Finansial terhadap kecenderungan Dropout.    
2) Tuition fees up to date Chart
    - Memberikan informasi mengenai distribusi jumlah mahasiswa sesuai kelompok statusnya yang terbagi dalam 2 golongan yaitu mahasiswa yang memiliki memiliki riwayat telat bayar tagihan semester dan tidak. Data ini digunakan untuk memahami pengaruh aspek Finansial terhadap kecenderungan Dropout.  
3) Scholarship holder Chart
    - Memberikan informasi mengenai distribusi jumlah mahasiswa sesuai kelompok statusnya yang terbagi dalam 2 golongan yaitu mahasiswa yang menerima beasiswa dan tidak. Data ini digunakan untuk memahami pengaruh aspek Finansial terhadap kecenderungan Dropout.  

F. Added Information
1) Displaced Chart
    - Memberikan informasi mengenai distribusi jumlah mahasiswa sesuai kelompok statusnya yang terbagi dalam 2 kelompok yaitu mahasiswa yang perlu kos/rumah sewa dan yang tidak. Data ini digunakan untuk memahami pengaruh aspek non-Akademik lainnya terhadap kecenderungan Dropout.  
2) International Chart
    - Memberikan informasi mengenai distribusi jumlah mahasiswa sesuai kelompok statusnya yang terbagi dalam 2 kelompok yaitu mahasiswa Internasional dan non-Internasional. Data ini digunakan untuk memahami pengaruh aspek non-Akademik lainnya terhadap kecenderungan Dropout.
3) Educational special needs Chart
    - Memberikan informasi mengenai distribusi jumlah mahasiswa sesuai kelompok statusnya yang terbagi dalam 2 golongan yaitu mahasiswa yang memiliki kebutuhan khusus dan tidak. Data ini digunakan untuk memahami pengaruh aspek non-Akademik lainnya terhadap kecenderungan Dropout.
4) Age at enrollment Chart
    - Memberikan informasi mengenai distribusi usia mahasiswa saat pendaftaran sesuai kelompok statusnya. Data ini digunakan untuk memahami pengaruh aspek non-Akademik lainnya terhadap kecenderungan Dropout.  
5) Admission Grade Chart
    - Memberikan informasi mengenai distribusi Admission Grade mahasiswa sesuai kelompok statusnya. Data ini digunakan untuk memahami pengaruh aspek non-Akademik lainnya terhadap kecenderungan Dropout.
6) Gender Chart
    - Memberikan informasi mengenai distribusi gender mahasiswa sesuai kelompok statusnya. Data ini digunakan untuk memahami pengaruh aspek non-Akademik lainnya terhadap kecenderungan Dropout.

## Menjalankan Sistem Machine Learning

Dropout Risk App yang telah dikembangkan dapat digunakan dengan cara memberikan input data-data mahasiswa yang ingin diperiksa melalui form yang tersedia. Setelah itu, tekan tombol **Prediksi** dan sistem akan melakukan assessment terhadap data-data yang telah diberikan dan akan menghasilkan hasil penilaian tingkat risiko dropout dari mahasiswa tersebut.  

![App-preview](https://github.com/user-attachments/assets/25ab1e67-bc37-4a81-85b2-16e7e193e417)

[Coba Dropout Risk Assessment App](https://dropout-risk-assessment.streamlit.app/)

## Conclusion

Berdasarkan hasil dalam proyek ini, maka dapat disimpulkan bahwa:
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
        - Aspek-aspek lain: Aspek lain seperti sosial dan psikologis juga turut menjadi faktor yang mampu mendorong motivasi belajar mahasiswa dan akhirnya berdampak terhadap kecenderungan untuk dapat menyelesaikan studi dengan baik atau tidak. Variabel-variabel tersebut diantaranya Usia saat penerimaan, jenis kelamin, kebutuhan sewa tempat tinggal, hingga kebutuhan khusus lainnya untuk keperluan studi. 
4. Dropout Risk Assessment App telah berhasil dikembangkan dengan melatih model klasifikasi menggunakan algoritma `RandomForestClassifier`. Berdasarkan hasil evaluasi, model diketahui mampu melakukan prediksi dengan cukup baik dengan akurasi mencapai 90%. Hasil uji menggunakan data Test menunjukkan bahwa model mampu memprediksi sebanyak 215 mahasiswa dropout dengan benar dari total 255 data yang diuji.


### Rekomendasi Action Items

Setelah dikembangkannya Dropout Risk Assessment App, kampus dapat melakukan screening awal terhadap mahasiswanya menggunakan data-data mulai dari saat mahasiswa masuk hingga data hasil pembelajaran selama 2 semester pertama. App dapat digunakan untuk melakukan prediksi tingkat risiko dropout. Jika hasil prediksi mengatakan bahwa mahasiswa memiliki risiko dropout yang tinggi, selanjutnya perlu ditinjau lebih lanjut melalui dashboard untuk melihat aspek-aspek apa saja yang menjadi faktor utama yang mendorong mahasiswa tersebut memiliki risiko dropout yang tinggi.

Berikut adalah langkah strategis potensial yang dapat diterapkan Jaya-Jaya Institut:

1. Penerapan Early Support System
    - Kampus harus lebih jeli dalam mengamati dan menganalisis hasil studi atau capaian akademik mahasiswa mulai dari periode awal (saat masuk maupun semester awal). Ketika menemukan mahasiswa memiliki nilai GPA sem 1 di bawah rata-rata (<= 7.26) yang kemudian nilai GPA sem 2 mengalami penurunan hingga <= 5.9, maka dapat segera ambil tindakan untuk melakukan bimbingan khusus kepada mereka seperti memberikan fasilitas mentoring belajar bersama senior yang berprestasi.
        
2. Program Bantuan Finansial
    - Apabila mahasiswa terindikasi sebagai Debtor dan/atau tercatat pernah telat melakukan pembayaran (meskipun memiliki nilai akademik yang memadai atau melebihi rata-rata), segera lakukan intervensi dini seperti menyediakan layanan konseling untuk membantu mengelola risiko Dropout akibat masalah finansial yang dihadapi.
    - Pemberian keringanan khusus seperti skema pembayaran cicilan dengan syarat juga diharapkan mampu memberikan sedikit kelonggaran terhadap mahasiswa dalam memenuhi biaya pendidikan mereka disaat kondisi finansial mereka sedang tidak baik.
